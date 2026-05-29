# SetGlobalBuffer

> **Section**: 6.2.2.2.3  
> **PDF Pages**: 837–838  

---

<!-- page 837 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

GlobalTensor构造函数。

函数原型

```cpp
__aicore__ inline GlobalTensor<T>() {}
```

参数说明

表6-66模板参数说明

参数名描述

TGlobalTensor的数据类型。

返回值说明

无。

约束说明

无。

调用示例

参考调用示例。

## 6.2.2.2.3 SetGlobalBuffer

产品支持情况

产品是否支持

Atlas 350 加速卡√

<!-- page 838 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

传入全局数据地址，初始化GlobalTensor。

函数原型

●传入全局数据的指针，并设置存储大小（通过元素个数表达）。__aicore__ inline void SetGlobalBuffer(__gm__ PrimType* buffer, uint64_t bufferSize)

●仅传入全局数据的指针，此时通过6.2.2.2.8 GetSize获取到的元素个数为0。__aicore__ inline void SetGlobalBuffer(__gm__ PrimType* buffer)

参数说明

表6-67参数说明

参数名输入/输出

描述

buffer输入Host侧传入的全局数据指针。PrimType类型。

PrimType定义如下：// PrimT用于从T中提取基础数据类型：T传入基础数据类型，直接返回数据类型；T传入为TensorTrait类型时萃取TensorTrait中的LiteType基础数据类型using PrimType = PrimT<T>;

bufferSize

输入GlobalTensor所包含的类型为PrimType的数据个数，需自行保证不会超出实际数据的长度。如指向的外部存储有连续256个int32_t，则其bufferSize为256。

返回值说明

无。

约束说明

无。
