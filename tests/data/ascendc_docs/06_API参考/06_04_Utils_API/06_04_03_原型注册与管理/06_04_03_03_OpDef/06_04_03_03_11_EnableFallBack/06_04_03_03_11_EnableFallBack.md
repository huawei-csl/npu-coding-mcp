# EnableFallBack

> **Section**: 6.4.3.3.11  
> **PDF Pages**: 3781–3781  

---

<!-- page 3781 -->

函数原型

```cpp
OpMC2Def &MC2(void)
```

参数说明

无

返回值说明

**OpMC2Def结构，后续可通过该结构配置通信域名称。**

约束说明

基于旧版本CANN包（不支持MC2特性）生成的自定义算子工程，无法兼容MC2接口。在使用非当前版本CANN包生成的自定义算子工程时，需特别注意兼容性问题。您可以通过查看自定义算子工程下cmake/util/ascendc_impl_build.py中有无_build_mc2_ctx字段来确认当前工程是否支持该特性，如果未找到该字段，则需要重新生成自定义算子工程以启用MC2特性。

## 6.4.3.3.11 EnableFallBack

功能说明

通过本接口启用fallback配置，启用后将自动生成一个fallback函数并注册给GE。fallback函数的核心逻辑是将GE的输入、输出及属性转换为aclnn单算子API所需的参数格式，随后调用aclnn接口。动态图场景下，GE可直接调用fallback函数（函数中调用了aclnn接口），从而简化调度流程。关于fallback下发算子的详细介绍请参考《图开发》中的“编程指南 > 自定义算子入图 > 基于fallback形式下发算子”章节。

函数原型

```cpp
OpDef &EnableFallBack(void)
```

参数说明

无

返回值说明

OpDef算子定义，OpDef请参考6.4.3.3 OpDef。

约束说明

●算子需要注册并实现InferShape函数。

●算子需要注册并实现InferDataType函数。

调用示例

```cpp
class AddCustom : public OpDef {public:    AddCustom(const char* name) : OpDef(name)    {        this->Input("x").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND});
        this->Input("y").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND});
        this->Output("z").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND})
```
