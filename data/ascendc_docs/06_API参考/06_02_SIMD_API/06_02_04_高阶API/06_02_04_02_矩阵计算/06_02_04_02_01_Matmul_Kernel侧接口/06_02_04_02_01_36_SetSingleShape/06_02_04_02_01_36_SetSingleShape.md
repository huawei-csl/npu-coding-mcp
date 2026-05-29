# SetSingleShape

> **Section**: 6.2.4.2.1.36  
> **PDF Pages**: 2388–2389  

---

<!-- page 2388 -->

返回值说明

无

约束说明

本接口需要在SetTensorA接口、SetTensorB接口、SetBias接口及SetSingleShape接口前调用。

调用示例

●设置矩阵原始完整的形状REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);mm.SetBias(gm_bias);mm.IterateAll(gm_c);//  复用mm对象mm.SetOrgShape(orgM, orgN, orgK);mm.SetTensorA(gm_a1);mm.SetTensorB(gm_b1);mm.SetBias(gm_bias1);mm.IterateAll(gm_c1);

●对于Atlas 350 加速卡上使用MDL模板的Matmul对象，设置GM或L1上完整的形状

完整的样例请参考matmul_tscm_mdl_setorgshape样例。REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);for (int m = 0; m < mIter_; m++) {     for (int n = 0; n < nIter_; n++) {          for (int k = 0; k < kIter_; k++) {               // 复用mm，指定A在L1和B在GM上的shape               mm.SetOrgShape(alignedSingleM, tiling.N, alignedSingleK, tiling.Kb, tiling.N);               mm.SetSingleShape(curBaseM, curBaseN, curBaseK);               mm.SetTensorA(tscm_a[offset_a]); // Set aMatrix tscm input               mm.SetTensorB(gm_b[offset_b]);               mm.SetBias(gm_bias[offset_bias]);               mm.Iterate(k != 0);            }            matmulObj.GetTensorC(gm_c[offset_c]);     }}

## 6.2.4.2.1.36 SetSingleShape

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

<!-- page 2389 -->

产品是否支持

Atlas 训练系列产品x

功能说明

设置Matmul单核计算的形状singleCoreM、singleCoreN、singleCoreK，单位为元素。用于运行时修改shape，比如复用Matmul对象来处理尾块。与SetTail接口功能一致，建议使用本接口。

函数原型

```cpp
__aicore__ inline void SetSingleShape(int singleM, int singleN, int singleK)
```

参数说明

表6-1058参数说明

参数名输入/输出

描述

singleM输入设置的singleCoreM大小，单位为元素。

singleN输入设置的singleCoreN大小，单位为元素。

singleK输入设置的singleCoreK大小，单位为元素。

返回值说明

无

约束说明

无

调用示例

```cpp
REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);
```

// tailM：M方向上剩余元素个数，tailN：N方向上剩余元素个数，tailK：K方向上剩余元素个数// 如果是尾核，剩余元素可能会少于单核需要计算的元素。此时，需要使用SetSingleShape重新设置本次计算的元素个数if (tailM < tiling.singleCoreM || tailN < tiling.singleCoreN || tailK < tiling.singleCoreK) {    matmulObj.SetSingleShape(tailM, tailN, tailK);}

```cpp
mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);if (tiling.isBias) {    mm.SetBias(gmBias);}mm.IterateAll(gm_c);mm.End();
```
