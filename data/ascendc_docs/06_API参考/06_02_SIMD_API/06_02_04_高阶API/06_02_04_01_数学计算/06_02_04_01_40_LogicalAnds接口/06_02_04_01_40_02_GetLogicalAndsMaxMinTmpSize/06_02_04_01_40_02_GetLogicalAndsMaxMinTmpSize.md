# GetLogicalAndsMaxMinTmpSize

> **Section**: 6.2.4.1.40.2  
> **PDF Pages**: 2211–2212  

---

<!-- page 2211 -->

约束说明

●本接口与操作的左操作数及右操作数中必须有一个为矢量，当前不支持左右操作数同时为标量。

●当传入LocalTensor的单点数据作为标量时，scalarTensorIndex参数需要传入编译期已知的常量，如果传入变量，则需要将该变量声明为constexpr。

●不支持源操作数与目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整样例请参考logicalands算子样例。

AscendC::LocalTensor<bool> dst;AscendC::LocalTensor<half> src0, src1;uint32_t count = 512; // 参与计算的元素个数// 标量在后AscendC::LogicalAnds(dst, src0, src1, count); // 标量在前static constexpr AscendC::LogicalAndsConfig config = { false, 0 };AscendC::LogicalAnds<config>(dst, src0, src1, count);

结果示例如下：// 标量在后输入数据（src0）: [1, 2, 0, -1, -2, 0, 3, 4, 0, -3, -4, 0, 5, 6, 0, -5, -6, 0, ... 0]输入数据（src1）: [3.0]输出数据（dst）: [ True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  ...  False]// 标量在前输入数据（src1）: [1, 2, 0, -1, -2, 0, 3, 4, 0, -3, -4, 0, 5, 6, 0, -5, -6, 0, ... 0]输入数据（src0）: [3.0]输出数据（dst）: [ True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  True,  True,  False,  ...  False]

## 6.2.4.1.40.2 GetLogicalAndsMaxMinTmpSize

功能说明

Kernel侧LogicalAnds接口的计算需要开发者预留/申请临时空间，本接口用于在Host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到Kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetLogicalAndsMaxMinTmpSize(const platform_ascendc::PlatformAscendC& ascendcPlatform, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

<!-- page 2212 -->

参数说明

表6-981接口参数列表

参数名输入/输出

功能

ascendcPlatform

输入输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入该参数预留，传入默认值false即可。

maxValue输出LogicalAnds接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出LogicalAnds接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;auto plat = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());AscendC::GetLogicalAndsMaxMinTmpSize(plat, shape, 2, false, maxValue, minValue);
