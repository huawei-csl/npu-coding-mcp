# SetKernelMode

> **Section**: 6.2.3.11.3.5  
> **PDF Pages**: 1925–1925  

---

<!-- page 1925 -->

产品是否支持

Atlas 训练系列产品√

功能说明

进行核函数的CPU侧运行验证时，用于释放通过 GmAlloc申请的共享内存。

函数原型

```cpp
void GmFree(void *ptr)
```

参数说明

参数名输入/输出

描述

ptr输入需要释放的共享内存的指针。

返回值说明

无

约束说明

传入的指针必须是之前通过GmAlloc申请过的共享内存的指针。

调用示例

```cpp
AscendC::GmFree((void*)x);
```

## 6.2.3.11.3.5 SetKernelMode

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√
