# NegativeInfinity

> **Section**: 6.2.3.13.1.6  
> **PDF Pages**: 1964–1964  

---

<!-- page 1964 -->

参数说明

表6-808参数说明

参数名输入/输出

描述

dstLocal输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

count输入输入数据元素个数。

返回值说明

标量接口返回值为对应数据类型的正无穷大值。

矢量接口无返回值。

约束说明

无。

调用示例

●标量接口float value = AscendC::NumericLimits<float>::Infinity();

●矢量接口AscendC::NumericLimits<float>::Infinity(dstLocal, 256); // 返回256个float类型的正无穷大值

## 6.2.3.13.1.6 NegativeInfinity

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
