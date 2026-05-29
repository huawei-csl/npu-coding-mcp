# SetMMRowMajor

> **Section**: 6.2.3.2.2.4  
> **PDF Pages**: 1097–1097  

---

<!-- page 1097 -->

调用示例

```cpp
int srcOffset = 0;int dstOffset = 0;AscendC::LocalTensor<int8_t> a1Local = inQueueA1.DeQue<int8_t>();AscendC::LocalTensor<int8_t> a2Local = inQueueA2.AllocTensor<int8_t>();
```

// a1Local矩阵为非稀疏矩阵AscendC::LoadData2DParams loadDataParams;loadDataParams.repeatTimes = kBlocks * mBlocks;loadDataParams.srcStride = 1;loadDataParams.ifTranspose = false;

```cpp
AscendC::LoadData(a2Local, a1Local, loadDataParams);
inQueueA2.EnQue<int8_t>(a2Local);inQueueA1.FreeTensor(a1Local);
AscendC::LocalTensor<int8_t> b2Local = inQueueB2.AllocTensor<int8_t>();
```

// transform nz to zn, 稀疏矩阵的加载需要配合稀疏的索引和loadDataWithSparse指令进行稀疏数据加载AscendC::LoadData2DParams loadDataParams;loadDataParams.repeatTimes = kBlocks * nBlocks / 2;loadDataParams.srcStride = 0;loadDataParams.ifTranspose = false;

```cpp
AscendC::LoadDataWithSparse(b2Local, b1Local, idxb1Local, loadDataParams);
inQueueB2.EnQue<int8_t>(b2Local);
AscendC::LocalTensor<int8_t> b2Local = inQueueB2.DeQue<int8_t>();AscendC::LocalTensor<int32_t> c1Local = outQueueCO1.AllocTensor<int32_t>();
```

// mmad 需要指定矩阵的维度进行计算uint32 m = 16;uint32 k = 64;uint32 n = 16;AscendC::MmadWithSparse(c1Local, a2Local, b2Local, { m, n, k, false, 0, false, false, false });

## 6.2.3.2.2.4 SetMMRowMajor

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

设置Mmad计算时优先通过N方向，CUBE将首先通过N方向，然后通过M方向生成结果。
