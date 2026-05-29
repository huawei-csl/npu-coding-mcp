# ReadGmByPassDCache(ISASI)

> **Section**: 6.2.3.5.10  
> **PDF Pages**: 1732–1732  

---

<!-- page 1732 -->

返回值说明

无

约束说明

无

调用示例

```cpp
__gm__ int32_t* addr = dstGlobal.GetPhyAddr();int32_t value = 2;WriteGmByPassDCache(addr, value);
```

## 6.2.3.5.10 ReadGmByPassDCache(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

不经过DCache从GM地址上读数据。

当多核操作GM地址时，如果数据无法对齐到Cache Line，经过DCache的方式下，由于按照Cache Line大小进行读写，会导致多核数据随机覆盖的问题。此时，可以采用不经过DCache直接读写GM地址的方式，从而避免上述随机覆盖的问题。

函数原型

```cpp
template <typename T>__aicore__ inline T ReadGmByPassDCache(__gm__ T* addr)
```
