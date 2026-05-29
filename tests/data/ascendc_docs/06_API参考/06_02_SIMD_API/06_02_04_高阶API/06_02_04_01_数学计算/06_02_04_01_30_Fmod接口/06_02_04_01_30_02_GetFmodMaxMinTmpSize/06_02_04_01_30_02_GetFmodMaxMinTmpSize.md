# GetFmodMaxMinTmpSize

> **Section**: 6.2.4.1.30.2  
> **PDF Pages**: 2162–2162  

---

<!-- page 2162 -->

// 接口框架申请临时空间，全部参与计算AscendC::Fmod(dstLocal, src0Local, src1Local);// 接口框架申请临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Fmod(dstLocal, src0Local, src1Local, 512);

// 通过sharedTmpBuffer入参传入临时空间，全部参与计算AscendC::Fmod(dstLocal, src0Local, src1Local, sharedTmpBuffer);// 通过sharedTmpBuffer入参传入临时空间，部分参与计算, 需要参与计算的元素个数为512AscendC::Fmod(dstLocal, src0Local, src1Local, sharedTmpBuffer, 512);__aicore__ constexpr AscendC::FmodConfig GetConfig() {    return { .algo = AscendC::FmodAlgo::ITERATION_COMPENSATION, .iterationNum = 11 };}static constexpr AscendC::FmodConfig config = GetConfig();AscendC::Fmod<float, false, config>(dstLocal, src0Local, src1Local, sharedTmpBuffer, 512);

结果示例如下：输入数据(src0Local): [-2.56 -2.55 -2.54 ... -0.01 0. 0.01 ... 2.53  2.54  2.55]输入数据(src1Local): [2.    2.    2.    ... 2.    2. 2.   ... 2.    2.    2.]输出数据(dstLocal):  [-0.56 -0.55 -0.54 ... -0.01 0. 0.01 ... 0.53  0.54  0.55]

## 6.2.4.1.30.2 GetFmodMaxMinTmpSize

功能说明

kernel侧Fmod接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大和最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetFmodMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t typeSize, const bool isReuseSource, uint32_t& maxValue, uint32_t& minValue)
```

参数说明

表6-940接口参数列表

参数名输入/输出

功能

srcShape输入输入的shape信息。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

isReuseSource

输入该参数预留，传入默认值false即可。
