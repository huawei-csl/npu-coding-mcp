# make_ulonglong4

> **Section**: 6.3.10.6  
> **PDF Pages**: 3673–3673  

---

<!-- page 3673 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel_make_ulonglong2(__gm__ ulonglong2* dst, __gm__ unsigned long long int* x, __gm__ unsigned long long int* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = make_ulonglong2(x[idx], y[idx]);}

## 6.3.10.6 make_ulonglong4

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

使用给定的四个unsigned long long int类型的数据创建一个ulonglong4类型的向量。

函数原型

```cpp
inline ulonglong4 make_ulonglong4(unsigned long long int x, unsigned long long int y,                                                                 unsigned long long int z, unsigned long long int w)
```

参数说明

表6-1892参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

z输入源操作数。

w输入源操作数。
