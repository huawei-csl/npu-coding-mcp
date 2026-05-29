# IgnoreContiguous

> **Section**: 6.4.3.4.11  
> **PDF Pages**: 3797–3797  

---

<!-- page 3797 -->

函数原型

```cpp
OpParamDef &ValueDepend(Option value_depend)OpParamDef &ValueDepend(Option value_depend, DependScope scope)
```

参数说明

参数输入/输出说明

value_depend

输入value_depend有以下两种取值：

●REQUIRED：表示算子的输入必须是Const类型。在调用算子的6.4.3.6.2 SetCheckSupport时，会校验算子的输入是否是Const类型。若校验通过，则将此输入的值下发到算子；否则报错。

●OPTIONAL：表示算子的输入可以是Const类型，也可以不是Const类型。如果输入是Const类型，则将输入的值下发到算子，否则不下发。

scope输入scope类型为枚举类型DependScope，支持的取值为：

●ALL：指在Tiling/InferShape等函数实现时都依赖该输入的具体数据，行为与调用单参数ValueDepend重载接口一致。

●TILING：指仅在Tiling时依赖Tensor的值，可以支持Tiling下沉。

返回值说明

OpParamDef算子定义，OpParamDef请参考6.4.3.4 OpParamDef。

约束说明

仅支持对算子输入配置，输入的参数数据类型可以配置为DT_FLOAT/DT_BOOL/DT_INT64/DT_UINT64/DT_INT32/DT_UINT32/DT_INT16/DT_UINT16/DT_INT8/DT_UINT8，且必须满足以下三种情况之一：

1. 输入的参数数据类型配置全为DT_FLOAT，对应生成的输出类型aclFloatArray（aclnn数据类型）。

2. 输入的参数数据类型配置全为DT_BOOL，对应生成的输出类型aclBoolArray（aclnn数据类型）。

3. 输入的参数数据类型配置全为整数类型，即DT_INT64/DT_UINT64/DT_INT32/DT_UINT32/DT_INT16/DT_UINT16/DT_INT8/DT_UINT8，对应生成的输出类型aclIntArray（aclnn数据类型）。当数据类型配置含有DT_INT64以外的数据类型时，需要增加一组DT_INT64对应的输入/输出数据类型组合。

## 6.4.3.4.11 IgnoreContiguous

功能说明

某些算子支持非连续的tensor，在算子的实现中对非连续的tensor做了转换处理。配置该参数后，框架会忽略对非连续的校验。
