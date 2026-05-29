# TRACE_STOP

> **Section**: 6.4.10.11  
> **PDF Pages**: 3896–3896  

---

<!-- page 3896 -->

●宏支持所有的产品型号，但实际调用时需与调测工具支持的型号保持一致。

●仅支持Kernel直调工程，不支持自定义算子工程下开启打点功能。

调用示例

在Kernel代码中特定指令位置打上TRACE_START/TRACE_STOP：

```cpp
TRACE_START(0x2);Add(zLocal, xLocal, yLocal, dataSize);TRACE_STOP(0x2);
```

## 6.4.10.11 TRACE_STOP

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

用于表示终止位置打点，一般与6.4.10.10 TRACE_START配套使用。

注意

该功能主要用于调试和性能分析，开启后会对算子性能产生一定影响，通常在调测阶段使用，生产环境建议关闭。

默认情况下，该功能关闭，开发者可以按需通过如下方式开启打点功能。

修改Kernel直调工程cmake目录下的npu_lib.cmake文件，在ascendc_compile_definitions命令中增加-DASCENDC_TRACE_ON编译选项，来开启打点功能。示例如下：// 打开算子的打点功能ascendc_compile_definitions(ascendc_kernels_${RUN_MODE} PRIVATE    -DASCENDC_TRACE_ON)
