# SetL2CacheHint

> **Section**: 6.2.2.2.12  
> **PDF Pages**: 847–848  

---

<!-- page 847 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

获取GlobalTensor的shape信息。注意：Shape信息没有默认值，只有通过SetShapeInfo设置过Shape信息后，才可以调用该接口获取正确的ShapeInfo。

函数原型

```cpp
__aicore__ inline ShapeInfo GetShapeInfo() const
```

参数说明

无。

返回值说明

GlobalTensor的shape信息，ShapeInfo类型。

约束说明

无。

调用示例

// 示例获取Tensor的ShapeInfo信息，获取通过SetShapeInfo设置过Shape信息AscendC::ShapeInfo maxShapeInfo = tglobal.GetShapeInfo();// 获取原始的shape各个维度的值uint32_t orgShape0 = maxShapeInfo.originalShape[0];uint32_t orgShape1 = maxShapeInfo.originalShape[1];uint32_t orgShape2 = maxShapeInfo.originalShape[2];uint32_t orgShape3 = maxShapeInfo.originalShape[3];// 获取现有的shape的2维的值uint32_t shape2 = maxShapeInfo.shape[2]

## 6.2.2.2.12 SetL2CacheHint

产品支持情况

产品是否支持

Atlas 350 加速卡√

<!-- page 848 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置GlobalTensor是否使能L2 Cache，默认使能L2 Cache。

函数原型

```cpp
template<CacheRwMode rwMode = CacheRwMode::RW>__aicore__ inline void SetL2CacheHint(CacheMode mode);
```

参数说明

表6-74模板参数说明

参数名描述

**rwMode设置L2 Cache读写模式。enum CacheRwMode {READ = 1,WRITE = 2,RW = 3};**

预留参数。为后续的功能做保留，开发者暂时无需关注，使用默认值即可。
