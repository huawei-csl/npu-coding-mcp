# AntiQuantize

> **Section**: 6.2.4.5.16  
> **PDF Pages**: 2719–2723  

---

<!-- page 2719 -->

## 6.2.4.5.16 AntiQuantize

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

按元素做伪量化计算，比如将int8_t数据类型伪量化为half数据类型。本接口最多支持输入为二维数据，不支持更高维度的输入。

AntiQuantize与AscendAntiQuant的功能类似，本接口在不同量化场景下的形式更统一，因此推荐使用本接口。

本接口的伪量化策略包括PER_TENSOR，PER_CHANNEL，PER_TOKEN，PER_GROUP四种，反量化系数scale、offset在PER_TENSOR场景下为标量，其余场景下为矢量，计算公式如下：

●PER_TENSOR场景（按张量量化）：scale和offset的shape为[1]。

![p2719_img001.png](../../../images/p2719_img001.png)

●PER_CHANNEL场景（按通道量化）：srcTensor的shape为[m, n]，每个channel维度对应一个量化参数，scale和offset的shape为[1, n]。

![p2719_img002.png](../../../images/p2719_img002.png)

●PER_TOKEN场景（按token量化）：srcTensor的每组token（token为n方向，共有m组token）中的元素共享一个量化参数，srcTensor的shape为[m, n]时，scale和offset的shape为[m, 1]。

![p2719_img003.png](../../../images/p2719_img003.png)

●PER_GROUP场景（按组量化）：定义group的计算方向为k方向，srcTensor在k方向上每groupSize个元素共享一组scale和offset。srcTensor的shape为[m, n]时，如果kDim=0，表示k是m方向，scale和offset的shape为[(m + groupSize -1) / groupSize, n]；如果kDim=1，表示k是n方向，scale和offset的shape为[m，(n + groupSize - 1) / groupSize]。

根据输入数据类型的不同，PER_GROUP分为两种场景：fp4x2_e2m1_t/fp4x2_e1m2_t场景（后续内容中简称为float4场景）和int8_t/hifloat8_t/fp8_e5m2_t/fp8_e4m3fn_t场景（后续内容中简称为b8场景）。

<!-- page 2720 -->

–fp4x2_e2m1_t/fp4x2_e1m2_t场景（float4场景）▪k为m方向，即公式中i轴为group的计算方向（kDim=0）：

![p2720_img001.png](../../../images/p2720_img001.png)

▪k为n方向，即公式中j轴为group的计算方向（kDim=1）：

![p2720_img002.png](../../../images/p2720_img002.png)

–int8_t/hifloat8_t/fp8_e5m2_t/fp8_e4m3fn_t场景（b8场景）▪k为m方向，即公式中i轴为group的计算方向（kDim=0）：

![p2720_img003.png](../../../images/p2720_img003.png)

▪k为n方向，即公式中j轴为group的计算方向（kDim=1）：

![p2720_img004.png](../../../images/p2720_img004.png)

函数原型

●通过sharedTmpBuffer入参传入临时空间template <const AntiQuantizeConfig& config, typename DstT, typename SrcT, typename ScaleT, typename OffsetT>__aicore__ inline void AntiQuantize(const LocalTensor<DstT>& dstTensor, const LocalTensor<SrcT>& srcTensor, const ScaleT& scale, const OffsetT& offset, const LocalTensor<uint8_t>& sharedTmpBuffer, const AntiQuantizeParams& params)

●接口框架申请临时空间template <const AntiQuantizeConfig& config, typename DstT, typename SrcT, typename ScaleT, typename OffsetT>__aicore__ inline void AntiQuantize(const LocalTensor<DstT>& dstTensor, const LocalTensor<SrcT>& srcTensor, const ScaleT& scale, const OffsetT& offset, const AntiQuantizeParams& params)

由于该接口的内部实现中涉及复杂的数学计算，需要额外的临时空间来存储计算过程中的中间变量。临时空间支持接口框架申请和开发者通过sharedTmpBuffer入参传入两种方式。

●接口框架申请临时空间，开发者无需申请，但是需要预留临时空间的大小。

●通过sharedTmpBuffer入参传入，使用该tensor作为临时空间进行处理，接口框架不再申请。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。

接口框架申请的方式，开发者需要预留临时空间；通过sharedTmpBuffer传入的情况，开发者需要为sharedTmpBuffer申请空间。临时空间大小BufferSize的获取方式如下：通过6.2.4.5.17 GetAntiQuantizeMaxMinTmpSize中提供的接口获取需要预留空间的范围大小。

<!-- page 2721 -->

参数说明

