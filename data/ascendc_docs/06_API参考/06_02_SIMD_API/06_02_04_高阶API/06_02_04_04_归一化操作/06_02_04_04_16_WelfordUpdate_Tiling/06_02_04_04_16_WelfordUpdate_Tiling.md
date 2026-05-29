# WelfordUpdate Tiling

> **Section**: 6.2.4.4.16  
> **PDF Pages**: 2638–2640  

---

<!-- page 2638 -->

// 使用 WelfordUpdate 接口执行 Welford 在线算法更新struct AscendC::WelfordUpdateParam para = { nLength, rLength, abComputeLength, 0.3 };AscendC::WelfordUpdate<T, U, false, WELFORD_UPDATE_ENABLE_INPLACE_CFG>(    outputMean,        // 输出：更新后的均值    outputVariance,    // 输出：更新后的方差中间结果    inputMean,         // 输入：上一时刻均值    inputVariance,     // 输入：上一时刻方差中间结果    inputX,            // 输入：当前输入 xi    sharedTmpBuffer,   // 输入：临时缓冲区（由开发者提供）    para               // 输入：Welford 更新参数);

示例结果如下：输入数据(inputX, shape:[1, 64]): [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. ]输入数据(gammaLocal, shape:[64]): [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53. 54. 55. 56. 57. 58. 59. 60. 61. 62. 63. ]输入数据(betaLocal, shape:[64]): [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37. 38. 39. 40. 41. 42. 43. 44. 45. 46. 47. 48. 49. 50. 51. 52. 53. 54. 55. 56. 57. 58. 59. 60. 61. 62. 63. ]输出数据(meanLocal): [ 0.125  1.     1.875  2.75   3.625  4.5    5.375  6.25   7.125  8.  8.875  9.75  10.625 11.5   12.375 13.25  14.125 15.    15.875 16.75 17.625 18.5   19.375 20.25  21.125 22.    22.875 23.75  24.625 25.5 26.375 27.25  28.125 29.    29.875 35.    36.    37.    38.    39. 40.    41.    42.    43.    44.    45.    46.    47.    48.    49. 50.    51.    52.    53.    54.    55.    56.    57.    58.    59. 60.    61.    62.    63. ]输出数据(varianceLocal): [8.75000e-01 1.00000e+00 2.87500e+00 6.50000e+00 1.18750e+01 1.90000e+01 2.78750e+01 3.85000e+01 5.08750e+01 6.50000e+01 8.08750e+01 9.85000e+01 1.17875e+02 1.39000e+02 1.61875e+02 1.86500e+02 2.12875e+02 2.41000e+02 2.70875e+02 3.02500e+02 3.35875e+02 3.71000e+02 4.07875e+02 4.46500e+02 4.86875e+02 5.29000e+02 5.72875e+02 6.18500e+02 6.65875e+02 7.15000e+02 7.65875e+02 8.18500e+02 8.72875e+02 9.29000e+02 9.86875e+02 3.50000e+01 3.60000e+01 3.70000e+01 3.80000e+01 3.90000e+01 4.00000e+01 4.10000e+01 4.20000e+01 4.30000e+01 4.40000e+01 4.50000e+01 4.60000e+01 4.70000e+01 4.80000e+01 4.90000e+01 5.00000e+01 5.10000e+01 5.20000e+01 5.30000e+01 5.40000e+01 5.50000e+01 5.60000e+01 5.70000e+01 5.80000e+01 5.90000e+01 6.00000e+01 6.10000e+01 6.20000e+01 6.30000e+01 ]

## 6.2.4.4.16 WelfordUpdate Tiling

功能说明

Ascend C提供WelfordUpdate Tiling API，方便用户获取WelfordUpdate kernel计算时所需的Tiling参数。

获取Tiling参数主要步骤如下：

具体为，通过GetWelfordUpdateMaxMinTmpSize获取WelfordUpdate接口计算所需最大和最小临时空间大小。

kernel侧WelfordUpdate接口的计算需要开发者预留/申请临时空间，GetWelfordUpdateMaxMinTmpSize用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

