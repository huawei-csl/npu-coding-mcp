# GetAxpyMaxMinTmpSize

> **Section**: 6.2.4.1.24.2  
> **PDF Pages**: 2129–2129  

---

<!-- page 2129 -->

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

●该接口支持的精度组合如下：

–half精度组合：srcLocal数据类型=half；scalar数据类型=half；dstLocal数据类型=half；PAR=128

–float精度组合：srcLocal数据类型=float；scalar数据类型=float；dstLocal数据类型=float；PAR=64

–mix精度组合：srcLocal数据类型=half；scalar数据类型=half；dstLocal数据类型=float；PAR=64

调用示例

// dstLocal: 存放Axpy计算结果的Tensor// srcLocal: 存放Axpy计算输入的Tensor// sharedTmpBuffer: 存放Axpy计算过程中临时缓存的Tensor

// 算子输入的数据类型为half, 需要参与计算的元素个数为512AscendC::Axpy(dstLocal, srcLocal, static_cast<half>(3.0), sharedTmpBuffer, 512);

结果示例如下：

输入数据(srcLocal):[1. 2. 3. 4. 5. 6. ... 512.]输入数据(scalarValue): 3.0输出数据(dstLocal)初始值:[0. 0. 0. 0. 0. 0. ... 0.]进行Axpy计算后，输出数据(dstLocal):[3. 6. 9. 12. 15. 18. ... 1536.]

## 6.2.4.1.24.2 GetAxpyMaxMinTmpSize

功能说明

kernel侧Axpy接口的计算需要开发者申请临时空间，本接口用于在host侧获取申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间申请。

函数原型

```cpp
void GetAxpyMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```
