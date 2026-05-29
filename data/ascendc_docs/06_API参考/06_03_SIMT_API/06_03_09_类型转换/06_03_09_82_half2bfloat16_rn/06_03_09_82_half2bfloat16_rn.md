# __half2bfloat16_rn

> **Section**: 6.3.9.82  
> **PDF Pages**: 3455–3455  

---

<!-- page 3455 -->

## 6.3.9.82 __half2bfloat16_rn

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

遵循CAST_RINT模式，将half类型数据转换为bfloat16类型，返回转换后的值。

函数原型

```cpp
inline bfloat16_t __half2bfloat16_rn(const half x)
```

参数说明

表6-1717参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_RINT模式转换成的bfloat16类型数据。特别场景说明如下：

●当x为nan时，返回值为nan。

●当x为inf时，返回值为inf。

●当x为-inf时，返回值为-inf。

约束说明

SIMT编程场景当前不支持使用该接口。
