# GetMeanMaxMinTmpSize

> **Section**: 6.2.4.6.2.2  
> **PDF Pages**: 2736–2736  

---

<!-- page 2736 -->

#include "kernel_operator.h"// 定义srcTensor的shape信息，输入元素类型为half，大小为2*3的二维数据AscendC::MeanParams meanParams;// m为2, outter等于m的值meanParams.outter = outter;// n为3meanParams.n = n;// inner = (n * sizeof(half) + 32 - 1)/32 * 32 / sizeof(half) = 16meanParams.inner = inner;// T为half，accTypes为实际计算的类型这里是half// dstLocal输出数据，srcLocal输入数据，tmplocalTensor用户传入的临时缓存                                                                     AscendC::Mean<T, accType>(dstLocal, srcLocal, tmplocalTensor, meanParams)// 也可不使用tmplocalTensor。调用如下// AscendC::Mean<T, accType>(dstLocal, srcLocal, meanParams);

结果示例如下：输入数据(srcLocal): [[1 2 3 0 0 0 0 0 0 0 0 0 0 0 0 0],                     [4 5 6 0 0 0 0 0 0 0 0 0 0 0 0 0]]输出数据(dstLocal): [2 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

## 6.2.4.6.2.2 GetMeanMaxMinTmpSize

功能说明

kernel侧Mean接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

函数原型

```cpp
void GetMeanMaxMinTmpSize(const uint32_t n, const uint32_t srcTypeSize, const uint32_t accTypeSize, const bool isReuseSource, uint32_t& maxSize, uint32_t& minSize)
```

参数说明

表6-1255接口参数列表

接口输入/输出

功能

n输入输入数据每行的实际计算个数。

srcTypeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处为2。

accTypeSize输入accType的数据类型大小，单位为字节，accType参数说明可参考Mean接口参数说明。

isReuseSource

输入是否复用源操作数输入的空间，与Mean接口一致。此处为预留参数。
