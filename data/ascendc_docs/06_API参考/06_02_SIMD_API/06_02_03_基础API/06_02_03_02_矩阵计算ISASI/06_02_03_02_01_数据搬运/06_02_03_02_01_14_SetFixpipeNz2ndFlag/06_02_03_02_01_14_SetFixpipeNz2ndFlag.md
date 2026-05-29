# SetFixpipeNz2ndFlag

> **Section**: 6.2.3.2.1.14  
> **PDF Pages**: 1057–1058  

---

<!-- page 1057 -->

约束说明

quantPre和reluPre必须是Fixpipe Buffer上的Tensor。

返回值说明

无

调用示例

完整示例可参考完整示例。

__aicore__inline void SetFPC(const LocalTensor <int32_t>& reluPreTensor, const LocalTensor <int32_t>& quantPreTensor){    AscendC::LocalTensor<uint64_t> workA1 = inQueueDeqA1.AllocTensor<uint64_t>();    uint16_t deqSize = 128; // deq tensor的size    AscendC::DataCopy(workA1, deqGlobal, deqSize); // deqGlobal为量化系数的gm地址    AscendC::LocalTensor<uint64_t> deqFB = inQueueDeqFB.AllocTensor<uint64_t>(); // deq tensor在Fix上的地址    uint16_t fbufBurstLen = deqSize / 128;  // l1->fix, burst_len unit is 128Bytes    AscendC::DataCopyParams dataCopyParams(1, fbufBurstLen, 0, 0);    AscendC::DataCopy(deqFB, workA1, dataCopyParams); 通过DataCopy搬入C2PIPE2GM。    AscendC::SetFixPipeConfig(deqFB); // 设置量化tensor    AscendC::PipeBarrier<PIPE_FIX>();}

## 6.2.3.2.1.14 SetFixpipeNz2ndFlag

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

**DataCopy（CO1->GM、CO1->A1）过程中进行随路格式转换（NZ格式转换为ND格式）时，通过调用该接口设置格式转换的相关配置。**

函数原型

__aicore__ inline void SetFixpipeNz2ndFlag(uint16_t ndNum, uint16_t srcNdStride, uint16_t dstNdStride)// 如下原型仅支持Atlas 350 加速卡__aicore__ inline void SetFixpipeNz2ndFlag(uint16_t ndNum, uint16_t srcNdStride, uint32_t dstNdStride)

<!-- page 1058 -->

参数说明

表6-201参数说明

参数名称输入/输出

含义

ndNum输入nd的数量，类型是uint16_t，取值范围：ndNum∈[1,65535]。

srcNdStride

输入以分形大小为单位的源步长，源相邻nz矩阵的偏移（头与头）。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，srcNdStride∈[1, 512]，单位：fractal_size 1024B。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，srcNdStride∈[1, 512]，单位：fractal_size 1024B。

Atlas 200I/500 A2 推理产品，srcNdStride∈[1, 512]，单位：fractal_size 1024B。

Atlas 350 加速卡，srcNdStride∈[0, 65535]，单位：C0_SIZE。

dstNdStride

输入目的相邻nd矩阵的偏移（头与头）。单位为元素。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，dstNdStride∈[1, 65535]。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，dstNdStride∈[1, 65535]。

Atlas 200I/500 A2 推理产品，dstNdStride∈[1, 65535]。

Atlas 350 加速卡，dstNdStride∈[1, 232 -1]。

返回值说明

无

约束说明

无

调用示例

完整示例可参考完整示例。

uint16_t ndNum = 2;uint16_t srcNdStride = 2;uint16_t dstNdStride = 1;AscendC::SetFixpipeNz2ndFlag(ndNum, srcNdStride, dstNdStride); // 设置FIX搬运NZ格式到ND格式转换的参数
