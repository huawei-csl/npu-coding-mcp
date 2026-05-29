# SIMD语言扩展层C API

> **Section**: 2.4.3  
> **PDF Pages**: 169–169  

---

<!-- page 169 -->

// 调用add_custom<<<block_num, thread_num_per_block, dyn_ubuf_size, stream>>>(x, y, z, 1024);

在执行函数之前，会先对上述配置参数进行校验。如果grid_dim或block_dim超出设备的最大允许规模，或dynamic_smem_bytes超过分配静态内存后剩余的可用共享内存，该函数将会执行失败。

在多线程并发执行时，每个线程使用较少的寄存器可以让更多的线程和线程块驻留在AI处理器上，从而提升性能。因此，编译器会采用启发式算法，将寄存器溢出（register spilling）和指令数量控制在最低水平，同时尽量减少寄存器的使用量。应用程序可以通过在__global__函数定义中使用__launch_bounds__()限定符来限制启动边界（launch bounds），提供附加信息辅助编译器优化这一过程，这属于可选配置。

●__launch_bounds__(N)是函数标记宏，在SIMT VF入口函数上可选配置，用于在编译期指定SIMT VF启动的最大线程数。若未配置__launch_bounds__，最大线程数默认为1024。参数N需要满足：

–N >= dimx * dimy * dimz；dimx，dimy，dimz为表示线程的dim3结构体。

–N的取值范围为1到2048。

最大线程数决定了每个线程可分配的寄存器数量，具体对应关系请见下表，寄存器用于存储线程中的局部变量，若局部变量的个数超出寄存器个数，容易出现栈溢出等问题。建议最大线程数与启动VF任务的dim3线程数保持一致。

表2-23 __launch_bounds__的Thread 数量与每个Thread 可用寄存器数

**Thread的个数(个)每个Thread可用寄存器个数(个)**

1025~204816

513~102432

257~51264

1~256127

配置SIMT函数最大线程数为512，示例如下：

```cpp
__simt_vf__ __launch_bounds__(512) inline void add(__gm__ uint8_t* x, __gm__ uint8_t* y, __gm__ uint8_t* z)
```

## 2.4.3 SIMD 语言扩展层C API

C API开放芯片完备编程能力，支持以数组形式分配内存，一般基于指针编程。提供与业界一致的C语言编程体验。

包含asc_simd.h文件来调用C API相应接口。如无特殊说明，包含该头文件即可满足接口调用需求。若API文档中有特殊说明，则应遵循API的具体说明。

```cpp
#include "c_api/asc_simd.h"
```

对于C API，主要分为以下几类：

●矢量计算，实现调用Vector计算单元执行计算的功能。

●数据搬运，计算API基于Local Memory数据进行计算，所以数据需要先从GlobalMemory搬运至Local Memory，再使用计算API完成计算，最后从Local Memory搬出至Global Memory。执行搬运过程的接口称之为数据搬运API。
