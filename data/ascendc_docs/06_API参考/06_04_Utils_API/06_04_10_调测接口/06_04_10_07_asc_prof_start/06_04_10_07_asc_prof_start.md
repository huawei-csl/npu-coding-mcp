# asc_prof_start

> **Section**: 6.4.10.7  
> **PDF Pages**: 3891–3891  

---

<!-- page 3891 -->

约束说明

●该功能仅用于NPU上板调试。

●暂不支持算子入图场景的打印。

●单次调用本接口打印的数据总量不可超过1MB（还包括少量框架需要的头尾信息，通常可忽略）。使用时应注意，如果超出这个限制，则数据不会被打印。在使用自定义算子工程进行工程化算子开发时，一个算子所有使用Dump功能的接口在每个核上Dump的数据总量不可超过1MB。请开发者自行控制待打印的内容数据量，超出则不会打印。

调用示例

```cpp
asc_time_stamp(11);
```

打印结果如下（Dump信息头等仅在使用自定义算子工程时才会打印）：

opType=AddCustom, DumpHead: AIV-0, CoreType=AIV, block dim=8, total_block_num=8, block_remain_len=1047136, block_initial_space=1048576, rsv=0, magic=5aa5bccd...// 一些框架内部的打点信息descId is 11, rsv is 0, timeStamp is 815603975350485, pcPtr is 19792358553124, entry is 815603975328116.

## 6.4.10.7 asc_prof_start

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

用于设置性能数据采集信号启动，和asc_prof_stop配合使用。使用msProf工具进行算子上板调优时，可在kernel侧代码段前后分别调用asc_prof_start和asc_prof_stop来指定需要调优的代码段范围。

函数原型

```cpp
__aicore__ inline void asc_prof_start()
```

参数说明

无