<!-- page 2639 -->

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetWelfordUpdateMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSizeT, const uint32_t typeSizeU, const bool isReuseSource, const bool isInplace, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1202 GetWelfordUpdateMaxMinTmpSize 接口参数说明

参数名输入/输出

描述

srcShape输入输入的shape信息{rnLength, abLength}。其中rnLength、abLength与WelfordUpdate接口含义一致。

typeSizeT输入输入(inputX)的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

typeSizeU输入均值、方差(outputMean、outputVariance、inputMean、inputVariance)的数据类型大小，单位为字节。比如输入的数据类型为float，此处应传入4。

isReuseSource

输入是否允许修改源操作数。与WelfordUpdate接口一致。

isInplace输入目的操作数是否复用源操作数。与WelfordUpdate接口一致。

maxValue输出WelfordUpdate接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出WelfordUpdate接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

<!-- page 2640 -->

约束说明

无

调用示例

步骤1将WelfordUpdate Tiling结构体参数增加至TilingData结构体，作为TilingData结构体的一个字段。

BEGIN_TILING_DATA_DEF(WelfordUpdateCustomTilingData) // 注册一个tiling的类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, inplace); // 添加tiling字段，output是否复用input  TILING_DATA_FIELD_DEF(uint32_t, nLength);  TILING_DATA_FIELD_DEF(uint32_t, rLength);  TILING_DATA_FIELD_DEF(uint32_t, abComputeLength);  TILING_DATA_FIELD_DEF(uint32_t, nRec);END_TILING_DATA_DEF;REGISTER_TILING_DATA_CLASS(WelfordUpdateCustom, WelfordUpdateCustomTilingData) // 将WelfordUpdateCustomTilingData结构体参数增加至TilingData结构体

步骤2Tiling实现函数中，首先调用GetWelfordUpdateMaxMinTmpSize接口获取WelfordUpdate接口能完成计算所需最大/最小临时空间大小，根据该范围结合实际的内存使用情况设置合适的空间大小，然后根据输入shape、剩余的可供计算的空间大小等信息获取WelfordUpdate kernel侧接口所需tiling参数。

```cpp
namespace optiling {static ge::graphStatus TilingFunc(gert::TilingContext *context){    WelfordUpdateCustomTilingData tiling;
    const gert::RuntimeAttrs *attrs = context->GetAttrs();
    const uint32_t inplace = *(attrs->GetAttrPointer<uint32_t>(0));
    const uint32_t abComputeLength = *(attrs->GetAttrPointer<uint32_t>(1));
    const uint32_t sharedtmpbuffer = *(attrs->GetAttrPointer<uint32_t>(2));
const gert::StorageShape *x1_shape = context->GetInputShape(1);
    const gert::Shape shape = x1_shape->GetStorageShape();
    auto nLength = shape.GetDim(0);
    auto rLength = shape.GetDim(1);
std::vector<int64_t> srcDims = {nLength, rLength};
    ge::Shape srcShape(srcDims);
```

uint32_t maxTmpsize = 0;    uint32_t minTmpsize = 0;    // 本样例中仅作为样例说明，通过GetWelfordUpdateMaxMinTmpSize获取最小值并传入，来保证功能正确，开发者可以根据需要传入合适的空间大小    AscendC::GetWelfordUpdateMaxMinTmpSize(srcShape, 4, 4, false, false, maxTmpsize, minTmpsize);    // auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    // AscendC::GetWelfordUpdateMaxMinTmpSize(srcShape, 4, 4, false, false, ascendcPlatform, maxTmpsize, minTmpsize);    ... // 其他逻辑    context->SetTilingKey(1);    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    size_t *currentWorkspace = context->GetWorkspaceSizes(1);    currentWorkspace[0] = 0;    return ge::GRAPH_SUCCESS;}} // namespace optiling

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的WelfordUpdate Tiling信息传入WelfordUpdate接口参与计算。完整的kernel侧样例请参考6.2.4.4.15 WelfordUpdate。

```cpp
extern "C" __global__ __aicore__ voidwelford_update_custom(    GM_ADDR inputX_gm, GM_ADDR mean_gm, GM_ADDR var_gm, GM_ADDR outputMean_gm, GM_ADDR outputVariance_gm, GM_ADDR workspace, GM_ADDR tiling)
```
