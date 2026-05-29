# add_volatile

> **Section**: 6.4.1.4.17  
> **PDF Pages**: 3745–3745  

---

<!-- page 3745 -->

```cpp
ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const<char>::type, const char>));// Test const typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const<const int>::type, const int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const<const double>::type, const double>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const<const char>::type, const char>));
ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const_t<int>, const int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const_t<double>, const double>));
ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const_t<const int>, const int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::add_const_t<const double>, const double>));
```

## 6.4.1.4.17 add_volatile

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

在程序编译时，为指定类型添加volatile限定符，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct add_volatile;
```

参数说明

表6-1943模板参数说明

参数名含义

Tp需要处理的类型，包括基本类型（如int、float等）、复合类型（如数组、指针、引用）、用户自定义类型（如类、结构体等），以及带有volatile限定符的类型。

约束说明

无
