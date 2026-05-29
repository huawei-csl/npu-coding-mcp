# GET_TILING_DATA_WITH_STRUCT

> **Section**: 6.2.3.14.2  
> **PDF Pages**: 1979–1979  

---

<!-- page 1979 -->

tiling.set_blkDim(numBlocks);  // 与算子host实现中定义TilingData结构体中的成员的对应    tiling.set_totalSize(totalSize);    tiling.set_splitTile(splitTile);    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());    ...    // 其他代码逻辑}

## 6.2.3.14.2 GET_TILING_DATA_WITH_STRUCT

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

使用该接口指定结构体名称，可获取指定的tiling信息，并填入对应的Tiling结构体中，此函数会以宏展开的方式进行编译。与6.2.3.14.1 GET_TILING_DATA的区别是：6.2.3.14.1 GET_TILING_DATA只能获取默认注册的结构体，该接口可以根据指定的结构体名称获取对应的结构体，常用于针对不同的TilingKey注册了不同结构体的情况下。

函数原型

```cpp
GET_TILING_DATA_WITH_STRUCT(struct_name, tiling_data, tiling_arg)
```

参数说明

参数输入/输出说明

struct_name

输入指定的结构体名称。

tiling_data输出返回指定Tiling结构体变量。

tiling_arg输入此参数为算子入口函数处传入的tiling参数。
