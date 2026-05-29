# asc_time_stamp

> **Section**: 6.4.10.6  
> **PDF Pages**: 3889–3890  

---

<!-- page 3889 -->

产品是否支持

Atlas 训练系列产品x

功能说明

本接口在SIMD与SIMT混合调试场景中提供Clock时间戳功能，用于记录从程序启动到接口调用时刻所经历的时钟周期数（Cycle Count），便于精确分析执行延迟和性能瓶颈。

函数原型

```cpp
__simt_callee__ inline uint64_t clock(void)
```

参数说明

无

返回值说明

从程序开始到调用时所经历的时钟周期数。

约束说明

无

需要包含的头文件

使用该接口需要包含"utils/debug/asc_time.h"头文件。

```cpp
#include "utils/debug/asc_time.h"
```

调用示例

```cpp
__simt_vf__ __launch_bounds__(1024) inline void SimtKernel(__gm__ uint64_t* dst){    int idx = threadIdx.x + blockIdx.x * blockDim.x;
     dst[idx] = clock();}
```

## 6.4.10.6 asc_time_stamp

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

<!-- page 3890 -->

产品是否支持

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

提供时间戳打点功能，用于在算子Kernel代码中标记关键执行点。调用后会打印如下信息：

●descId:用户自定义标识符，用于区分不同打点位置；

●rsv ：保留值，默认为0，无需关注；

●timeStamp :当前系统cycle数，用于计算时间差，时间换算规则可参考6.2.3.9.9GetSystemCycle(ISASI)；

●pcPtr：pc指针数值，若无特殊需求，用户无需关注。

●entry：算子开始执行的cycle数，若无特殊需求，用户无需关注。

打印示例如下：

```cpp
descId is 11, rsv is 0, timeStamp is 815603975350485, pcPtr is 19792358553124, entry is 815603975328116.
```

注意

该功能主要用于调试和性能分析，开启后会对算子性能产生一定影响，生产环境建议关闭。

默认情况下，该功能关闭，开发者可以按需通过增加-DASCENDC_TIME_STAMP_ON编译选项的方式，开启打点功能。

函数原型

```cpp
__aicore__ inline void asc_time_stamp(uint32_t desc_id)
```

参数说明

参数名输入/输出

描述

desc_id输入用户自定义标识符（自定义数字），用于区分不同打点位置。

注意

[0, 0xffff]是预留给Ascend C内部各个模块使用的id值，用户自定义的desc_id建议使用大于0xffff的数值。

返回值说明

无
