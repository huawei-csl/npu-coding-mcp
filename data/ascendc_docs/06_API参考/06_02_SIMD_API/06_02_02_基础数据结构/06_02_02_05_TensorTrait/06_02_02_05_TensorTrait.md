# TensorTrait

> **Section**: 6.2.2.5  
> **PDF Pages**: 867–878  

---

<!-- page 867 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

判断输入的数据结构是否为Layout数据结构，可通过检查其成员常量value的值来判断。当value为true时，表示输入的数据结构是Layout类型；反之则为非Layout类型。

函数原型

```cpp
template <typename T> struct is_layout
```

参数说明

表6-81模板参数说明

参数名描述

T根据输入的数据类型，判断是否为Layout数据结构。

返回值说明

无

约束说明

无

调用示例

// 初始化Layout数据结构并判断其类型AscendC::Shape<int,int,int> shape = AscendC::MakeShape(10, 20, 30);AscendC::Stride<int,int,int> stride = AscendC::MakeStride(1, 100, 200);

```cpp
auto layoutMake = AscendC::MakeLayout(shape, stride);AscendC::Layout<AscendC::Shape<int, int, int>, AscendC::Stride<int, int, int>> layoutInit(shape, stride);
bool value = AscendC::is_layout<decltype(shape)>::value; //value = falsevalue = AscendC::is_layout<decltype(stride)>::value; //value = false
value = AscendC::is_layout<decltype(layoutMake)>::value;//value = truevalue = AscendC::is_layout<decltype(layoutInit)>::value;//value = true
```

## 6.2.2.5 TensorTrait

