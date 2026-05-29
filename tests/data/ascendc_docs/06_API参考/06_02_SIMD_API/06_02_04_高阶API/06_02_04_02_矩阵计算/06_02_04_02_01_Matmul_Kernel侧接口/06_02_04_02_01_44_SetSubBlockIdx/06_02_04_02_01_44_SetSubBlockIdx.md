# SetSubBlockIdx

> **Section**: 6.2.4.2.1.44  
> **PDF Pages**: 2397–2397  

---

<!-- page 2397 -->

## 6.2.4.2.1.44 SetSubBlockIdx

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

设置当前AIV核的ID。分离架构下，一个AI Core由Cube Core（AIC）和Vector Core（AIV）按照一定比例1：N进行组合，其中N个AIV核的ID分别为0, 1, ..., N-1。

函数原型

```cpp
__aicore__ inline void SetSubBlockIdx(uint8_t subBlockIdx)
```

参数说明

表6-1060参数说明

参数名输入/输出描述

subBlockIdx

输入当前AIV核的ID。

返回值说明

无

约束说明

●该接口仅支持在分离架构下使用。

●在分离架构中，AIV核的ID会在REGIST_MATMUL_OBJ()接口内部自动初始化和赋值。如果在算子程序中使用了REGIST_MATMUL_OBJ()接口，则不建议调用此接口；若未使用REGIST_MATMUL_OBJ()接口，则请调用此接口并将子核ID设置为0。
