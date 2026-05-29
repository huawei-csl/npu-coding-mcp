# GetCoreNumAiv

> **Section**: 6.4.2.1.8  
> **PDF Pages**: 3765–3765  

---

<!-- page 3765 -->

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto aicNum = ascendcPlatform.GetCoreNumAic();    auto aivNum = ascendcPlatform.GetCoreNumAiv();    // ...按照aivNum切分    context->SetBlockDim(ascendcPlatform.CalcTschNumBlocks(aivNum, aicNum, aivNum));    return ret;}

## 6.4.2.1.8 GetCoreNumAiv

功能说明

获取当前硬件平台AI Core中Vector核数。若AI Core的架构为Cube、Vector分离模式，返回Vector Core的核数；耦合模式返回AI Core的核数。

函数原型

```cpp
uint32_t GetCoreNumAiv(void) const
```

参数说明

无

返回值说明

Atlas 训练系列产品，耦合模式，返回AI Core的核数

Atlas 推理系列产品，耦合模式，返回AI Core的核数

Atlas A2 训练系列产品/Atlas A2 推理系列产品，分离模式，返回Vector Core的核数

Atlas A3 训练系列产品/Atlas A3 推理系列产品，分离模式，返回Vector Core的核数

Atlas 350 加速卡，分离模式，返回Vector Core的核数

约束说明

无

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto aicNum = ascendcPlatform.GetCoreNumAic();    auto aivNum = ascendcPlatform.GetCoreNumAiv();    // ...按照aivNum切分    context->SetBlockDim(ascendcPlatform.CalcTschNumBlocks(aivNum, aicNum, aivNum));    return ret;}

## 6.4.2.1.9 GetCoreNumVector

功能说明

用于获取硬件平台独立的Vector Core的核数。

该接口仅在Atlas 推理系列产品有效，其他硬件平台型号均返回0。
