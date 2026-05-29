# Utils API

> **Section**: 2.5.4  
> **PDF Pages**: 186–186  

---

<!-- page 186 -->

●算子实现需要调用两个Kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLiveNodeCnt、extraBuf)以及当前现有的临时空间currBuff，推导单次最大计算元素数量currentShapeSize为：

currentShapeSize1 = (currBuff - extraBuf1) / maxLiveNodeCnt1 / typeSize

currentShapeSize2 = (currBuff - extraBuf2) / maxLiveNodeCnt2 / typeSize

currentShapeSize = min(currentShapeSize1 , currentShapeSize2)

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间。

以算子中需要同时调用Asin、Acos接口为例：

// 算子输入的数据类型T为halfauto shape_input = context->GetInputTensor(0)->GetOriginShape();std::vector<int64_t> srcDims = { shape_input.GetDim(0), shape_input.GetDim(1) };uint32_t srcSize = 1;uint32_t srcCurSize = 1;for (auto dim : srcDims) {    srcSize *= dim;}uint32_t typeSize = 2;

auto platformInfo = context->GetPlatformInfo();auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfo);uint64_t tailSize = 0; // UB剩余空间大小ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, tailSize);

```cpp
uint32_t asinMaxLiveNodeCount = 0;uint32_t asinExtraBuf = 0;
uint32_t acosMaxLiveNodeCount = 0;uint32_t acosExtraBuf = 0;
```

**AscendC::GetAsinTmpBufferFactorSize(typeSize, asinMaxLiveNodeCount, asinExtraBuf);AscendC::GetAcosTmpBufferFactorSize(typeSize, acosMaxLiveNodeCount, acosExtraBuf);// tmp的大小需要减去UB上调用api接口输入和输出占用的大小// 该示例中包括Asin接口的输入输出，以及Acos的输入输出，其中Asin接口的输出作为Acos的输入，因此一共需要3份src的空间大小auto tmpSize = tailSize - srcSize * typeSize * 3;assert(tmpSize >= asinExtraBuf);assert(tmpSize >= acosExtraBuf);// 计算Asin算子单次最大计算元素数量if (asinMaxLiveNodeCount != 0) {    srcAsinCurSize = (tmpSize - asinExtraBuf) / asinMaxLiveNodeCount / typeSize;} else {    srcAsinCurSize = srcSize;}// 计算Acos算子单次最大计算元素数量if (acosMaxLiveNodeCount != 0) {    srcAcosCurSize = (tmpSize - acosExtraBuf) / acosMaxLiveNodeCount / typeSize; } else {    srcAcosCurSize = srcSize;}srcCurSize = std::min(srcAsinCurSize, srcAcosCurSize);**

AsinCustomTilingData tiling;tiling.set_srcCurSize(srcCurSize); // 将单次最大计算元素数量设置为Tiling参数

## 2.5.4 Utils API

Ascend C开发提供了丰富的通用工具类，涵盖标准库、平台信息获取、上下文构建、运行时编译及日志输出等功能，支持开发者高效实现算子开发与性能优化。
