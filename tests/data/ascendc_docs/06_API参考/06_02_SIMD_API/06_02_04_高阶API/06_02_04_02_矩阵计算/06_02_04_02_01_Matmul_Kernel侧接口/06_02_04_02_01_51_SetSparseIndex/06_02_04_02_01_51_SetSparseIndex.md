# SetSparseIndex

> **Section**: 6.2.4.2.1.51  
> **PDF Pages**: 2407–2407  

---

<!-- page 2407 -->

## 6.2.4.2.1.51 SetSparseIndex

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置稀疏矩阵稠密化过程生成的索引矩阵。

索引矩阵在稠密化中的作用请参考MmadWithSparse。

函数原型

```cpp
__aicore__ inline void SetSparseIndex(const GlobalTensor<uint8_t>& indexGlobal)
```

参数说明

表6-1067参数说明

参数名输入/输出

描述

indexGlobal

输入索引矩阵在Global Memory上的首地址，类型为GlobalTensor。

索引矩阵的数据类型为uint2，需要由用户拼成uint8的数据类型，再传入本接口。索引矩阵的Format格式只支持NZ格式。

返回值说明

无

约束说明

●索引矩阵的Format格式要求为NZ格式。

●本接口仅支持在纯Cube模式（只有矩阵计算）且MDL模板的场景使用。
