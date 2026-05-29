# add_lvalue_reference

> **Section**: 6.4.1.4.20  
> **PDF Pages**: 3749–3749  

---

<!-- page 3749 -->

```cpp
// Test void typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<void>::type, void*>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<const void>::type, const void*>));
// Test reference typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<int&>::type, int*>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<const int&>::type, const int*>));
// Test function typeusing FuncType = void();ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<FuncType>::type, FuncType*>));
// Test array typeusing ArrayType = int[];ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<ArrayType>::type, ArrayType*>));// Test pointer typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_pointer<int*>::type, int**>));
```

## 6.4.1.4.20 add_lvalue_reference

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

在程序编译时，为指定类型添加左值引用限定符，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct add_lvalue_reference;
```

参数说明

表6-1946模板参数说明

参数名含义

Tp需要处理的类型，包括基本类型（如int、float等）、复合类型（如数组、指针）、用户自定义类型（如类、结构体等），以及带有引用限定符的类型。
