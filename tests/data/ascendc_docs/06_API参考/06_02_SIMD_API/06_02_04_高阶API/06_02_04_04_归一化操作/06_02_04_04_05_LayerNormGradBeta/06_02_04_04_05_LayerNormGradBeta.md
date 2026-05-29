# LayerNormGradBeta

> **Section**: 6.2.4.4.5  
> **PDF Pages**: 2598–2600  

---

<!-- page 2598 -->

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的LayerNormGradTiling信息传入LayerNormGrad接口参与计算。完整的kernel侧样例请参考调用示例。

extern "C" __global__ __aicore__ void func_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling){    GET_TILING_DATA(tilingData, tiling);    KernelFunc op;    op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum,tilingData.layernormGradTilingData);    if (TILING_KEY_IS(1)) {        op.Process();    }}

**----结束**

## 6.2.4.4.5 LayerNormGradBeta

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

LayerNormGradBeta接口用于获取反向beta/gamma的数值，和LayerNormGrad共同输出pdx, gamma和beta：

算法公式为:

![p2598_img001.png](../../../images/p2598_img001.png)

![p2598_img002.png](../../../images/p2598_img002.png)

<!-- page 2599 -->

函数原型

由于该接口的内部实现中涉及复杂的计算，需要额外的临时空间来存储计算过程中的中间变量。临时空间大小BufferSize的获取方法：通过6.2.4.4.6 LayerNormGradBetaTiling中提供的GetLayerNormGradBetaMaxMinTmpSize接口获取所需最大和最小临时空间大小，最小空间可以保证功能正确，最大空间用于提升性能。

临时空间支持接口框架申请和开发者通过sharedTmpBuffer入参传入两种方式，因此LayerNormGradBeta接口的函数原型有两种：

●通过sharedTmpBuffer入参传入临时空间template <typename T, bool isReuseSource = false>__aicore__ inline void LayerNormGradBeta(const LocalTensor<T>& outputPdGamma, const LocalTensor<T>& outputPdBeta, const LocalTensor<T>& resForGamma, const LocalTensor<T>& inputDy, const LocalTensor<uint8_t>& sharedTmpBuffer, const LayerNormGradBetaTiling& tiling)

该方式下开发者需自行申请并管理临时内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。

●接口框架申请临时空间template <typename T, bool isReuseSource = false>__aicore__ inline void LayerNormGradBeta(const LocalTensor<T>& outputPdGamma, const LocalTensor<T>& outputPdBeta, const LocalTensor<T>& resForGamma, const LocalTensor<T>& inputDy, LayerNormGradBetaTiling& tiling)

该方式下开发者无需申请，但是需要预留临时空间的大小。

参数说明

表6-1183模板参数说明

参数名描述

T操作数的数据类型。

Atlas 350 加速卡，支持的数据类型为：half、float。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持的数据类型为：half、float。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持的数据类型为：half、float。

Atlas 推理系列产品AI Core，支持的数据类型为：half、float。

isReuseSource是否允许修改源操作数，默认值为false。如果开发者允许源操作数被改写，可以使能该参数，使能后能够节省部分内存空间。

设置为true，则本接口内部计算时复用inputDy的内存空间，节省内存空间；设置为false，则本接口内部计算时不复用inputDy的内存空间。

对于float数据类型输入支持开启该参数，half数据类型输入不支持开启该参数。

isReuseSource的使用样例请参考更多样例。

<!-- page 2600 -->

表6-1184接口参数说明

参数名称输入/输出含义

outputPdGamma

输出目的操作数，shape为[H]，LocalTensor数据结构的定义请参考6.2.2.1 LocalTensor。尾轴长度需要32B对齐

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

outputPdBeta输出目的操作数，shape为[H]，LocalTensor数据结构的定义请参考6.2.2.1 LocalTensor。尾轴长度需要32B对齐

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

resForGamma输入源操作数，shape为[B, S, H]，LocalTensor数据结构的定义请参考6.2.2.1 LocalTensor。resForGamma的数据类型需要与目的操作数保持一致，尾轴长度需要32B对齐。需提前调用LayerNormGrad接口获取resForGamma参数值。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

inputDy输入源操作数，shape为[B, S, H]，LocalTensor数据结构的定义请参考6.2.2.1 LocalTensor。inputDy的数据类型需要与目的操作数保持一致，尾轴长度需要32B对齐。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

sharedTmpBuffer

输入共享缓冲区，用于存放API内部计算产生的临时数据。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。共享缓冲区大小的获取方式请参考6.2.4.4.6 LayerNormGradBeta Tiling。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

tiling输入LayerNormGradBeta计算所需Tiling信息，Tiling信息的获取请参考6.2.4.4.6 LayerNormGradBetaTiling。

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。
