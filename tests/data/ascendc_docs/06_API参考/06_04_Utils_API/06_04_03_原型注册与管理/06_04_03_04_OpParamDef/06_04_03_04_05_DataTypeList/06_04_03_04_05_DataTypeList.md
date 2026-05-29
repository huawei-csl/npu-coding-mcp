# DataTypeList

> **Section**: 6.4.3.4.5  
> **PDF Pages**: 3789–3789  

---

<!-- page 3789 -->

```cpp
.Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("z")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32, ge::DT_INT16})            .DataTypeForBinQuery({ge::DT_FLOAT, ge::DT_FLOAT, ge::DT_FLOAT16, ge::DT_FLOAT16})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
```

## 6.4.3.4.5 DataTypeList

功能说明

定义算子参数数据类型。如果某个输入/输出支持的数据类型支持和其他所有输入/输出支持的数据类型、数据格式组合使用，可以使用该接口定义数据类型。

使用DataType配置数据类型时，算子参数的数据类型和格式必须通过显式组合配置，每个组合包含完整的输入/输出数据类型与数据格式的对应关系。如下的示例中表示：当输入x和y数据类型为DT_FLOAT16时，对应的输出z数据类型也为DT_FLOAT16，支持的数据格式要求为FORMAT_ND。

```cpp
class AddCustom : public OpDef {public:    AddCustom(const char* name) : OpDef(name)    {        this->Input("x")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("y")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("z")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});        ...    }};
```

如果某个输入/输出支持的数据类型支持和其他所有输入/输出支持的数据类型、数据格式组合使用，使用DataType接口需要写成如下的格式，表示当输入x为DT_FLOAT16时，支持输入y和输入z的所有数据类型、数据格式组合。

```cpp
class XxxCustom : public OpDef {public:    XxxCustom(const char* name) : OpDef(name)    {        this->Input("x")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT16, ge::DT_FLOAT16})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("y")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("z")            .ParamType(REQUIRED)            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});        ...    }};
```

此时可以通过DataTypeList指定数据类型，无需重复列出，例如：
