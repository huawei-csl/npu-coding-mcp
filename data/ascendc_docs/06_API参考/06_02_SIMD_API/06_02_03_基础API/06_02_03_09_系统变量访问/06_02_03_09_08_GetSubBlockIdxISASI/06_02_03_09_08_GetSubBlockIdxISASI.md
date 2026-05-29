# GetSubBlockIdx(ISASI)

> **Section**: 6.2.3.9.8  
> **PDF Pages**: 1871–1871  

---

<!-- page 1871 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

分离模式下，获取一个AI Core上Cube Core（AIC）或者Vector Core（AIV）的数量。

函数原型

```cpp
__aicore__ inline int64_t GetSubBlockNum()
```

参数说明

无

返回值说明

不同Kernel类型下（通过6.2.3.14.12 设置Kernel类型设置），在AIC和AIV上调用该接口的返回值如下：

表6-752返回值列表

**Kernel类型**

**KERNEL_TYPE_AIV_ONLY**

**KERNEL_TYPE_AIC_ONLY**

**KERNEL_TYPE_MIX_AIC_1_2**

**KERNEL_TYPE_MIX_AIC_1_1**

**KERNEL_TYPE_MIX_AIC_1_0**

**KERNEL_TYPE_MIX_AIV_1_0**

AIV1-21-1

AIC-1111-

约束说明

无

调用示例

```cpp
int64_t subBlockNum = AscendC::GetSubBlockNum();
```

## 6.2.3.9.8 GetSubBlockIdx(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√
