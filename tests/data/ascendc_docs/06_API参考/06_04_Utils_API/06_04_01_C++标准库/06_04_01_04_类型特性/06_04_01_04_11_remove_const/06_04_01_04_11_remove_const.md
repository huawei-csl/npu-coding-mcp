# remove_const

> **Section**: 6.4.1.4.11  
> **PDF Pages**: 3737–3737  

---

<!-- page 3737 -->

```cpp
AscendC::Std::is_const::value:0AscendC::Std::is_const::value:0AscendC::Std::is_const::value:0AscendC::Std::is_const::value:0AscendC::Std::is_const::value:0AscendC::Std::is_const::value:0AscendC::Std::is_const::value:1AscendC::Std::is_const::value:1AscendC::Std::is_const::value:1AscendC::Std::is_const::value:1AscendC::Std::is_const::value:1AscendC::Std::is_const::value:1
```

## 6.4.1.4.11 remove_const

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

在程序编译时，对传入的模板参数类型移除const限定符，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct remove_const;
```

参数说明

表6-1937模板参数说明

参数名含义

Tp需要处理的类型，包括基本类型（如int、float等）、复合类型（如数组、指针、引用）、用户自定义类型（如类、结构体等），以及const限定的类型。
