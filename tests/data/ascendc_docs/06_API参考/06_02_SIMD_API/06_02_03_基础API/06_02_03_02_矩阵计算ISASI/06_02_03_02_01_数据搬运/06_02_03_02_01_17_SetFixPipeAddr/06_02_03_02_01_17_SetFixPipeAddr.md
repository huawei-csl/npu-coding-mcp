# SetFixPipeAddr

> **Section**: 6.2.3.2.1.17  
> **PDF Pages**: 1061–1061  

---

<!-- page 1061 -->

返回值说明

无

调用示例

完整示例可参考完整示例。

uint64_t clipReluMaxVal = 0x3c00;SetFixPipeClipRelu(clipReluMaxVal); // 使能Relu的情况下，先进行Relu操作，再进行clip，clipReluMaxVal为通过该接口设置的最大值

## 6.2.3.2.1.17 SetFixPipeAddr

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

**DataCopy（CO1->GM）过程中进行随路量化后，通过调用该接口设置Elementwise操作时LocalTensor的地址。**

函数原型

```cpp
template <typename T>__aicore__ inline void SetFixPipeAddr(const LocalTensor<T>& eleWiseData, uint16_t c0ChStride)
```

参数说明

表6-204参数说明

参数名称输入/输出

含义

eleWiseData

输入L1 Buffer上的源操作数。类型为LocalTensor。

支持的TPosition为A1/B1/C1。起始地址需要保证32字节对齐，仅支持half数据类型。
