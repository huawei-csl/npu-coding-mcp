# HcclServerType

> **Section**: 6.4.3.10.4  
> **PDF Pages**: 3835–3835  

---

<!-- page 3835 -->

参数说明

参数输入/输出说明

value输入配置的通信域名称。单个通信域使用const char *，多通信域使用std::vector<const char *>。

约束说明

使用该接口前，算子需要先通过6.4.3.3.10 MC2接口注册该算子是通算融合算子，注册后即返回一个OpMC2Def结构。

通信域名称必须先配置为REQUIRED String类型的属性，属性名即为通信域名称。

调用示例

class MC2Custom : public OpDef {public:    MC2Custom(const char* name) : OpDef(name)    {        this->Input("x").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND});        this->Input("y").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND});        this->Output("z").ParamType(REQUIRED).DataType({ge::DT_FLOAT}).Format({ge::FORMAT_ND});        this->Attr("group").AttrType(REQUIRED).String();        this->AICore().AddConfig("ascendxxx");        this->MC2().HcclGroup("group"); // 配置通信域名称为group    }};OP_ADD(MC2Custom);

## 6.4.3.10.4 HcclServerType

功能说明

配置HCCL的服务端类型。

函数原型

```cpp
void HcclServerType(enum HcclServerType type, const char *soc=nullptr)
```

参数说明

参数输入/输出说明

type输入HCCL的服务端类型，类型为HcclServerType枚举类，定义如下：namespace ops{enum HcclServerType : uint32_t {    AICPU = 0,  // AI CPU服务端    AICORE, // AI Core服务端    CCU,    // CCU服务端，仅在AI处理器包含CCU单元时支持    MAX     // 预留参数，不支持使用};}
