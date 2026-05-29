# UserDefined

> **Section**: 6.4.3.8.8  
> **PDF Pages**: 3825–3825  

---

<!-- page 3825 -->

约束说明

无

## 6.4.3.8.8 UserDefined

功能说明

配置该算子是否为用户自定义算子，HostCPU自定义算子的userDefined仅支持配置为“True”，若开发者没有配置的情况下，该参数会被默认设置为“True”。

函数原型

```cpp
OpHostCPUDef &UserDefined(bool flag)
```

参数说明

参数输入/输出说明

flag输入HostCPU自定义算子的userDefined仅支持配置为“True”，若开发者没有配置的情况下，该参数会被默认设置为“True”。

返回值说明

OpHostCPUDef算子定义，OpHostCPUDef请参考6.4.3.8 OpHostCPUDef。

约束说明

无

## 6.4.3.8.9 ExtendCfgInfo

功能说明

为HostCPU自定义算子额外添加一组键值对形式的扩展配置。

函数原型

```cpp
OpHostCPUDef &ExtendCfgInfo(const char *key, const char *value)
```

参数说明

参数输入/输出说明

key输入扩展配置的“键名”，配置项的名称。

value输入扩展配置的“值”，对应键名的配置内容。
