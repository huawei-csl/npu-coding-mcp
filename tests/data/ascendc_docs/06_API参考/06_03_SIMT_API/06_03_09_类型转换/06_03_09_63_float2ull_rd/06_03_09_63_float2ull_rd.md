# __float2ull_rd

> **Section**: 6.3.9.63  
> **PDF Pages**: 3430–3430  

---

<!-- page 3430 -->

## 6.3.9.63 __float2ull_rd

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

遵循CAST_FLOOR模式，将浮点数转换为64位无符号整数，返回转换后的值。

函数原型

```cpp
inline unsigned long long int __float2ull_rd(const float x)
```

参数说明

表6-1698参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

输入遵循CAST_FLOOR模式转换成的64位无符号整数。特别场景说明如下：

●当x为nan时，返回值为0。

●当x为inf时，返回值为18446744073709551615。

●当x为-inf时，返回值为0。

约束说明

SIMT编程场景当前不支持使用该接口。
