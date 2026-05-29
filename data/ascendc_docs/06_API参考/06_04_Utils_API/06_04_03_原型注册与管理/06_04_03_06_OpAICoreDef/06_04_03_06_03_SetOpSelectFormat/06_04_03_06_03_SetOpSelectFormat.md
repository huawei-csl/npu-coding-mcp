# SetOpSelectFormat

> **Section**: 6.4.3.6.3  
> **PDF Pages**: 3813–3813  

---

<!-- page 3813 -->

OpAICoreConfig aicConfig;        aicConfig.DynamicCompileStaticFlag(true)            .DynamicFormatFlag(true)            .DynamicRankSupportFlag(true)            .DynamicShapeSupportFlag(true).NeedCheckSupportFlag(true)            .PrecisionReduceFlag(true);        // 注意：soc_version请替换成实际的AI处理器型号        this->AICore().AddConfig("soc_version", aicConfig);    }};

## 6.4.3.6.3 SetOpSelectFormat

功能说明

如果您需要自行推导算子输入输出所支持的数据类型与格式，则可实现推导回调函数，并通过该接口进行注册。同时需要将6.4.3.9.5 DynamicFormatFlag配置为true，则算子融合时会自动调用推导函数进行数据类型与格式的设置，算子原型注册时无需配置输入输出支持的数据类型与格式。

注意，如果算子原型已经注册过数据类型与格式，则以算子原型注册的数据类型与格式为准，即使注册了推导函数也不会执行。

函数原型

```cpp
OpAICoreDef &SetOpSelectFormat(optiling::OP_CHECK_FUNC func)
```

参数说明

参数输入/输出说明

func输入推导算子输入输出所支持数据类型与格式的函数。OP_CHECK_FUNC类型定义如下：using OP_CHECK_FUNC = ge::graphStatus (*)(const ge::Operator &op, ge::AscendString &result);

该函数的入参是算子的描述，包括算子的输入、输出、属性等信息，出参为包含了当前算子输入输出支持的数据类型与格式列表的字符串，字符串的格式样例如下：{    "input0": {"name": "x","dtype": "float16,float32,int32","format": "ND,ND,ND"},    "input1": {"name": "y","dtype": "float16,float32,int32","format": "ND,ND,ND"},    "output0": {"name": "z","dtype": "float16,float32,int32","format": "ND,ND,ND"}}

返回值说明

OpAICoreDef算子定义，OpAICoreDef请参考6.4.3.6 OpAICoreDef。

约束说明

无
