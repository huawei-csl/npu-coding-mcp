# GetUBSizeInBytes

> **Section**: 6.2.3.13.4  
> **PDF Pages**: 1972–1972  

---

<!-- page 1972 -->

表6-815返回值列表

**KERNEL_TYPE_AIV_ONLY**

**KERNEL_TYPE_AIC_ONLY**

**KERNEL_TYPE_MIX_AIC_1_2**

**KERNEL_TYPE_MIX_AIC_1_1**

**KERNEL_TYPE_MIX_AIC_1_0**

**KERNEL_TYPE_MIX_AIV_1_0**

**Kernel类型**

AIV1-21-1

AIC-1111-

●针对耦合模式，固定返回1。

约束说明

无

调用示例

uint64_t ratio = AscendC::GetTaskRatio(); // 返回AIC和AIV的数量比例AscendC::PRINTF("task ratio is %u", ratio);

## 6.2.3.13.4 GetUBSizeInBytes

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取UB空间的大小，单位为byte。开发者根据UB的大小来计算循环次数等参数值。

函数原型

```cpp
__aicore__ inline constexpr uint32_t GetUBSizeInBytes()
```

参数说明

无
