# GetReduceRepeatMaxMinSpr(ISASI)

> **Section**: 6.2.3.3.6.13  
> **PDF Pages**: 1429–1430  

---

<!-- page 1429 -->

AscendC::LocalTensor<float> dst;AscendC::ReduceSum(dst, src, work, 128);float res = AscendC::GetReduceRepeatSumSpr<float>(); // 返回前128个数的和

## 6.2.3.3.6.13 GetReduceRepeatMaxMinSpr(ISASI)

产品支持情况

产品是否支持（仅获取

是否支持（获取最值和索引的原型）

最值的原型）

Atlas 350 加速卡x√

Atlas A3 训练系列产品/Atlas A3 推理系列产品

x√

Atlas A2 训练系列产品/Atlas A2 推理系列产品

x√

Atlas 200I/500 A2 推理产品xx

Atlas 推理系列产品AI Core√x

Atlas 推理系列产品Vector Corexx

Atlas 训练系列产品xx

功能说明

获取ReduceMax、ReduceMin连续场景下的最大/最小值以及相应的索引值。

函数原型

●获取ReduceMax、ReduceMin连续场景下的最大值与最小值，以及相应的索引值。template <typename T>__aicore__ inline void GetReduceRepeatMaxMinSpr(T &maxMinValue, T &maxMinIndex)

●获取ReduceMax、ReduceMin连续场景下的最大值与最小值。template <typename T>__aicore__ inline void GetReduceRepeatMaxMinSpr(T &maxMinValue)

参数说明

表6-402模板参数说明

参数名描述

TReduceMax/ReduceMin指令的数据类型，支持half/float。

<!-- page 1430 -->

表6-403参数说明

参数名输入/输出

描述

maxMinValue

输出ReduceMax/ReduceMin指令的最大值/最小值。

maxMinIndex

输出ReduceMax/ReduceMin指令的最值对应的索引值。

返回值说明

无

约束说明

●针对Atlas A2 训练系列产品/Atlas A2 推理系列产品，由于ReduceMax/ReduceMin的内部实现原因，直接调用GetReduceRepeatMaxMinSpr接口无法获取到准确的索引值，验证时需要使用WholeReduceMax/WholeReduceMin接口来获取准确的索引值。

●针对Atlas A3 训练系列产品/Atlas A3 推理系列产品，由于ReduceMax/ReduceMin的内部实现原因，直接调用GetReduceRepeatMaxMinSpr接口无法获取到准确的索引值，验证时需要使用WholeReduceMax/WholeReduceMin接口来获取准确的索引值。

●针对Atlas 350 加速卡，由于ReduceMax/ReduceMin的内部实现原因，直接调用GetReduceRepeatMaxMinSpr接口无法获取到准确的索引值，验证时需要使用WholeReduceMax/WholeReduceMin接口来获取准确的索引值。同时，GetReduceRepeatMaxMinSpr必须紧跟着WholeReduceMax/WholeReduceMin接口进行调用。

●索引maxMinIndex数据`是按照ReduceMax/ReduceMin的数据类型进行存储的，比如ReduceMax/ReduceMin使用half类型时，maxMinIndex是按照half类型进行存储的，如果按照half格式进行读取，maxMinIndex的值是不对的，因此maxMinIndex的读取需要使用reinterpret_cast方法转换到整数类型，若输入数据类型是half，需要使用reinterpret_cast<uint16_t*>，若输入是float，需要使用reinterpret_cast<uint32_t*>。

调用示例

1.以ReduceMax指令为例，首先执行ReduceMax指令。AscendC::LocalTensor<float> src;AscendC::LocalTensor<float> work;AscendC::LocalTensor<float> dst;int32_t mask = 64;AscendC::ReduceMax(dst, src, work, mask, 1, 8, true); // 连续场景，srcRepStride = 8，且calIndex = true

2.获取上述ReduceMax指令的最值与索引值。

针对Atlas A2 训练系列产品/Atlas A2 推理系列产品，需要使用WholeReduceMax指令获取准确的索引值，然后再调用GetReduceRepeatMaxMinSpr指令。AscendC::LocalTensor<float> src;AscendC::LocalTensor<float> dst;int32_t mask = 64;AscendC::WholeReduceMax(dst, src, mask, 1, 1, 1, 8);
