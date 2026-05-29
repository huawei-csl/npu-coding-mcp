# InitDetermineComputeWorkspace

> **Section**: 6.2.3.7.2.6  
> **PDF Pages**: 1849–1849  

---

<!-- page 1849 -->

Kernel直调场景下通过__schedmode__(mode)限定符来设置batchmode模式；工程化算子开发场景下，通过TilingContext的SetScheduleMode接口来设置batchmode模式，具体请参考《基础数据结构和接口》。

调用示例

请参考调用示例。

## 6.2.3.7.2.6 InitDetermineComputeWorkspace

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

初始化GM共享内存的值，完成初始化后才可以调用 WaitPreBlock和NotifyNextBlock。

函数原型

```cpp
__aicore__ inline void InitDetermineComputeWorkspace(GlobalTensor<int32_t>& gmWorkspace, LocalTensor<int32_t>& ubWorkspace)
```

参数说明

表6-744接口参数说明

参数名称输入/输出

含义

gmWorkspace

输入临时空间，初始化核间同步的共享内存，类型为GlobalTensor。

ubWorkspace

输入临时空间，用于操作gmWorkspace，类型为LocalTensor。
