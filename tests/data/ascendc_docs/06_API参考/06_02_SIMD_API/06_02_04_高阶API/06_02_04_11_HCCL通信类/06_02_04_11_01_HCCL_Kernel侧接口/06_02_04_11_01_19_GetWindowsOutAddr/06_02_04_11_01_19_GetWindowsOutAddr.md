# GetWindowsOutAddr

> **Section**: 6.2.4.11.1.19  
> **PDF Pages**: 2960–2960  

---

<!-- page 2960 -->

GM_ADDR contextGM = AscendC::GetHcclContext<0>();  // AscendC自定义算子kernel中，通过此方式获取HCCL contexthccl.InitV2(contextGM, &tilingData);

auto winInAddr = hccl.GetWindowsInAddr(0);auto winOutAddr = hccl.GetWindowsOutAddr(0);auto rankId = hccl.GetRankId();auto rankDim = hccl.GetRankDim();  // 4张卡

## 6.2.4.11.1.19 GetWindowsOutAddr

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

获取卡间通信数据WindowsOut起始地址，可用来直接作为计算的输入输出地址，减少拷贝。该接口默认在所有核上工作，用户也可以在调用前通过GetBlockIdx指定其在某一个核上运行。

函数原型

```cpp
__aicore__ inline GM_ADDR GetWindowsOutAddr(uint32_t rankId)
```

参数说明

表6-1363接口参数说明

参数名输入/输出

描述

rankId输入待查询的卡的Id。

返回值说明

返回对应卡的卡间通信数据WindowsOut起始地址。当rankId非法时，返回nullptr。
