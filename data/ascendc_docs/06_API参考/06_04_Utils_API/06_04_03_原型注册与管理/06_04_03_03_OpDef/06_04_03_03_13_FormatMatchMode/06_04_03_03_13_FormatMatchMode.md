# FormatMatchMode

> **Section**: 6.4.3.3.13  
> **PDF Pages**: 3783–3783  

---

<!-- page 3783 -->

约束说明

当用户使用CATEGORY参数设置算子分组名称时，会对应生成同名的代码文件。若文件名过长在编译时可能超过tar的打包文件名称长度限制，导致报错。

具体参考2.10.10.6 算子工程编译时出现文件名过长报错。

调用示例

AddCustomComment(const char* name) : OpDef(name){    this->Comment(CommentSection::CATEGORY, "catg"); // 算子分组    this->Comment(CommentSection::BRIEF, "Brief cmt") // BRIEF注释            .Comment(CommentSection::CONSTRAINTS, "Constraints cmt1") // CONSTRAINTS注释            .Comment(CommentSection::CONSTRAINTS, "Constraints cmt2");    this->Comment(CommentSection::RESTRICTIONS, "Restrictions cmt1") // RESTRICTIONS注释        .Comment(CommentSection::RESTRICTIONS, "Restrictions cmt2")        .Comment(CommentSection::THIRDPARTYFWKCOMPAT, "Third-party framework compatibility cmt1") // THIRDPARTYFWKCOMPAT注释        .Comment(CommentSection::THIRDPARTYFWKCOMPAT, "Third-party framework compatibility cmt2")        .Comment(CommentSection::SEE, "See cmt1")// SEE注释        .Comment(CommentSection::SEE, "See cmt2");    this->Input("x")        .ParamType(REQUIRED)        .DataType({ge::DT_FLOAT, ge::DT_INT32})        .FormatList({ge::FORMAT_ND});    this->Input("y")        .ParamType(REQUIRED)        .DataType({ge::DT_FLOAT, ge::DT_INT32})        .FormatList({ge::FORMAT_ND});

```cpp
this->Output("z")        .ParamType(REQUIRED)        .DataType({ge::DT_FLOAT, ge::DT_INT32})        .FormatList({ge::FORMAT_ND});
    this->AICore()        .SetTiling(optiling::TilingFunc);
    this->AICore().AddConfig("ascendxxx");}
```

## 6.4.3.3.13 FormatMatchMode

功能说明

设置输入输出tensor的format匹配模式。

函数原型

```cpp
OpDef &FormatMatchMode(FormatCheckOption option)
```
