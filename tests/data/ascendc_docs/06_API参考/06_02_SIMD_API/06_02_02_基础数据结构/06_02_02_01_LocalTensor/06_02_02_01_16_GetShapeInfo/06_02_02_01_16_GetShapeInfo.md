# GetShapeInfo

> **Section**: 6.2.2.1.16  
> **PDF Pages**: 831–831  

---

<!-- page 831 -->

## 6.2.2.1.16 GetShapeInfo

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

获取LocalTensor的Shape信息。注意：Shape信息没有默认值，只有通过SetShapeInfo设置过Shape信息后，才可以调用该接口获取正确的Shape信息。

函数原型

```cpp
__aicore__ inline ShapeInfo GetShapeInfo() const
```

参数说明

无

返回值说明

LocalTensor的Shape信息，ShapeInfo结构体类型。

约束说明

无

调用示例

// 示例获取Tensor的ShapeInfo信息AscendC::ShapeInfo maxShapeInfo = maxUb.GetShapeInfo();uint32_t orgShape0 = maxShapeInfo.originalShape[0];uint32_t orgShape1 = maxShapeInfo.originalShape[1];uint32_t orgShape2 = maxShapeInfo.originalShape[2];uint32_t orgShape3 = maxShapeInfo.originalShape[3];uint32_t shape2 = maxShapeInfo.shape[2];
