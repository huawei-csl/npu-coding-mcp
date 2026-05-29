# SetAntiQuantScalar

> **Section**: 6.2.4.2.1.39  
> **PDF Pages**: 2392–2392  

---

<!-- page 2392 -->

参数说明

参数名输入/输出

描述

addr输入用户传入的GM上的workspace空间，GlobalTensor类型。

addr输入用户传入的GM上的workspace空间，GM地址类型。

size输入传入GM地址时，需要配合传入元素个数。

返回值说明

无

约束说明

当使能MixDualMaster（双主模式）场景时，即模板参数enableMixDualMaster设置为true，不支持使用该接口。

调用示例

REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetWorkspace(workspaceGM);    //设置异步时使用的临时空间mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);if (tiling.isBias) {    mm.SetBias(biasGlobal);}mm.template Iterate<false>();for (int i = 0; i < singleCoreM/baseM * singleCoreN/baseN; ++i) {    mm.template GetTensorC<false>(ub_c);}

## 6.2.4.2.1.39 SetAntiQuantScalar

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
