# is_tensorTrait

> **Section**: 6.2.2.5.6  
> **PDF Pages**: 875–875  

---

<!-- page 875 -->

约束说明

无

调用示例

见调用示例。

## 6.2.2.5.6 is_tensorTrait

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

判断输入的数据结构是否为TensorTrait数据结构，可通过检查其成员常量value的值来判断。当value为true时，表示输入的数据结构是TensorTrait类型；反之则为非TensorTrait类型。

函数原型

```cpp
template <typename T> struct is_tensorTrait
```

参数说明

参数名描述

T根据输入的数据类型，判断是否为TensorTrait数据结构。

返回值说明

无

约束说明

无
