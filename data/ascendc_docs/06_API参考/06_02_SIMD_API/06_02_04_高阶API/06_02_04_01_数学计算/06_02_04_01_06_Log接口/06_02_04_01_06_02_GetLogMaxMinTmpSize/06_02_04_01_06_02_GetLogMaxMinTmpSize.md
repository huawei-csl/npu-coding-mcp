# GetLogMaxMinTmpSize

> **Section**: 6.2.4.1.6.2  
> **PDF Pages**: 2029–2030  

---

<!-- page 2029 -->

参数名输入/输出

描述

sharedTmpBuffer

输入临时缓存。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

临时空间大小BufferSize的获取方式请参考 GetLogMaxMinTmpSize。

calCount输入参与计算的元素个数。

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例可参考Log样例。

// dstLocal: 存放计算结果的Tensor// srcLocal: 参与计算的输入Tensor

// 以e为底，所有元素全部参与计算AscendC::Log(dstLocal, srcLocal);// 以10为底// AscendC::Log10(dstLocal, srcLocal);// 以2为底// AscendC::Log2(dstLocal, srcLocal);

Log接口结果示例如下：输入数据(srcLocal): [144.22607 9634.764 ... 1835.1245 3145.5125]输出数据(dstLocal): [4.971382 9.173133 ... 7.514868 8.053732]

Log2接口结果示例如下：输入数据(srcLocal): [6299.54 338.45963 ... 2.853525 5752.1323]输出数据(dstLocal): [12.621031 8.40284 ... 1.5127451 12.4898815]

Log10接口结果示例如下：输入数据(srcLocal): [712.7535 78.36265 ... 3099.0571 9313.082]输出数据(dstLocal): [2.8529394 1.8941091 ... 3.4912295 3.9690933]

## 6.2.4.1.6.2 GetLogMaxMinTmpSize

功能说明

Host侧接口，用于获取Log接口能完成计算所需最小的临时空间大小，此空间为预留空间，即需要保证预留有足够的物理空间，用于执行计算。

函数原型

```cpp
void GetLogMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)void GetLog10MaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

<!-- page 2030 -->

```cpp
void GetLog2MaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-841接口参数列表

参数名输入/输出

描述

srcShape输入

输入的shape信息。

typeSize输入

输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

是否复用源操作数输入的空间，与Log接口一致。

输入

maxValue输出

Log接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出

Log接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。

●GetLogMaxMinTmpSize接口样例：// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetLogMaxMinTmpSize(shape, 2, false, maxValue, minValue);
