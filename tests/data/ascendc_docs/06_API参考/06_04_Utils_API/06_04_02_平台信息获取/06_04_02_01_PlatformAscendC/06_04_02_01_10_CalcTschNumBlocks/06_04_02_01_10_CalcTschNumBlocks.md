# CalcTschNumBlocks

> **Section**: 6.4.2.1.10  
> **PDF Pages**: 3766–3766  

---

<!-- page 3766 -->

函数原型

```cpp
uint32_t GetCoreNumVector(void) const
```

参数说明

无

返回值说明

返回硬件平台Vector Core的核数。

约束说明

Atlas 训练系列产品，不支持该接口，返回0

Atlas 推理系列产品，支持该接口，返回硬件平台Vector Core的核数

Atlas A2 训练系列产品/Atlas A2 推理系列产品不支持该接口，返回0

Atlas A3 训练系列产品/Atlas A3 推理系列产品不支持该接口，返回0

Atlas 200I/500 A2 推理产品不支持该接口，返回0

Atlas 350 加速卡不支持该接口，返回0

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto aivCoreNum = ascendcPlatform.GetCoreNumAiv();    auto vectorCoreNum = ascendcPlatform.GetCoreNumVector();    auto allVecCoreNums = aivCoreNum + vectorCoreNum;    // ...按照allVecCoreNums切分    return ret;}

## 6.4.2.1.10 CalcTschNumBlocks

功能说明

针对Cube、Vector分离模式，用于计算Cube、Vector融合算子的numBlocks。针对Vector/Cube融合计算的算子，启动时，按照AIV和AIC组合启动，numBlocks用于设置启动多少个组合执行，比如某款AI处理器上有40个Vector核+20个Cube核，一个组合是2个Vector和1个Cube核，建议设置为20，此时会启动20个组合，即40个Vector和20个Cube核。使用该接口可以自动获取合适的numBlocks值。

获取该值后，使用SetBlockDim进行numBlocks的设置。

函数原型

```cpp
uint32_t CalcTschNumBlocks(uint32_t sliceNum, uint32_t aicCoreNum, uint32_t aivCoreNum) const
```
