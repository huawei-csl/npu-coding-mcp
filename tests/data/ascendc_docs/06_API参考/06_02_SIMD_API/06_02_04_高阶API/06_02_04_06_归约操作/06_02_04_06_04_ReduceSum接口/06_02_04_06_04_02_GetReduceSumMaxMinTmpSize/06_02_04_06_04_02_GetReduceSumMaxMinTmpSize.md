# GetReduceSumMaxMinTmpSize

> **Section**: 6.2.4.6.4.2  
> **PDF Pages**: 2746–2746  

---

<!-- page 2746 -->

输入shape：(2,8)输出数据(dst): [13.0 9.0]

## 6.2.4.6.4.2 GetReduceSumMaxMinTmpSize

功能说明

kernel侧ReduceSum接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

函数原型

```cpp
void GetReduceSumMaxMinTmpSize(const ge::Shape& srcShape, const ge::DataType dataType, ReducePattern pattern, bool isSrcInnerPad, bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-1262接口参数列表

接口输入/输出

功能

srcShape输入输入的shape信息，参数取值与ReduceSum接口的srcShape参数保持一致。

dataType输入输入的数据类型，ge::DataType类型，当前支持的数据类型与ReduceSum接口的模板参数T保持一致。

pattern输入用于指定ReduceSum的计算轴。ReducePattern类型，该类型的定义如下，包括Reduce轴和Normal轴。pattern由与输入向量维度数量相同的A、R字母组合形成，字母A表示Normal轴，R表示Reduce轴。该参数的取值与ReduceSum接口的pattern参数保持一致，当前只支持取值为AscendC::ReducePattern::AR，AscendC::ReducePattern::RA。enum class ReducePattern : uint32_t {    AR = 0,    RA = 1,    R,    ARA,    ARAR,    ARARA,    ARARAR,    ARARARA,    ARARARAR,    ARARARARA,    RAR,    RARA,    RARAR,    RARARA,    RARARAR,    RARARARA,};
