# GetExpMaxMinTmpSize

> **Section**: 6.2.4.1.25.2  
> **PDF Pages**: 2134–2135  

---

<!-- page 2134 -->

表6-920接口参数说明

参数名输入/输出

描述

dstLocal输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

srcLocal输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

源操作数的数据类型需要与目的操作数保持一致。

sharedTmpBuffer

输入临时缓存。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

用于Exp内部复杂计算时存储中间变量，由开发者提供。

临时空间大小BufferSize的获取方式请参考 GetExpMaxMinTmpSize。

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整示例请参考Exp算子样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor// sharedTmpBuffer: 临时缓存, 内部复杂计算时存储中间变量// 操作数类型为half，泰勒展开项数为15，不允许修改源操作数// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512AscendC::Exp<half, 15, false>(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：

输入数据(srcLocal): [ 0.0        0.01       0.02       0.03       ...  5.11     ]输出数据(dstLocal):[ 1.0000000  1.0100503  1.0202013  1.0304545  ...  165.67036]

## 6.2.4.1.25.2 GetExpMaxMinTmpSize

功能说明

kernel侧Exp接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

<!-- page 2135 -->

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
bool GetExpMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-921接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Exp接口一致。

maxValue输出Exp接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Exp接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

返回true/false，表明是否能正常获取所需最大最小临时空间。

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};
