# asc_mark_stamp

> **Section**: 6.4.10.9  
> **PDF Pages**: 3893–3893  

---

<!-- page 3893 -->

调用示例

```cpp
asc_prof_stop();
```

## 6.4.10.9 asc_mark_stamp

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

用户通过调用接口，用于在算子执行过程中标记特定位置，便于后期通过流水图分析代码执行路径与性能热点。

函数原型

```cpp
template<pipe_t pipe = PIPE_S>__aicore__ inline void asc_mark_stamp(uint16_t idx)
template<pipe_t pipe = PIPE_S, uint16_t idx>__aicore__ inline void asc_mark_stamp()
```

参数说明

参数名含义

pipe指定打点所在的pipeline类型。

index用户设置的打点的唯一标识id。

返回值说明

无

约束说明

●index取值范围为[0,4095]。为方便从打点图中找到对应的代码，建议不要重复使用相同的index。
