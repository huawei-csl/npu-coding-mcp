# TPosition

> **Section**: 6.2.6.7  
> **PDF Pages**: 3095–3096  

---

<!-- page 3095 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

复数类型，其中complex32表示实部和虚部都是half类型的复数，位宽为32位；complex64表示实部和虚部都是float类型的复数，位宽为64位。

具体定义如下：namespace AscendC {template<class T>struct Complex {    T real;    T imag;};} // namespace AscendCusing complex32 = AscendC::Complex<half>;using complex64 = AscendC::Complex<float>;

表6-1448 Complex 模板参数说明

参数名称描述

T实部和虚部的数据类型，仅支持half/float。

表6-1449 Complex 结构体参数说明

函数名称入参说明

real实部，类型为T，仅支持half/float。

imag虚部，类型为T，仅支持half/float。

使用示例如下：

// value0代表实部为1，虚部为2的复数，即1+2jcomplex32 value0(1, 2);// value1代表实部为3，虚部为0的复数，即3+0jcomplex32 value1(3);// value2代表实部为4，虚部为0的复数，即4+0jcomplex64 value2 = 4;

## 6.2.6.7 TPosition

Ascend C管理不同层级的物理内存时，用一种抽象的逻辑位置（TPosition）来表达各级别的存储，代替了片上物理存储的概念，达到隐藏硬件架构的目的。主要的TPosition类型包括：VECIN、VECOUT、VECCALC、A1、A2、B1、B2、C1、C2、

<!-- page 3096 -->

CO1、CO2，其中VECIN、VECCALC、VECOUT主要用于矢量编程，A1、A2、B1、B2、C1、C2、CO1、CO2用于矩阵编程。您可以参考2.2.3.3 SIMD编程了解TPosition的基础概念，通过表6-48了解TPosition和物理存储的映射关系。

TPosition定义如下：

```cpp
enum class TPosition : uint8_t {    GM,    A1,    A2,    B1,    B2,    C1,    C2,    CO1,    CO2,    VECIN,    VECOUT,    VECCALC,    LCM = VECCALC,    SPM,    SHM = SPM,    TSCM,    C2PIPE2GM,    C2PIPE2LOCAL,    MAX,};
```

TPosition枚举值的具体定义如下：

表6-1450 TPosition 枚举值含义说明

枚举值具体含义

GMGlobal Memory，对应AI Core的外部存储。

VECIN用于矢量计算，搬入数据的存放位置，在数据搬入Vector计算单元时使用此位置。

VECOUT用于矢量计算，搬出数据的存放位置，在将Vector计算单元结果搬出时使用此位置。

VECCALC用于矢量计算/矩阵计算，在计算需要临时变量时使用此位置。

A1用于矩阵计算，存放整块A矩阵，可类比CPU多级缓存中的二级缓存。

B1用于矩阵计算，存放整块B矩阵，可类比CPU多级缓存中的二级缓存。

C1用于矩阵计算，存放整块Bias矩阵，可类比CPU多级缓存中的二级缓存。

A2用于矩阵计算，存放切分后的小块A矩阵，可类比CPU多级缓存中的一级缓存。

B2用于矩阵计算，存放切分后的小块B矩阵，可类比CPU多级缓存中的一级缓存。

C2用于矩阵计算，存放切分后的小块Bias矩阵，可类比CPU多级缓存中的一级缓存。
