# REGISTER_TILING_FOR_TILINGKEY

> **Section**: 6.2.3.14.10  
> **PDF Pages**: 1989–1990  

---

<!-- page 1989 -->

注册TilingData结构体用于告知框架侧用户使用标准C++语法来定义TilingData，同时告知框架TilingData结构体类型，用于框架做tiling数据解析。

函数原型

```cpp
REGISTER_TILING_DEFAULT(TILING_STRUCT)
```

参数说明

参数输入/输出说明

TILING_STRUCT

输入用户注册的默认自定义TilingData结构体。

约束说明

●若TilingData结构体在命名空间内，注册时需要携带对应的命名空间作用域符。

●暂不支持Kernel直调工程。

调用示例

extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling){    REGISTER_TILING_DEFAULT(optiling::TilingData); // 用于在kernel侧注册用户使用标准C++语法自定义的默认TilingData结构体    GET_TILING_DATA(tilingData, tiling);    KernelAdd op;    op.Init(x, y, z, tilingData.blkDim, tilingData.totalSize, tilingData.splitTile);    op.Process();}

## 6.2.3.14.10 REGISTER_TILING_FOR_TILINGKEY

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

<!-- page 1990 -->

功能说明

用于在kernel侧注册与TilingKey相匹配的TilingData自定义结构体；该接口需提供一个逻辑表达式，逻辑表达式以字符串“TILING_KEY_VAR”代指实际TilingKey，表达TilingKey所满足的范围。

函数原型

```cpp
REGISTER_TILING_FOR_TILINGKEY(EXPRESSION, TILING_STRUCT)
```

参数说明

参数输入/输出说明

EXPRESSION

输入EXPRESSION为逻辑运算，其中用TILING_KEY_VAR指代TilingKey。

TILING_STRUCT

输入用户注册的与TilingKey相匹配的TilingData自定义结构体。

约束说明

●使用该接口时，需确保已使用REGISTER_TILING_DEFAULT注册默认的用户自定义TilingData结构体，用于告知框架侧用户使用标准C++语法来定义TilingData。

●EXPRESSION当前支持位运算：&、|、~、^；移位运算符：<<、>>；算术运算：+、-、*、/、%；条件运算符：==、!=、>、<、>=、<=；逻辑与&&、或||以及()。优先级同C++。

●若TilingData结构体在命名空间内，注册时需要携带对应的命名空间作用域符。

●不支持同个TilingKey指向不同TilingData结构体，会出现拦截报错。

●暂不支持kernel直调工程。

调用示例

extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling){    REGISTER_TILING_DEFAULT(optiling::TilingData);  // 注册用户默认自定义TilingData结构体    REGISTER_TILING_FOR_TILINGKEY("TILING_KEY_VAR == 1", optiling::TilingDataA); // 注册TilingKey为1的TilingData结构体    REGISTER_TILING_FOR_TILINGKEY("(TILING_KEY_VAR >= 10) && (TILING_KEY_VAR <= 15)", optiling::TilingDataB); // 注册TilingKey在[10,15]之间的TilingData结构体    REGISTER_TILING_FOR_TILINGKEY("TILING_KEY_VAR & 0xFF", optiling::TilingDataC); // 注册TilingKey低16位为1的TilingData结构体    if (TILING_KEY_IS(1)) {        GET_TILING_DATA_WITH_STRUCT(optiling::TilingDataA, tilingData, tiling);        ......    } else if (TILING_KEY_IS(11)) {        GET_TILING_DATA_WITH_STRUCT(optiling::TilingDataB, tilingData, tiling);        ......    } else if (TILING_KEY_IS(14)) {        GET_TILING_DATA_WITH_STRUCT(optiling::TilingDataB, tilingData, tiling);        ......    } else if (TILING_KEY_IS(255)) {        GET_TILING_DATA_WITH_STRUCT(optiling::TilingDataC, tilingData, tiling);        ......    } else {        GET_TILING_DATA(tilingData, tiling);
