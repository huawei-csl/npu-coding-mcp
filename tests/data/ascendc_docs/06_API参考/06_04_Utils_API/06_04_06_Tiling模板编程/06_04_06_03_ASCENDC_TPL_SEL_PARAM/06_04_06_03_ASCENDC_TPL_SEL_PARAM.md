# ASCENDC_TPL_SEL_PARAM

> **Section**: 6.4.6.3  
> **PDF Pages**: 3868–3868  

---

<!-- page 3868 -->

```cpp
return ge::GRAPH_SUCCESS;}
```

## 6.4.6.3 ASCENDC_TPL_SEL_PARAM

功能说明

Tiling模板编程时，开发者通过调用此接口自动生成并配置TilingKey。

使用该接口需要包含定义模板参数和模板参数组合的头文件。详细内容请参考Tiling模板编程。

函数原型

#define ASCENDC_TPL_SEL_PARAM(context, ...)           \do {                                                  \    uint64_t key = GET_TPL_TILING_KEY({__VA_ARGS__}); \    context->SetTilingKey(key);                       \} while(0)// context指代TilingFunc(gert::TilingContext *context)中的context

参数说明

参数输入/输出说明

context输入TilingFunc注册上下文。

...输入可变长参数，模板参数的具体值，传入时需要与定义模板参数和模板参数组合的头文件中的模板参数顺序保持一致。

返回值说明

无

约束说明

无

调用示例

```cpp
#include "tiling_key_add_custom.h"static ge::graphStatus TilingFunc(gert::TilingContext *context){    TilingDataTemplate tiling;
    uint32_t totalLength = context->GetInputShape(0)->GetOriginShape().GetShapeSize();
    ge::DataType dtype_x = context->GetInputDesc(0)->GetDataType();
    ge::DataType dtype_y = context->GetInputDesc(1)->GetDataType();
    ge::DataType dtype_z = context->GetOutputDesc(0)->GetDataType();
    uint32_t D_T_X = static_cast<int>(dtype_x), D_T_Y = static_cast<int>(dtype_y), D_T_Z = static_cast<int>(dtype_z), TILE_NUM = 1, IS_SPLIT = 0;
    if (totalLength < MIN_LENGTH_FOR_SPLIT) {        IS_SPLIT = 0;
        TILE_NUM = 1;    } else {        IS_SPLIT = 1;
        TILE_NUM = DEFAULT_TILE_NUM;    }
```
