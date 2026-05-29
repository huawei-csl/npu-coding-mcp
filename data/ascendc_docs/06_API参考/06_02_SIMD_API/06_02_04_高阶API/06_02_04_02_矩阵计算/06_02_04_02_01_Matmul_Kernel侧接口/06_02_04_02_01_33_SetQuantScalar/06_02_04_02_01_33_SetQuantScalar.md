# SetQuantScalar

> **Section**: 6.2.4.2.1.33  
> **PDF Pages**: 2383–2383  

---

<!-- page 2383 -->

## 6.2.4.2.1.33 SetQuantScalar

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

本接口提供对输出矩阵的所有值采用同一系数进行量化或反量化的功能，即整个C矩阵对应一个量化参数，量化参数的shape为[1]。量化、反量化的详细内容请参考量化场景。

Matmul反量化场景：在Matmul计算时，左、右矩阵的输入为int8_t或int4b_t类型，输出为half类型；或者左、右矩阵的输入为int8_t类型，输出为int8_t类型。该场景下，输出C矩阵的数据从CO1搬出到Global Memory时，会执行反量化操作，将最终结果反量化为对应的half或int8_t类型。

Matmul量化场景：在Matmul计算时，左、右矩阵的输入为half或bfloat16_t类型，输出为int8_t类型。该场景下，输出C矩阵的数据从CO1搬出到Global Memory时，会执行量化操作，将最终结果量化为int8_t类型。

函数原型

```cpp
__aicore__ inline void SetQuantScalar(const uint64_t quantScalar)
```

参数说明

参数名输入/输出

描述

quantScalar

输入量化或反量化系数。

将float数据类型的量化计算参数scale、offset转换为uint64类型的入参的计算公式如下：

1.quantScalar为64位格式，初始为0。

2.scale按bit位取高19位截断，存储于quantScalar的bit位32位处，并将46位修改为1。
