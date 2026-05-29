# ReinterpretCast

> **Section**: 6.2.2.2.13  
> **PDF Pages**: 849–850  

---

<!-- page 849 -->

表6-75参数说明

参数名输入/输出

描述

**mode输入用户指定的L2 Cache模式。enum class CacheMode : uint8_t {CACHE_MODE_DISABLE = 0, // 不使能L2 CacheCACHE_MODE_NORMAL = 1,  // 使能L2 Cache};**

如果用户在写算子时，相比不使能L2 Cache，某GlobalTensor使能L2 Cache反而会导致实测性能下降，可以手动禁止该GlobalTensor使能L2 Cache。比如某算子仅会读一次某个GlobalTensor数据，数据进L2 Cache并不会对算子产生收益，反而会因为数据频繁的搬入L2 Cache造成性能损耗，可以考虑不使能该GlobalTensor L2 Cache能力。

如果不调用该接口，默认为CacheMode::CACHE_MODE_NORMAL，即GlobalTensor会使能L2 Cache。

返回值说明

无。

约束说明

使用mssanitizer工具时，默认使能L2 Cache，无法通过本接口设置L2 Cache模式为CACHE_MODE_DISABLE。

调用示例

uint64_t dataSize = 256; //设置input_global的大小为256

AscendC::GlobalTensor<int32_t> inputGlobal; // 类型为int32_tinputGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ int32_t *>(src_gm), dataSize); // 设置源操作数在Global Memory上的起始地址为src_gm，所占外部存储的大小为256个int32_tinputGlobal.SetL2CacheHint(AscendC::CacheMode::CACHE_MODE_DISABLE); // 设置GlobalTensor不会写入L2 Cache

AscendC::LocalTensor<int32_t> inputLocal = inQueueX.AllocTensor<int32_t>();    AscendC::DataCopy(inputLocal, inputGlobal, dataSize); // 将Global Memory上的inputGlobal拷贝到Local Memory的inputLocal上

## 6.2.2.2.13 ReinterpretCast

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

<!-- page 850 -->

产品是否支持

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将当前GlobalTensor重解释为用户指定的新类型。转换后的Tensor与原Tensor地址及内容完全相同，Tensor的内存大小（比特数）保持不变。

函数原型

```cpp
template <typename CAST_T>__aicore__ inline GlobalTensor<CAST_T> ReinterpretCast() const
```

参数说明

表6-76模板参数说明

参数名描述

CAST_T指定重解释后的新类型。

返回值说明

重解释后的GlobalTensor。

约束说明

当数据类型发生转换后，元素个数可能无法取整，例如3个int4b_t类型转换为uint32_t，则转换后调用GetSize接口，只能获取向下取整的整数值，这种场景在CPU状态运行时，会有对应的提示告警信息。

调用示例

uint64_t dataSize = 256; //设置input_global的大小为256

AscendC::GlobalTensor<int32_t> inputGlobal; // 类型为int32_tinputGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ int32_t *>(src_gm), dataSize); // 设置源操作数在Global Memory上的起始地址为src_gm，所占外部存储的大小为256个int32_t

AscendC::LocalTensor<int32_t> inputLocal = inQueueX.AllocTensor<int32_t>();    AscendC::DataCopy(inputLocal, inputGlobal, dataSize); // 将Global Memory上的inputGlobal拷贝到Local Memory的inputLocal上...// 假设inputGlobal为int32_t 类型，包含16个元素（64字节）// 调用ReinterpretCast将inputGlobal重解释为int16_t类型AscendC::GlobalTensor<int16_t> interpreTensor = inputGlobal.template ReinterpretCast<int16_t>();// 示例结果如下，二者数据完全一致，在物理内存上也是同一地址，仅根据不同类型进行了重解释
