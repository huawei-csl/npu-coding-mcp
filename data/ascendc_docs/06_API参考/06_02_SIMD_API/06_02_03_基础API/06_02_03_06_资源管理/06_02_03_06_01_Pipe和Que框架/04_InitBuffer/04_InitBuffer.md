# InitBuffer

> **Section**: 4  
> **PDF Pages**: 1757–1758  

---

<!-- page 1757 -->

2.输入长度需要小于等于被复用资源池长度；

3.其他泛用约束参考 TBufPool；

返回值说明

无

调用示例

数据量较大且内存有限时，无法一次完成所有数据搬运，需要拆分成多个阶段计算，每次计算使用其中的一部分数据，可以通过TBufPool资源池进行内存地址复用。本例中，从Tpipe划分出资源池tbufPool0，tbufPool0为src0Gm分配空间后，继续分配了资源池tbufPool1，指定tbufPool1与tbufPool2复用并分别运用于第一、二轮计算，此时tbufPool1及tbufPool2共享起始地址及长度。

AscendC::TPipe pipe;AscendC::TBufPool<AscendC::TPosition::VECCALC> tbufPool0, tbufPool1, tbufPool2;// srcQue0、srcQue1、srcQue2为VECIN上的TQue，dstQue0、dstQue1为VECOUT上的TQue// 从Tpipe划分出资源池tbufPool0pipe.InitBufPool(tbufPool0, 131072);// 给srcQue0分配空间tbufPool0.InitBuffer(srcQue0, 1, 65536); // Total src0// 通过tbufPool0给tbufPool1分配空间，并指定tbufPool1与tbufPool2复用同一块空间tbufPool0.InitBufPool(tbufPool1, 65536);tbufPool0.InitBufPool(tbufPool2, 65536, tbufPool1);// 通过tbufPool1给srcQue1、dstQue0分配空间tbufPool1.InitBuffer(srcQue1, 1, 32768);tbufPool1.InitBuffer(dstQue0, 1, 32768);// 切换资源池到tbufPool2，并通过tbufPool2给srcQue2、dstQue1分配空间tbufPool1.Reset();tbufPool2.InitBuffer(srcQue2, 1, 32768);tbufPool2.InitBuffer(dstQue1, 1, 32768);tbufPool2.Reset();tbufPool0.Reset();pipe.Reset();

## ?.4. InitBuffer

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

<!-- page 1758 -->

功能说明

调用TBufPool::InitBuffer接口为TQue/TBuf进行内存分配。

函数原型

```cpp
template <class T> __aicore__ inline bool InitBuffer(T& que, uint8_t num, uint32_t len)template <TPosition pos> __aicore__ inline bool InitBuffer(TBuf<pos>& buf, uint32_t len)
```

参数说明

表6-679模板参数说明

参数名说明

Tque参数的类型。

posBuffer逻辑位置，可以为VECIN、VECOUT、VECCALC、A1、B1、C1。关于TPosition的具体介绍请参考6.2.6.7 TPosition。

表6-680 InitBuffer(T& que, uint8_t num, uint32_t len) 原型定义参数说明

输入/输出

参数名称

含义

que输入需要分配内存的TQue对象

num输入分配内存块的个数

len输入每个内存块的大小，单位为Bytes，非32Bytes对齐会自动向上补齐至32Bytes对齐

表6-681 InitBuffer(TBuf<pos>& buf, uint32_t len)原型定义参数说明

输入/输出

参数名称

含义

buf输入需要分配内存的TBuf对象

len输入为TBuf分配的内存大小，单位为Bytes，非32Bytes对齐会自动向上补齐至32Bytes对齐

约束说明

声明TBufPool时，可以通过bufIDSize指定可分配Buffer的最大数量，默认上限为4，最大为16。TQue或TBuf的物理内存需要和TBufPool一致。

返回值说明

无
