# SetReduceType

> **Section**: 6.2.4.11.2.8  
> **PDF Pages**: 2978–2979  

---

<!-- page 2978 -->

参数说明

表6-1377参数说明

参数名输入/输出

描述

algConfig输入通信算法配置。string类型，支持的最大长度为128字节。

针对Atlas 350 加速卡，该参数为预留字段，配置后不生效，默认仅支持FullMesh算法。FullMesh算法即NPU之间的全连接，任意两个NPU之间可以直接进行数据收发。详细的算法内容可参见《HCCL集合通信库》中的相关参考 > 集合通信算法介绍。

针对Atlas A3 训练系列产品/Atlas A3 推理系列产品，当前支持的取值为：

●"AllReduce=level0:doublering"：AllReduce通信任务。

●"AllGather=level0:doublering"：AllGather通信任务。

●"ReduceScatter=level0:doublering"：ReduceScatter通信任务。

●"AlltoAll=level0:fullmesh;level1:pairwise"：AlltoAllV和AlltoAll通信任务。

●"BatchWrite=level0:fullmesh"：BatchWrite通信任务。

针对Atlas A2 训练系列产品/Atlas A2 推理系列产品，该参数为预留字段，配置后不生效，默认仅支持FullMesh算法。FullMesh算法即NPU之间的全连接，任意两个NPU之间可以直接进行数据收发。详细的算法内容可参见《HCCL集合通信库》中的相关参考 > 集合通信算法介绍。

返回值说明

●0表示设置成功。

●非0表示设置失败。

约束说明

无

调用示例

本接口的调用示例请见调用示例。

## 6.2.4.11.2.8 SetReduceType

功能说明

设置Reduce操作类型，仅对有归约操作的通信任务生效。

<!-- page 2979 -->

函数原型

```cpp
uint32_t SetReduceType(uint32_t reduceType, uint8_t dstDataType = 0, uint8_t srcDataType = 0)
```

参数说明

表6-1378参数说明

参数名输入/输出

描述

reduceType

输入归约操作类型，仅对有归约操作的通信任务生效。uint32_t类型，取值详见表6-1338参数说明。

dstDataType

输入通信任务中输出数据的数据类型。uint8_t类型，该参数的取值范围请参考表6-1337。

Atlas 350 加速卡，不同通信任务支持的输出数据类型不同，具体为：

●对于AllReduce、AllGather、AllToAll、AllToAllV、AllToAllVWrite通信任务：输出的数据类型必须与输入的数据类型一致。各通信任务支持的输入数据类型请参考srcDataType。

●对于ReduceScatter通信任务，当输入的数据类型为int16_t、int32_t、half、float、bfloat16_t时，输出的数据类型必须与其一致；当输入的数据类型为int8_t、hifloat8_t、fp8_e5m2_t、fp8_e4m3fn_t时，输出的数据类型必须为half、bfloat16_t、float三者之一。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，该参数暂不支持，配置后不生效。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，该参数暂不支持，配置后不生效。

srcDataType

输入通信任务中输入数据的数据类型。uint8_t类型，该参数的取值范围请参考表6-1337。

Atlas 350 加速卡，不同通信任务支持的输入数据类型如下：

●AllReduce通信任务：支持的输入类型为int16_t、half、bfloat16_t、int32_t、float。

●AllGather、AllToAll、AllToAllV、AllToAllVWrite通信任务：支持的输入类型为int8_t、uint8_t、hifloat8_t、fp8_e5m2_t、fp8_e4m3fn_t、int16_t、uint16_t、half、bfloat16_t、int32_t、uint32_t、float、int64_t、double。

●ReduceScatter通信任务：支持的输入类型为int8_t、hifloat8_t、fp8_e5m2_t、fp8_e4m3fn_t、int16_t、half、bfloat16_t、int32_t、float。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，该参数暂不支持，配置后不生效。

针对Atlas A2 训练系列产品/Atlas A2 推理系列产品，该参数暂不支持，配置后不生效。
