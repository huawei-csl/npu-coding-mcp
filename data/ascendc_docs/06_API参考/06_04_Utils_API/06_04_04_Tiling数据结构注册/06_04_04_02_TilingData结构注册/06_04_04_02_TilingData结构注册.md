# TilingData结构注册

> **Section**: 6.4.4.2  
> **PDF Pages**: 3839–3840  

---

<!-- page 3839 -->

●tiling结构体是全局属性，需注意应通过结构体名作为全局唯一标记，不同算子若注册同名不同结构tiling结构体则会发生未定义行为。

●注册中间结构体时，若中间结构体名为struct_name，则第一个参数固定为struct_name#Op。

●设置TILING_DATA_FIELD_DEF_ARR定义的字段值时，需注意set_{field_name}仅传入数组指针并按照宏中定义的数组长度进行赋值，因此，需用户自行保证传入数组指针指向的数组长度不小于宏中定义的数组长度，避免越界访问的问题。

调用示例

```cpp
#include "register/tilingdata_base.h"
```

// 定义tilingdata类namespace optiling {BEGIN_TILING_DATA_DEF(Matmul)  TILING_DATA_FIELD_DEF(uint16_t, mmVar);  TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);END_TILING_DATA_DEF;//注册中间结构体，第一个参数固定为struct_name#Op，第二个参数即struct_name, 如struct_name为Matmul，第一个参数为MatmulOp，第二个参数为MatmulREGISTER_TILING_DATA_CLASS(MatmulOp, Matmul)      //注册中间结构体

BEGIN_TILING_DATA_DEF(AddCustomTilingData)        // 注册一个tiling类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, blkDim);        // 添加tiling变量类型字段，参与计算核数  TILING_DATA_FIELD_DEF(uint32_t, totalSize);     // 添加tiling变量类型字段，总计算数据量  TILING_DATA_FIELD_DEF(uint32_t, splitTile);     // 添加tiling变量类型字段，每个core处理的数据分块计算  TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, arrSample);    // 添加tiling数组类型字段  TILING_DATA_FIELD_DEF_STRUCT(Matmul, mm);             // 添加tiling结构体类型字段END_TILING_DATA_DEF;                                    // 定义结束// 注册算子tilingdata类到对应的AddCustom算子REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData) }

// host侧设置参数值和使用tiling参数static void TilingAddInit(AddCustomTilingData *tiling, uint32_t numBlocks){  // 设置参数值  tiling->set_blkDim(numBlocks);                  // 置值通用数据类型变量numBlocks  uint16_t arr[] = {10,2,8,2,3,4,5,2,1,2,4,4,5,};  tiling->set_arrSample(arr);                    // 置值通用数据类型数组变量arrSample，仅会复制arr数据的前三个数据，与TILING_DATA_FIELD_DEF_ARR中arr_size一致  tiling->mm.set_mmVar(1);                       // 置值嵌套结构体通用数据类型变量mmVar  tiling->mm.set_mmArr(arr);                     // 置值嵌套结构体通用数据类型数组mmArr  // 使用参数值  uint32_t useNumBlocks = tiling->get_blkDim();    // 获取通用数据类型变量numBlocks  uint32_t* arrPoint = tiling->get_arrSample();   // 获取通用数据类型数组变量arrSample  useNumBlocks = tiling->mm.get_mmVar();           // 获取嵌套结构体通用数据类型变量mmVar  arrPoint = tiling->mm.get_mmArr();              // 获取嵌套结构体通用数据类型数组mmArr}

## 6.4.4.2 TilingData 结构注册

功能说明

注册定义的TilingData结构体并和自定义算子绑定。具体使用说明请参考调用示例。

函数原型

```cpp
#define REGISTER_TILING_DATA_CLASS(op_type, class_name)  class op_type##class_name##Helper {  public:    op_type##class_name##Helper() {
```

<!-- page 3840 -->

```cpp
CTilingDataClassFactory::RegisterTilingData(#op_type, op_type##class_name##Helper::CreateTilingDataInstance);    }    static std::shared_ptr<TilingDef> CreateTilingDataInstance() {      return std::make_shared<class_name>();    }  };
  op_type##class_name##Helper g_tilingdata_##op_type##class_name##helper;
```

参数说明

表6-1960参数说明

参数输入/输出说明

op_type输入注册的算子名

struct_name

输入tiling结构体名，与c++变量命名要求一致

约束说明

●使用时需要包含头文件register/tilingdata_base.h。

●中间结构体和定制tilingkey结构体需注意op_type命名规则，具体见调用示例。

●算子定制tilingkey结构体需保证必须注册op_type默认结构体。

●tiling结构体是全局属性，需注意应通过结构体名作为全局唯一标记，不同算子若注册同名不同结构tiling结构体则会发生未定义行为。

调用示例

●注册算子Tiling结构体#include "register/tilingdata_base.h"

// 定义tilingdata类namespace optiling {BEGIN_TILING_DATA_DEF(AddCustomTilingData)    // 注册一个tiling的类，以tiling的名字作为入参  TILING_DATA_FIELD_DEF(uint32_t, blkDim);    // 添加tiling字段，参与计算核数  TILING_DATA_FIELD_DEF(uint32_t, totalSize); // 添加tiling字段，总计算数据量-输入shape大小  TILING_DATA_FIELD_DEF(uint32_t, splitTile); // 添加tiling字段，每个core处理的数据分块计算END_TILING_DATA_DEF;                          // 定义结束// 注册算子tilingdata类到对应的AddCustom算子REGISTER_TILING_DATA_CLASS(AddCustom, AddCustomTilingData) }

●注册中间结构体。当用户有结构体嵌套场景时，嵌套的结构体称为中间结构体。因为一个算子名只能注册一个Tiling结构体，为使得框架能够检测中间结构体信息，需要构造“虚拟算子名”（结构体名+Op）并通过REGISTER_TILING_DATA_CLASS接口注册中间结构体，注册方式如下：BEGIN_TILING_DATA_DEF(Matmul)  TILING_DATA_FIELD_DEF(uint16_t, mmVar);  TILING_DATA_FIELD_DEF_ARR(uint16_t, 3, mmArr);END_TILING_DATA_DEF;//注册中间结构体，第一个参数固定为struct_name#Op，第二个参数即struct_name, 如struct_name为Matmul，第一参数为MatmulOp，第二个参数为MatmulREGISTER_TILING_DATA_CLASS(MatmulOp, Matmul)      //注册中间结构体

●定制tiling_key注册不同Tiling结构体/*REGISTER_TILING_DATA_CLASS中第一个参数为${op_type} + ‘_’ + tiling_key。若tiling_key未注册匹配的tiling结构体，则会使用默认的结构体。如下面两种方式，tiling_key不指定或者非1情况，tiling结构体
