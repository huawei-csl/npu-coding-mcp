# InterHcclGroupSync

> **Section**: 6.2.4.11.1.16  
> **PDF Pages**: 2955–2956  

---

<!-- page 2955 -->

参数说明

表6-1361接口参数说明

参数名输入/输出

描述

handleId输入对应通信任务的标识ID，只能使用Prepare原语接口的返回值。using HcclHandle = int8_t;

返回值说明

●返回handleId对应的通信任务已执行的次数，最大值为repeat。

●当执行异常时，返回-1。

约束说明

●调用本接口前确保已调用过InitV2和SetCcTilingV2接口。

●入参handleId只能使用Prepare原语对应接口的返回值。

●本接口在AIC核或者AIV核上调用必须与对应的Prepare接口的调用核保持一致。

调用示例

REGISTER_TILING_DEFAULT(ReduceScatterCustomTilingData); //ReduceScatterCustomTilingData为对应算子头文件定义的结构体GET_TILING_DATA_WITH_STRUCT(ReduceScatterCustomTilingData, tilingData, tilingGM);Hccl hccl;GM_ADDR contextGM = AscendC::GetHcclContext<0>();  // AscendC自定义算子kernel中，通过此方式获取HCCL contexthccl.InitV2(contextGM, &tilingData);auto ret = hccl.SetCcTiling(offsetof(ReduceScatterCustomTilingData, mc2CcTiling));if (ret != HCCL_SUCCESS) {  return;}if (AscendC::g_coreType == AIC) {    auto repeat = 10;    HcclHandle handleId = hccl.ReduceScatter(sendBuf, recvBuf, 100, HcclDataType::HCCL_DATA_TYPE_INT8, HcclReduceOp::HCCL_REDUCE_SUM, repeat);    hccl.Commit(handleId ); // 通知服务端可以执行上述的ReduceScatter任务    int32_t finishedCount = hccl.Query(handleId);    while (hccl.Query(handleId) < repeat) {} // 等待查询到handleId对应的通信任务执行repeat次    hccl.Finalize(); // 后续无其他通信任务，通知服务端执行上述ReduceScatter任务之后即可以退出}

## 6.2.4.11.1.16 InterHcclGroupSync

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 2956 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

用于等待一个跨通信域的通信任务完成。调用该接口后，本通信域后续下发的通信任务，均等待指定的srcGroupID通信域中的srcHandleID通信任务执行完成，才开始执行。

函数原型

```cpp
__aicore__ inline void InterHcclGroupSync(int8_t srcGroupID, HcclHandle srcHandleID)
```

参数说明

参数名输入/输出

描述

srcGroupID输入通信域编号，即后续通信任务所等待的通信任务所在的通信域编号。

srcHandleID输入通信任务，即后续通信任务所等待的通信任务的标识HcclHandle。

返回值说明

无

约束说明

●调用本接口前确保已调用过InitV2和SetCcTilingV2接口。

●本接口在AIC核或者AIV核上调用必须与对应的Prepare接口的调用核保持一致。

●一个通信域内，所有Prepare接口和InterHcclGroupSync接口的总调用次数不能超过63。

调用示例

本示例构造一个通信融合算子，该算子有1个输入xGM，2个输出alltoallGM和allgatherGM。算子内有2个通信域，首先通信域0对输入进行AlltoAll通信，将结果输出至alltoallGM。当结果数据输出到alltoallGM完成后，通信域1将该结果alltoallGM作为AllGather通信的输入，并将通信结果输出至allgatherGM。extern "C" __global__ __aicore__ void alltoall_allgather_custom(GM_ADDR xGM, GM_ADDR alltoallGM, GM_ADDR allgatherGM) {    REGISTER_TILING_DEFAULT(AlltoAllAllGatherCustomTilingData); //AlltoAllAllGatherCustomTilingData为对
