# OutputShapeDependOnCompute

> **Section**: 6.4.3.4.18  
> **PDF Pages**: 3804–3804  

---

<!-- page 3804 -->

约束说明

●InitValue和SetNeedAtomic接口配合使用，否则会出现初始化不生效的情况。

●针对OpParamDef &InitValue(uint64_t value)接口，算子输出参数的数据类型支持范围如下：UINT64/INT64/UINT32/INT32/UINT16/INT16/UINT8/INT8/FLOAT32/FLOAT16，超出该范围为未定义行为。

●针对OpParamDef &InitValue(const std::vector<ScalarVar> &value)接口输入value的size需要与输出参数配置的DataType或DataTypeList接口参数的size一致。同时，相同数据类型需保证设置的类型和值相同，否则将会报错。

●对于同一个输出参数仅支持调用一种接口设置初值，调用多种InitValue接口为未定义行为；多次调用同一种接口以最后一次调用设置的初值为准。

●基于旧版本CANN包（不支持InitValue特性）生成的自定义算子工程，无法兼容InitValue接口。在使用非当前版本CANN包生成的自定义算子工程时，需特别注意兼容性问题。您可以通过查看自定义算子工程下cmake/util/ascendc_impl_build.py中有无output_init_value字段来确认当前工程是否支持该特性，如果未找到该字段，则需要重新生成自定义算子工程以启用InitValue特性。

调用示例

// OpParamDef &InitValue(uint64_t value)示例this->Output("z")     .ParamType(REQUIRED)     .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})     .FormatList({ ge::FORMAT_ND})     .InitValue(0);

// OpParamDef &InitValue(const ScalarVar &value)示例this->Output("z")     .ParamType(REQUIRED)     .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})     .FormatList({ ge::FORMAT_ND})     .InitValue({ScalarType::INT16, 1});

// OpParamDef &InitValue(const std::vector<ScalarVar> &value)示例this->Output("z")     .ParamType(REQUIRED)     .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})     .FormatList({ ge::FORMAT_ND})     .InitValue({{ScalarType::INT16, 1}, {ScalarType::FLOAT32, 3.2}, {ScalarType::INT64, 7}});

this->Output("z")     .ParamType(REQUIRED)     .DataType({ge::DT_INT32, ge::DT_FLOAT, ge::DT_INT32})  // 第一个和第三个DataType相同     .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_NHWC})     .InitValue({{ScalarType::INT16, 1}, {ScalarType::FLOAT32, 3.2}, {ScalarType::INT16, 1}}); // InitValue对应的数据类型和数值也需相同

## 6.4.3.4.18 OutputShapeDependOnCompute

功能说明

标识算子输出的shape是否依赖于计算得到。某些算子，比如NonZero（统计tensor中非零值的个数），计算完成前无法得知算子输出的shape信息，算子计算完成后才能获取。该类算子在原型定义时，需要使用OutputShapeDependOnCompute接口进行标识，同时在算子核函数中将实际输出shape写入到出参中，便于框架侧基于该信息进行输出内存的管理。对应的kernel侧实现请参考输出shape依赖计算的算子kernel实现。
