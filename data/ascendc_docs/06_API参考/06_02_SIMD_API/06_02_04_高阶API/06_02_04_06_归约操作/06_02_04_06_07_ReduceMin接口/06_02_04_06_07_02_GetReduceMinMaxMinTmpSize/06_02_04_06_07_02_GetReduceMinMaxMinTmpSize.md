# GetReduceMinMaxMinTmpSize

> **Section**: 6.2.4.6.7.2  
> **PDF Pages**: 2761–2762  

---

<!-- page 2761 -->

参数名输入/输出

描述

srcInnerPad输入表示实际需要计算的最内层轴数据是否32Bytes对齐。

Atlas 350 加速卡，该参数预留。接口内由参数srcShape和pattern计算最内层轴数据是否32Bytes对齐。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，当前只支持true。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，当前只支持true。

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●不支持源操作数与目的操作数地址重叠。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

调用示例

完整的算子样例请参考ReduceMin算子样例。

uint32_t shape[] = { 2, 8 };constexpr bool isReuse = true;AscendC::ReduceMin<float, AscendC::Pattern::Reduce::AR, isReuse>(dstLocal, srcLocal, tmp, shape, true); // tmp为传入的临时空间大小，shape为srcLocal输入的shape， true表示地址是否32B对齐

结果示例如下：

输入输出的数据类型为float输入数据(src): [[ 0.0 4.0 2.0 0.0 -1.0 2.0 -1.0 7.0], [ 0.0 1.0 -9.0 2.0 2.0 2.0 8.0 3.0]]输入pattern：AR输入shape：(2,8)输出数据(dst): [-1.0 -9.0]

## 6.2.4.6.7.2 GetReduceMinMaxMinTmpSize

功能说明

kernel侧ReduceMin接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

<!-- page 2762 -->

函数原型

```cpp
void GetReduceMinMaxMinTmpSize(const ge::Shape& srcShape, const ge::DataType dataType, ReducePattern pattern, bool isSrcInnerPad, bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1271接口参数列表

接口输入/输出

功能

srcShape输入输入的shape信息，参数取值与ReduceMin接口的srcShape参数保持一致。

dataType输入输入的数据类型，ge::DataType类型，当前支持的数据类型与ReduceMin接口的模板参数T保持一致。

pattern输入用于指定ReduceMin的计算轴。ReducePattern类型，该类型的定义如下，包括Reduce轴和Normal轴。pattern由与输入向量维度数量相同的A、R字母组合形成，字母A表示Normal轴，R表示Reduce轴。该参数的取值与ReduceMin接口的pattern参数保持一致，当前只支持取值为AscendC::ReducePattern::AR，AscendC::ReducePattern::RA。enum class ReducePattern : uint32_t {    AR = 0,    RA = 1,    R,    ARA,    ARAR,    ARARA,    ARARAR,    ARARARA,    ARARARAR,    ARARARARA,    RAR,    RARA,    RARAR,    RARARA,    RARARAR,    RARARARA,};

isSrcInnerPad

输入表示实际需要计算的最内层轴数据是否32Bytes对齐，参数取值与ReduceMin接口的isSrcInnerPad参数保持一致。

isReuseSource

输入是否复用源操作数输入的空间，参数取值与ReduceMin接口的isReuseSource参数保持一致。

maxValue输出ReduceMin接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出ReduceMin接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。
