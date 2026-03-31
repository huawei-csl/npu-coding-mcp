"""
Tools to extract function signatures from ELF shared libraries with DWARF debug info.
"""

from dataclasses import dataclass, field

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import SymbolTableSection


@dataclass
class ArgInfo:
    name: str  # parameter name (or '' if anonymous)
    type_name: str  # resolved human-readable type string


@dataclass
class FunctionSignature:
    name: str
    return_type: str
    args: list[ArgInfo] = field(default_factory=list)

    @property
    def arg_count(self) -> int:
        return len(self.args)

    @property
    def arg_types(self) -> list[str]:
        return [a.type_name for a in self.args]

    def __str__(self) -> str:
        args_str = (
            ", ".join(f"{a.type_name} {a.name}".strip() for a in self.args) or "void"
        )
        return f"{self.return_type} {self.name}({args_str})"


# Tags that just wrap another type (add a qualifier or alias)
_TRANSPARENT_TAGS = {
    "DW_TAG_typedef",
    "DW_TAG_const_type",
    "DW_TAG_volatile_type",
    "DW_TAG_restrict_type",
}


def _resolve_type(
    offset: int | None, offset_map: dict[int, object], depth: int = 0
) -> str:
    """Recursively resolve a DWARF type offset to a human-readable string."""
    if offset is None:
        return "void"
    if depth > 32:
        return "<recursive>"

    die = offset_map.get(offset)
    if die is None:
        return f"<unknown@{offset}>"

    tag = die.tag

    # ---- base type (int, float, char, …) ---------------------------------
    if tag == "DW_TAG_base_type":
        name_attr = die.attributes.get("DW_AT_name")
        return name_attr.value.decode() if name_attr else "<base>"

    # ---- pointer / reference / rvalue-ref --------------------------------
    if tag in (
        "DW_TAG_pointer_type",
        "DW_TAG_reference_type",
        "DW_TAG_rvalue_reference_type",
    ):
        suffix = {
            "DW_TAG_pointer_type": "*",
            "DW_TAG_reference_type": "&",
            "DW_TAG_rvalue_reference_type": "&&",
        }[tag]
        inner_offset = die.attributes.get("DW_AT_type")
        inner = _resolve_type(
            inner_offset.value if inner_offset else None, offset_map, depth + 1
        )
        return f"{inner}{suffix}"

    # ---- array type ------------------------------------------------------
    if tag == "DW_TAG_array_type":
        elem_offset = die.attributes.get("DW_AT_type")
        elem = _resolve_type(
            elem_offset.value if elem_offset else None, offset_map, depth + 1
        )
        # Try to read the dimension from a DW_TAG_subrange_type child
        dims = []
        for child in die.iter_children():
            if child.tag == "DW_TAG_subrange_type":
                upper = child.attributes.get("DW_AT_upper_bound")
                dims.append(str(upper.value + 1) if upper else "")
        dim_str = "".join(f"[{d}]" for d in dims) if dims else "[]"
        return f"{elem}{dim_str}"

    # ---- transparent qualifiers / typedefs --------------------------------
    if tag in _TRANSPARENT_TAGS:
        name_attr = die.attributes.get("DW_AT_name")
        inner_offset = die.attributes.get("DW_AT_type")
        if name_attr:
            # Typedef: use the alias name (more readable than the underlying type)
            return name_attr.value.decode()
        # Qualifier with no name (e.g. anonymous const): pass through
        return _resolve_type(
            inner_offset.value if inner_offset else None, offset_map, depth + 1
        )

    # ---- struct / union / class / enum -----------------------------------
    if tag in (
        "DW_TAG_structure_type",
        "DW_TAG_union_type",
        "DW_TAG_class_type",
        "DW_TAG_enumeration_type",
    ):
        keyword = {
            "DW_TAG_structure_type": "struct",
            "DW_TAG_union_type": "union",
            "DW_TAG_class_type": "class",
            "DW_TAG_enumeration_type": "enum",
        }[tag]
        name_attr = die.attributes.get("DW_AT_name")
        tag_name = name_attr.value.decode() if name_attr else "<anonymous>"
        return f"{keyword} {tag_name}"

    # ---- subroutine (function pointer) -----------------------------------
    if tag == "DW_TAG_subroutine_type":
        ret_offset = die.attributes.get("DW_AT_type")
        ret = _resolve_type(
            ret_offset.value if ret_offset else None, offset_map, depth + 1
        )
        params = []
        for child in die.iter_children():
            if child.tag == "DW_TAG_formal_parameter":
                p_offset = child.attributes.get("DW_AT_type")
                params.append(
                    _resolve_type(
                        p_offset.value if p_offset else None, offset_map, depth + 1
                    )
                )
        return f"{ret}(*)({', '.join(params)})"

    return f"<{tag}>"


def extract_signatures(library_path: str) -> dict[str, FunctionSignature]:
    """
    Parse an ELF shared library compiled with -g and return a dict mapping
    function name -> FunctionSignature (arg count, arg types, return type).

    Raises ValueError if no DWARF debug info is found.
    """
    with open(library_path, "rb") as f:
        elf = ELFFile(f)
        if not elf.has_dwarf_info():
            raise ValueError(
                f"No DWARF debug info in {library_path}. Was it compiled with -g?"
            )
        dwarf = elf.get_dwarf_info()

        results: dict[str, FunctionSignature] = {}

        for CU in dwarf.iter_CUs():
            # Build a flat offset -> DIE map for this compilation unit
            offset_map: dict[int, object] = {}
            for die in CU.iter_DIEs():
                offset_map[die.offset] = die

            # Second pass: extract functions
            for die in CU.iter_DIEs():
                if die.tag != "DW_TAG_subprogram":
                    continue

                name_attr = die.attributes.get("DW_AT_name")
                if not name_attr:
                    continue  # skip anonymous / inlined stubs

                # Skip declarations (no body in this TU)
                if "DW_AT_declaration" in die.attributes:
                    continue

                fn_name = name_attr.value.decode()

                # Return type
                ret_offset = die.attributes.get("DW_AT_type")
                ret_type = _resolve_type(
                    ret_offset.value if ret_offset else None, offset_map
                )

                # Parameters
                args: list[ArgInfo] = []
                for child in die.iter_children():
                    if child.tag != "DW_TAG_formal_parameter":
                        continue
                    pname_attr = child.attributes.get("DW_AT_name")
                    ptype_attr = child.attributes.get("DW_AT_type")
                    args.append(
                        ArgInfo(
                            name=pname_attr.value.decode() if pname_attr else "",
                            type_name=_resolve_type(
                                ptype_attr.value if ptype_attr else None, offset_map
                            ),
                        )
                    )

                results[fn_name] = FunctionSignature(
                    name=fn_name,
                    return_type=ret_type,
                    args=args,
                )

        return results


def get_extern_c_functions(library_path: str) -> list[str]:
    with open(library_path, "rb") as f:
        elf = ELFFile(f)
        results = []
        for section in elf.iter_sections():
            if not isinstance(section, SymbolTableSection):
                continue
            for sym in section.iter_symbols():
                if (
                    sym.entry.st_info.type == "STT_FUNC"  # it's a function
                    and sym.entry.st_info.bind != "STB_LOCAL"  # exported
                    and sym.entry.st_value
                    != 0  # has an address (defined, not imported)
                    and sym.name  # non-empty name
                    and not sym.name.startswith("_Z")  # not a C++ mangled name
                ):
                    results.append(sym.name)
        return results
