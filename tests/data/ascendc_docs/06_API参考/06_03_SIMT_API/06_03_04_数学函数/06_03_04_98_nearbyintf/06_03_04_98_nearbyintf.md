# nearbyintf

> **Section**: 6.3.4.98  
> **PDF Pages**: 3241–3241  

---

<!-- page 3241 -->

## 6.3.4.98 nearbyintf

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

获取与输入浮点数最接近的整数，输入浮点数与左右整数的距离相等时，返回偶数。

函数原型

```cpp
inline float nearbyintf(float x)
```

参数说明

表6-1552参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

最接近浮点数的整数。

●若x=inf，返回值为inf。

●若x=-inf，返回值为-inf。

●若x=nan，返回值为nan。

约束说明

SIMT编程场景当前不支持使用该接口。
