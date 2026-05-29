# SetCmpMask(ISASI)

> **Section**: 6.2.3.3.4.6  
> **PDF Pages**: 1324–1325  

---

<!-- page 1324 -->

调用示例

**Compare（结果存入寄存器）指令的结果使用uint8_t类型数据存储，因此dstLocal使用uint8_t类型。**

AscendC::LocalTensor<float> src0Local;AscendC::LocalTensor<float> src1Local;AscendC::LocalTensor<uint8_t> dstLocal;uint64_t mask = 256 / sizeof(float); // 256为每个迭代处理的字节数，结果为64AscendC::BinaryRepeatParams repeatParams = { 1, 1, 1, 8, 8, 8 };AscendC::Compare(src0Local, src1Local, AscendC::CMPMODE::LT, mask, repeatParams);AscendC::GetCmpMask(dstLocal); // mask为0x40, 比较数据类型为float，则每次迭代的32B里只有第7个float数字参与compare

输出示例：src0Local:   [1, 2, 3, 4, 5, 6, 7, 8, 9, ...256]src1Local:   [2, 3, 4, 5, 6, 7, 8, 9, ...257]mask后参与比较的数src0Local:   [1, 8, 16, ...256]src1Local:   [2, 10, 18, ...257]GetCmpMask结果：[256, 256, 256, 256, 256, 256, 256, 256]

## 6.2.3.3.4.6 SetCmpMask(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

为Select不传入mask参数的接口设置比较寄存器。配合不同的selMode传入不同的数据。

●模式0（SELMODE::VSEL_CMPMASK_SPR）

SetCmpMask中传入selMask LocalTensor。

●模式1（SELMODE::VSEL_TENSOR_SCALAR_MODE）

SetCmpMask中传入src1 LocalTensor。

●模式2（SELMODE::VSEL_TENSOR_TENSOR_MODE）

SetCmpMask中传入LocalTensor，LocalTensor中存放的是selMask的地址。

<!-- page 1325 -->

函数原型

```cpp
template <typename T>__aicore__ inline void SetCmpMask(const LocalTensor<T>& src)
```

参数说明

表6-359模板参数说明

参数名

描述

T操作数的数据类型。

表6-360参数说明

输入/输出

参数名

描述

src输入类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要16字节对齐。

返回值说明

无

约束说明

无

调用示例

●当selMode为模式0或模式2时：uint32_t dataSize = 256;uint32_t selDataSize = 8;TPipe pipe;TQue<TPosition::VECIN, 1> inQueueX;TQue<TPosition::VECIN, 1> inQueueY;TQue<TPosition::VECIN, 1> inQueueSel;TQue<TPosition::VECOUT, 1> outQueue;pipe.InitBuffer(inQueueX, 1, dataSize * sizeof(float));pipe.InitBuffer(inQueueY, 1, dataSize * sizeof(float));pipe.InitBuffer(inQueueSel, 1, selDataSize * sizeof(uint8_t));pipe.InitBuffer(outQueue, 1, dataSize * sizeof(float));AscendC::LocalTensor<float> dst = outQueue.AllocTensor<float>();AscendC::LocalTensor<uint8_t> sel = inQueueSel.AllocTensor<uint8_t>();AscendC::LocalTensor<float> src0 = inQueueX.AllocTensor<float>();AscendC::LocalTensor<float> src1 = inQueueY.AllocTensor<float>();uint8_t repeat = 4;uint32_t mask = 64;AscendC::BinaryRepeatParams repeatParams = { 1, 1, 1, 8, 8, 8 };

// selMode为模式0（SELMODE::VSEL_CMPMASK_SPR）AscendC::SetCmpMask(sel);AscendC::PipeBarrier<PIPE_V>();
