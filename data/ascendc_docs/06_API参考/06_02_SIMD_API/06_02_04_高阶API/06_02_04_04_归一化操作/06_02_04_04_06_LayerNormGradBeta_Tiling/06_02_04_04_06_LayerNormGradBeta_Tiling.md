# LayerNormGradBeta Tiling

> **Section**: 6.2.4.4.6  
> **PDF Pages**: 2601–2604  

---

<!-- page 2601 -->

●源操作数和目的操作数的Tensor空间可以复用。

●仅支持输入shape为ND格式。

●输入数据不满足对齐要求时，开发者需要进行补齐，补齐的数据应设置为0，防止出现异常值从而影响网络计算。

●不支持对尾轴H轴的切分。

调用示例

完整的调用样例可参考LayerNormGradBeta样例。

// outputPdGamma: 输出对 gamma 参数的梯度，shape 为 [H]// outputPdBeta: 输出对 beta 参数的梯度，shape 为 [H]// resForGamma: 前一步 LayerNormGrad 输出的中间结果，即 normalizedX * inputDy，shape 为 [B, S, H]// inputDy: 上游传入的梯度，shape 为 [B, S, H]// tiling: Tiling 调度信息，包含并行划分、块大小等参数

// 使用 LayerNormGradBeta 接口计算 gamma 和 beta 的梯度AscendC::LayerNormGradBeta<T, isReuseSource>(    outputPdGamma,   // 输出：gamma 的梯度，shape [H]    outputPdBeta,    // 输出：beta 的梯度，shape [H]    resForGamma,     // 输入：中间结果 normalizedX * inputDy，来自 LayerNormGrad    inputDy,         // 输入：上游梯度 dy，shape [B, S, H]    tiling           // 输入：Tiling信息);

示例结果如下：输入数据(inputDy, shape:[1, 8, 8]): [  0.  1.  2.  3.  4.  5.  6.  7.   8.  9. 10. 11. 12. 13. 14. 15.  16. 17. 18. 19. 20. 21. 22. 23.  24. 25. 26. 27. 28. 29. 30. 31.  32. 33. 34. 35. 36. 37. 38. 39.  40. 41. 42. 43. 44. 45. 46. 47.  48. 49. 50. 51. 52. 53. 54. 55.  56. 57. 58. 59. 60. 61. 62. 63. ]输入数据(resForGamma, shape:[1, 8, 8]): [  0.  1.  2.  3.  4.  5.  6.  7.   8.  9. 10. 11. 12. 13. 14. 15.  16. 17. 18. 19. 20. 21. 22. 23.  24. 25. 26. 27. 28. 29. 30. 31.  32. 33. 34. 35. 36. 37. 38. 39.  40. 41. 42. 43. 44. 45. 46. 47.  48. 49. 50. 51. 52. 53. 54. 55.  56. 57. 58. 59. 60. 61. 62. 63. ]输出数据(outputPdGamma): [ 8960.  9416.  9888. 10376. 10880. 11400. 11936. 12488.]输出数据(outputPdBeta): [ 224. 232. 240. 248. 256. 264. 272. 280. ]

## 6.2.4.4.6 LayerNormGradBeta Tiling

功能说明

LayerNormGradBeta Tiling的功能如下：

●在host侧获取预留/申请的最大最小临时空间大小：

kernel侧LayerNormGradBeta接口的计算需要开发者预留/申请临时空间，GetLayerNormGradBetaMaxMinTmpSize接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

<!-- page 2602 -->

–为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

–在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

●通过GetLayerNormGradBetaNDTilingInfo获取LayerNormGradBeta kernel侧接口所需tiling参数，需要传入输入shape，剩余的可供LayerNormGradBeta接口计算的空间大小和计算的数据类型。

LayerNormGradBeta Tiling结构体的定义如下，开发者无需关注该Tiling结构的具体信息，只需要传递到kernel侧，传入LayerNormGradBeta高阶API接口，直接进行使用即可。

```cpp
struct LayerNormGradBetaTiling {    uint32_t stackBufferSize = 0;
    uint32_t bLength = 0;
    uint32_t sLength = 0;
    uint32_t hLength = 0;
    uint32_t originalHLength = 0;
    uint32_t bshLength = 0;
    uint32_t bsLength = 0;
    uint32_t oneCalSize = 0;
    uint32_t numberOfTmpBuf = 0;
    uint32_t loopRound = 0;
    uint32_t inputTailSize = 0;
    uint32_t inputTailPos = 0;
    uint32_t bsTailSize = 0;
    uint32_t bshCurLength = 0;
    uint32_t bsCurLength = 0;
    uint32_t gammaTempTensorPos = 0;
    uint32_t betaTempTensorPos = 0;
    uint32_t inputDyTmpTensorPos = 0;
    uint32_t resForGammaTmpTensorPos = 0;
    uint32_t reserved = 0;};
```

