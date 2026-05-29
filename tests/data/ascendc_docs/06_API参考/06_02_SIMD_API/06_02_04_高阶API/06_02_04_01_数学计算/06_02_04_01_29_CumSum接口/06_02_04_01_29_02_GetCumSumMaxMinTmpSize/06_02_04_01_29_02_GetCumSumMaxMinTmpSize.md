# GetCumSumMaxMinTmpSize

> **Section**: 6.2.4.1.29.2  
> **PDF Pages**: 2157–2157  

---

<!-- page 2157 -->

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●输入input只支持二维结构。

●cumSumInfo.inner * sizeof(T)必须是32字节的整数倍。

调用示例

完整的调用样例请参考CumSum样例。

// dstLocal: 存放计算结果的Tensor// lastRowLocal: 存放计算结果最后一行数据的Tensor// srcLocal: 参与计算的输入Tensor

// 按last轴处理（按列累加），输出最后一列数据，采用逐行累加算法constexpr AscendC::CumSumConfig cumSumConfig{true, false, true, AscendC::CumSumAlgorithm::CUMSUM_ALGORITHM_LINEBYLINE};// outer: 外轴长度// inner: 内轴长度const AscendC::CumSumInfo cumSumInfo{outer, inner};AscendC::CumSum<T, cumSumConfig>(dstLocal, lastRowLocal, srcLocal, cumSumInfo);

// 按first轴处理（按行累加），输出最后一行数据，采用逐行累加算法constexpr AscendC::CumSumConfig cumSumConfig{false, false, true, AscendC::CumSumAlgorithm::CUMSUM_ALGORITHM_LINEBYLINE};AscendC::CumSum<T, cumSumConfig>(dstLocal, lastRowLocal, srcLocal, cumSumInfo);

cumSumConfig取值{true, false, true,AscendC::CumSumAlgorithm::CUMSUM_ALGORITHM_LINEBYLINE}时示例数据如下：输入数据(srcLocal): [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]输出数据(dstLocal): [1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8]输出数据(lastRowLocal): [8 8 8 8]

cumSumConfig取值{false, false, true,AscendC::CumSumAlgorithm::CUMSUM_ALGORITHM_LINEBYLINE}时示例数据如下：输入数据(srcLocal): [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]输出数据(dstLocal): [1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4]输出数据(lastRowLocal): [4 4 4 4 4 4 4 4]

## 6.2.4.1.29.2 GetCumSumMaxMinTmpSize

功能说明

kernel侧CumSum接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetCumSumMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isLastAxis, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```
