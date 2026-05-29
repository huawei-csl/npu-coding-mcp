# GET_TILING_DATA

> **Section**: 6.2.3.14.1  
> **PDF Pages**: 1977–1978  

---

<!-- page 1977 -->

产品是否支持

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

该接口用于获取SSBuffer的基地址。

函数原型

```cpp
__aicore__ inline __ssbuf__ void*  GetSsbufBaseAddr()
```

参数说明

无

返回值说明

返回指向SSBuffer基地址的指针。

约束说明

●SSBuffer中存在脏数据，读取时数据时不保证全为0。

●AIC和AIV启动不同的任务时，不能访问SSBuffer。

●访问超过最末端的地址存在异常。每个核在非MIX模式下运行时，可以独立占用1KB的空间（AIC，AIV0，AIV1各占据1KB）；或者在Mix模式下运行时共享整个3KB的空间(AIC:AIV = 1:2)。目前ssbuf的大小为3KB。

●只支持通过读写指令32B,64B 的对齐访问。

调用示例

__ssbuf__ void* ssbuf = GetSsbufBaseAddr(); // NPU域中返回(void*) 0 ,CPU域中返回CPU模拟分配的地址AscendC::printf("Ssbuf基地址指针： %p\n", ssbuf ); // %p为打印指针格式符，NPU环境中，将特殊的 0 指针值显示为 nilAscendC::PRINTF("Ssbuf基地址指针： %p\n", ssbuf ); //输出为nil

## 6.2.3.14 Kernel Tiling

## 6.2.3.14.1 GET_TILING_DATA

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

<!-- page 1978 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

用于获取算子kernel入口函数传入的Tiling信息，并填入注册的TilingData结构体中，此函数会以宏展开的方式进行编译。对应的算子host实现中需要定义TilingData结构体，实现并注册计算TilingData的Tiling函数，具体请参考2.10.2.5 Host侧Tiling实现。如果用户通过6.4.4.2 TilingData结构注册注册了多个TilingData结构体，使用该接口返回默认注册的结构体。

函数原型

```cpp
GET_TILING_DATA(tiling_data, tiling_arg)
```

参数说明

参数输入/输出说明

tiling_data输出返回默认TilingData结构体变量。

tiling_arg输入此参数为算子入口函数处传入的Tiling参数。

约束说明

●本函数需在算子kernel代码处使用，并且传入的tiling_data参数不需要声明类型。

●暂不支持kernel直调工程。

调用示例

extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling){    GET_TILING_DATA(tilingData, tiling);// 反序列化SaveToBuffer生成的数据，并填入注册的TilingData结构体中    KernelAdd op;    op.Init(x, y, z, tilingData.numBlocks, tilingData.totalSize, tilingData.splitTile);    op.Process();}

配套的host侧Tiling函数示例：ge::graphStatus TilingFunc(gert::TilingContext* context){    // 其他代码逻辑    ...    TilingData tiling;  // 与算子host实现中定义TilingData结构体的对应
