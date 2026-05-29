# GetAtanMaxMinTmpSize

> **Section**: 6.2.4.1.7.2  
> **PDF Pages**: 2035–2036  

---

<!-- page 2035 -->

参数名输入/输出

描述

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

// dstLocal: 存放Atan计算结果的Tensor// srcLocal: 存放Atan计算输入的Tensor// sharedTmpBuffer: 存放Atan计算过程中临时缓存的Tensor

// 接口框架申请临时空间，全部参与计算AscendC::Atan(dstLocal, srcLocal);// 接口框架申请临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Atan(dstLocal, srcLocal, 512);

// 通过sharedTmpBuffer入参传入临时空间，全部参与计算AscendC::Atan(dstLocal, srcLocal, sharedTmpBuffer);// 通过sharedTmpBuffer入参传入临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Atan(dstLocal, srcLocal, sharedTmpBuffer, 512);

// 指定输入算法为POLYNOMIAL_APPROXIMATION, 输入的数据类型为float, 实际计算个数为512static constexpr AscendC::AtanConfig atanConfig = { AscendC::AtanAlgo::POLYNOMIAL_APPROXIMATION};AscendC::Atan<float, false, atanConfig>(dstLocal, srcLocal, sharedTmpBuffer, 512);

示例数据如下：

输入数据(srcLocal): [-2.56 -2.55 -2.54 ... 0. ... 2.53  2.54  2.55]输出数据(dstLocal): [-1.19847027, -1.19717361, -1.19560622 ... 0. ... 1.19429046, 1.19560622, 1.19717361]

## 6.2.4.1.7.2 GetAtanMaxMinTmpSize

功能说明

kernel侧Atan接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

<!-- page 2036 -->

函数原型

```cpp
void GetAtanMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-845接口参数列表

功能

参数名输入/输出

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

是否复用源操作数输入的空间，与Atan接口一致。

输入

maxValue输出

Atan接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

Atan接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetAtanMaxMinTmpSize(shape, 2, false, maxValue, minValue);
