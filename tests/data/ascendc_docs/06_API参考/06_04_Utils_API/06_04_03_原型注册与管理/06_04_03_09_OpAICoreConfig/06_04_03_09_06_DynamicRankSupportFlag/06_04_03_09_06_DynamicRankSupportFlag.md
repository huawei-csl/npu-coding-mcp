# DynamicRankSupportFlag

> **Section**: 6.4.3.9.6  
> **PDF Pages**: 3830–3830  

---

<!-- page 3830 -->

函数原型

```cpp
OpAICoreConfig &DynamicFormatFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入标记是否自动推导算子输入输出的dtype和format。

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无

调用示例

请参考6.4.3.6.3 SetOpSelectFormat节调用示例。

## 6.4.3.9.6 DynamicRankSupportFlag

功能说明

标识算子是否支持dynamicRank（动态维度）。

函数原型

```cpp
OpAICoreConfig &DynamicRankSupportFlag(bool flag)
```

参数说明

参数输入/输出说明

flag输入●true：表示算子支持dynamic rank，算子支持shape包含（-2），用于判断是否进行动态编译；

●false：表示算子不支持dynamic rank。

返回值说明

OpAICoreConfig类，请参考6.4.3.9 OpAICoreConfig。

约束说明

无
