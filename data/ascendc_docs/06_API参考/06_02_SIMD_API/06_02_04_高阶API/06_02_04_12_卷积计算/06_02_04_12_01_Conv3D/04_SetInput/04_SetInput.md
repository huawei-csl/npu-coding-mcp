# SetInput

> **Section**: 4  
> **PDF Pages**: 3004–3004  

---

<!-- page 3004 -->

调用示例

```cpp
TPipe pipe;conv3dApi.Init(&tiling);
```

## ?.4. SetInput

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

设置特征矩阵Input。

函数原型

```cpp
__aicore__ inline void SetInput(const AscendC::GlobalTensor<InputT>& input)
```

参数说明

参数名输入/输出描述

input输入Input在Global Memory上的首地址。类型为GlobalTensor。特征矩阵Input支持的数据类型为：half、bfloat16_t。

返回值说明

无

约束说明

无

调用示例

```cpp
GlobalTensor<half> inputGm;inputGm.SetGlobalBuffer(reinterpret_cast<__gm__ half *>(input));conv3dApi.SetInput(inputGm);
```
