# Cast（float转bfloat16_t）

> **Section**: 6.2.3.5.6  
> **PDF Pages**: 1727–1727  

---

<!-- page 1727 -->

约束说明

无

调用示例

float valueIn = 2.5;// 输出数据valueOut：3， 2.5向上取整为3int32_t valueOut = AscendC::Cast<float, int32_t, AscendC::RoundMode::CAST_ROUND>(valueIn);

## 6.2.3.5.6 Cast（float 转bfloat16_t）

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

float类型标量数据转换成bfloat16_t类型标量数据。

函数原型

```cpp
__aicore__ inline bfloat16_t Cast(const float& fVal)
```

参数说明

表6-652接口参数说明

参数名称输入/输出

含义

fVal输入float类型标量数据。

返回值说明

转换后的bfloat16_t类型标量数据。
