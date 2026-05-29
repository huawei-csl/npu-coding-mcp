# GetSysWorkSpacePtr

> **Section**: 1  
> **PDF Pages**: 1811–1811  

---

<!-- page 1811 -->

## ?.1. GetSysWorkSpacePtr

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

获取系统workspace指针。部分高阶API如Matmul需要使用系统workspace，相关接口需要传入系统workspace指针，此时可以通过该接口获取。使用系统workspace时，host侧开发者需要自行申请系统workspace的空间，其预留空间大小可以通过6.4.2.1.13 GetLibApiWorkSpaceSize接口获取。具体内容请参考2.10.9.3 如何使用workspace。

函数原型

```cpp
__aicore__ inline __gm__ uint8_t* __gm__ GetSysWorkSpacePtr()
```

参数说明

无

约束说明

无

返回值说明

系统workspace指针。

调用示例

...REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling); // 初始化，传入系统workspace指针// CopyIn阶段：完成从GM到LocalMemory的搬运mm.SetTensorA(gm_a);    // 设置左矩阵Amm.SetTensorB(gm_b);    // 设置右矩阵Bmm.SetBias(gm_bias);    // 设置Bias// Compute阶段：完成矩阵乘计算while (mm.Iterate()) {     // CopyOut阶段：完成从LocalMemory到GM的搬运    mm.GetTensorC(gm_c);
