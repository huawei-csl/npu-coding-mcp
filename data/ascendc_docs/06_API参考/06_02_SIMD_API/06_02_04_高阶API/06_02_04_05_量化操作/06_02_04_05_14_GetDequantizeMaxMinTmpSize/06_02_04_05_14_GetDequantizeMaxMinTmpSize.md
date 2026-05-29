# GetDequantizeMaxMinTmpSize

> **Section**: 6.2.4.5.14  
> **PDF Pages**: 2716–2716  

---

<!-- page 2716 -->

●PER_TENSOR模式constexpr static DequantizePolicy tensorPolicy = DequantizePolicy::PER_TENSOR;// 不使能offsetconstexpr static DequantizeConfig config = {tensorPolicy, false, -1};DequantizeParams params;// m,n为外部传入参数，表示srcLocal实际参与的m、n方向的元素个数params.m = m;params.n = n;params.groupSize = 0;  // 仅PER_GROUP场景下生效// srcLocal为int32_t类型的LocalTensor，dstLocal为float类型的LocalTensor，scale、offset为float类型的标量Dequantize<config>(dstLocal, srcLocal, scale, offset, params);  // offset为预留参数，可配置为0;

结果示例如下：

输入数据（srcLocal）: [-4, 2, -2, -3, -1, -4, 1, 3, 4, 1, -2, 0, ... 1]输入数据（scale矢量）: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ... 1]输入数据（scale标量）:[1]输出数据（dstLocal），此时dstLocal = srcLocal: [-4, 2, -2, -3, -1, -4, 1, 3, 4, 1, -2, 0, ... 1]

## 6.2.4.5.14 GetDequantizeMaxMinTmpSize

功能说明

kernel侧Dequantize接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetDequantizeMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1243接口参数列表

参数名输入/输出

描述

srcShape输入

Dequantize接口的输入srcTensor的shape信息。

typeSize输入

Dequantize接口的输入srcTensor的数据类型大小，单位为字节。比如输入的数据类型为int32_t，此处应传入4。
