# GetArchVersion

> **Section**: 6.2.3.9.4  
> **PDF Pages**: 1867–1867  

---

<!-- page 1867 -->

函数原型

```cpp
__aicore__ inline constexpr int16_t GetDataBlockSizeInBytes()
```

参数说明

无

返回值说明

当前芯片版本一个datablock的大小，单位为byte。

约束说明

无

调用示例

如下样例通过GetDataBlockSizeInBytes获取的datablock值，来计算repeatTime的值：

int16_t dataBlockSize = AscendC::GetDataBlockSizeInBytes();// 每个repeat有8个datablock,可计算8 * dataBlockSize / sizeof(half)个数，mask配置为迭代内所有元素均参与计算uint64_t mask = 8 * dataBlockSize / sizeof(half);// 共计算512个数，除以每个repeat参与计算的元素个数，得到repeatTimeuint8_t repeatTime = 512 / mask; // dstBlkStride, src0BlkStride, src1BlkStride = 1, 单次迭代内数据连续读取和写入// dstRepStride, src0RepStride, src1RepStride = 8, 相邻迭代间数据连续读取和写入AscendC::Add(dstLocal, src0Local, src1Local, mask, repeatTime, { 1, 1, 1, 8, 8, 8 });

## 6.2.3.9.4 GetArchVersion

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取当前AI处理器架构版本号。
