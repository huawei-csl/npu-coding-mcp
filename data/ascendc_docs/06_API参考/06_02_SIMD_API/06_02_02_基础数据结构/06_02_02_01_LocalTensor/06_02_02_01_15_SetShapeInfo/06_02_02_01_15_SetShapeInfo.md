# SetShapeInfo

> **Section**: 6.2.2.1.15  
> **PDF Pages**: 830–830  

---

<!-- page 830 -->

## 6.2.2.1.15 SetShapeInfo

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

设置LocalTensor的Shape信息。

函数原型

```cpp
__aicore__ inline void SetShapeInfo(const ShapeInfo& shapeInfo)
```

参数说明

表6-61参数说明

参数名输入/输出

描述

shapeInfo

输入Shape信息，ShapeInfo结构体类型。

返回值说明

无

约束说明

无

调用示例

// 示例设置Tensor的ShapeInfo信息AscendC::LocalTensor<float> maxUb = softmaxMaxBuf.template Get<float>();uint32_t shapeArray[] = {16, 1024};maxUb.SetShapeInfo(AscendC::ShapeInfo(2, shapeArray, AscendC::DataFormat::ND));
