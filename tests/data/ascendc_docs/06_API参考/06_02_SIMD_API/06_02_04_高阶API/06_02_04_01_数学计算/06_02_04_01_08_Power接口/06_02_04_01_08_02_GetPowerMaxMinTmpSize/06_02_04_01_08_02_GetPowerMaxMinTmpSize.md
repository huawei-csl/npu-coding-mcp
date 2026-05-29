# GetPowerMaxMinTmpSize

> **Section**: 6.2.4.1.8.2  
> **PDF Pages**: 2042–2043  

---

<!-- page 2042 -->

返回值说明

无

约束说明

●不支持源操作数与目的操作数地址重叠。

●对于Atlas 推理系列产品AI Core，幂运算的指数必须小于231-1。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

完整的调用样例请参考Power样例。

// dstLocal: 存放计算结果的Tensor// srcLocalExp: Power计算使用的指数Tensor// srcLocalBase: Power计算使用的底数Tensor

// 使用srcLocalBase做底数对srcLocalExp中的全部元素做幂运算AscendC::Power<T, false>(dstLocal, srcLocalBase, srcLocalExp);

// scalarValueBase: Power计算使用的底数T scalarValueBase = srcLocalBase.GetValue(0);// 使用同一个底数scalarValueBase对srcLocalExp中的全部元素做幂运算AscendC::Power<T, false>(dstLocal, scalarValueBase, srcLocalExp);

// scalarValueExp: Power计算使用的指数T scalarValueExp = srcLocalExp.GetValue(0);// 使用同一个指数scalarValueExp对srcLocalBase中的全部元素做幂运算AscendC::Power<T, false>(dstLocal, srcLocalBase, scalarValueExp);

```cpp
// static constexpr AscendC::PowerConfig config = { AscendC::PowerAlgo::DOUBLE_FLOAT_TECH };// AscendC::Power<srcType, false, config>(dstLocal, scalarValue, srcLocal2);
```

AscendC::Power<T, false>(dstLocal, srcLocalBase, srcLocalExp) 示例数据如下：输入数据(srcLocalBase): [2 3 4 5 6 7 8 9]输入数据(srcLocalExp): [4 3 2 1 4 3 2 1]输出数据(dstLocal): [16 27 16 5 1296 343 64 9]

AscendC::Power<T, false>(dstLocal, scalarValueBase, srcLocalExp) 示例数据如下：输入数据(scalarValueBase): 2输入数据(srcLocalExp): [4 3 2 1 4 3 2 1]输出数据(dstLocal): [16 8 4 2 16 8 4 2]

AscendC::Power<T, false>(dstLocal, srcLocalBase, scalarValueExp) 示例数据如下：输入数据(srcLocalBase): [2 3 4 5 6 7 8 9]输入数据(scalarValueExp): 4输出数据(dstLocal): [16 81 256 625 1296 2401 4096 6561]

## 6.2.4.1.8.2 GetPowerMaxMinTmpSize

功能说明

kernel侧Power接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

<!-- page 2043 -->

接口内部根据srcShape1、srcShape2输入判断接口为Power(dstTensor, srcTensor1,srcTensor2)、Power(dstTensor, srcTensor1, scalarValue) 或Power(dstTensor,scalarValue, srcTensor2)类型中的哪一种，进而返回对应临时空间大小。

函数原型

```cpp
void GetPowerMaxMinTmpSize(const ge::Shape& srcShape1, const ge::Shape& srcShape2, const bool typeIsInt, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-849接口参数列表

参数名输入/输出

描述

srcShape1输入输入srcTensor1的shape信息。

srcShape2输入输入srcTensor2的shape信息。

typeIsInt输入bool类型，true表示输入是int32_t。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Power接口一致。

maxValue输出Power接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

请注意，maxValue仅作为参考值，有可能大于UnifiedBuffer剩余空间的大小，该场景下，开发者需要根据UnifiedBuffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Power接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。
