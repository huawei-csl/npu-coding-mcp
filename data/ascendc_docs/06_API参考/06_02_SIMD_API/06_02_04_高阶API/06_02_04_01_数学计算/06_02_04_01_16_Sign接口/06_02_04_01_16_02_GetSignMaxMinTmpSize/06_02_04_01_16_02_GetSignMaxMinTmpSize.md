# GetSignMaxMinTmpSize

> **Section**: 6.2.4.1.16.2  
> **PDF Pages**: 2084–2084  

---

<!-- page 2084 -->

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例请参考Sign算子样例。

// dstLocal: 存放Sign计算结果的Tensor// srcLocal: 存放Sign计算输入的Tensor// sharedTmpBuffer: 存放Sign计算过程中临时缓存的Tensor

// 接口框架申请临时空间，全部参与计算AscendC::Sign(dstLocal, srcLocal);// 接口框架申请临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Sign(dstLocal, srcLocal, 512);

// 通过sharedTmpBuffer入参传入临时空间，全部参与计算AscendC::Sign(dstLocal, srcLocal, sharedTmpBuffer);// 通过sharedTmpBuffer入参传入临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Sign(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：输入输出的数据类型为float，一维向量包含8个数字;输入数据(srcLocal): [-inf, -2.0, -0.0, 0.0, nan, -nan, 2.0, inf]输出数据(dstLocal): [-1, -1, 0, 0, 0, 0, 1, 1]

## 6.2.4.1.16.2 GetSignMaxMinTmpSize

功能说明

kernel侧Sign接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetSignMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```
