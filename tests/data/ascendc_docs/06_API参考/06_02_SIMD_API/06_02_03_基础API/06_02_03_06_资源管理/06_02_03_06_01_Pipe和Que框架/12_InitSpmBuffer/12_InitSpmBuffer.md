# InitSpmBuffer

> **Section**: 12  
> **PDF Pages**: 1747–1747  

---

<!-- page 1747 -->

// 计算串行，不存在数据踩踏，实现了内存复用及自动同步的能力tbufPool1.InitBuffer(queSrc0, 1, BUF_SIZE);tbufPool1.InitBuffer(queSrc1, 1, BUF_SIZE);tbufPool1.InitBuffer(queDst0, 1, BUF_SIZE);CopyIn();Compute(); CopyOut();tbufPool1.Reset();tbufPool2.InitBuffer(queSrc2, 1, BUF_SIZE);tbufPool2.InitBuffer(queSrc3, 1, BUF_SIZE);tbufPool2.InitBuffer(queDst1, 1, BUF_SIZE);CopyIn1();Compute1();CopyOut1();tbufPool2.Reset();

## ?.12. InitSpmBuffer

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

初始化SPM Buffer。

函数原型

●暂存到workspace初始化，需要指定GM地址为SPM Buffer：template <typename T>__aicore__ inline void InitSpmBuffer(const GlobalTensor<T>& workspace, const int32_t bufferSize)

●暂存到L1 Buffer初始化，不需要指定地址，会默认暂存到L1 Buffer，只需要传入需要的SPM Buffer大小：__aicore__ inline void InitSpmBuffer(const int32_t  bufferSize)

Atlas A2 训练系列产品/Atlas A2 推理系列产品，不支持暂存到L1 Buffer初始化接口。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，不支持暂存到L1 Buffer初始化接口。
