# SetLocalWorkspace

> **Section**: 6.2.4.2.1.37  
> **PDF Pages**: 2390–2390  

---

<!-- page 2390 -->

## 6.2.4.2.1.37 SetLocalWorkspace

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

对于某些场景Matmul内部需要额外占用VECCALC空间，如果用户希望在算子中复用这个额外占用的VECCALC空间，则该空间需要用户预留，并申请好LocalTensor，将其起始物理地址传入给Matmul。具体需要申请的VECCALC临时空间大小由tiling接口MatmulGetTmpBufSize给出，满足以下几个条件之一就需要使用该接口传入UB临时空间：

●C矩阵Position为TPosition::GM；

●C矩阵CubeFormat为CubeFormat::ND；

●A矩阵或者B矩阵CubeFormat为CubeFormat::ND；

●存在Bias且Bias的Position不是VECCALC。

请在Iterate或者 IterateAll之前调用该接口。

获取到的UB临时空间大小以字节为单位。

函数原型

```cpp
__aicore__ inline void SetLocalWorkspace(const LocalTensor<uint8_t>& tmpBuffer)
```

参数说明

参数名输入/输出

描述

tmpBuffer输入临时空间，由用户申请并管理，TPosition为VECCALC。

返回值说明

无
