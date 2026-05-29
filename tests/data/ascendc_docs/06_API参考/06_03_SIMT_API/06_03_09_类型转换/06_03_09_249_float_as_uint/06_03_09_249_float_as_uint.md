# __float_as_uint

> **Section**: 6.3.9.249  
> **PDF Pages**: 3663–3663  

---

<!-- page 3663 -->

```cpp
int idx = threadIdx.x + blockIdx.x * blockDim.x;
    dst[idx] = __float_as_int(x[idx]);}
```

## 6.3.9.249 __float_as_uint

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

将浮点数中的位重新解释为无符号整数，即将浮点数存储的位按照无符号整数的格式进行读取。

函数原型

```cpp
inline unsigned int __float_as_uint(const float x)
```

参数说明

表6-1884参数说明

参数名输入/输出

描述

x输入源操作数。

返回值说明

与输入浮点数最接近的整数值。特别场景说明如下：

●当x为nan时，返回值为2143289344。

●当x为inf时，返回值为2139095040。

●当x为-inf时，返回值为4286578688。
