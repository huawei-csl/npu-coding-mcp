# GetICachePreloadStatus(ISASI)

> **Section**: 6.2.3.8.4  
> **PDF Pages**: 1863–1863  

---

<!-- page 1863 -->

参数说明

表6-751参数说明

参数名输入/输出

描述

preFetchLen输入预取长度。

针对Atlas A2 训练系列产品/Atlas A2 推理系列产品：preFetchLen参数单位为2K Byte, 取值应小于ICache的大小/2K。AIC和AIV的ICache大小分别为32KB和16KB。

针对Atlas A3 训练系列产品/Atlas A3 推理系列产品：preFetchLen参数单位为2K Byte, 取值应小于ICache的大小/2K。AIC和AIV的ICache大小分别为32KB和16KB。

针对Atlas 推理系列产品AI Core：传入该参数无效，预取长度均为128Byte。

针对Atlas 350 加速卡：preFetchLen参数单位为2K Byte,取值应小于ICache的大小/2K。AIC和AIV的ICache大小分别为32KB和16KB。

返回值说明

无

约束说明

无

调用示例

int64_t preFetchLen = 2; // 预取指令长度AscendC::ICachePreLoad(preFetchLen);

## 6.2.3.8.4 GetICachePreloadStatus(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
