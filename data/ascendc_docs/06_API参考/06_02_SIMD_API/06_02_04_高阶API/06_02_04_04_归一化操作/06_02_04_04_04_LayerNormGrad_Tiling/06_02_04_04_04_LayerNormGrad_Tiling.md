# LayerNormGrad Tiling

> **Section**: 6.2.4.4.4  
> **PDF Pages**: 2594–2597  

---

<!-- page 2594 -->

sharedTmpBuffer,  // 输入：开发者提供的临时空间（需通过 GetLayerNormGradMaxMinTmpSize 获取大小）    epsilon,          // 输入：防除零系数ε    tiling,           // 输入：Tiling 信息，由 Tiling 工具生成    {DataFormat::ND}  // 输入：shapeInfo，默认为 DataFormat::ND);

示例结果如下：输入数据(inputDy, shape:[1, 8, 8]): [  0.  1.  2.  3.  4.  5.  6.  7.   8.  9. 10. 11. 12. 13. 14. 15.  16. 17. 18. 19. 20. 21. 22. 23.  24. 25. 26. 27. 28. 29. 30. 31.  32. 33. 34. 35. 36. 37. 38. 39.  40. 41. 42. 43. 44. 45. 46. 47.  48. 49. 50. 51. 52. 53. 54. 55.  56. 57. 58. 59. 60. 61. 62. 63. ]输入数据(inputX, shape:[1, 8, 8]): [  0.  1.  2.  3.  4.  5.  6.  7.   8.  9. 10. 11. 12. 13. 14. 15.  16. 17. 18. 19. 20. 21. 22. 23.  24. 25. 26. 27. 28. 29. 30. 31.  32. 33. 34. 35. 36. 37. 38. 39.  40. 41. 42. 43. 44. 45. 46. 47.  48. 49. 50. 51. 52. 53. 54. 55.  56. 57. 58. 59. 60. 61. 62. 63. ]输入数据(inputMean, shape:[8]): [ 3.5 11.5 19.5 27.5 35.5 43.5 51.5 59.5 ]输入数据(inputVariance, shape:[8]): [ 5.25 5.25 5.25 5.25 5.25 5.25 5.25 5.25 ]输入数据(inputGamma, shape:[8]): [ 0. 1. 2. 3. 4. 5. 6. 7. ]输出数据(outputPdX): [ 3.0548172 0.4362857 -1.3093826 -2.182187 -2.1821284 -1.309207 0.4365778 3.0552254 3.0545845 0.4361186 -1.3094826 -2.1822214 -2.1820965 -1.3091087 0.4367447 3.055458 3.0543518 0.4359522 -1.3095818 -2.1822548 -2.182064 -1.3090096 0.43690872 3.055687 3.054119 0.43578815 -1.309679 -2.1822853 -2.182026 -1.3089066 0.437088 3.0559235 3.0538864 0.43562222 -1.3097801 -2.1823158 -2.1819916 -1.3088074 0.43724823 3.05616 3.0536423 0.4354477 -1.3098869 -2.1823578 -2.181961 -1.3087158 0.43740845 3.0563965 3.0534134 0.43528175 -1.3099861 -2.1823883 -2.1819305 -1.308609 0.43756104 3.0566254 3.0531921 0.43511963 -1.3100777 -2.1824188 -2.1818848 -1.3085022 0.43774414 3.0568542 ]输出数据(resForGamma): [ -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 -1.5275106 -1.091079 -0.6546474 -0.21821581 0.21821581 0.6546474 1.091079 1.5275106 ]

## 6.2.4.4.4 LayerNormGrad Tiling

功能说明

LayerNormGrad Tiling的功能如下：

●在host侧获取预留/申请的最大最小临时空间大小：

kernel侧LayerNormGrad接口的计算需要开发者预留/申请临时空间，GetLayerNormGradMaxMinTmpSize接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

–为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

<!-- page 2595 -->

–在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

●通过GetLayerNormGradNDTilingInfo获取LayerNormGrad kernel侧接口所需tiling参数，需要传入输入shape，剩余的可供LayerNormGrad接口计算的空间大小和计算的数据类型。

LayerNormGrad Tiling结构体的定义如下，开发者无需关注该Tiling结构的具体信息，只需要传递到kernel侧，传入LayerNormGrad高阶API接口，直接进行使用即可。

