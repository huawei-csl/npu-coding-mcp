# REGISTER_NONE_TILING

> **Section**: 6.2.3.14.11  
> **PDF Pages**: 1991–1992  

---

<!-- page 1991 -->

```cpp
......    }}
```

使用标准C++语法注册tiling结构体：

```cpp
class TilingDataA{public:    ...};class TilingDataB{public:    ...};class TilingDataC{public:    ...};
```

配套的host侧tiling函数示例：

ge::graphStatus TilingFunc(gert::TilingContext* context){    // 其他代码逻辑    ...    if(condition1){        context->SetTilingKey(1);        optiling::TilingDataA *Addtiling = context->GetTilingData<optiling::TilingDataA>();        ...    } else if (condition2){        context->SetTilingKey(11);        optiling::TilingDataB *Addtiling = context->GetTilingData<optiling::TilingDataB >();        ...    } else if (condition3){        context->SetTilingKey(14);        optiling::TilingDataB *Addtiling = context->GetTilingData<optiling::TilingDataB >();        ...    } else if (condition4){        context->SetTilingKey(255);        optiling::TilingDataC *Addtiling = context->GetTilingData<optiling::TilingDataC >();        ...    }    ...    // 其他代码逻辑}

## 6.2.3.14.11 REGISTER_NONE_TILING

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 1992 -->

功能说明

在Kernel侧使用标准C++语法自定义的TilingData结构体时，若用户不确定需要注册哪些结构体，可使用该接口告知框架侧需使用未注册的标准C++语法来定义TilingData，并配套6.2.3.14.2 GET_TILING_DATA_WITH_STRUCT，6.2.3.14.3GET_TILING_DATA_MEMBER，6.2.3.14.4 GET_TILING_DATA_PTR_WITH_STRUCT来获取对应的TilingData。

函数原型

```cpp
REGISTER_NONE_TILING
```

参数说明

无

约束说明

●暂不支持Kernel直调工程。

●使用GET_TILING_DATA需提供默认注册的TilingData结构体，但本接口不注册TilingData结构体，故不支持与5.11.1-GET_TILING_DATA组合使用。

●不支持和6.2.3.14.9 REGISTER_TILING_DEFAULT或6.2.3.14.10REGISTER_TILING_FOR_TILINGKEY混用，即不支持注册TilingData结构体的场景与非注册场景混合使用。

调用示例

# Tiling模板库提供方，无法预知用户实例化何种TilingData结构体template <class BrcDag>struct BroadcastBaseTilingData {    int32_t scheMode;    int32_t shapeLen;    int32_t ubSplitAxis;    int32_t ubFormer;    int32_t ubTail;    int64_t ubOuter;    int64_t blockFormer;    int64_t blockTail;    int64_t dimProductBeforeUbInner;    int64_t elemNum;    int64_t blockNum;    int64_t outputDims[BROADCAST_MAX_DIMS_NUM];    int64_t outputStrides[BROADCAST_MAX_DIMS_NUM];    int64_t inputDims[BrcDag::InputSize][2]; // 整块 + 尾块    int64_t inputBrcDims[BrcDag::CopyBrcSize][BROADCAST_MAX_DIMS_NUM];    int64_t inputVecBrcDims[BrcDag::VecBrcSize][BROADCAST_MAX_DIMS_NUM];    int64_t inputStrides[BrcDag::InputSize][BROADCAST_MAX_DIMS_NUM];    int64_t inputBrcStrides[BrcDag::CopyBrcSize][BROADCAST_MAX_DIMS_NUM];    int64_t inputVecBrcStrides[BrcDag::VecBrcSize];    char scalarData[BROADCAST_MAX_SCALAR_BYTES];};

template <uint64_t schMode, class BrcDag> class BroadcastSch {public:    __aicore__ inline explicit BroadcastSch(GM_ADDR& tmpTiling)        : tiling(tmpTiling)    {}    template <class... Args>    __aicore__ inline void Process(Args... args)    {        REGISTER_NONE_TILING; // 告知框架侧使用未注册的TilingData结构体        if constexpr (schMode == 1) {
