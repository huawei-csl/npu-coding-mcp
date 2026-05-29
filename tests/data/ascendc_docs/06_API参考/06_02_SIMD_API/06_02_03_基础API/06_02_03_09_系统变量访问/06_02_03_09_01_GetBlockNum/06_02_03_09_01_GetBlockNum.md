# GetBlockNum

> **Section**: 6.2.3.9.1  
> **PDF Pages**: 1864–1864  

---

<!-- page 1864 -->

功能说明

获取ICACHE的PreLoad的状态。

函数原型

```cpp
__aicore__ inline int64_t GetICachePreloadStatus()
```

参数说明

无

返回值说明

int64_t类型，0表示空闲，1表示忙。

约束说明

无

调用示例

// 获取预取状态，0-空闲，1-忙int64_t cachePreloadStatus = AscendC::GetICachePreloadStatus();

## 6.2.3.9 系统变量访问

## 6.2.3.9.1 GetBlockNum

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

获取当前任务配置的核数，用于代码内部的多核逻辑控制等。
