# WelfordFinalize

> **Section**: 6.2.4.4.17  
> **PDF Pages**: 2641–2645  

---

<!-- page 2641 -->

```cpp
{    GET_TILING_DATA(tilingData, tiling);
    if (TILING_KEY_IS(1))    {        if (tilingData.inplace)        {            KernelWelfordUpdate<DTYPE_INPUTX, DTYPE_U, true> op;
             op.Init(inputX_gm, mean_gm, var_gm, outputMean_gm, outputVariance_gm, tilingData.nLength, tilingData.rLength, tilingData.abComputeLength);
            op.Process();        }        else        {            KernelWelfordUpdate<DTYPE_INPUTX, DTYPE_U, false> op;
            op.Init(inputX_gm, mean_gm, var_gm, outputMean_gm, outputVariance_gm, tilingData.nLength, tilingData.rLength, tilingData.abComputeLength);
            op.Process();        }    }}
```

**----结束**

## 6.2.4.4.17 WelfordFinalize

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

Welford计算是一种在线计算均值和方差的方法。一方面，它可以在不存储所有样本的情况下，逐步计算所有样本的均值和方差，更适合处理海量数据；另一方面，它只需要对数据进行一次遍历，能减少访存次数，提高计算性能。本接口为Welford算法的后处理。

LayerNorm算法中Reduce轴较大的场景，可以通过切分Reduce轴，联合使用本接口与WelfordUpdate，能够实现等效计算LayerNorm。根据Reduce轴切分后是否有尾块，本接口分为如下两种计算公式：

●不带尾块/不带counts参数场景：

<!-- page 2642 -->

![p2642_img001.png](../../../images/p2642_img001.png)

对于Atlas 350 加速卡，方差计算公式如下。

–方差系数未修正场景：

![p2642_img002.png](../../../images/p2642_img002.png)

–方差系数修正场景：

![p2642_img003.png](../../../images/p2642_img003.png)

其中，Mean为均值输出，Var为方差输出。

Meani代表输入的第i个均值，Vari代表输入的第i个方差。Ab代表Reduce轴切分后

![p2642_img004.png](../../../images/p2642_img004.png)

一次计算的大小，Rn代表Reduce轴按Ab拆分的次数，

代表未修

![p2642_img005.png](../../../images/p2642_img005.png)

正的方差系数rRec，

代表修正方差系数rRecWithCorrection。

●带尾块/带counts参数场景：

![p2642_img006.png](../../../images/p2642_img006.png)

对于Atlas 350 加速卡，方差计算公式如下。

–方差系数未修正场景：

![p2642_img007.png](../../../images/p2642_img007.png)

–方差系数修正场景：

<!-- page 2643 -->

![p2643_img001.png](../../../images/p2643_img001.png)

除上述参数含义外，countsi代表Meani对应的系数，R代表未切分的原始Reduce

![p2643_img002.png](../../../images/p2643_img002.png)

![p2643_img003.png](../../../images/p2643_img003.png)

代表未修正的方差系数rRec，

轴长度，

代表修正系数rRecWithCorrection。

函数原型

●通过sharedTmpBuffer入参传入临时空间

–不带counts参数场景template <bool isReuseSource = false, const WelfordFinalizeConfig& config = WFFINALIZE_DEFAULT_CFG>__aicore__ inline void WelfordFinalize(const LocalTensor<float>& outputMean, const LocalTensor<float>& outputVariance, const LocalTensor<float>& inputMean, const LocalTensor<float>& inputVariance, const LocalTensor<uint8_t>& sharedTmpBuffer, WelfordFinalizePara& para)

–带counts参数场景template <bool isReuseSource = false, const WelfordFinalizeConfig& config = WFFINALIZE_DEFAULT_CFG>__aicore__ inline void WelfordFinalize(const LocalTensor<float>& outputMean, const LocalTensor<float>& outputVariance, const LocalTensor<float>& inputMean, const LocalTensor<float>& inputVariance, const LocalTensor<int32_t>& counts, const LocalTensor<uint8_t>& sharedTmpBuffer, WelfordFinalizePara& para)

●接口框架申请临时空间

–不带counts参数场景template <bool isReuseSource = false, const WelfordFinalizeConfig& config = WFFINALIZE_DEFAULT_CFG>__aicore__ inline void WelfordFinalize(const LocalTensor<float>& outputMean, const LocalTensor<float>& outputVariance, const LocalTensor<float>& inputMean, const LocalTensor<float>& inputVariance, WelfordFinalizePara& para)

