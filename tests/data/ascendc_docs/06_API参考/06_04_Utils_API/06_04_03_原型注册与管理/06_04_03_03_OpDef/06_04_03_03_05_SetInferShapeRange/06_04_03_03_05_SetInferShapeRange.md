# SetInferShapeRange

> **Section**: 6.4.3.3.5  
> **PDF Pages**: 3778–3778  

---

<!-- page 3778 -->

函数原型

```cpp
OpDef &SetInferShape(gert::OpImplRegisterV2::InferShapeKernelFunc func)
```

参数说明

参数输入/输出说明

func输入Shape推导函数。InferShapeKernelFunc类型定义如下：using InferShapeKernelFunc = UINT32 (*)(InferShapeContext *);

返回值说明

OpDef算子定义，OpDef请参考6.4.3.3 OpDef。

约束说明

无

## 6.4.3.3.5 SetInferShapeRange

功能说明

使用图模式时，需要调用该接口注册ShapeRange推导函数。

函数原型

```cpp
OpDef &SetInferShapeRange(gert::OpImplRegisterV2::InferShapeRangeKernelFunc func)
```

参数说明

参数输入/输出说明

func输入ShapeRange推导函数。InferShapeRangeKernelFunc类型定义如下：using InferShapeRangeKernelFunc = UINT32 (*)(InferShapeRangeContext *);

返回值说明

OpDef算子定义，OpDef请参考6.4.3.3 OpDef。

约束说明

无
