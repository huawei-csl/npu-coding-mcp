# add_rvalue_reference

> **Section**: 6.4.1.4.21  
> **PDF Pages**: 3750–3751  

---

<!-- page 3750 -->

约束说明

无

返回值说明

add_lvalue_reference是一个结构体，其提供一个嵌套类型type，表示添加左值引用限定符后的类型。通过add_lvalue_reference<Tp>::type来访问该类型。

调用示例

```cpp
// Test basic typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<int>, int&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<float>, float&>));
// Test pointer typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<int*>, int*&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<const int*>, const int*&>));
// Test reference typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<int&>, int&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<int&&>, int&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<const int&>, const int&>));
// Test void typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<void>, void>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<const void>, const void>));
// Test function typeusing FuncType = void();ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<FuncType>, FuncType&>));
// Test array typeusing ArrayType = int[];ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<ArrayType>, ArrayType&>));
// Test class typeclass MyClass {};ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<MyClass>, MyClass&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_lvalue_reference_t<const MyClass>, const MyClass&>));
```

## 6.4.1.4.21 add_rvalue_reference

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

<!-- page 3751 -->

功能说明

在程序编译时，为指定类型添加右值引用限定符，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct add_rvalue_reference;
```

参数说明

表6-1947模板参数说明

参数名含义

Tp需要处理的类型，包括基本类型（如int、float等）、复合类型（如数组、指针）、用户自定义类型（如类、结构体等），以及带有引用限定符的类型。

约束说明

无

返回值说明

add_rvalue_reference是一个结构体，其提供一个嵌套类型type，表示添加右值引用限定符后的类型。通过add_rvalue_reference<Tp>::type来访问该类型。

调用示例

```cpp
// Test basic typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<int>, int&&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<float>, float&&>));
// Test pointer typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<int*>, int*&&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<const int*>, const int*&&>));
// Test reference typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<int&>, int&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<int&&>, int&&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<const int&>, const int&>));
// Test void typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<void>, void>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<const void>, const void>));
// Test function typeusing FuncType = void();ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<FuncType>, FuncType&&>));
// Test array typeusing ArrayType = int[];ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<ArrayType>, ArrayType&&>));
// Test class typeclass MyClass {};ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<MyClass>, MyClass&&>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_rvalue_reference_t<const MyClass>, const MyClass&&>));
```
