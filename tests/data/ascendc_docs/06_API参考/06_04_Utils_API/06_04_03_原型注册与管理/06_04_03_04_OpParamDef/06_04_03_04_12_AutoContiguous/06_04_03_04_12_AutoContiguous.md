# AutoContiguous

> **Section**: 6.4.3.4.12  
> **PDF Pages**: 3798–3798  

---

<!-- page 3798 -->

函数原型

```cpp
OpParamDef &IgnoreContiguous(void)
```

参数说明

无

返回值说明

OpParamDef算子定义，OpParamDef请参考6.4.3.4 OpParamDef。

约束说明

无

## 6.4.3.4.12 AutoContiguous

功能说明

配置该参数，当单算子API（aclnnxxx）接口中的输入（aclTensor类型）是非连续tensor时，框架会自动将其转换为连续tensor。

该接口仅在如下场景支持：

●通过单算子API执行的方式开发单算子调用应用。

●间接调用单算子API(aclnnxxx)接口：Pytorch框架单算子直调的场景。

函数原型

```cpp
OpParamDef &AutoContiguous()
```

参数说明

无

返回值说明

OpParamDef算子定义，OpParamDef请参考6.4.3.4 OpParamDef。

约束说明

无

## 6.4.3.4.13 Scalar

功能说明

配置该参数后，自动生成的单算子API（aclnnxxx）接口中，输入类型为aclScalar类型。

函数原型

```cpp
OpParamDef &Scalar()
```
