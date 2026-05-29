# GetWorkspaceLen

> **Section**: 6.2.3.12.2.5  
> **PDF Pages**: 1955–1955  

---

<!-- page 1955 -->

调用示例

if (id >= 0 && id < ARRIVE_NUM) {  //各种Vector计算逻辑，用户自行实现  barA.Arrive(id);} else if(id >= ARRIVE_NUM && id < ARRIVE_NUM + WAIT_NUM){  barA.Wait(id - ARRIVE_NUM);  // Wait组的6个AIV中的AIV需要等待Arrive组AIV做完任务  // 各种Vector计算逻辑，用户自行实现}

## 6.2.3.12.2.5 GetWorkspaceLen

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

返回当前GroupBarrier所占用的Global Memory消息空间大小。

函数原型

```cpp
__aicore__ inline uint64_t GetWorkspaceLen()
```

参数说明

无

返回值说明

当前GroupBarrier所占用的Global Memory消息空间大小。

约束说明

无

调用示例

// 6个AIV等3个AIV Arrive后再开始后续业务，总共需要6*512B地址空间，起始地址为用户指定的startAddr。AscendC::GroupBarrier<AscendC::PipeMode::MTE3_MODE> barA(startAddr, 3, 6);uint64_t offset = barA.GetWorkspaceLen(); // 返回barA所占用的GlobalMemory空间。

结果示例如下：
