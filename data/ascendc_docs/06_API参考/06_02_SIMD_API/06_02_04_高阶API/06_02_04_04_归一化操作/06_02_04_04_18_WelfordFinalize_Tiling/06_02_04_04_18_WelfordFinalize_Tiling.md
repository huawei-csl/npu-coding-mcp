# WelfordFinalize Tiling

> **Section**: 6.2.4.4.18  
> **PDF Pages**: 2646–2648  

---

<!-- page 2646 -->

约束说明

●接口参数para.abLength的取值必须为32/sizeof(float)的整数倍。

●接口参数para.headCountLength与para.tailCountLength的和必须等于参数para.abLength。

●接口处理逻辑以参数para中设置的具体参数值为准，不依赖源操作数的shape信息。

●接口参数para.tailCount为0时，禁止配置para.tailCountLength为非0值。

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

调用示例

完整的调用样例可参考WelfordFinalize样例。pipe.InitBuffer(sharedTmpBuffer, stackBufferSize);        AscendC::LocalTensor<uint8_t> tmpLocalTensor = sharedTmpBuffer.Get<uint8_t>();         struct AscendC::WelfordFinalizePara para = {rnLength, abLength, head, headLength, tail, tailLength, abRec, rRec};AscendC::WelfordFinalize<false>(meanLocal, varianceLocal, inputMeanLocal, inputVarianceLocal, inputCountsLocal, tmpLocalTensor, para);

// meanLocal：均值目的操作数// varianceLocal：方差目的操作数// inmeanLocal：均值源操作数// invarLocal：方差源操作数// inputXLocal：源操作数// para：计算所需参数信息，WelfordFinalizePara类型

// 计算方差时不使用修正系数static constexpr AscendC::WelfordFinalizeConfig CONFIG = {false};AscendC::WelfordFinalizePara para = { rnLength, abLength, head, headLength, tail, tailLength, abRec, rRec, rRecWithCorrection};AscendC::WelfordFinalize<false, CONFIG>(meanLocal, varianceLocal, inmeanLocal, invarLocal, inputXLocal, para);

示例结果如下：输入数据(inmeanLocal, shape:[1, 32]): [  0.0  1.0  2.0  3.0  4.0  5.0  6.0  7.0  8.0  9.0 10.0 11.0 12.0 13.0 14.0 15.0   16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0 25.0 26.0 27.0 28.0 29.0 30.0 31.0 ]输入数据(invarLocal, shape:[1, 32]): [  0.0  1.0  2.0  3.0  4.0  5.0  6.0  7.0  8.0  9.0 10.0 11.0 12.0 13.0 14.0 15.0   16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0 25.0 26.0 27.0 28.0 29.0 30.0 31.0 ]输入数据(inputX, shape:[1, 32]): [ 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 ]输出数据(meanLocal): [ 0.484375 0.       0.       0.       0.       0.       0.       0.      ]输出数据(varianceLocal): [ 9.831062 0.       0.       0.       0.       0.       0.       0.      ]

## 6.2.4.4.18 WelfordFinalize Tiling

功能说明

Ascend C提供WelfordFinalize Tiling API，方便用户获取WelfordFinalize kernel计算时所需的Tiling参数。

获取Tiling参数主要步骤如下：

具体为，通过GetWelfordFinalizeMaxMinTmpSize获取WelfordFinalize接口计算所需最大和最小临时空间大小。

<!-- page 2647 -->

kernel侧WelfordFinalize接口的计算需要开发者预留/申请临时空间，GetWelfordFinalizeMaxMinTmpSize用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetWelfordFinalizeMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1205 GetWelfordFinalizeMaxMinTmpSize 接口参数说明

参数名输入/输出

描述

srcShape输入输入inputMean/inputVariance的shape信息{abLength}。

typeSize输入输入inputMean/inputVariance的数据类型大小，单位为字节。比如输入的数据类型为float，此处应传入4。

isReuseSource

