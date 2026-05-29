# End

> **Section**: 10  
> **PDF Pages**: 3010–3010  

---

<!-- page 3010 -->

参数说明

参数名输入/输出描述

output输入Output在GM上的地址。类型为GlobalTensor。结果矩阵Output支持的数据类型为：half、bfloat16_t。

enPartialSum输入预留参数。

返回值说明

无

约束说明

●IterateAll接口仅支持处理单batch数据，在多batch计算场景中，需要通过batch次循环调用IterateAll接口完成计算。for (uint64_t batchIter = 0; batchIter < singleCoreBatch; ++batchIter) {    conv3dApi.SetInput(inputGm[batchIter * inputOneBatchSize]);    conv3dApi.IterateAll(outputGm[batchIter * outputOneBatchSize]);    conv3dApi.End();}

●IterateAll接口必须在初始化接口及输入输出配置接口之后进行调用，完成Conv3D计算，调用顺序如下。Init(...);... // 输入输出配置IterateAll(...);End();

调用示例

```cpp
TPipe pipe;conv3dApi.Init(&tiling);conv3dApi.SetWeight(weightGm);if (biasFlag) {    conv3dApi.SetBias(biasGm);}conv3dApi.SetInputStartPosition(diIdxStart, mIdxStart);conv3dApi.SetSingleOutputShape(singleCoreCout, singleCoreDout, singleCoreM);for (uint64_t batchIter = 0;
 batchIter < singleCoreBatch; ++batchIter) {    conv3dApi.SetInput(inputGm[batchIter * inputOneBatchSize]);
    conv3dApi.IterateAll(outputGm[batchIter * outputOneBatchSize]);
    conv3dApi.End();}
```

## ?.10. End

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√