–带counts参数场景template <bool isReuseSource = false, const WelfordFinalizeConfig& config = WFFINALIZE_DEFAULT_CFG>__aicore__ inline void WelfordFinalize(const LocalTensor<float>& outputMean, const LocalTensor<float>& outputVariance, const LocalTensor<float>& inputMean, const LocalTensor<float>& inputVariance, const LocalTensor<int32_t>& counts, WelfordFinalizePara& para)

由于该接口的内部实现中涉及复杂的计算，需要额外的临时空间来存储计算过程中的中间变量。临时空间支持接口框架申请和开发者通过sharedTmpBuffer入参传入两种方式。

●接口框架申请临时空间，开发者无需申请，但是需要预留临时空间的大小。

●通过sharedTmpBuffer入参传入，使用该tensor作为临时空间进行处理，接口框架不再申请。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。

接口框架申请的方式，开发者需要预留临时空间；通过sharedTmpBuffer传入的情况，开发者需要为tensor申请空间。临时空间大小BufferSize的获取方式如下：通过6.2.4.4.18 WelfordFinalize Tiling中提供的GetWelfordFinalizeMaxMinTmpSize接口获取所需最大和最小临时空间大小，最小空间可以保证功能正确，最大空间用于提升性能。

<!-- page 2644 -->

参数说明

表6-1203模板参数说明

参数名描述

isReuseSource该参数预留，传入默认值false即可。

config该参数仅支持Atlas 350 加速卡。

结构体模板参数，用于配置相关信息，WelfordFinalizeConfig类型，具体定义如下：struct WelfordFinalizeConfig {     bool isCorrection = false;}

●isCorrection：计算方差时，是否使用修正系数，取值如下：

–false：不使用修正系数，即方差系数为rRec。

–true：使用修正系数rRecWithCorrection。

配置示例如下。constexpr WelfordFinalizeConfig WFFINALIZE_DEFAULT_CFG = { false };

表6-1204接口参数说明

参数名输入/输出

描述

outputMean输出均值目的操作数，数据类型为float。输出的均值为1个数，需要sizeof(float)大小的空间进行保存，根据存储单元的对齐要求，开发者实际需要为outputMean分配32字节对齐的内存空间。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

outputVariance

输出方差目的操作数，数据类型为float。输出的方差为1个数，需要sizeof(float)大小的空间进行保存，根据存储单元的对齐要求，开发者实际需要为outputVariance分配32字节对齐的内存空间。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

inputMean输入均值源操作数，数据类型为float。shape为[abLength]。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

inputVariance

输入方差源操作数，数据类型为float。shape为[abLength]。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

counts输入源操作数，数据类型为int32_t。shape为[abLength]。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

<!-- page 2645 -->

参数名输入/输出

描述

sharedTmpBuffer

输入临时空间，数据类型为uint8_t。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

接口内部复杂计算时用于存储中间变量，由开发者提供。

临时空间大小BufferSize的获取方式请参考WelfordFinalizeTiling。

para输入计算所需的参数信息。WelfordFinalizePara类型，定义如下。struct WelfordFinalizePara {    uint32_t rnLength;    uint32_t abLength;    uint32_t headCount;    uint32_t headCountLength;    uint32_t tailCount;    uint32_t tailCountLength;    float abRec;    float rRec;    float rRecWithCorrection;};

●rnLength：输入的Reduce轴，按abLength为一次计算的大小，拆分的次数。如果拆分后有尾块，则次数向上取整。

●abLength：Reduce轴拆分的大小。在不带counts参数的接口中，abLength=headCountLength+tailCountLength。

●headCount：在不带counts参数的接口中使能该参数，作为公式中非尾块的counts系数，headCount值。

●headCountLength：在不带counts参数的接口中使能该参数，headCount值对应的长度。

●tailCount：在不带counts参数的接口中使能该参数，作为公式中尾块的counts系数，tailCount值。

●tailCountLength：在不带counts参数的接口中使能该参数，tailCount值对应的长度。

●abRec：abLength的倒数，即为1/abLength的值。

●rRec：输入的Reduce轴拆分后，若没有尾块，表示1/(rnLength*abLength)的值，若有尾块，表示1/R的值。

●rRecWithCorrection：输入的方差修正系数，当模板参数config中的isCorrection为true时生效。该参数仅支持Atlas 350 加速卡。

返回值说明

无