表6-1245模板参数说明

参数名描述

config用于配置伪量化相关信息，AntiQuantizeConfig类型，具体定义如下。struct AntiQuantizeConfig {    AntiQuantizePolicy policy;    bool hasOffset;    int32_t kDim = 1; }

●policy：用于配置量化策略，枚举类型，具体定义如下。enum class AntiQuantizePolicy : int32_t {    PER_TENSOR,    PER_CHANNEL,    PER_TOKEN,    PER_GROUP}

●hasOffset：用于配置offset是否参与计算。

–true：表示offset参与计算。

–false：表示offset不参与计算。

●kDim：group的计算方向，即k方向。仅在PER_GROUP场景有效，支持的取值如下。

–0：k轴是第0轴，即m方向为group的计算方向。

–1：k轴是第1轴，即n方向为group的计算方向。

DstT目的操作数的数据类型。接口内根据入参dstTensor自动推导数据类型，开发者无需配置该参数，保证dstTensor满足表3 输入输出支持的数据类型组合即可。

SrcT源操作数的数据类型。接口内根据入参srcTensor自动推导数据类型，开发者无需配置该参数，保证srcTensor满足表3 输入输出支持的数据类型组合即可。

ScaleTscale的数据类型。接口内根据入参scale自动推导数据类型，开发者无需配置该参数。ScaleT可以为标量数据类型或LocalTensor类型。

注意：

●对于PER_TENSOR场景，scale为标量，ScaleT只能为标量数据类型。

●对于PER_CHANNEL、PER_TOKEN、PER_GROUP场景，scale为矢量，ScaleT只能为LocalTensor类型。

OffsetToffset的数据类型。接口内根据入参offset自动推导数据类型，开发者无需配置该参数。OffsetT可以为标量数据类型或LocalTensor类型。

注意：

●对于PER_TENSOR量化策略，offset为标量，OffsetT只能为标量数据类型。

●对于PER_CHANNEL、PER_TOKEN、PER_GROUP量化策略，offset为矢量，OffsetT只能为LocalTensor类型。

<!-- page 2722 -->

表6-1246接口参数说明

参数名输入/输出

描述

dstTensor输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

srcTensor输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

scale输入输入数据伪量化时的缩放因子。

offset输入输入数据伪量化时的偏移量。

Atlas 350 加速卡，对于PER_GROUP量化的float4场景，offset不生效。

sharedTmpBuffer

输入临时缓存。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

临时空间大小BufferSize的获取方式请参考6.2.4.5.17GetAntiQuantizeMaxMinTmpSize。

params输入量化接口的参数，AntiQuantizeParams类型，具体定义如下。struct AntiQuantizeParams {        uint32_t m;        uint32_t n;        uint32_t groupSize = 0;}

●m：m方向元素个数。

●n：n方向元素个数。n值对应的数据大小需满足32字节对齐的要求，即shape最后一维为n的输入或输出均需要满足该维度上32字节对齐的要求。

●groupSize：PER_GROUP场景有效，表示groupSize行/列数据共用一个scale/offset。groupSize的取值必须大于0且是32的整倍数。

表6-1247输入输出支持的数据类型组合

量化策略SrcTScaleT/OffsetTDstT

PER_TENSOR/PER_CHANNEL

fp8_e4m3fn_thalfhalf

fp8_e5m2_thalfhalf

hifloat8_thalfhalf

int8_thalfhalf

fp8_e4m3fn_tbfloat16_tbfloat16_t

fp8_e5m2_tbfloat16_tbfloat16_t

hifloat8_tbfloat16_tbfloat16_t

<!-- page 2723 -->

量化策略SrcTScaleT/OffsetTDstT

int8_tbfloat16_tbfloat16_t

PER_TOKEN/PER_GROUP

int8_thalfhalf

bfloat16_tbfloat16_t

floatfloat

floathalf

floatbfloat16_t

hifloat8_thalfhalf

bfloat16_tbfloat16_t

floatfloat

floathalf

floatbfloat16_t

fp8_e5m2_t/fp8_e4m3fn_t

halfhalf

bfloat16_tbfloat16_t

floatfloat

floathalf

floatbfloat16_t

fp8_e8m0_thalf

fp4x2_e1m2_t/fp4x2_e2m1_t

bfloat16_t

（当前均只支持PER_GROUP场景）

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

●输入输出操作数参与计算的数据长度要求32字节对齐。

●连续计算方向（即n方向）的数据量要求32字节对齐。

●PER_GROUP量化的float4场景不支持offset，该场景下模板参数config中的hasOffset参数必须配置为false。
