# GetAsinMaxMinTmpSize

> **Section**: 6.2.4.1.2.2  
> **PDF Pages**: 2006–2006  

---

<!-- page 2006 -->

调用示例

完整示例请参考Asin算子样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor// sharedTmpBuffer: 临时缓存, 内部复杂计算时存储中间变量// 输入tensor长度为1024, 算子输入的数据类型为half, 实际计算个数为512AscendC::Asin(dstLocal, srcLocal, sharedTmpBuffer, 512);

结果示例如下：// 首位和末尾两位为特殊值输入数据(srcLocal): [0.000000  0.001000 0.002000  ... 0.252000 0.253000 -1.000000 1.000000]输出数据(dstLocal): [0.000000  0.001000 0.002000  ... 0.254746 0.255780 -1.570796 1.570796]

## 6.2.4.1.2.2 GetAsinMaxMinTmpSize

功能说明

kernel侧Asin接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetAsinMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-825接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Asin接口一致。
