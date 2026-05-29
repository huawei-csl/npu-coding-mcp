# HelloWorld

> **Section**: 1.3.2.1  
> **PDF Pages**: 59–59  

---

<!-- page 59 -->

## 1.3.1 简介

AI Core是AI处理器的计算核心，一块AI处理器通常集成多个AI Core以实现并行计算。相比传统CPU，AI处理器更适用于模型训练与推理，这得益于其内部集成的大量计算单元以及丰富的向量计算指令——单个硬件指令即可完成对多组数据的并行操作。

AI处理器上主要支持以下两种编程模型：

●SIMT（Single Instruction Multiple Thread，单指令多线程）：以单条指令驱动多个线程的形式实现并行计算。

●SIMD（Single Instruction Multiple Data，单指令多数据）：以单条指令操作多个数据的形式实现并行计算。

其中，SIMT编程适用于离散访存、复杂分支控制等场景下的矢量算子开发，也便于熟悉业界SIMT算子开发的开发者快速上手Ascend C算子开发。

SIMD编程则适用于纯矩阵计算、连续访存的矢量算子或融合算子场景。

此外，我们还提供SIMD与SIMT混合编程方式，融合两种模型的优势，在性能与易用性之间取得更好的平衡。

## 1.3.2 基于SIMD 编程

## 1.3.2.1 HelloWorld

本示例展示了如何使用Ascend C编写一个简单的"Hello World"程序，包括核函数（设备侧实现的入口函数）的实现、调用流程以及编译运行的完整步骤。通过本示例，您可以快速了解Ascend C的基本开发流程。完整样例请参考LINK。

代码文件hello_world.asc包括核函数实现和主函数实现。

●核函数实现：该核函数的核心逻辑是输出"Hello World!!!"字符串。

●主函数实现：在主函数中，进行初始化环境、申请资源、通过<<<>>>调用核函数以及释放资源等操作。完整的代码流程和逻辑可以通过代码注释查看。

// Host侧应用程序需要包含的头文件#include "acl/acl.h"// Kernel侧需要包含的头文件#include "kernel_operator.h"__global__ __vector__ void hello_world(){    AscendC::printf("[Block (%lu/%lu)]: Hello World!!!\n", AscendC::GetBlockIdx(), AscendC::GetBlockNum());}

int32_t main(int argc, char const *argv[]){    // 初始化    aclInit(nullptr);    // 运行管理资源申请    int32_t deviceId = 0;    aclrtSetDevice(deviceId);    aclrtStream stream = nullptr;    aclrtCreateStream(&stream);

// 设置参与计算的核数为8（核数可根据实际需求设置）    constexpr uint32_t numBlocks = 8;    // 用内核调用符<<<>>>调用核函数    hello_world<<<numBlocks, nullptr, stream>>>();    aclrtSynchronizeStream(stream);    // 资源释放和去初始化
