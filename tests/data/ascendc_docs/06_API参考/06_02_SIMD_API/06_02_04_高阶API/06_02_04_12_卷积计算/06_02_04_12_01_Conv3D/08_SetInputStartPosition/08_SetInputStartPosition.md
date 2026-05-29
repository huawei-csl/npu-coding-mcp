# SetInputStartPosition

> **Section**: 8  
> **PDF Pages**: 3008–3008  

---

<!-- page 3008 -->

参数说明

参数名输入/输出描述

singleCo输入单核上Output的C维度大小。

singleDo输入单核上Output的D维度大小。

singleM输入单核上Output的M维度大小，即H维度大小与W维度大小的乘积。

返回值说明

无

约束说明

本接口当前仅支持设置Output的C维度、D维度和M维度（即H轴、W轴合并后的维度），不支持设置原始Output的大小。

调用示例

```cpp
conv3dApi.SetSingleOutputShape(singleCoreCout, singleCoreDout, singleCoreM);
```

## ?.8. SetInputStartPosition

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

设置单核上特征矩阵Input载入数据的起始位置。

函数原型

```cpp
__aicore__ inline void SetInputStartPosition(int64_t diStartPos, int64_t mStartPos)
```
