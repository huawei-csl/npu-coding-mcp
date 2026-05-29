# MetricsProfStop

> **Section**: 6.2.3.11.4.2  
> **PDF Pages**: 1927–1927  

---

<!-- page 1927 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

推荐使用asc_prof_start接口进行性能数据采集信号启动的设置，该接口同时适用于C语言和C++语言编程。

用于设置性能数据采集信号启动，和MetricsProfStop配合使用。使用算子调优（msProf）工具进行算子上板调优时，可在kernel侧代码段前后分别调用MetricsProfStart和MetricsProfStop来指定需要调优的代码段范围。

函数原型

```cpp
__aicore__ inline void MetricsProfStart()
```

参数说明

无

返回值说明

无

约束说明

无

调用示例

```cpp
MetricsProfStart();
```

## 6.2.3.11.4.2 MetricsProfStop

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√
