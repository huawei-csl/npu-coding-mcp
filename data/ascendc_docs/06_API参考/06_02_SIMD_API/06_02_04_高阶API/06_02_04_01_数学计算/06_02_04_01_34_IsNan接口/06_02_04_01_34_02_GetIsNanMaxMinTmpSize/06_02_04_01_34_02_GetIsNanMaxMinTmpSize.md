# GetIsNanMaxMinTmpSize

> **Section**: 6.2.4.1.34.2  
> **PDF Pages**: 2180–2181  

---

<!-- page 2180 -->

表6-955输入输出支持的数据类型组合

**srcDtypedstDtype**

halfhalf

halfbool

floatfloat

floatbool

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●操作数地址偏移对齐要求请参见6.2.1 通用说明和约束。

调用示例

完整样例请参考IsNan算子样例。

●通过sharedTmpBuffer入参传入AscendC::TPipe pipe;AscendC::TQue<AscendC::TPosition::VECCALC, 1> tmpQue;pipe.InitBuffer(tmpQue, 1, bufferSize);  // bufferSize通过Host侧tiling参数获取AscendC::LocalTensor<uint8_t> sharedTmpBuffer = tmpQue.AllocTensor<uint8_t>();// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512static constexpr AscendC::IsNanConfig isNanConfig = { false }; // 不修改源操作数// dst为bool类型的LocalTensor，src为half类型的LocalTensorAscendC::IsNan<isNanConfig, bool, half>(dst, src, sharedTmpBuffer, 512);

●接口框架申请临时空间AscendC::TPipe pipe;AscendC::TQue<AscendC::TPosition::VECCALC, 1> tmpQue;pipe.InitBuffer(tmpQue, 1, bufferSize);  // bufferSize通过Host侧tiling参数获取// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512static constexpr AscendC::IsNanConfig isNanConfig = { false }; // 不修改源操作数// dst为bool类型的LocalTensor，src为half类型的LocalTensorAscendC::IsNan<isNanConfig, bool, half>(dst, src, 512);

结果示例如下：输入的数据类型为half，输出的数据类型为bool输入数据(src):[1.0 nan 3.0 4.0 nan 6.0 nan 8.0]输出数据(dst):[false true false false true false true false]

## 6.2.4.1.34.2 GetIsNanMaxMinTmpSize

功能说明

Kernel侧IsNan接口的计算需要开发者预留/申请临时空间，本接口用于在Host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到Kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

<!-- page 2181 -->

●在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetIsNanMaxMinTmpSize(const platform_ascendc::PlatformAscendC& ascendcPlatform, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-956接口参数列表

参数名输入/输出

功能

ascendcPlatform

输入输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入该参数预留，传入默认值false即可。

maxValue输出IsNan接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出IsNan接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。
