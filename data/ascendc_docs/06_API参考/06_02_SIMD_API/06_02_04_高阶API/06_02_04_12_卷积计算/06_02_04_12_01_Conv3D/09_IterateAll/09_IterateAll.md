# IterateAll

> **Section**: 9  
> **PDF Pages**: 3009–3009  

---

<!-- page 3009 -->

参数说明

参数名输入/输出描述

diStartPos输入单核上Din方向起始位置。

mStartPos输入单核上M方向起始位置。

返回值说明

无

约束说明

无

调用示例

```cpp
conv3dApi.SetInputStartPosition(diIdxStart, mIdxStart);
```

## ?.9. IterateAll

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

通过设置结果矩阵Output在GM上的首地址，本接口一次性计算singleCo * singleDo *singleM大小的数据块，并写到结果矩阵Output中。

本接口提供单核内卷积计算能力，singleCo为多核切分后单个核内的输出通道大小；singleDo为多核切分后单个核内的Dout大小；singleM为多核切分后单个核内的M大小。singleCo、singleDo和singleM的大小通过SetSingleOutputShape接口设置。

函数原型

```cpp
__aicore__ inline void IterateAll(const AscendC::GlobalTensor<OutputT>& output, bool enPartialSum = false)
```
