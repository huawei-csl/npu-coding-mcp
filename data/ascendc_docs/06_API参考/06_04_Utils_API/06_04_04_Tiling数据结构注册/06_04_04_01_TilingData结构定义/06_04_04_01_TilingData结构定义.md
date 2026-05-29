# TilingData结构定义

> **Section**: 6.4.4.1  
> **PDF Pages**: 3837–3838  

---

<!-- page 3837 -->

参数说明

参数输入/输出说明

def输入被拷贝的OpMC2Def类对象。

返回值说明

拷贝后的结果对象的引用。

约束说明

无。

## 6.4.4 Tiling 数据结构注册

## 6.4.4.1 TilingData 结构定义

功能说明

定义一个TilingData的类，添加所需的成员变量（TilingData字段），用于保存所需TilingData参数。完成该TilingData类的定义后，该类通过继承TilingDef类（用来存放、处理用户自定义Tiling结构体成员变量的基类）提供以下接口：

●set_{field_name}接口：用于设置TilingData类的字段值，field_name为定义TilingData类时添加的字段名。

●get_{field_name}接口：用于获取字段名为field_name的字段值。

●SaveToBuffer接口：完成TilingData的序列化和保存。

●GetDataSize接口：获取TilingData的长度。

●CheckAlignAndGenPlaceHolder：该接口是内部关联接口，用于框架侧检查Tiling结构体中成员变量是否满足字节对齐要求，并对不对齐的变量进行补齐，开发者无需关注。

●SetDataPtr接口：该接口为预留接口，开发者无需关注。

函数原型

●定义一个TilingData类BEGIN_TILING_DATA_DEF(class_name)

●添加通用数据类型的TilingData字段TILING_DATA_FIELD_DEF(data_type, field_name)

●添加数组类型的TilingData字段，数组的元素数据类型为通用数据类型TILING_DATA_FIELD_DEF_ARR(arr_type, arr_size, field_name)

●添加结构体类型的TilingData字段TILING_DATA_FIELD_DEF_STRUCT(struct_type, field_name)

●定义结束END_TILING_DATA_DEF

<!-- page 3838 -->

参数说明

表6-1956BEGIN_TILING_DATA_DEF 参数说明

参数输入/输出说明

class_name输入用户定义tiling结构体名，与c++变量命名要求一致

表6-1957TILING_DATA_FIELD_DEF 参数说明

参数输入/输出说明

data_type输入字段的数据类型

field_name输入字段名，与c++变量命名要求一致

表6-1958TILING_DATA_FIELD_DEF_ARR 参数说明

参数输入/输出说明

arr_type输入数组元素数据类型

arr_size输入数组元素个数

field_name输入字段名，与c++变量命名要求一致

表6-1959TILING_DATA_FIELD_DEF_STRUCT 参数说明

参数输入/输出说明

struct_type输入结构体类型

field_name输入字段名，与c++变量命名要求一致

约束说明

●使用时需要包含头文件register/tilingdata_base.h。

●TILING_DATA_FIELD_DEF和TILING_DATA_FIELD_DEF_ARR中定义的变量，仅支持int8_t, uint8_t, int16_t, uint16_t, int32_t, uint32_t, int64_t, uint64_t, float数据类型。

●TILING_DATA_FIELD_DEF_STRUCT中struct_type仅支持用BEGIN_TILING_DATA_DEF等定义的tiling结构体，不支持直接使用c++语法定义的结构体类型。

●用户在host侧设置参数值和使用tiling数据需要使用set_xxx和get_xxx接口（xxx请替换为字段名），具体使用方法见调用示例。

●tiling数据成员需要满足字节对齐要求，即：当前数据成员dataVar位于结构体的偏移offset满足， offset % sizeof(dataVar) == 0。
