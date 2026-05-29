# SetFixPipeConfig

> **Section**: 6.2.3.2.1.13  
> **PDF Pages**: 1055–1056  

---

<!-- page 1055 -->

```cpp
662.  889.  841. 1492. 1742.  884. 1674.  940. 1800. 1892.  809.  782.  1574.  966. 2034. 1866.  814. 1826.  592. 1686.] [ 861. 1508.  839. 1670.  806.  884.  777. 1308. 1542. 1538.  838.  650.   627.  865.  799. 1362. 1530.  753. 1824.  848. 1496. 1744.  755.  811.  1362. 1018. 1798. 1700.  809. 1690.  628. 1524.] [ 916. 1632.  918. 1792.  847.  948.  807. 1450. 1622. 1644.  848.  752.   655.  883.  830. 1530. 1636.  784. 1750.  959. 1636. 1852.  725.  860.  1498. 1032. 1818. 1660.  752. 1950.  662. 1574.] [ 822. 1602.  807. 1662.  757.  812.  678. 1306. 1734. 1624.  840.  633.   568.  804.  737. 1366. 1586.  830. 1734.  860. 1544. 1862.  747.  801.  1578.  921. 1696. 1490.  689. 1740.  622. 1506.]]
```

●示例三：通路CO1->C1，使能tensor量化功能接口。输入A矩阵和输入B矩阵的数据类型为half，输出C矩阵为float，使能ND2DN搬运，不使能量化，将mmad计算出的结果由float量化成float。AscendC::LocalTensor<l1out_T> dst_l0c = outQueueCO1.DeQue<l1out_T>();AscendC::LocalTensor<uint64_t> cbufWorkspace = deqQueue.DeQue<uint64_t>();uint16_t deqDataSize = AscendC::DivCeil(deq_size * sizeof(uint64_t), 128) * 128;float tmp = 0.5;uint64_t val = static_cast<uint64_t>(*reinterpret_cast<int32_t*>(&tmp));AscendC::FixpipeParamsArch3510<AscendC::CO2Layout::COLUMN_MAJOR> fixpipeParams = {n, m, static_cast<uint16_t>(AscendC::AlignUp(m, AscendC::BLOCK_CUBE)), m};fixpipeParams.params = {1, 0, 0, 1};fixpipeParams.reluEn = 1;AscendC::Fixpipe<dst_T, l1out_T, AscendC::CFG_COLUMN_MAJOR>(output_gm, dst_l0c, fixpipeParams);outQueueCO1.FreeTensor(dst_l0c);deqQueue.FreeTensor(cbufWorkspace);

●示例四：通路CO1->C1，使能tensor量化功能接口。输入A矩阵和输入B矩阵的数据类型为half，输出C矩阵为float，使能ND2DN搬运，使能量化F322F16，将mmad计算出的结果由float量化成half。AscendC::LocalTensor<l1out_T> dst_l0c = outQueueCO1.DeQue<l1out_T>();AscendC::LocalTensor<uint64_t> cbufWorkspace = deqQueue.DeQue<uint64_t>();uint16_t deqDataSize = AscendC::DivCeil(deq_size * sizeof(uint64_t), 128) * 128;float tmp = 0.5;uint64_t val = static_cast<uint64_t>(*reinterpret_cast<int32_t*>(&tmp));AscendC::FixpipeParamsArch3510<AscendC::CO2Layout::COLUMN_MAJOR> fixpipeParams = {n, m, static_cast<uint16_t>(AscendC::AlignUp(m, AscendC::BLOCK_CUBE)), m};fixpipeParams.params = {1, 0, 0, 1};fixpipeParams.reluEn = 1;fixpipeParams.quantPre = F322F16;AscendC::Fixpipe<dst_T, l1out_T, AscendC::CFG_COLUMN_MAJOR>(output_gm, dst_l0c, fixpipeParams);outQueueCO1.FreeTensor(dst_l0c);deqQueue.FreeTensor(cbufWorkspace);

## 6.2.3.2.1.13 SetFixPipeConfig

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

<!-- page 1056 -->

产品是否支持

Atlas 训练系列产品x

功能说明

**DataCopy（CO1->GM、CO1->A1）过程中进行随路量化时，通过调用该接口设置量化流程中tensor量化参数。**

函数原型

```cpp
template <typename T>__aicore__ inline void SetFixPipeConfig(const LocalTensor<T>& reluPre, const LocalTensor<T>& quantPre, bool isUnitFlag = false)template <typename T, bool setRelu = false>__aicore__ inline void SetFixPipeConfig(const LocalTensor<T>& preData, bool isUnitFlag = false)
```

参数说明

表6-199模板参数说明

参数名描述

T操作数的数据类型。

setRelu针对设置一个tensor的情况，当setRelu为true时，设置reluPre；反之设置quantPre。setRelu当前仅支持设置为false。

表6-200参数说明

参数名称输入/输出

含义

reluPre输入源操作数，relu操作时参与计算的tensor，类型为LocalTensor，支持的TPosition为C2PIPE2GM。

reluPre为预留参数，暂未启用，为后续的功能扩展做保留，传入一个空LocalTensor即可。

quantPre输入源操作数，quant tensor，量化操作时参与计算的tensor，类型为LocalTensor，支持的TPosition为C2PIPE2GM。

isUnitFlag

输入UnitFlag配置项，默认值为false。

●false：关闭UnitFlag配置。

●true：打开UnitFlag配置。

preData输入支持设置一个Tensor，通过开关控制是relu Tensor还是quantTensor，支持的TPosition为C2PIPE2GM。当前仅支持传入quant Tensor。
