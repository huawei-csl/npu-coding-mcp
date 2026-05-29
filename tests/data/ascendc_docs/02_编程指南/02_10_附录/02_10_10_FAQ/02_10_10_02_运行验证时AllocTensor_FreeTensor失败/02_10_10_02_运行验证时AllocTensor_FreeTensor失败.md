# 运行验证时AllocTensor/FreeTensor失败

> **Section**: 2.10.10.2  
> **PDF Pages**: 401–401  

---

<!-- page 401 -->

## 2.10.10.2 运行验证时AllocTensor/FreeTensor 失败

现象描述

通过NPU进行核函数的运行验证时，出现挂死现象；通过CPU进行核函数的运行验证时，出现AllocTensor/FreeTensor失败的报错，日志报错和调用栈打印如下：

[ERROR][Core_0][/usr/local/Ascend/cann/x86_64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:730][AllocEventID][321678] current size is 4, max buffer number in same queue position is 4[ERROR][CORE_0][pid 321674] error happened! =========SIGABRT Signal (Abort Signal from abort) catched, backtrace info:[#0] 0x000000000001e7c0: handler(int) at /usr/local/Ascend/cann/tools/tikicpulib/lib/include/kern_fwk.h:105[#1] 0x0000000000017c4f: signed char AscendC::TPipe::AllocEventID<(AscendC::HardEvent)5>() at /usr/local/Ascend/cann/x86_64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:733[#2] 0x000000000001426d: AscendC::TQueBind<(AscendC::TPosition)0, (AscendC::TPosition)9, 4, 0>::FreeBuffer(unsigned char*) at /usr/local/Ascend/cann/x86_64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:1217[#3] 0x0000000000011058: void AscendC::TQueBind<(AscendC::TPosition)0, (AscendC::TPosition)9, 4, 0>::FreeTensor<float16::Fp16T>(AscendC::LocalTensor<float16::Fp16T>&) at /usr/local/Ascend/cann/x86_64-linux/tikcpp/tikcfw/interface/kernel_tpipe.h:1237[#4] 0x000000000000dfde: KernelAdd::Compute(int) at /home/xxxx/xxxx.cpp:59[#5] 0x000000000000dd1c: KernelAdd::Process() at /home/xxxx/xxxx.cpp:37 (discriminator 2)...

问题根因

根据日志信息“current size is 4, max buffer number in same queue position is4”可以明确该问题是因为同一个TPosition上QUE Buffer的数量超出限制导致。

同一个TPosition上的所有Queue，连续调用AllocTensor接口申请的Tensor数量，根据AI处理器型号的不同，有数量约束。申请Buffer时，需要满足该约束。

Atlas 训练系列产品不超过4个。

Atlas 推理系列产品AI Core不超过8个。

Atlas 推理系列产品Vector Core不超过8个。

Atlas A2 训练系列产品/Atlas A2 推理系列产品不超过8个。

Atlas A3 训练系列产品/Atlas A3 推理系列产品不超过8个。

Atlas 200I/500 A2 推理产品不超过8个。

不满足该约束，在后续使用AllocTensor/FreeTensor可能会出现分配资源失败。比如：

AscendC::TQue<AscendC::TPosition::VECIN, 1> que0;AscendC::TQue<AscendC::TPosition::VECIN, 1> que1;AscendC::TQue<AscendC::TPosition::VECIN, 1> que2;AscendC::TQue<AscendC::TPosition::VECIN, 1> que3;AscendC::TQue<AscendC::TPosition::VECIN, 1> que4;AscendC::TQue<AscendC::TPosition::VECIN, 1> que5;// 比如，算子有6个输入，需要申请6块buffer// 通过6个队列为其申请内存，分别为que0~que5，每个que分配1块,申请VECIN TPosition上的buffer总数为6// 假设，同一个Position上连续Alloc的Buffer数量限制为4，超出该限制后，使用AllocTensor/FreeTensor会出现分配资源失败// 在NPU上可能体现为卡死等异常行为，在CPU Debug场景会出现报错提示pipe.InitBuffer(que0, 1, len);pipe.InitBuffer(que1, 1, len);pipe.InitBuffer(que2, 1, len);pipe.InitBuffer(que3, 1, len);pipe.InitBuffer(que4, 1, len);pipe.InitBuffer(que5, 1, len);
