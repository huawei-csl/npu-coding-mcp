# remove_reference

> **Section**: 6.4.1.4.14  
> **PDF Pages**: 3741–3741  

---

<!-- page 3741 -->

## 6.4.1.4.14 remove_reference

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

在程序编译时，从给定类型中移除引用限定符，包括左值引用T&和右值引用T&&，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct remove_reference;
```

参数说明

表6-1940模板参数说明

参数名含义

Tp需要处理的类型，包括基本类型（如int、float等）、复合类型（如数组、指针）、用户自定义类型（如类、结构体等），以及带有左值引用&或右值引用&&限定的类型。

约束说明

无

返回值说明

remove_reference是一个结构体，其提供一个嵌套类型type，表示移除引用限定符后的类型。通过remove_reference<Tp>::type来访问该类型。

调用示例

```cpp
// Test non-reference typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_reference<int>::type, int>));
```