函数原型

```cpp
void GetLayerNormGradBetaMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)void GetLayerNormGradBetaNDTilingInfo(const ge::Shape srcShape, const uint32_t stackBufferSize, const uint32_t typeSize, const bool isReuseSource, optiling::LayerNormGradBetaTiling& tiling)void GetLayerNormGradBetaNDTilingInfo(const ge::Shape srcShape, const uint32_t stackBufferSize, const uint32_t typeSize, const bool isReuseSource, AscendC::tiling::LayerNormGradBetaTiling& tiling)
```

参数说明

表6-1185 GetLayerNormGradBetaMaxMinTmpSize 接口参数列表

参数名称输入/输出含义

srcShape输入输入数据inputDy的shape信息{B, S,storageHLength, originHLength}，包括当前输入的inputDy的shape信息，以及地址对齐前（如存在H轴补齐操作）的原有shape信息。

在API支持的场景下，storageHLength和originHLength保持一致。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

<!-- page 2603 -->

参数名称输入/输出含义

isReuseSource输入是否复用源操作数的内存空间，与LayerNorm接口一致。

maxValue输出LayerNormGradBeta接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出LayerNormGradBeta接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

表6-1186 GetLayerNormGradBetaNDTilingInfo 接口参数列表

参数名称输入/输出含义

srcShape输入输入数据inputDy的shape信息，包括当前输入的shape信息，以及地址对齐前的原有shape信息。

stackBufferSize

输入可供接口使用的空间大小，单位为元素个数。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource输入是否可以复用inputDy的内存空间。

tiling输出输入数据的切分信息。

返回值说明

无

约束说明

无

调用示例

如下样例介绍了使用LayerNormGradBeta高阶API时host侧获取Tiling参数的流程以及该参数如何在kernel侧使用。样例中输入Tensor的shape大小为[2, 16, 64]，输入的数据类型为half。

<!-- page 2604 -->

步骤1将LayerNormGradBetaTiling结构体参数增加至TilingData结构体，作为TilingData结构体的一个字段。

BEGIN_TILING_DATA_DEF(TilingData)               // 注册一个tiling的类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, totalLength); // 添加tiling字段，总计算数据量  TILING_DATA_FIELD_DEF(uint32_t, tileNum);     // 添加tiling字段，每个核上总计算数据分块个数  ...                                           // 添加其他tiling字段TILING_DATA_FIELD_DEF_STRUCT(LayerNormGradBetaTiling, layernormGradBetaTilingData); // 将LayerNormGradBetaTiling结构体参数增加至TilingData结构体END_TILING_DATA_DEF;

步骤2Tiling实现函数中，首先调用GetLayerNormGradBetaMaxMinTmpSize接口获取LayerNormGradBeta接口能完成计算所需最大/最小临时空间大小，根据该范围结合实际的内存使用情况设置合适的空间大小，然后调用GetLayerNormGradBetaNDTilingInfo接口根据输入shape、剩余的可供计算的空间大小等信息获取LayerNormGradBeta kernel侧接口所需tiling参数。

namespace optiling {const uint32_t NUM_BLOCKS = 8;const uint32_t TILE_NUM = 8;static ge::graphStatus TilingFunc(gert::TilingContext* context){    TilingData tiling;    uint32_t totalLength = context->GetInputTensor(0)->GetShapeSize();    context->SetBlockDim(NUM_BLOCKS);    tiling.set_totalLength(totalLength);    tiling.set_tileNum(TILE_NUM);    // 设置其他Tiling参数    ...    // {B, S, storageHLength, originHLength}    std::vector<int64_t> shapeVec = {2, 16, 64, 64};    ge::Shape srcShape(shapeVec);    // 本样例中仅作为样例说明，通过GetLayerNormGradBetaMaxMinTmpSize获取最小值并传入，来保证功能正确，开发者可以根据需要传入合适的空间大小    uint32_t max;    uint32_t min;    AscendC::GetLayerNormGradBetaMaxMinTmpSize(srcShape, sizeof(half), false, max, min);    // 获取LayerNormGradBeta Tiling参数    AscendC::GetLayerNormGradBetaNDTilingInfo(srcShape, min, sizeof(half), false, tiling.layernormGradBetaTilingData);     ... // 其他逻辑    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    context->SetTilingKey(1);    return ge::GRAPH_SUCCESS;}} // namespace optiling

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的LayerNormGradBetaTiling信息传入LayerNormGradBeta接口参与计算。完整的kernel侧样例请参考6.2.4.4.5 LayerNormGradBeta。

extern "C" __global__ __aicore__ void func_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling){    GET_TILING_DATA(tilingData, tiling);    KernelFunc op;    op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum,tilingData.layernormGradBetaTilingData);    if (TILING_KEY_IS(1)) {        op.Process();    }}

**----结束**
