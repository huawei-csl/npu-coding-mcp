# GetCoshMaxMinTmpSize

> **Section**: 6.2.4.1.10.2  
> **PDF Pages**: 2053–2053  

---

<!-- page 2053 -->

约束说明

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

更多示例请参考Cosh算子样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor// sharedTmpBuffer: 临时缓存, 内部复杂计算时存储中间变量// 输入tensor长度为512, 算子输入的数据类型为half, 实际计算个数为256AscendC::Cosh(dstLocal, srcLocal, sharedTmpBuffer, 256);

结果示例如下：// 末尾使用三位特殊值验证输入数据(srcLocal): [ 0.000000   0.010000  0.020000  ...  2.520000  -11.089000    0.000000  11.089000]输出数据(dstLocal): [ 1.000000   1.000050  1.000200  ...  6.254528  32723.625000  1.000000  32723.625000]

## 6.2.4.1.10.2 GetCoshMaxMinTmpSize

功能说明

kernel侧Cosh接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetCoshMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-857接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否允许修改源操作数。
