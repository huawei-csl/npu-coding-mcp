# GetShapeInfo

> **Section**: 6.2.2.2.11  
> **PDF Pages**: 846–846  

---

<!-- page 846 -->

产品是否支持

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

设置GlobalTensor的shape信息。

函数原型

```cpp
__aicore__ inline void SetShapeInfo(const ShapeInfo& shapeInfo)
```

参数说明

表6-73参数说明

参数名输入/输出

描述

shapeInfo

输入ShapeInfo结构体。

返回值说明

无。

约束说明

无。

调用示例

// 示例设置Tensor的ShapeInfo信息AscendC::GlobalTensor<float> tglobal;uint32_t shapeArray[] = {16, 1024};tglobal.SetShapeInfo(AscendC::ShapeInfo(2, shapeArray, AscendC::DataFormat::ND));

## 6.2.2.2.11 GetShapeInfo

产品支持情况

产品是否支持

Atlas 350 加速卡√
