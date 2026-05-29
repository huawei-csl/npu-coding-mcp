# GetClampMaxMinTmpSize

> **Section**: 6.2.4.1.22.4  
> **PDF Pages**: 2119–2119  

---

<!-- page 2119 -->

调用示例

完整示例请参考ClampMin算子样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor// sharedTmpBuffer: 临时缓存, 内部复杂计算时存储中间变量// 输入shape信息为128，scalar为2，参与计算元素为128AscendC::ClampMin<half>(dstLocal, srcLocal, sharedTmpBuffer, static_cast<half>(2), 128);

结果示例如下：输入数据(srcLocal): [0 1 2 ...  126 127]输出数据(dstLocal): [2 2 2  ... 126 127]

## 6.2.4.1.22.4 GetClampMaxMinTmpSize

功能说明

kernel侧ClampMax/ClampMin/Clamp接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetClampMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-909参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与ClampMax/ClampMin接口一致。
