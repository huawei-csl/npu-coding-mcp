# EXTERN_IMPL_BUFPOOL宏

> **Section**: 1  
> **PDF Pages**: 1760–1761  

---

<!-- page 1760 -->

## ?.1. EXTERN_IMPL_BUFPOOL 宏

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

开发者可以通过TBufPool类手动管理Unified Buffer、L1 Buffer物理内存。

TBufPool类切分的内存块都是连续的，开发者可能有一些自定义的内存块分配需求，比如不连续内存块、内存块在不同TQue之间共享等，这时就需要开发者自定义一个TBufPool的实现。

为了简化开发者的自定义实现，提供EXTERN_IMPL_BUFPOOL宏来辅助用户自定义TBufPool。使用自定义TBufPool功能时，需要注意：

●自定义TBufPool之前，必须通过TPipe::InitBufPool接口进行TBufPool内存资源池初始化。

●自定义TBufPool需要开发者自行实现对TQue/TBuf内存块的分配、初始化、释放等操作。

EXTERN_IMPL_BUFPOOL宏内部定义的函数Reset、Init、GetBufHandle、SetCurAddr、GetCurAddr、SetCurBufSize、GetCurBufSize接口参见后续章节描述。使用该宏后，即可使用上述接口完成自定义TBufPool功能。

说明

自定义TBufPool相关接口为试验接口，在后续版本中可能会调整或改进，不保证后续兼容性。请开发者在使用过程中关注后续版本更新。

函数原型

// 省略宏定义具体内容#define EXTERN_IMPL_BUFPOOL(EXT_BUFPOOL, POSITION, BUFID_SIZE) ...

<!-- page 1761 -->

参数说明

表6-682 EXTERN_IMPL_BUFPOOL 宏原型定义参数说明

参数名称

含义

输入/输出

EXT_BUFPOOL

自定义TBufPool类名。

输入

POSITION

自定义TBufPool逻辑位置，可以为VECIN、VECOUT、VECCALC、A1、B1、C1。关于TPosition的具体介绍请参考6.2.6.7TPosition。

输入

BUFID_SIZE

自定义TBufPool分配的Buffer块数量，建议不超过16。

输入

约束说明

无

返回值说明

无

调用示例

详细示例请参考自定义TBufPool样例。

如下示例中，为tbufPool0划分65536 * 3大小的内存，然后自定义MyBufPool的InitBuffer函数，实现TQue和Tbuf的内存分配。

```cpp
#include "kernel_operator.h"
class MyBufPool {public:    __aicore__ inline MyBufPool() {        Init();    }
template<class T>     __aicore__ inline bool InitBuffer(T& que, uint8_t num, uint32_t len) {    }
```

template<AscendC::TPosition bufPos>    __aicore__ inline bool InitBuffer(AscendC::TBuf<bufPos>& buf, uint32_t len) {    }    // MyBufPool，自定义TBufPool类名。自定义TBufPool逻辑位置选择VECCALC。    // 自定义TBufPool分配的Buffer块数量为16    EXTERN_IMPL_BUFPOOL(MyBufPool, AscendC::TPosition::VECCALC, 16);};
