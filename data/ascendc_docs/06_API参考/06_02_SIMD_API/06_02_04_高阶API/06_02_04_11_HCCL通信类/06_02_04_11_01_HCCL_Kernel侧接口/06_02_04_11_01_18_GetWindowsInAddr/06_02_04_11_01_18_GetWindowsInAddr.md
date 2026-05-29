# GetWindowsInAddr

> **Section**: 6.2.4.11.1.18  
> **PDF Pages**: 2959–2959  

---

<!-- page 2959 -->

## 6.2.4.11.1.18 GetWindowsInAddr

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取卡间通信数据WindowsIn起始地址，可用来直接作为计算的输入输出地址，减少拷贝。该接口默认在所有核上工作，用户也可以在调用前通过GetBlockIdx指定其在某一个核上运行。

函数原型

```cpp
__aicore__ inline GM_ADDR GetWindowsInAddr(uint32_t rankId)
```

参数说明

表6-1362接口参数说明

参数名输入/输出

描述

rankId输入待查询的卡的Id。

返回值说明

返回对应卡的卡间通信数据WindowsIn起始地址。当rankId非法时，返回nullptr。

约束说明

无

调用示例

REGISTER_TILING_DEFAULT(ReduceScatterCustomTilingData); //ReduceScatterCustomTilingData为对应算子头文件定义的结构体GET_TILING_DATA_WITH_STRUCT(ReduceScatterCustomTilingData, tilingData, tilingGM);Hccl hccl;