输入是否允许修改源操作数。该参数取值与WelfordFinalize接口一致。

maxValue输出WelfordFinalize接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出WelfordFinalize接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

<!-- page 2648 -->

调用示例

步骤1将WelfordFinalizeTiling结构体参数增加至TilingData结构体，作为TilingData结构体的一个字段。

BEGIN_TILING_DATA_DEF(WelfordFinalizeCustomTilingData) // 注册一个tiling的类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, isCounts); // 添加tiling字段  TILING_DATA_FIELD_DEF(uint32_t, rnLength);  TILING_DATA_FIELD_DEF(uint32_t, abLength);  TILING_DATA_FIELD_DEF(uint32_t, rLength);  TILING_DATA_FIELD_DEF(uint32_t, head);  TILING_DATA_FIELD_DEF(uint32_t, headLength);  TILING_DATA_FIELD_DEF(uint32_t, tail);  TILING_DATA_FIELD_DEF(uint32_t, tailLength);END_TILING_DATA_DEF;REGISTER_TILING_DATA_CLASS(WelfordFinalizeCustom, WelfordFinalizeCustomTilingData)// 将WelfordFinalizeCustomTilingData结构体参数增加至TilingData结构体

步骤2Tiling实现函数中，首先调用GetWelfordFinalizeMaxMinTmpSize接口获取WelfordFinalize接口能完成计算所需最大/最小临时空间大小，根据该范围结合实际的内存使用情况设置合适的空间大小，然后根据输入shape、剩余的可供计算的空间大小等信息获取WelfordFinalize kernel侧接口所需tiling参数。

```cpp
namespace optiling {static ge::graphStatus TilingFunc(gert::TilingContext *context){    WelfordFinalizeCustomTilingData tiling;
    const gert::RuntimeAttrs *attrs = context->GetAttrs();
    const uint32_t isCounts = *(attrs->GetAttrPointer<uint32_t>(0));
    const uint32_t rnLength = *(attrs->GetAttrPointer<uint32_t>(1));
    const uint32_t abLength = *(attrs->GetAttrPointer<uint32_t>(2));
    const uint32_t rLength = *(attrs->GetAttrPointer<uint32_t>(3));
    const uint32_t head = *(attrs->GetAttrPointer<uint32_t>(4));
    const uint32_t headLength = *(attrs->GetAttrPointer<uint32_t>(5));
    const uint32_t tail = *(attrs->GetAttrPointer<uint32_t>(6));
    const uint32_t tailLength = *(attrs->GetAttrPointer<uint32_t>(7));
std::vector<int64_t> srcDims = {abLength};
    ge::Shape srcShape(srcDims);
```

// 本样例中仅作为样例说明，通过GetWelfordFinalizeMaxMinTmpSize获取最小值并传入，来保证功能正确，开发者可以根据需要传入合适的空间大小    uint32_t maxTmpsize = 0;    uint32_t minTmpsize = 0;    AscendC::GetWelfordFinalizeMaxMinTmpSize(srcShape, 4, false, maxTmpsize, minTmpsize);

// auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    // AscendC::GetWelfordFinalizeMaxMinTmpSize(srcShape, 4, false, ascendcPlatform, maxTmpsize, minTmpsize);    ... // 其他逻辑    context->SetTilingKey(1);    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    size_t *currentWorkspace = context->GetWorkspaceSizes(1);    currentWorkspace[0] = 0;    return ge::GRAPH_SUCCESS;}} // namespace optiling

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的WelfordFinalize Tiling信息传入WelfordFinalize接口参与计算。完整的kernel侧样例请参考6.2.4.4.17 WelfordFinalize。

```cpp
extern "C" __global__ __aicore__ voidwelford_finalize_custom(    GM_ADDR inputX_gm, GM_ADDR mean_gm, GM_ADDR var_gm, GM_ADDR outputMean_gm, GM_ADDR outputVariance_gm, GM_ADDR workspace, GM_ADDR tiling){
```
