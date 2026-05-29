# FunctionName

> **Section**: 6.4.3.7.7  
> **PDF Pages**: 3820–3820  

---

<!-- page 3820 -->

## 6.4.3.7.7 FunctionName

功能说明

配置自定义算子调用的kernel函数接口名称，functionName固定为“RunCpuKernel”。

函数原型

```cpp
OpAICPUDef &FunctionName(const char *value)
```

参数说明

参数输入/输出说明

value输入算子调用的kernel函数接口名称，functionName固定为“RunCpuKernel”。

返回值说明

OpAICPUDef算子定义，OpAICPUDef请参考6.4.3.7 OpAICPUDef。

约束说明

无

## 6.4.3.7.8 UserDefined

功能说明

配置该算子是否为用户自定义算子，AICPU自定义算子的userDefined仅支持配置为“True”，若开发者没有配置的情况下，该参数会被默认设置为“True”。

函数原型

```cpp
OpAICPUDef &UserDefined(bool flag)
```

参数说明

参数输入/输出说明

flag输入AICPU自定义算子的userDefined仅支持配置为“True”，若开发者没有配置的情况下，该参数会被默认设置为“True”。

返回值说明

OpAICPUDef算子定义，OpAICPUDef请参考6.4.3.7 OpAICPUDef。
