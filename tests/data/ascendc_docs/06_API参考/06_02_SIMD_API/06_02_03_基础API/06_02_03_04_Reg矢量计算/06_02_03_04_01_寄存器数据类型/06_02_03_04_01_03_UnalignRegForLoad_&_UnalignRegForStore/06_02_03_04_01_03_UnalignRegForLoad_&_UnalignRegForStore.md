# UnalignRegForLoad & UnalignRegForStore

> **Section**: 6.2.3.4.1.3  
> **PDF Pages**: 1508–1508  

---

<!-- page 1508 -->

参数名输入/输出描述

regTrait输入当前仅针对b64/complex32数据类型生效，分为RegTraitNumOne和RegTraitNumTwo，含义和RegTensor的模板regTrait类型一致，配合RegTensor的regTrait一起使用。regTrait为RegTraitNumOne时，表明当前MaskReg的作用范围可覆盖至256B（一个VL的长度）。对于使用RegTraitNumOne的b64 RegTensor的指令，生成的b64 mask为每8位有效；RegTraitNumTwo表明当前MaskReg的作用范围可覆盖至512B（两个VL的长度），生成的b64 mask为每4位有效，作用于使用RegTraitNumTwo的b64 RegTensor的指令。该参数默认值为RegTraitNumOne。

scalarValue

输入/输出矢量计算需要操作的元素的具体数量，生成对应的MaskReg，元素有效范围从0到VL_T（位宽为VL的T类型元素个数）。

执行完该函数后，scalarValue会减去VL_T。

scalarValue = (scalarValue < VL_T) ? 0 : (scalarValue -VL_T)

返回值说明

MaskReg

支持的型号

Atlas 350 加速卡

约束说明

无

调用示例

```cpp
AscendC::Reg::RegTensor<uint32_t> srcReg;AscendC::Reg::MaskReg mask0 = AscendC::Reg::CreateMask<uint32_t,AscendC::Reg:: MaskPattern::ALL >();AscendC::Reg::MaskReg mask1;uint32_t scalarValue = 127;for (uint16_t i = 0;
 i < 2;
 i++) {    mask1 = AscendC::Reg::UpdateMask<uint32_t>(scalarValue);
    AscendC::Reg::LoadAlign<T, AscendC::Reg::PostLiteral::POST_MODE_UPDATE>(srcReg, srcAddr, 0);
    AscendC::Reg::Adds(srcReg, srcReg, 1, mask0);
    AscendC::Reg::StoreAlign<T, AscendC::Reg::PostLiteral::POST_MODE_UPDATE>(dst0Addr, srcReg, 0, mask0);
    AscendC::Reg::StoreAlign<T, AscendC::Reg::PostLiteral::POST_MODE_UPDATE>(dst1Addr, srcReg, 0, mask1);}
```

## 6.2.3.4.1.3 UnalignRegForLoad & UnalignRegForStore

功能说明

UnalignRegForLoad、UnalignRegForStore用作缓冲区来优化UB和RegTensor之间连续不对齐地址访问的开销。在读不对齐地址前，UnalignRegForLoad、UnalignRegForStore应该通过LoadUnAlignPre API初始化，然后使用LoadUnAlign
