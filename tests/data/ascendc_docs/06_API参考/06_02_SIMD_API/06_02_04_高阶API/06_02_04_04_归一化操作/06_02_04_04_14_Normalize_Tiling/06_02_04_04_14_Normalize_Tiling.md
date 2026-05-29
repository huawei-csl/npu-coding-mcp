# Normalize Tiling

> **Section**: 6.2.4.4.14  
> **PDF Pages**: 2630–2632  

---

<!-- page 2630 -->

AscendC::Normalize<DTYPE_Y, DTYPE_X, false, CONFIG>(    yLocal,          // 输出：归一化结果 y，shape [A, R]    rstdLocal,       // 输出：标准差倒数 rstd，shape [A]    meanLocal,       // 输入：均值 mean，shape [A]    varianceLocal,   // 输入：方差 variance，shape [A]    xLocal,          // 输入：原始数据 X，shape [A, R]    gammaLocal,      // 输入：缩放系数γ，shape [R]    betaLocal,       // 输入：平移系数β，shape [R]    epsilon,         // 输入：防除零系数ε    para             // 输入：Tiling 参数，包含 aLength、rLength、rLengthWithPadding);

示例结果如下：输入数据(srcLocal, shape:[8, 8]): [  0.  1.  2.  3.  4.  5.  6.  7.   8.  9. 10. 11. 12. 13. 14. 15.  16. 17. 18. 19. 20. 21. 22. 23.  24. 25. 26. 27. 28. 29. 30. 31.  32. 33. 34. 35. 36. 37. 38. 39.  40. 41. 42. 43. 44. 45. 46. 47.  48. 49. 50. 51. 52. 53. 54. 55.  56. 57. 58. 59. 60. 61. 62. 63. ]输入数据(meanLocal, shape:[8]): [ 0. 1. 2. 3. 4. 5. 6. 7. ]输入数据(varianceLocal, shape:[8]): [ 0. 1. 2. 3. 4. 5. 6. 7. ]输入数据(gammaLocal, shape:[8]): [ 1. 1. 1. 1. 1. 1. 1. 1. ]输入数据(betaLocal, shape:[8]): [ 1. 1. 1. 1. 1. 1. 1. 1. ]输出数据(yLocal): [ 1.0 32.622772 64.245544 95.868324 127.4911 159.11388 190.73665 222.35942   7.996503 8.996003 9.995503 10.995004 11.994504 12.994005 13.9935055 14.993006   10.897021 11.603951 12.310882 13.017812 13.724742 14.431672 15.138602 15.845532   13.122336 13.699591 14.276845 14.854099 15.431353 16.008606 16.585861 17.163115   14.998251 15.498188 15.998126 16.498064 16.998001 17.497938 17.997875 18.497814   16.65091 17.09808 17.545248 17.992416 18.439585 18.886755 19.333923 19.781092   18.144999 18.553213 18.961428 19.369642 19.777857 20.186071 20.594284 21.002499   19.518936 19.896873 20.27481 20.652748 21.030685 21.408623 21.78656 22.164497 ]输出数据(rstdLocal): [ 31.622774    0.9995004   0.7069301   0.5772541   0.49993753  0.44716886  0.40821427  0.37793747 ]

## 6.2.4.4.14 Normalize Tiling

功能说明

Ascend C提供Normalize Tiling API，方便用户获取Normalize kernel计算时所需的Tiling参数。

具体为，通过GetNormalizeMaxMinTmpSize获取Normalize接口计算所需最大和最小临时空间大小。

kernel侧Normalize接口的计算需要开发者预留/申请临时空间，GetNormalizeMaxMinTmpSize用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

<!-- page 2631 -->

函数原型

```cpp
void GetNormalizeMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSizeU, const uint32_t typeSizeT, const bool isReuseSource, const bool isComputeRstd, const bool isOnlyOutput, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1199 GetNormalizeMaxMinTmpSize 接口参数说明

参数名输入/输出

描述

srcShape输入Normalize输入数据inputX的shape信息{A, R}。

typeSizeU输入输入数据gamma, beta的数据类型大小，单位为字节。比如输入的数据类型为float，此处应传入4。

typeSizeT输入输入数据inputX的数据类型大小，单位为字节。比如输入的数据类型为float，此处应传入4。

isReuseSource

输入是否复用源操作数的内存空间，与Normalize接口一致。

isComputeRstd

输入是否计算rstd。该参数的取值只支持true。

isOnlyOutput

输入是否只输出y，不输出标准差的倒数rstd。当前该参数仅支持取值为false，表示y和rstd的结果全部输出。

maxValue输出输出Normalize接口所需的tiling信息（最大临时空间大小）。

Normalize接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出输出Normalize接口所需的tiling信息（最小临时空间大小）。

Normalize接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。

返回值说明

无

<!-- page 2632 -->

约束说明

无

调用示例

步骤1将Normalize接口所需参数增加至TilingData结构体，作为TilingData结构体的一个字段。

BEGIN_TILING_DATA_DEF(NormalizeCustomTilingData)  TILING_DATA_FIELD_DEF(float, epsilon);  TILING_DATA_FIELD_DEF(uint32_t, isNoBeta);  TILING_DATA_FIELD_DEF(uint32_t, isNoGamma);  TILING_DATA_FIELD_DEF(uint32_t, isOnlyOutput);  TILING_DATA_FIELD_DEF(uint32_t, aLength);  TILING_DATA_FIELD_DEF(uint32_t, rLength);  TILING_DATA_FIELD_DEF(uint32_t, rLengthWithPadding);  ...                                           // 添加其他tiling字段END_TILING_DATA_DEF;

步骤2Tiling实现函数中，首先调用GetNormalizeMaxMinTmpSize接口获取Normalize接口能完成计算所需最大/最小临时空间大小，根据该范围结合实际的内存使用情况设置合适的空间大小，然后根据输入shape、剩余的可供计算的空间大小等信息获取Normalize kernel侧接口所需tiling参数。

namespace optiling {static ge::graphStatus TilingFunc(gert::TilingContext *context){    NormalizeCustomTilingData tiling;    const gert::RuntimeAttrs *attrs = context->GetAttrs();    const float epsilon = *(attrs->GetAttrPointer<float>(0));    const uint32_t isNoBeta = *(attrs->GetAttrPointer<uint32_t>(1));    const uint32_t isNoGamma = *(attrs->GetAttrPointer<uint32_t>(2));    const uint32_t isOnlyOutput = *(attrs->GetAttrPointer<uint32_t>(3));    const gert::StorageShape* x1_shape = context->GetInputShape(0);    ...// 其他逻辑    const gert::Shape shape = x1_shape->GetStorageShape();    uint32_t aLength = shape.GetDim(0);    uint32_t rLength = shape.GetDim(1);    uint32_t rLengthWithPadding = (rLength + alignNum - 1) / alignNum * alignNum;    std::vector<int64_t> srcDims = {aLength, rLength};    ge::Shape srcShape(srcDims);

```cpp
uint32_t maxTmpsize = 0;
    uint32_t minTmpsize = 0;
    AscendC::GetNormalizeMaxMinTmpSize(srcShape, typeSizeU, typeSizeT, false, true, isOnlyOutput, maxTmpsize, minTmpsize);    // auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    // AscendC::GetNormalizeMaxMinTmpSize(srcShape, typeSizeU, typeSizeT, false, true, isOnlyOutput, ascendcPlatform, maxTmpsize, minTmpsize);
```

... // 其他逻辑    context->SetTilingKey(1);    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    size_t *currentWorkspace = context->GetWorkspaceSizes(1);    currentWorkspace[0] = 0;    return ge::GRAPH_SUCCESS;}} // namespace optiling

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的Normalize Tiling信息传入Normalize接口参与计算。完整的kernel侧样例请参考6.2.4.4.13 Normalize。