```cpp
struct LayerNormGradTiling {    uint32_t stackBufferSize = 0;
    uint32_t bLength = 0;
    uint32_t sLength = 0;
    uint32_t hLength = 0;
    uint32_t originalHLength = 0;
    uint32_t oneCalSize = 0;
    uint32_t nohCalSize = 0;
    uint32_t loopNum = 0;
    uint32_t tailSize = 0;
    uint32_t nohTailSize = 0;
    uint32_t tmpTensorBSHPos = 0;
    uint32_t tmpTensorBSHSize = 0;
    uint32_t pdVarTensorPos = 0;
    uint32_t pdVarTensorSize = 0;
    uint32_t pdMeanTensorPos = 0;
    uint32_t pdMeanTensorSize = 0;
    uint32_t x1TensorPos = 0;
    uint32_t x1TensorSize = 0;
    uint32_t x2TensorPos = 0;
    uint32_t x2TensorSize = 0;
    uint32_t x3TensorPos = 0;
    uint32_t x3TensorSize = 0;
    uint32_t tmpTensorPos = 0;
    uint32_t tmpTensorSize = 0;
    uint32_t tmpTensor1Pos = 0;
    uint32_t tmpTensor1Size = 0;
    uint32_t tmpTensor2Pos = 0;
    uint32_t tmpTensor2Size = 0;
    uint32_t lastDimValueBack = 0;
    uint32_t lastDimValueBackMulTwo = 0;};
```

函数原型

```cpp
void GetLayerNormGradMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
void GetLayerNormGradNDTilingInfo(const ge::Shape srcShape, const uint32_t stackBufferSize, const uint32_t typeSize, const bool isReuseSource, optiling::LayerNormGradTiling& tiling)void GetLayerNormGradNDTilingInfo(const ge::Shape srcShape, const uint32_t stackBufferSize, const uint32_t typeSize, const bool isReuseSource, AscendC::tiling::LayerNormGradTiling& tiling)
```

<!-- page 2596 -->

参数说明

表6-1181 GetLayerNormGradMaxMinTmpSize 接口参数列表

参数名称输入/输出含义

srcShape输入输入数据inputDy的shape信息{B, S,storageHLength, originHLength}，包括当前输入的inputDy的shape信息，以及地址对齐前（如存在H轴补齐操作）的原有shape信息。

在API支持的场景下，storageHLength和originHLength保持一致。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource输入是否复用源操作数的内存空间，与LayerNorm接口一致。

maxValue输出LayerNormGrad接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出LayerNormGrad接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

表6-1182 GetLayerNormGradNDTilingInfo 接口参数列表

参数名称输入/输出含义

srcShape输入输入数据inputDy的shape信息，包括当前输入的shape信息，以及地址对齐前的原有shape信息

stackBufferSize

输入可供接口使用的空间大小，单位元素个数

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource输入是否可以复用inputX和inputDy的内存空间

tiling输出输入数据的切分信息

<!-- page 2597 -->

返回值说明

无

约束说明

无

调用示例

如下样例介绍了使用LayerNormGrad高阶API时host侧获取Tiling参数的流程以及该参数如何在kernel侧使用。样例中输入Tensor的shape大小为[2, 16, 64]，输入的数据类型为half。

步骤1将LayerNormGradTiling结构体参数增加至TilingData结构体，作为TilingData结构体的一个字段。

BEGIN_TILING_DATA_DEF(TilingData)               // 注册一个tiling的类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, totalLength); // 添加tiling字段，总计算数据量  TILING_DATA_FIELD_DEF(uint32_t, tileNum);     // 添加tiling字段，每个核上总计算数据分块个数  ...                                           // 添加其他tiling字段TILING_DATA_FIELD_DEF_STRUCT(LayerNormGradTiling, layernormGradTilingData); // 将LayerNormGradTiling结构体参数增加至TilingData结构体END_TILING_DATA_DEF;

步骤2Tiling实现函数中，首先调用GetLayerNormGradMaxMinTmpSize接口获取LayerNormGrad接口能完成计算所需最大/最小临时空间大小，根据该范围结合实际的内存使用情况设置合适的空间大小，然后调用GetLayerNormGradNDTilingInfo接口根据输入shape、剩余的可供计算的空间大小等信息获取LayerNormGradBeta kernel侧接口所需tiling参数。

namespace optiling {const uint32_t NUM_BLOCKS = 8;const uint32_t TILE_NUM = 8;static ge::graphStatus TilingFunc(gert::TilingContext* context){    TilingData tiling;    uint32_t totalLength = context->GetInputTensor(0)->GetShapeSize();    context->SetBlockDim(NUM_BLOCKS);    tiling.set_totalLength(totalLength);    tiling.set_tileNum(TILE_NUM);    // 设置其他Tiling参数    ...    // {B, S, storageHLength, originHLength}    std::vector<int64_t> shapeVec = {2, 16, 64, 64};    ge::Shape srcShape(shapeVec);    // 本样例中仅作为样例说明，通过GetLayerNormGradMaxMinTmpSize获取最小值并传入，来保证功能正确，开发者可以根据需要传入合适的空间大小    uint32_t max;    uint32_t min;    AscendC::GetLayerNormGradMaxMinTmpSize(srcShape, sizeof(half), false, max, min);    // 获取LayerNormGrad Tiling参数    AscendC::GetLayerNormGradNDTilingInfo(srcShape, min, sizeof(half), false, tiling.layernormGradTilingData);     ... // 其他逻辑    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    context->SetTilingKey(1);    return ge::GRAPH_SUCCESS;}} // namespace optiling
