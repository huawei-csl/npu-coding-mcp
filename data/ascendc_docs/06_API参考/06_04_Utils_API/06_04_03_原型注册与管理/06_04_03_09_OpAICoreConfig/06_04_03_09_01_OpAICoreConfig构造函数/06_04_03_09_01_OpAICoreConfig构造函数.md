# OpAICoreConfig构造函数

> **Section**: 6.4.3.9.1  
> **PDF Pages**: 3826–3826  

---

<!-- page 3826 -->

返回值说明

OpHostCPUDef算子定义，OpHostCPUDef请参考6.4.3.8 OpHostCPUDef。

约束说明

无

## 6.4.3.9 OpAICoreConfig

## 6.4.3.9.1 OpAICoreConfig 构造函数

功能说明

OpAICoreConfig构造函数。

函数原型

```cpp
OpAICoreConfig()OpAICoreConfig(const char *soc)
```

参数说明

参数名输入/输出描述

soc输入AI处理器型号。

返回值说明

无

约束说明

传入soc入参的构造函数会对OpAICoreConfig结构中的部分参数进行初始化，具体的参数和初始化值如下表所示：

配置参数说明初始化值

**DynamicCompileStaticFlag**

用于标识该算子实现是否支持入图时的静态Shape编译。

true

**DynamicFormatFlag**

标识是否根据6.4.3.6.3 SetOpSelectFormat设置的函数自动推导算子输入输出支持的dtype和format。

true

**DynamicRankSupportFlag**

标识算子是否支持dynamicRank（动态维度）。true
