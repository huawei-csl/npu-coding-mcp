# Conv3D模板参数

> **Section**: 2  
> **PDF Pages**: 3001–3002  

---

<!-- page 3001 -->

步骤3设置3D卷积的输入Input、Weight、Bias和输出Output。

conv3dApi.SetWeight(weightGm);               // 设置当前核的输入weight在gm上的地址if (biasFlag) {    conv3dApi.SetBias(biasGm);               // 设置当前核的输入bias在gm上的地址}// 设置input各个维度在当前核的偏移conv3dApi.SetInputStartPosition(diStartPos, mStartPos);// 设置当前核的cout,dout,m大小conv3dApi.SetSingleOutputShape(singleCoreCout, singleCoreDout, singleCoreM);

// 当前Conv3D仅支持单batch的卷积计算，多batch场景通过for循环实现，在循环间计算当前batch的地址偏移for (uint64_t batchIter = 0; batchIter < singleCoreBatch; ++batchIter) {    conv3dApi.SetInput(inputGm[batchIter * inputOneBatchSize]);    // 设置当前核的输入input在gm上的地址}

步骤4完成3D卷积操作。

调用IterateAll完成单核上所有数据的计算。for (uint64_t batchIter = 0; batchIter < singleCoreBatch; ++batchIter) {    ...    conv3dApi.IterateAll(outputGm[batchIter * outputOneBatchSize]);    // 调用IterateAll完成Conv3D计算    ...}

步骤5结束3D卷积操作。

for (uint64_t batchIter = 0; batchIter < singleCoreBatch; ++batchIter) {    ...    conv3dApi.End();    //清除EventID和释放内部申请的临时内存}

**----结束**

需要包含的头文件

```cpp
#include "lib/conv/conv3d/conv3d_api.h"
```

## ?.2. Conv3D 模板参数

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

创建Conv3D对象时需要传入：

<!-- page 3002 -->

●Input、Weight、Output和Bias（可选）的参数类型信息，类型信息通过ConvType来定义，包括：内存逻辑位置、数据格式、数据类型。

●Conv3dParam信息（可选），用于使能不同场景的性能优化模板。当前暂不支持使用。

函数原型

```cpp
template <class INPUT_TYPE, class WEIGHT_TYPE, class OUTPUT_TYPE, class BIAS_TYPE = biasType, class CONV_CFG = Conv3dParam>using Conv3D = Conv3dIntfExt<Config<ConvApi::ConvDataType<INPUT_TYPE, WEIGHT_TYPE, OUTPUT_TYPE, BIAS_TYPE, CONV_CFG>>, Impl, Intf>
```

参数说明

表6-1394模板参数说明

参数名输入/输出描述

INPUT_TYPE输入ConvType类型模板参数，指定Input的参数类型信息。

WEIGHT_TYPE输入ConvType类型模板参数，指定Weight的参数类型信息。

OUTPUT_TYPE输入ConvType类型模板参数，指定Output的参数类型信息。

BIAS_TYPE可选输入ConvType类型模板参数，指定Bias的参数类型信息。

CONV_CFG可选输入ConvParam类型模板参数，用于使能不同场景的性能优化模板，当前版本只支持基础模板，不使能性能优化。

返回值说明

无

约束说明

无

调用示例

```cpp
#include "lib/conv/conv3d/conv3d_api.h"
```

using inputType = ConvApi::ConvType<AscendC::TPosition::GM, ConvFormat::NDC1HWC0, bfloat16_t>;using weightType = ConvApi::ConvType<AscendC::TPosition::GM, ConvFormat::FRACTAL_Z_3D, bfloat16_t>;using outputType = ConvApi::ConvType<AscendC::TPosition::GM, ConvFormat::NDC1HWC0, bfloat16_t>;using biasType = ConvApi::ConvType<AscendC::TPosition::GM, ConvFormat::ND, float>; // 可选参数，如果不带Bias场景，可以不传struct ConvCustom : public ConvApi::ConvParam {    __aicore__ inline ConvCustom(){};}; // 可选参数，当前版本只支持基础模板，不使能性能优化，可以不传

```cpp
Conv3dApi::Conv3D<inputType, weightType, outputType, biasType, ConvCustom> conv3dApi;
```
