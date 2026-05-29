# SetMMColumnMajor

> **Section**: 6.2.3.2.2.5  
> **PDF Pages**: 1098–1098  

---

<!-- page 1098 -->

函数原型

```cpp
__aicore__ inline void SetMMRowMajor()
```

参数说明

无

返回值说明

无

约束说明

无

调用示例

AscendC::SetMMRowMajor();// 设置Mmad优先计算输出矩阵的N方向，再计算M方向。

## 6.2.3.2.2.5 SetMMColumnMajor

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置Mmad计算时优先通过M方向，CUBE将首先通过M方向，然后通过N方向产生结果。

函数原型

```cpp
__aicore__ inline void SetMMColumnMajor()
```

参数说明

无
