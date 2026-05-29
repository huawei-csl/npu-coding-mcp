# GET_TPL_TILING_KEY

> **Section**: 6.4.6.2  
> **PDF Pages**: 3866–3867  

---

<!-- page 3866 -->

宏功能描述参数解释

ASCENDC_TPL_DETERMINISTIC_SEL(args0)

args0: 表示参数名，可选值范围[true, false, 1,0]，其中[true/1]表示该组模板参数组合使能确定性计算，[false/0]表示不使能确定性计算。需要注意，该值不作为算子的模板参数入参，在使能该值编译时，会添加"-DDETERMINISTIC_MODE=1", 同时会生成以"_deterministic"结尾的json与.o文件，例如："AddCustomTemplate_816f04e052850554f4b3cacb35f8e8c6_deterministic.json"/"AddCustomTemplate_816f04e052850554f4b3cacb35f8e8c6_deterministic.o"。

该组模板参数组合用于配置是否使能确定性计算。

备注：若通过ASCENDC_TPL_DETERMINISTIC_SEL(true)接口编译出了确定性计算的版本，在算子调用时，通常需要打开确定性计算的的开关，例如通过aclnn单算子调用时，需要使用aclrtCtxSetSysParamOpt接口进行相关配置。

该参数仅支持如下型号：

●Atlas A3 训练系列产品/Atlas A3 推理系列产品

●Atlas A2 训练系列产品/Atlas A2 推理系列产品

ASCENDC_TPL_SHARED_KERNEL_TYPE_SEL(args0, ...)

args0: 参数名

设置算子模板参数组合的Kernel类型，该参数可以作为核函数的模板参数传入。

args1-argsn: 该模板参数组合下，算子的Kernel类型，后续参数为若干Kernel类型。该接口不能与ASCENDC_TPL_KERNEL_TYPE_SEL接口同时使用。

若同时使用KERNEL_TASK_TYPE_DEFAULT(value)接口，本接口优先级更高。

返回值说明

无。

约束说明

对模板参数定义的取值进行修改或新增后，需要重新编译自定义算子包，不能再继续使用之前的算子二进制。

## 6.4.6.2 GET_TPL_TILING_KEY

功能说明

Tiling模板编程时，开发者通过调用此接口自动生成TilingKey。该接口将传入的模板参数通过定义的位宽，转成二进制，按照顺序组合后转成uint64数值，即TilingKey。

<!-- page 3867 -->

使用该接口需要包含定义模板参数和模板参数组合的头文件。详细内容请参考Tiling模板编程。

函数原型

```cpp
namespace AscendC {    uint64_t EncodeTilingKey(TilingDeclareParams declareParams,                             TilingSelectParams selectParamsVec,                             std::vector<uint64_t> tilingParams);}
```

#define GET_TPL_TILING_KEY(...) \    AscendC::EncodeTilingKey(g_tilingDeclareParams, g_tilingSelectParams, {__VA_ARGS__}) // GET_TPL_TILING_KEY通过调用EncodeTilingKey接口生成TilingKey， EncodeTilingKey属于内部关联接口，开发者无需关注

参数说明

参数输入/输出说明

...输入可变长参数，模板参数的具体值，传入时需要与定义模板参数和模板参数组合的头文件中的模板参数顺序保持一致。

返回值说明

TilingKey数值。

约束说明

无。

调用示例

#include "tiling_key_add_custom.h"static ge::graphStatus TilingFunc(gert::TilingContext *context){    TilingDataTemplate tiling;    uint32_t totalLength = context->GetInputShape(0)->GetOriginShape().GetShapeSize();    ge::DataType dtype_x = context->GetInputDesc(0)->GetDataType();    ge::DataType dtype_y = context->GetInputDesc(1)->GetDataType();    ge::DataType dtype_z = context->GetOutputDesc(0)->GetDataType();    uint32_t D_T_X = static_cast<int>(dtype_x), D_T_Y = static_cast<int>(dtype_y), D_T_Z = static_cast<int>(dtype_z), TILE_NUM = 1, IS_SPLIT = 0;    if (totalLength < MIN_LENGTH_FOR_SPLIT) {        IS_SPLIT = 0;        TILE_NUM = 1;    } else {        IS_SPLIT = 1;        TILE_NUM = DEFAULT_TILE_NUM;    }    context->SetBlockDim(NUM_BLOCKS);    tiling.set_totalLength(totalLength);    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());    const uint64_t tilingKey = GET_TPL_TILING_KEY(D_T_X, D_T_Y, D_T_Z, TILE_NUM, IS_SPLIT);  // 模板参数tilingkey配置    context->SetTilingKey(tilingKey);    size_t *currentWorkspace = context->GetWorkspaceSizes(1);    currentWorkspace[0] = 0;
