# GetHcclContext

> **Section**: 6.2.4.11.3.3  
> **PDF Pages**: 2995–2995  

---

<!-- page 2995 -->

功能说明

设置通算融合算子每个通信域对应的context（消息区）地址。

函数原型

```cpp
template <uint32_t index>__aicore__ inline void SetHcclContext(__gm__ uint8_t* context)
```

参数说明

表6-1390参数说明

参数名描述

index模板参数，用来表示要设置的通信域ID，当前只支持2个通信域，index只能为0/1。

context对应通信域的context（消息区）地址。

返回值说明

无

约束说明

当前最多只支持2个通信域。

调用示例

// 给GROUP_0设置消息区地址AscendC::SetHcclContext<0>(contextGM);

## 6.2.4.11.3.3 GetHcclContext

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x
