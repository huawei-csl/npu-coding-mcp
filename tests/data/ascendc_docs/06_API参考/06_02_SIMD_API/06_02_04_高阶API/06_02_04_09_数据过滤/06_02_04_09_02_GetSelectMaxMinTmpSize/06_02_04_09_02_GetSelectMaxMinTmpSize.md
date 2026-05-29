# GetSelectMaxMinTmpSize

> **Section**: 6.2.4.9.2  
> **PDF Pages**: 2837–2838  

---

<!-- page 2837 -->

调用示例

完整示例可以参考Select样例。

// dstLocal：结果数据// srcLocal1：输入张量// scalar：待比较标量// maskLocal：选择掩码// tmpBuffer：临时空间// info：srcLocal和maskLocal的shape信息AscendC::SelectWithBytesMaskShapeInfo info;AscendC::Select(dstLocal, srcLocal1, scalar, maskLocal, tmpBuffer, info);

结果示例如下：输入数据srcLocal1: [-84.6    -24.38    30.97   -30.25    22.28   -92.56    90.44   -58.72  -86.56     5.74     6.754  -86.3    -96.7    -37.38   -81.9     46.9 -99.4     94.2    -41.78   -60.3    -14.43    78.6      8.93   -65.2    79.94   -46.88     4.516   20.03   -25.56    24.73     0.3223  21.98

-87.4    -93.9     46.22   -69.9     90.8    -24.17   -96.2    -91.    90.44     9.766   68.25   -57.78   -75.44    -8.86   -91.56    21.6  76.      82.1    -78.     -23.75    92.     -66.44    75.      94.9   2.62   -90.9     15.945   38.16    50.84    96.94   -59.38    44.22  ]输入数据scalar: [35.6]输入数据maskLocal: [False  True False False  True  True False  True  True False False  True False  True False  True   True   False False False  True  True  True  True   True False  True False  True  True  True  True

```cpp
False False  True False  True False  True False  True False  True False  True  True  True False True False  True False  True False  True  True   True False False False  True False  True  True]
```

输出数据dstLocal: [-84.6    35.6    30.97   -30.25   35.6    35.6    90.44   35.6  35.6    5.74    6.754   35.6   -96.7    35.6   -81.9    35.6  35.6    94.2    -41.78  -60.3    35.6    35.6    35.6    35.6  35.6   -46.88   35.6    20.03   35.6    35.6    35.6    35.6 -87.4   -93.9    35.6    -69.9    35.6   -24.17   35.6   -91.   35.6   9.766  35.6   -57.78   35.6     35.6    35.6    21.6  35.6    82.1    35.6    -23.75   35.6   -66.44   35.6    35.6  35.6   -90.9    15.945  38.16   35.6    96.94   35.6    35.6  ]

## 6.2.4.9.2 GetSelectMaxMinTmpSize

功能说明

kernel侧Select接口的计算需要开发者申请临时空间，本接口用于在host侧获取申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间申请。

<!-- page 2838 -->

函数原型

说明

GetSelectWithBytesMaskMinTmpSize、GetSelectWithBytesMaskMaxTmpSize、GetSelectWithBytesMaskMaxMinTmpSize接口废弃，并将在后续版本移除，请不要使用该接口。请使用GetSelectMinTmpSize、GetSelectMaxTmpSize、GetSelectMaxMinTmpSize接口。

●获取最小临时空间大小uint32_t GetSelectMinTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask)uint32_t GetSelectWithBytesMaskMinTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask)

●获取最大临时空间大小uint32_t GetSelectMaxTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask)uint32_t GetSelectWithBytesMaskMaxTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask)

●获取最大和最小临时空间大小void GetSelectMaxMinTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask, uint32_t& maxValue, uint32_t& minValue)void GetSelectWithBytesMaskMaxMinTmpSize(const ge::Shape& src0Shape, const ge::Shape& src1Shape, const uint32_t srcTypeSize, const ge::Shape& maskShape, const uint32_t maskTypeSize, const bool isReuseMask, uint32_t& maxValue, uint32_t& minValue)

参数说明

表6-1310接口参数列表

参数名输入/输出

描述

src0Shape输入输入src0的shape信息。src0为scalar时，shape应为{1}。

src1Shape输入输入src1的shape信息。src1为scalar时，shape应为{1}。

srcTypeSize输入输入srcTensor的数据类型大小，比如数据类型为half，此处应传入2。

maskShape输入输入maskTensor的shape信息。

maskTypeSize

输入输入maskTensor的数据类型大小，比如数据类型为bool，此处应传入1。

isReuseMask

输入是否复用maskTensor输入的空间。与kernel侧保持一致。

maxValue输出Select接口能完成计算所需最大临时空间大小。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Select接口能完成计算所需最小临时空间大小。
