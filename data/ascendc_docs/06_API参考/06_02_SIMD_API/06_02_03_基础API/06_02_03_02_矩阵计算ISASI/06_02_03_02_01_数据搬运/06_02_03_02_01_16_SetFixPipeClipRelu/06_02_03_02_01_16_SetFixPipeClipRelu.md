# SetFixPipeClipRelu

> **Section**: 6.2.3.2.1.16  
> **PDF Pages**: 1060–1060  

---

<!-- page 1060 -->

uint64_t deqScalar = static_cast<uint64_t>(*reinterpret_cast<int32_t*>(&tmp)); AscendC::SetFixpipePreQuantFlag(deqScalar);  // 设置量化参数AscendC::PipeBarrier<PIPE_FIX>();

## 6.2.3.2.1.16 SetFixPipeClipRelu

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

**DataCopy（CO1->GM）过程中进行随路量化后，通过调用该接口设置ClipRelu操作的最大值。**

ClipRelu计算公式为min(clipReluMaxVal，srcData)，clipReluMaxVal为通过该接口设置的最大值，srcData为源数据。

函数原型

```cpp
__aicore__ inline void SetFixPipeClipRelu(uint64_t config)
```

参数说明

表6-203参数说明

参数名称输入/输出

含义

config输入clipReluMaxVal，ClipRelu操作中的最大值。clipReluMaxVal只占用0-15bit，必须大于0，不能为INF/NAN。

约束说明

使能Relu的情况下，先进行Relu操作，之后再进行ClipRelu。
