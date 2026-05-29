# PrecisionReduceFlag

> **Section**: 6.4.3.9.9  
> **PDF Pages**: 3832–3833  

---

<!-- page 3832 -->

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无

调用示例

请参考6.4.3.6.2 SetCheckSupport节调用示例。

## 6.4.3.9.9 PrecisionReduceFlag

功能说明

此字段用于进行ATC模型转换或者进行网络调测时，控制算子的精度模式。只有当精度模式("precision_mode")配置为混合精度("allow_mix_precision")前提下生效。

函数原型

```cpp
OpAICoreConfig& PrecisionReduceFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入●若配置为"false"，则认为是黑名单，算子必须保持算子本身的原始数据类型。

●若配置为"true"，则认为是白名单，如果算子既支持float32又支持float16数据类型，同时算子的原图格式是float32或者float16的情况下，优先为算子选择float16数据类型。

●若未配置这个字段，则认为是灰名单，在有上一个算子的情况下，选择和上一个算子相同的数据类型，否则选择当前算子的原始数据类型。

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无

## 6.4.3.9.10 ExtendCfgInfo

功能说明

用于扩展算子相关参数配置，提供更灵活的参数配置能力。

<!-- page 3833 -->

函数原型

```cpp
OpAICoreConfig &OpAICoreConfig::ExtendCfgInfo(const char *key, const char *value)
```

参数说明

表6-1954参数说明

参数输入/输出说明

key输入配置项，如“aclnnSupport.value”。

value输入配置项key对应的取值，如“aclnnSupport.value”，可以填充“support_aclnn”或者“aclnn_only”。

ExtendCfgInfo支持的参数如下表：

表6-1955 ExtendCfgInfo 支持配置的参数

参数功能介绍

aclnnSupport.value

●support_aclnn：此模式下，静态Shape场景中该算子通过模型下沉执行，动态Shape场景则在Host侧调用fallback函数下发算子。如果调用了EnableFallBack则默认采用该模式。// 如下为动态Shape场景的示例OpAICoreConfig aicore_config;aicore_config.DynamicShapeSupportFlag(true)   // 动态Shape场景需要设置DynamicShapeSupportFlag为true             .ExtendCfgInfo("aclnnSupport.value", "support_aclnn");this->AICore().AddConfig("ascendxxx", aicore_config);

// 如下为静态Shape场景的示例OpAICoreConfig aicore_config;aicore_config.DynamicCompileStaticFlag(true)  // 静态Shape场景需要设置DynamicCompileStaticFlag为true             .ExtendCfgInfo("aclnnSupport.value", "support_aclnn");this->AICore().AddConfig("ascendxxx", aicore_config);

●aclnn_only：此模式下，动静态Shape场景中该算子均以fallback形式下发。不建议用户使用该模式，后续版本待废弃。// 如下为动态Shape场景的示例OpAICoreConfig aicore_config;aicore_config.DynamicShapeSupportFlag(true) // 动态Shape场景需要设置DynamicShapeSupportFlag为true             .ExtendCfgInfo("aclnnSupport.value", "aclnn_only");this->AICore().AddConfig("ascendxxx", aicore_config);// 如下为静态Shape场景的示例OpAICoreConfig aicore_config;              // 无需配置DynamicCompileStaticFlag/DynamicShapeSupportFlag，算子均以fallback形式下发，即动态Shape模型的下发方式aicore_config.ExtendCfgInfo("aclnnSupport.value", "aclnn_only");this->AICore().AddConfig("ascendxxx", aicore_config);

关于fallback下发算子的详细介绍请参考《图开发》中的“编程指南> 自定义算子入图 > 基于fallback形式下发算子”章节。
