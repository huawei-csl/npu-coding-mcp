# Cast（float转half/int32_t）

> **Section**: 6.2.3.5.5  
> **PDF Pages**: 1725–1726  

---

<!-- page 1725 -->

参数说明

表6-648模板参数说明

参数名描述

countValue指定要查找的值，0表示查找第一个0的位置，1表示查找第一个1的位置，数据类型是int，只能输入0或1。

表6-649参数说明

参数名输入/输出

描述

valueIn输入输入数据，数据类型是uint64_t。

返回值说明

int64_t类型的数，valueIn中第一个0或1出现的位置。

约束说明

无。

调用示例

uint64_t valueIn = 28;  // 0x1c// 输出数据oneCount：2，最低位0，倒数第3为1，则最低位起连续2个0int64_t oneCount = AscendC::GetSFFValue<1>(valueIn);

## 6.2.3.5.5 Cast（float 转half/int32_t）

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 1726 -->

功能说明

对标量的数据类型进行转换。

函数原型

```cpp
template <typename T, typename U, RoundMode roundMode>__aicore__ inline U Cast(T valueIn)
```

参数说明

表6-650模板参数说明

参数名描述

TvalueIn的数据类型，支持float。

U转换后的数据类型，支持half、int32_t。

roundMode精度转换处理模式，类型是RoundMode。

RoundMode为枚举类型，用以控制精度转换处理模式，具体定义为：enum class RoundMode {    CAST_NONE = 0,  // 在转换有精度损失时表示CAST_RINT模式，不涉及精度损失时表示不取整    CAST_RINT,      // rint，四舍六入五成双取整    CAST_FLOOR,     // floor，向负无穷取整    CAST_CEIL,      // ceil，向正无穷取整    CAST_ROUND,     // round，四舍五入取整    CAST_TRUNC,     // trunc，向零取整    CAST_ODD,       // Von Neumann rounding，最近邻奇数舍入};

对于Cast，转换类型仅支持float转half(f322f16)与float转int32_t(f322s32)，相应支持的RoundMode如下：

●f322f16：CAST_ODD；

●f322s32：CAST_ROUND、CAST_CEIL、CAST_FLOOR、CAST_RINT。

Cast的精度转换规则具体可参考表6-368。

表6-651参数说明

参数名输入/输出

描述

valueIn输入被转换数据类型的标量。

返回值说明

U类型的valueIn。
