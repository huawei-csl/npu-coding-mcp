# GetKfcWorkspace

> **Section**: 6.2.3.12.3.3  
> **PDF Pages**: 1958–1958  

---

<!-- page 1958 -->

## 6.2.3.12.3.3 GetKfcWorkspace

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

获取用于CubeResGroupHandle消息通信区的内存地址。用户使用CubeResGroupHandle接口时，需要用此接口自主管理空间地址。

函数原型

```cpp
__aicore__ inline GM_ADDR GetKfcWorkspace()
```

参数说明

无

返回值说明

workspace地址。

约束说明

本接口不能和CreateCubeResGroup接口同时使用。

调用示例

```cpp
AscendC::KfcWorkspace desc(workspaceGM);GM_ADDR workspace = desc.GetKfcWorkspace();
```

## 6.2.3.13 工具函数

## 6.2.3.13.1 NumericLimits

## 6.2.3.13.1.1 简介

NumericLimits工具类，用于查询指定数据类型的最大值/最小值等属性。
