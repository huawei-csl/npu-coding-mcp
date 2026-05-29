# TRACE_START

> **Section**: 6.4.10.10  
> **PDF Pages**: 3894–3895  

---

<!-- page 3894 -->

●如果在循环中增加了一个MarkStamp指令，每次执行到指令时都会输出一个打点，且index是相同的。

●如果开发者在两个相邻的VF分别打标记，由于编译器可能会对VF A和VF B做融合，MarkStamp1和MarkStamp2则会被优化掉，不会输出打点。

调用示例

mte2_opt();mte1_opt();//在算子执行开始处打点asc_mark_stamp<CUBE, 0>();//执行核心计算cube_opt();//在算子执行结束处打点asc_mark_stamp<CUBE, 1>();mte3_opt();

## 6.4.10.10 TRACE_START

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

通过CAModel进行算子性能仿真时，可对算子任意运行阶段打点，从而分析不同指令的流水图，以便进一步性能调优。

用于表示起始位置打点，一般与6.4.10.11 TRACE_STOP配套使用。

<!-- page 3895 -->

注意

该功能主要用于调试和性能分析，开启后会对算子性能产生一定影响，通常在调测阶段使用，生产环境建议关闭。

默认情况下，该功能关闭，开发者可以按需通过如下方式开启打点功能。

修改Kernel直调工程cmake目录下的npu_lib.cmake文件，在ascendc_compile_definitions命令中增加-DASCENDC_TRACE_ON编译选项，来开启打点功能。示例如下：// 打开算子的打点功能ascendc_compile_definitions(ascendc_kernels_${RUN_MODE} PRIVATE    -DASCENDC_TRACE_ON)

函数原型

#define TRACE_START(TraceId apid)#define TRACE_START(pipe_t pipe, TraceId apid) // 该接口仅支持Atlas 350 加速卡

参数说明

参数名输入/输出

描述

apid输入当前预留了十个用户自定义的类型：

●0x0：USER_DEFINE_0

●0x1：USER_DEFINE_1

●0x2：USER_DEFINE_2

●0x3：USER_DEFINE_3

●0x4：USER_DEFINE_4

●0x5：USER_DEFINE_5

●0x6：USER_DEFINE_6

●0x7：USER_DEFINE_7

●0x8：USER_DEFINE_8

●0x9：USER_DEFINE_9

pipe输入指定打点所在的pipeline类型。

返回值说明

无

约束说明

●TRACE_START/TRACE_STOP需配套使用，若Trace图上未显示打点，则说明两者没有配对。

●不支持跨核使用，例如TRACE_START在AI Cube打点，则TRACE_STOP打点也需要在AI Cube上，不能在AI Vector上。
