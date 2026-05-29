# 算子与高阶API共享临时Buffer

> **Section**: 3.8.5.8  
> **PDF Pages**: 597–597  

---

<!-- page 597 -->

原始实现优化实现

实现方案

总数据量700MB，其中：x：100MB；y：300MB；z：300MB。

总数据量700MB，其中：x：100MB；y：300MB；z：300MB。

实现方法

使用40个核参与计算，按列方向切分。

使用40个核参与计算，按列方向切分。

x对应的GlobalTensor的CacheMode设置为CACHE_MODE_NORMAL；y和z对应的GlobalTensor的CacheMode设置为CACHE_MODE_DISABLE。只有需要频繁访问的x，设置为需要经过L2 Cache。需要进入L2 Cache的总数据量为100MB。

x、y、z 对应GlobalTensor的CacheMode均设置为CACHE_MODE_NORMAL，需要经过L2 Cache，需要进入L2Cache的总数据量为700MB。

```cpp
xGm.SetGlobalBuffer((__gm__ float *)x + AscendC::GetBlockIdx() * TILE_N);yGm.SetGlobalBuffer((__gm__ float *)y + AscendC::GetBlockIdx() * TILE_N);zGm.SetGlobalBuffer((__gm__ float *)z + AscendC::GetBlockIdx() * TILE_N);
xGm.SetGlobalBuffer((__gm__ float *)x + AscendC::GetBlockIdx() * TILE_N);yGm.SetGlobalBuffer((__gm__ float *)y + AscendC::GetBlockIdx() * TILE_N);zGm.SetGlobalBuffer((__gm__ float *)z + AscendC::GetBlockIdx() * TILE_N);// disable the L2 cache mode of y and zyGm.SetL2CacheHint(AscendC::CacheMode::CACHE_MODE_DISABLE);zGm.SetL2CacheHint(AscendC::CacheMode::CACHE_MODE_DISABLE);
```

示例代码

说明

你可以通过执行如下命令行，通过算子调优（msProf）工具获取上述示例的性能数据并进行对比。

```cpp
msprof op --launch-count=2 --output=./prof ./execute_add_op
```

重点关注Memory.csv中的aiv_gm_to_ub_bw(GB/s)和aiv_main_mem_write_bw(GB/s)写带宽的速率。

## 3.8.5.8 算子与高阶API 共享临时Buffer

【优先级】高

【描述】如果算子使用的高阶API需要传入临时Buffer，如SoftMax，该临时空间会挤占算子其他计算的空间，从而导致单次计算搬运的数据量变少，搬运的次数变多。此场景可通过共享临时Buffer空间，提升单次搬运的数据量，减少搬运的次数，提升内存使用效率。

【反例】

SoftMax高阶API计算需要临时Buffer空间，算子在进行其他计算时拥有独立临时Buffer。UB空间是固定的，假设可以给SoftMax和Add能分配临时空间为64KB，SoftMax计算需要的临时Buffer空间tmpSoftmaxBuf占用32KB，则存储Add计算结果的LocalTensor tmpSumBuf最多只能分配32KB。如果src0Tensor计算的数据量是512KB，则需要搬运512 / 32 = 16次。...constexpr int32_t blockLen = 32 * 1024;TBuf<TPosition::VECCALC> tmpSoftmaxBuf;
