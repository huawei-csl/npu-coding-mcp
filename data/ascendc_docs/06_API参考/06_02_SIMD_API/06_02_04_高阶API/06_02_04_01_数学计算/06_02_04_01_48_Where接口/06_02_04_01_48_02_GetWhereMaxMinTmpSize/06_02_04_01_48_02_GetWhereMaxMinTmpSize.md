# GetWhereMaxMinTmpSize

> **Section**: 6.2.4.1.48.2  
> **PDF Pages**: 2248–2249  

---

<!-- page 2248 -->

表6-1012参数说明

参数名称类型说明

dst输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

src0、src1

输入源操作数。类型为标量或LocalTensor，当类型为LocalTensor时，支持的TPosition为VECIN/VECCALC/VECOUT。

数据类型需要与目的操作数保持一致。

condition输入条件操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

count输入参与计算的元素个数。

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●操作数地址偏移对齐要求请参见6.2.1 通用说明和约束。

调用示例

完整样例请参考where算子样例。AscendC::LocalTensor<half> dst, src0, src1;AscendC::LocalTensor<bool> condition;uint32_t count = 512; // 参与计算的元素个数AscendC::Where(dst, src0, src1,  condition, count);

结果示例如下：

输入数据（src0）:[1, 2, 3, ... 511, 512]输入数据（src1）:[-1, -2, -3, ... -511, -512]条件输入数据（condition），为0时选择src1，为1时选择src0:[0, 1, 0, ... 0, 1]输出数据（dst）:[-1, 2, -3, ... -511, 512]

## 6.2.4.1.48.2 GetWhereMaxMinTmpSize

功能说明

Kernel侧Where接口的计算需要开发者预留/申请临时空间，本接口用于在Host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到Kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

<!-- page 2249 -->

●在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetWhereMaxMinTmpSize(const platform_ascendc::PlatformAscendC& ascendcPlatform, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1013接口参数列表

参数名输入/输出

功能

ascendcPlatform

输入输入的平台信息。PlatformAscendC的定义请参见6.4.2.1.2 构造及析构函数。

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入该参数预留，传入默认值false即可。

maxValue输出Where接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，Kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Where接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。
