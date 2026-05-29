# SetInferDataType

> **Section**: 6.4.3.3.6  
> **PDF Pages**: 3779–3779  

---

<!-- page 3779 -->

## 6.4.3.3.6 SetInferDataType

功能说明

使用图模式时，需要调用该接口注册DataType推导函数。

函数原型

```cpp
OpDef &SetInferDataType(gert::OpImplRegisterV2::InferDataTypeKernelFunc func)
```

参数说明

参数输入/输出说明

func输入DataType推导函数。InferDataTypeKernelFunc类型定义如下：using InferDataTypeKernelFunc = UINT32 (*)(InferDataTypeContext *);

返回值说明

OpDef算子定义，OpDef请参考6.4.3.3 OpDef。

约束说明

无

## 6.4.3.3.7 AICore

功能说明

设置AICore的配置信息：包括Tiling处理回调函数、能力检查回调函数、基础的配置信息等。

函数原型

```cpp
OpAICoreDef &AICore(void)
```

参数说明

无

返回值说明

OpAICoreDef请参考6.4.3.6 OpAICoreDef。

约束说明

无
