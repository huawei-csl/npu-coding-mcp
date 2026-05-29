# DynamicShapeSupportFlag

> **Section**: 6.4.3.9.7  
> **PDF Pages**: 3831–3831  

---

<!-- page 3831 -->

## 6.4.3.9.7 DynamicShapeSupportFlag

功能说明

用于标识该算子是否支持入图时的动态Shape场景。

函数原型

```cpp
OpAICoreConfig &DynamicShapeSupportFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入●true：表示算子支持入图时的动态Shape场景。

●false：表示算子不支持入图时的动态Shape场景。

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无

## 6.4.3.9.8 NeedCheckSupportFlag

功能说明

标识是否在算子融合阶段调用算子参数校验函数进行data type与shape的校验。

●若配置为"true"，框架会调用通过6.4.3.6.2 SetCheckSupport设置的算子参数校验函数，检查算子是否支持指定输入，此场景下需要自行实现算子参数校验的回调函数。

●若配置为"false"，表示不需要进行校验。

函数原型

```cpp
OpAICoreConfig &NeedCheckSupportFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入标识是否在算子融合阶段调用算子参数校验函数进行data type与shape的校验。
