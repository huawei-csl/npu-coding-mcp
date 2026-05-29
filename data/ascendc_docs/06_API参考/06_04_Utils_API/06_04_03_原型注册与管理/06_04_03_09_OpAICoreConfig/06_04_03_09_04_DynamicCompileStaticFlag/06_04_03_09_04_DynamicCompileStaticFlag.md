# DynamicCompileStaticFlag

> **Section**: 6.4.3.9.4  
> **PDF Pages**: 3829–3829  

---

<!-- page 3829 -->

调用示例

```cpp
class AddCustom : public OpDef {public:    AddCustom(const char* name) : OpDef(name)    {        this->Input("x").DataType({ ge::DT_FLOAT16 }).ParamType(OPTIONAL);
        this->Output("y").DataType({ ge::DT_FLOAT16 });
        OpAICoreConfig aicConfig1;
        OpAICoreConfig aicConfig2;
        aicConfig1.Output("y")            .ParamType(OPTIONAL)            .DataType({ ge::DT_FLOAT })            .Format({ ge::FORMAT_ND });
        aicConfig2.Output("y")            .ParamType(REQUIRED)            .DataType({ ge::DT_INT32 })            .Format({ ge::FORMAT_ND });
        this->AICore().AddConfig("ascendxxx1", aicConfig1);
        this->AICore().AddConfig("ascendxxx2", aicConfig2);    }};
```

## 6.4.3.9.4 DynamicCompileStaticFlag

功能说明

用于标识该算子实现是否支持入图时的静态Shape编译。

函数原型

```cpp
OpAICoreConfig &DynamicCompileStaticFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入用户开发的自定义算子，如果需要支持入图时静态Shape场景下的编译，需要配置该选项为true，否则配置为false。

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无

## 6.4.3.9.5 DynamicFormatFlag

功能说明

标识是否根据6.4.3.6.3 SetOpSelectFormat设置的函数自动推导算子输入输出支持的dtype和format。设置为“true”，则无需在原型注册时配置固定的dtype与format，会调用推导函数来推导算子输入输出支持的dtype和format。
