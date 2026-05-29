# GetCosMaxMinTmpSize

> **Section**: 6.2.4.1.5.2  
> **PDF Pages**: 2023–2024  

---

<!-- page 2023 -->

–Atlas A3 训练系列产品/Atlas A3 推理系列产品

–Atlas A2 训练系列产品/Atlas A2 推理系列产品

–Atlas 推理系列产品AI Core

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的算子样例请参考Cos算子样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor// sharedTmpBuffer: 临时缓存, 内部复杂计算时存储中间变量// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512AscendC::Cos(dstLocal, srcLocal, sharedTmpBuffer, 512);constexpr AscendC::CosAlgo algo = AscendC::CosAlgo::RADIAN_REDUCTION;constexpr AscendC::CosConfig config = { algo };AscendC::Cos<half, false, config>(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：输入数据(srcLocal): [0.00            0.01            0.02             ...  5.10            5.11]输出数据(dstLocal): [1.00000000e+00  9.99949992e-01  9.99800026e-01   ...  3.77977639e-01  3.87216508e-01]

## 6.2.4.1.5.2 GetCosMaxMinTmpSize

功能说明

kernel侧Cos接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetCosMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
void GetCosMaxMinTmpSize(const CosConfig& config, const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

<!-- page 2024 -->

参数说明

表6-837接口参数列表

参数名输入/输出

描述

config输入

该参数仅支持Atlas 350 加速卡。

Cos接口的相关配置信息。该参数的配置必须与Cos Kernel接口模板参数config的配置保持一致。

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

是否复用源操作数输入的空间，与Cos接口的isReuseSource参数保持一致。对于float数据类型的输入支持开启该参数，half数据类型的输入不支持开启该参数。

输入

maxValue输出

Cos接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

Cos接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。

// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;
