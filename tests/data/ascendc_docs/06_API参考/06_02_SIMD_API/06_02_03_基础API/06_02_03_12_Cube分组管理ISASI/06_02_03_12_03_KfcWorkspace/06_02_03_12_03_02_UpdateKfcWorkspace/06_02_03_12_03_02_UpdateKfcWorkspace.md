# UpdateKfcWorkspace

> **Section**: 6.2.3.12.3.2  
> **PDF Pages**: 1957–1957  

---

<!-- page 1957 -->

调用示例

```cpp
AscendC::KfcWorkspace desc(workspaceGM);
```

## 6.2.3.12.3.2 UpdateKfcWorkspace

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

更新用于CubeResGroupHandle消息通信区的内存地址。用户使用CubeResGroupHandle接口时，需要用此接口自主管理空间地址。

函数原型

```cpp
__aicore__ inline void UpdateKfcWorkspace(uint32_t offset)
```

参数说明

表6-804接口参数说明

参数输入/输出说明

offset输入更新workspace地址为原地址偏移offset后的地址。

返回值说明

无。

约束说明

本接口不能和CreateCubeResGroup接口同时使用。

调用示例

```cpp
AscendC::KfcWorkspace desc(workspaceGM);desc.UpdateKfcWorkspace(1024);
```
