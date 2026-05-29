# GetAtanhMaxMinTmpSize

> **Section**: 6.2.4.1.17.2  
> **PDF Pages**: 2089–2089  

---

<!-- page 2089 -->

参数名输入/输出

描述

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●输入源数据需保持值域在(-0.99，-0.001)或者(0.001， 0.99)区间内。若输入不在范围内，输出结果无效。

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例请参考atanh算子样例。

// dstLocal: 存放Atanh计算结果的Tensor// srcLocal: 存放Atanh计算输入的Tensor// sharedTmpBuffer: 存放Atanh计算过程中临时缓存的Tensor// 算子输入的数据类型为half, 需要参与计算的元素个数为512AscendC::Atanh(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：输入数据(srcLocal): [0.000000 0.010000 0.020000 ...  0.990000 1.000000 1.010000 ...]输出数据(dstLocal): [0.000000 0.010000 0.020003 ...  2.646650 inf -nan ...]

## 6.2.4.1.17.2 GetAtanhMaxMinTmpSize

功能说明

kernel侧Atanh接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetAtanhMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```
