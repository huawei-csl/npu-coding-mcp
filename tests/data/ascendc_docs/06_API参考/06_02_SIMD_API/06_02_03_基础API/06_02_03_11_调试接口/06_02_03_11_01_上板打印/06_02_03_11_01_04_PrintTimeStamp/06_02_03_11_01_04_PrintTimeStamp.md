# PrintTimeStamp

> **Section**: 6.2.3.11.1.4  
> **PDF Pages**: 1909–1910  

---

<!-- page 1909 -->

–position：表示Tensor所在的物理存储位置，当前仅支持Unified Buffer/L1Buffer/L0C Buffer/Global Memory。

–dump_size：表示用户需要dump的元素个数。

DumpAccChkPoint打印结果的最前面会自动打印CANN_VERSION_STR值与CANN_TIMESTAMP值。其中，CANN_VERSION_STR与CANN_TIMESTAMP为宏定义，CANN_VERSION_STR代表CANN软件包的版本号信息，形式为字符串，CANN_TIMESTAMP为CANN软件包发布时的时间戳，形式为数值（uint64_t）。开发者也可在代码中直接使用这两个宏。

打印结果的样例如下：

```cpp
opType=AddCustom, DumpHead: AIV-0, CoreType=AIV, block dim=8, total_block_num=8, block_remain_len=1046912, block_initial_space=1048576, rsv=0, magic=5aa5bccd CANN Version: XX.XX,TimeStamp: XXXXXXDumpTensor: desc=5, addr=40, data_type=float16, position=UB, dump_size=32[16.000000, 22.000000, 2.000000, 3.000000, 58.000000, 62.000000, 33.000000, 74.000000, 51.000000, 69.000000, 61.000000, 9.000000, 53.000000, 35.000000, 14.000000, 43.000000, 20.000000, 43.000000, 92.000000, 84.000000, 9.000000, 6.000000, 78.000000, 53.000000, 52.000000, 33.000000, 51.000000, 61.000000, 92.000000, 45.000000, 39.000000,34.000000]...DumpTensor: desc=5, addr=140, data_type=float16, position=UB, dump_size=32[41.000000, 91.000000, 12.000000, 32.000000, 28.000000, 49.000000, 2.000000, 75.000000, 11.000000, 32.000000, 17.000000, 31.000000, 70.000000, 38.000000, 76.000000, 87.000000, 61.000000, 8.000000, 55.000000, 70.000000, 17.000000, 37.000000, 35.000000, 58.000000, 94.000000, 31.000000, 50.000000, 29.000000, 13.000000, 37.000000, 79.000000,29.000000]
```

该接口使用Dump功能，一个算子所有使用Dump功能的接口在每个核上Dump的数据总量不可超过1M。请开发者自行控制待打印的内容数据量，超出则不会打印。

调用示例

constexpr uint32_t totalLength = 256;    // 参与搬运的元素个数AscendC::LocalTensor<half> srcLocal;AscendC::GlobalTensor<half> srcGlobal;AscendC::DataCopy(srcLocal, srcGlobal, totalLength * sizeof(half));uint32_t index = 8;    // 用户自定义附加信息，此处传入DumpAccChkPoint指令的行号uint32_t countOff = 32;    // 偏移元素个数，从srcLocal[32]开始打印uint32_t dupmSize = 128;    // dump的元素个数，从srcLocal[32]开始打印128个元素个数AscendC::DumpAccChkPoint(srcLocal, index, countOff, dupmSize);

## 6.2.3.11.1.4 PrintTimeStamp

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 1910 -->

功能说明

推荐使用asc_time_stamp接口进行时间戳的获取，该接口同时适用于C语言和C++语言编程。

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
__aicore__ inline void PrintTimeStamp(uint32_t descId)
```

参数说明

参数名输入/输出

描述

descId输入用户自定义标识符（自定义数字），用于区分不同打点位置。

注意

[0, 0xffff]是预留给Ascend C内部各个模块使用的id值，用户自定义的descId建议使用大于0xffff的数值。

返回值说明

无

约束说明

●该功能仅用于NPU上板调试。

●暂不支持算子入图场景的打印。
