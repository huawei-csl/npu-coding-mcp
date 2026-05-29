# LoadUnzipIndex

> **Section**: 6.2.3.2.1.3  
> **PDF Pages**: 1007–1008  

---

<!-- page 1007 -->

返回值说明

无

调用示例

该调用示例支持的运行平台为Atlas 推理系列产品AI Core。

```cpp
uint16_t C1 = 2;uint16_t H = 4, W = 4;uint8_t Kh = 2, Kw = 2;uint16_t Cout = 16;uint16_t C0 = 16;uint8_t dilationH = 2, dilationW = 2;uint8_t padTop = 1, padBottom = 1, padLeft = 1, padRight = 1;uint8_t strideH = 1, strideW = 1;uint8_t padList[4] = {padLeft, padRight, padTop, padBottom};LoadData3DParamsV2 param = { padList, H, W, 0, 0, 0, -1, -1, strideW, strideH, Kw, Kh, dilationW, dilationH, 1, 0, fmRepeat, 0, (half)(0)};Load3DBitModeParam paramBitMode(param);
  AscendC::LoadData<A2, A1, half>(featureMapA2, featureMapA1, paramBitMode);AscendC::LoadData(weightB2, weightB1, { 0, weRepeat, 1, 0, 0, false, 0 });
```

## 6.2.3.2.1.3 LoadUnzipIndex

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

加载GM上的压缩索引表到内部寄存器。

索引表为LoadDataUnzip压缩信息，例如压缩长度等，以获取压缩后的数据。

索引表由压缩工具根据对应的权重数据离线生成。一个LoadUnzipIndex指令可以加载多个索引表，而每个LoadDataUnzip指令只能消耗一个索引表。因此，索引表之间的顺序应该由用户来确定，以确保其与压缩数据的对应性。

函数原型

```cpp
template <typename T = int8_t, typename Std::enable_if<Std::is_same<PrimT<T>, int8_t>::value, bool>::type = true> __aicore__ inline void LoadUnzipIndex(const GlobalTensor<T>& src, uint32_t numOfIndexTabEntry)
```

<!-- page 1008 -->

参数说明

表6-178模板参数说明

参数名描述

Tsrc的数据类型。

●当src使用基础数据类型时，其数据类型必须为uint8_t，否则编译失败。

●当src使用TensorTrait类型时， src数据类型T的LiteType必须为int8_t，否则编译失败。

最后一个模板参数仅用于上述数据类型检查，用户无需关注。

表6-179参数说明

参数名称输入/输出

含义

src输入源操作数，索引表地址，类型为GlobalTensor。

src地址必须2字节对齐。src长度必须是512字节的整数倍，最大为32KB。

numOfIndexTabEntry

输入输入数据，表示加载的索引表个数。索引表个数必须大于0。

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●LoadUnzipIndex必须在任何LoadDataUnzip指令之前执行。

●LoadUnzipIndex加载的索引表个数必须大于或等于LoadDataUnzip指令执行的次数。

调用示例

该调用示例支持的运行平台为Atlas 推理系列产品AI Core。详细用例请参考LoadDataUnzip。

```cpp
indexGlobal.SetGlobalBuffer((__gm__ int8_t*)indexGm);AscendC::LoadUnzipIndex(indexGlobal, numOfIndexTabEntry);
```
