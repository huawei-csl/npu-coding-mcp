# MulsCast(ISASI)

> **Section**: 6.2.3.3.3.14  
> **PDF Pages**: 1300–1302  

---

<!-- page 1300 -->

参数名输入/输出

描述

count输入参与计算的元素个数。

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

```cpp
AscendC::ExpSub(dstLocal, src0Local, src1Local, 512);
```

结果示例如下：输入数据src0Local：[1 2 4 ... 510]输入数据src1Local：[1 1 2 ... 510]输出数据dstLocal：[1 2.71828 7.38905 ... 1]

## 6.2.3.3.3.14 MulsCast(ISASI)

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

将矢量源操作数前count个数据与标量相乘再按照CAST_ROUND模式转换成half类型，并将计算结果写入dst，此接口支持标量在前和标量在后两种场景。计算公式如下。

![p1300_img001.png](../../../../images/p1300_img001.png)

<!-- page 1301 -->

其中标量输入也支持配置LocalTensor单点元素，计算公式如下，idx表示LocalTensor单点元素的位置系数。

![p1301_img001.png](../../../../images/p1301_img001.png)

函数原型

```cpp
template <typename T0 = BinaryDefaultType, typename T1 = BinaryDefaultType, const BinaryConfig &config = DEFAULT_BINARY_CONFIG, typename T2, typename T3, typename T4>__aicore__ inline void MulsCast(const T2 &dst, const T3 &src0, const T4 &src1, const uint32_t count)
```

参数说明

表6-346模板参数说明

参数名描述

T0目的操作数数据类型。

预留参数，暂未启用，为后续的功能扩展做保留，需要指定时，传入默认值BinaryDefaultType即可。

T1源操作数数据类型。

预留参数，暂未启用，为后续的功能扩展做保留，需要指定时，传入默认值BinaryDefaultType即可。

config类型为BinaryConfig，当标量为LocalTensor单点元素类型时生效，用于指定单点元素操作数位置。默认值DEFAULT_BINARY_CONFIG，表示右操作数为标量。struct BinaryConfig {    int8_t scalarTensorIndex = 1; // 用于指定标量为LocalTensor单点元素时标量的位置，0表示左操作数，1表示右操作数};constexpr BinaryConfig DEFAULT_BINARY_CONFIG = {1};

T2LocalTensor类型，根据输入参数dst自动推导相应的数据类型，开发者无需配置该参数，保证dst满足数据类型的约束即可。

T3LocalTensor类型或标量类型，根据输入参数src0自动推导相应的数据类型，开发者无需配置该参数，保证src0满足数据类型的约束即可。

T4LocalTensor类型或标量类型，根据输入参数src1自动推导相应的数据类型，开发者无需配置该参数，保证src1满足数据类型的约束即可。

<!-- page 1302 -->

表6-347参数说明

参数名输入/输出

描述

dst输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

Atlas 350 加速卡，支持的数据类型为：half

不同数据类型对应的精度转换规则见表6-348。

src0/src1输入源操作数。

●类型为LocalTensor时，支持当作矢量操作数或标量单点元素，支持的TPosition为VECIN/VECCALC/VECOUT。LocalTensor的起始地址需要32字节对齐。

Atlas 350 加速卡，支持的数据类型为：float

●类型为标量时：Atlas 350 加速卡，支持的数据类型为：float

count输入参与计算的元素个数。

表6-348精度转换规则

**src类型**

**dst类型**

类型转换模式介绍

floathalf将源操作数按照CAST_ROUND模式取到half所能表示的数，以half格式（溢出默认按照饱和处理）存入dst中。

返回值说明

无

约束说明

●左操作数及右操作数中，必须有一个为矢量；当前不支持左右操作数同时为标量。

●本接口传入LocalTensor单点数据作为标量时，idx参数需要传入编译期已知的常量，传入变量时需要声明为constexpr。

调用示例

// 标量在后示例AscendC::MulsCast(dstLocal, src0Local, src1Local[0], 512);

// 标量在前示例static constexpr AscendC::BinaryConfig config = { 0 };AscendC::MulsCast<BinaryDefaultType, BinaryDefaultType, config>(dstLocal, src0Local[0], src1Local, 512);

结果示例如下：
