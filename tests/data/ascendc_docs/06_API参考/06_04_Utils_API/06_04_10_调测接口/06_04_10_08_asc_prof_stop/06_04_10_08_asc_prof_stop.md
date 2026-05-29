# asc_prof_stop

> **Section**: 6.4.10.8  
> **PDF Pages**: 3892–3892  

---

<!-- page 3892 -->

返回值说明

无

约束说明

无

调用示例

```cpp
asc_prof_start();
```

## 6.4.10.8 asc_prof_stop

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

设置性能数据采集信号停止，和asc_prof_start配合使用。使用msProf工具进行算子上板调优时，可在kernel侧代码段前后分别调用asc_prof_start和asc_prof_stop来指定需要调优的代码段范围。

函数原型

```cpp
__aicore__ inline void asc_prof_stop()
```

参数说明

无

返回值说明

无

约束说明

无
