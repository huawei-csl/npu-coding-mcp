# make_ushort4

> **Section**: 6.3.10.18  
> **PDF Pages**: 3688–3688  

---

<!-- page 3688 -->

调用示例

SIMD与SIMT混合编程场景：__simt_vf__ __launch_bounds__(1024) inline void kernel_make_ushort2(__gm__ ushort2* dst, __gm__ unsigned short* x, __gm__ unsigned short* y){    int idx = threadIdx.x + blockIdx.x * blockDim.x;    dst[idx] = make_ushort2(x[idx], y[idx]);}

## 6.3.10.18 make_ushort4

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

使用给定的四个unsigned short类型的数据创建一个ushort4类型的向量。

函数原型

```cpp
inline ushort4 make_ushort4(unsigned short x, unsigned short y, unsigned short z,unsigned short w)
```

参数说明

表6-1904参数说明

参数名输入/输出

描述

x输入源操作数。

y输入源操作数。

z输入源操作数。

w输入源操作数。
