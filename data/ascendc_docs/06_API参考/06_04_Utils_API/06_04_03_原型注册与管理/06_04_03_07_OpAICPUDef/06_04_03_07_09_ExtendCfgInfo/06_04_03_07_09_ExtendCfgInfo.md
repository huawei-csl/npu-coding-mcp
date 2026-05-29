# ExtendCfgInfo

> **Section**: 6.4.3.7.9  
> **PDF Pages**: 3821–3821  

---

<!-- page 3821 -->

约束说明

无

## 6.4.3.7.9 ExtendCfgInfo

功能说明

为AICPU自定义算子额外添加一组键值对形式的扩展配置。

函数原型

```cpp
OpAICPUDef &ExtendCfgInfo(const char *key, const char *value)
```

参数说明

参数输入/输出说明

key输入扩展配置的“键名”，配置项的名称。

value输入扩展配置的“值”，对应键名的配置内容。

返回值说明

OpAICPUDef算子定义，OpAICPUDef请参考6.4.3.7 OpAICPUDef。

约束说明

无

## 6.4.3.8 OpHostCPUDef

## 6.4.3.8.1 Engine

功能说明

配置算子调用的引擎，入参固定为“DNN_VM_HOST_CPU”。

函数原型

```cpp
OpHostCPUDef &Engine(const char *value)
```

参数说明

参数输入/输出说明

value输入配置算子调用的引擎名称。
