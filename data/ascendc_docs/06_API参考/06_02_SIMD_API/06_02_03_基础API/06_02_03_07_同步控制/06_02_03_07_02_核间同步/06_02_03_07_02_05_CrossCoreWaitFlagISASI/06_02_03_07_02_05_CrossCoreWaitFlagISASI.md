# CrossCoreWaitFlag(ISASI)

> **Section**: 6.2.3.7.2.5  
> **PDF Pages**: 1846–1848  

---

<!-- page 1846 -->

–对于Vector和Cube混合场景，需根据实际情况灵活配置Kernel类型。

●因为Matmul高阶API内部实现中使用了本接口进行核间同步控制，所以不建议开发者同时使用该接口和Matmul高阶API，否则会有flagID冲突的风险。

●同一flagId的计数器最多设置15次。

●使用该接口模式0时，建议开启batchmode模式，使算子独占全部所需核资源，否则可能因满足以下条件导致死锁：

–多流并发场景（≥2条执行流）。

–≥2个算子并发执行。

–所有并发算子的核数总和超过物理核数。

–≥2个并发算子使用了核间同步功能。

具体而言，在多流场景下，某条流的核间同步算子虽分配到n个物理核，但可能仅有n-m个核先被调度执行，而其余m个核因被其他流的核间同步算子抢占而尚未启动。先启动的n-m个核执行到核间同步时等待剩余m核完成，而剩余m核因被其他流的核间同步算子占用而无法释放，形成死锁。

Kernel直调场景下通过__schedmode__(mode)限定符来设置batchmode模式；工程化算子开发场景下，通过TilingContext的SetScheduleMode接口来设置batchmode模式，具体请参考《基础数据结构和接口》。

调用示例

// 使用模式0的方式同步所有的AIV核if (g_coreType == AscendC::AIV) {    AscendC::CrossCoreSetFlag<0x0, PIPE_MTE3>(0x8);    AscendC::CrossCoreWaitFlag(0x8);}

// 使用模式1的方式同步当前AICore内的所有AIV子核if (g_coreType == AscendC::AIV) {    AscendC::CrossCoreSetFlag<0x1, PIPE_MTE3>(0x8);    AscendC::CrossCoreWaitFlag(0x8);}

// 注意：如果调用高阶API,无需开发者处理AIC和AIV的同步// 以Matmul为例：AIC侧做完Matmul计算后通知AIV进行后处理if (g_coreType == AscendC::AIC) {    // Matmul处理    AscendC::CrossCoreSetFlag<0x2, PIPE_FIX>(0x8);}

// AIV侧等待AIC Set消息, 进行Vector后处理if (g_coreType == AscendC::AIV) {    AscendC::CrossCoreWaitFlag(0x8);    // Vector后处理}

## 6.2.3.7.2.5 CrossCoreWaitFlag(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

<!-- page 1847 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

面向分离模式的核间同步控制接口。该接口和CrossCoreSetFlag接口配合使用。具体使用方法请参考CrossCoreSetFlag。

函数原型

```cpp
template <uint8_t modeId = 0, pipe_t pipe = PIPE_S>__aicore__ inline void CrossCoreWaitFlag(uint16_t flagId)
```

参数说明

表6-742模板参数说明

参数名描述

modeId核间同步的模式，取值如下：

●模式0：AI Core核间的同步控制。

●模式1：AI Core内部，Vector核（AIV）之间的同步控制。

●模式2：AI Core内部，Cube核（AIC）与Vector核（AIV）之间的同步控制。

●模式4：AI Core内部，AIC与AIV之间的同步控制。AIV0与AIV1可单独触发AIC等待。

pipe设置这条指令所在的流水类型，流水类型可参考硬件流水类型。

特别地，PIPE_S流水类型仅Atlas 350 加速卡支持。

<!-- page 1848 -->

表6-743参数说明

参数名输入/输出

描述

flagId输入核间同步的标记。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，取值范围是0-10。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，取值范围是0-10。

Atlas 350 加速卡，取值范围如下：

AIV0发起的flagId 0-10的CrossCoreSetFlag操作对应AICCrossCoreWaitFlag中flagId 0-10的操作。

AIV1发起的flagId 0-10的CrossCoreSetFlag操作对应AICCrossCoreWaitFlag中flagId 16-26的操作。

AIC发起的flagId 0-10的CrossCoreSetFlag操作对应AIV0CrossCoreWaitFlag中flagId 0-10的操作。

AIC发起的flagId 16-26的CrossCoreSetFlag操作对应AIV1CrossCoreWaitFlag中flagId 0-10的操作。

返回值说明

无

约束说明

●使用该同步接口时，需要按照如下规则设置Kernel类型：

–在纯Vector/Cube场景下，需设置Kernel类型为KERNEL_TYPE_MIX_AIV_1_0或KERNEL_TYPE_MIX_AIC_1_0。

–对于Vector和Cube混合场景，需根据实际情况灵活配置Kernel类型。

●CrossCoreWaitFlag必须与CrossCoreSetFlag接口配合使用，避免计算核一直处于阻塞阶段。

●如果执行CrossCoreWaitFlag时该flagId的计数器的值为0，则CrossCoreWaitFlag之后的所有指令都将被阻塞，直到该flagId的计数器的值不为0。同一个flagId的计数器最多设置15次。

●使用该接口模式0时，建议开启batchmode模式，使算子独占全部所需核资源，否则可能因满足以下条件导致死锁：

–多流并发场景（≥2条执行流）。

–≥2个算子并发执行。

–所有并发算子的核数总和超过物理核数。

–≥2个并发算子使用了核间同步功能。

具体而言，在多流场景下，某条流的核间同步算子虽分配到n个物理核，但可能仅有n-m个核先被调度执行，而其余m个核因被其他流的核间同步算子抢占而尚未启动。先启动的n-m个核执行到核间同步时等待剩余m核完成，而剩余m核因被其他流的核间同步算子占用而无法释放，形成死锁。
