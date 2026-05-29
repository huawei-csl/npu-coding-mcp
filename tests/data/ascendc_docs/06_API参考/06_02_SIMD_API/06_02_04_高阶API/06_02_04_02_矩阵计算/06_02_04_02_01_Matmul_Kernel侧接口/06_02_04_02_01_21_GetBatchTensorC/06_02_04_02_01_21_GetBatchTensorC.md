# GetBatchTensorC

> **Section**: 6.2.4.2.1.21  
> **PDF Pages**: 2355–2356  

---

<!-- page 2355 -->

返回值说明

无

约束说明

无

调用示例

REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.SetTensorA(gm_a);mm.SetTensorB(gm_b);mm.DisableBias();    //清除tiling中的Bias标志位mm.IterateAll(gm_c);mm.End();

## 6.2.4.2.1.21 GetBatchTensorC

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

调用一次GetBatchTensorC，会获取C矩阵片，该接口可以与IterateNBatch异步接口配合使用。用于在调用IterateNBatch迭代计算后，获取一片std::max(batchA, batchB)* singleCoreM * singleCoreN大小的矩阵分片。

函数原型

```cpp
template <bool sync = true>__aicore__ inline GlobalTensor<DstT> GetBatchTensorC(uint32_t batchA, uint32_t batchB, bool enSequentialWrite = false)template <bool sync = true>__aicore__ inline void GetBatchTensorC(const LocalTensor<DstT>& c, uint32_t batchA, uint32_t batchB, bool enSequentialWrite = false)
```

<!-- page 2356 -->

参数说明

表6-1045模板参数说明

参数名描述

sync当前仅支持异步模式，即该参数只支持取值为false。

表6-1046接口参数说明

参数名输入/输出

描述

batchA输入左矩阵的batch数。

batchB输入右矩阵的batch数。

enSequentialWrite

输入该参数预留，保持默认值false即可。

c输入C矩阵放置于Local Memory的地址，用于保存矩阵分片。

返回值说明

GlobalTensor<DstT>，返回计算的矩阵分片。

约束说明

●当使能MixDualMaster（双主模式）场景时，即模板参数enableMixDualMaster设置为true，不支持使用该接口。

●C矩阵片输出到Local Memory，且单核计算的N方向大小singleCoreN非32字节对齐的场景，C矩阵的CubeFormat仅支持ND_ALIGN格式，输出C矩阵片时，自动将singleCoreN方向上的数据补齐至32字节。

调用示例

// 计算需要多Batch计算循环次数int for_extent = tiling.ALayoutInfoB * tiling.ALayoutInfoN * g_lay / tiling.BatchNum;mm1.SetTensorA(gm_a[0], isTransposeAIn);mm1.SetTensorB(gm_b[0], isTransposeBIn);if (tiling.isBias) {    mm1.SetBias(gm_bias[0]);}// 多batch Matmul计算mm1.template IterateNBatch<false>(for_extent, batchA, batchB, false);...other computefor (int i = 0; i < for_extent; ++i) {       mm1.template GetBatchTensorC<false>(ubCmatrix);     ...other compute}
