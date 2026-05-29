# DataCachePreload

> **Section**: 6.2.3.8.1  
> **PDF Pages**: 1857–1857  

---

<!-- page 1857 -->

函数原型

```cpp
__aicore__ inline void WaitPreTaskEnd()
```

参数说明

无

返回值说明

无

约束说明

●该接口适用于TorchAir图模式开发场景，且需在启用SuperKernel特性后方可生效。相关信息可参考《PyTorch图模式使用指南(TorchAir)》中的“GE图模式 >GE图模式功能 > 图内标定SuperKernel范围”章节。

●在算子运行过程中，需要保证此接口在每个核上都被调用，且每个核上仅被调用一次。

●若子Kernel某个TilingKey分支调用了此接口，则开发者需要保证当前算子可能会运行的所有TilingKey均调用了此接口，否则会出现因同步指令数量不匹配而卡住的现象。

调用示例

```cpp
#include "kernel_operator.h"
```

AscendC::LocalTensor<half> src0Local = inQueueSrc0.AllocTensor<half>();// 算子第一条搬运指令前插入，且保证只调用一次AscendC::WaitPreTaskEnd();AscendC::DataCopy(src0Local, src0Global, 512);inQueueSrc0.EnQue(src0Local);;

## 6.2.3.8 缓存控制

## 6.2.3.8.1 DataCachePreload

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
