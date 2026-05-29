# GetSumMaxMinTmpSize

> **Section**: 6.2.4.6.1.2  
> **PDF Pages**: 2731–2731  

---

<!-- page 2731 -->

// 定义srcTensor的shape信息，输入元素类型为half，大小为2*3的二维数据AscendC::SumParams params;// m为2, outter等于m的值params.outter = outter;// n为3params.n = n;// inner = (n * sizeof(half) + 32 - 1)/32 * 32 / sizeof(half) = 16params.inner = inner;// 填充时的值T scalar(0);// yLocal填充为0，out_inner是2向上16取整到的值，为16，计算方法参考innerAscendC::Duplicate<T>(yLocal, scalar, out_inner);// 对shape为(2, 3)的二维矩阵进行运算，输出结果为[6, 15]// xLocal和yLocal中的0是计算时padding的值AscendC::Sum(yLocal, xLocal, sharedTmpBuffer, params);

结果示例如下。输入数据srcLocal: [[1 2 3 0 0 0 0 0 0 0 0 0 0 0 0 0],                     [4 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0]]输出数据dstLocal: [6 15 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

## 6.2.4.6.1.2 GetSumMaxMinTmpSize

功能说明

kernel侧Sum接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

函数原型

```cpp
inline void GetSumMaxMinTmpSize(const uint32_t n, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxSize, uint32_t& minSize)
```

参数说明

表6-1252接口参数列表

接口输入/输出

功能

n输入输入数据每行的实际计算个数。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入是否复用源操作数输入的空间，与Sum接口一致，此处预留。
