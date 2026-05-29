# GetXorMaxMinTmpSize

> **Section**: 6.2.4.1.28.2  
> **PDF Pages**: 2150–2150  

---

<!-- page 2150 -->

输入数据(srcLocal): [ 2  3  5  7 11 13 17 19 ]输入数据(srcLocal): [ 1  2  3  4  5  6  7  8 ]输出数据(dstLocal): [ 3  1  6  3 14 10 22 27 ]

## 6.2.4.1.28.2 GetXorMaxMinTmpSize

功能说明

kernel侧Xor接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetXorMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-933接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为int16_t，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Xor接口一致。

maxValue输出Xor接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Xor接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。

返回值说明

无
