# is_reference

> **Section**: 6.4.1.4.9  
> **PDF Pages**: 3734–3734  

---

<!-- page 3734 -->

## 6.4.1.4.9 is_reference

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

在程序编译时，检测一个类型是否为引用类型，可以用于在编译时进行类型检查和条件处理。

函数原型

```cpp
template <typename Tp>struct is_reference;
```

参数说明

表6-1935模板参数说明

参数名含义

Tp需要检测的类型，包括基本类型（如int、float等）、复合类型（如数组、指针）、用户自定义类型（如类、结构体等），以及引用类型本身。

约束说明

无

返回值说明

is_reference的静态常量成员value用于获取返回的布尔值，is_reference<Tp>::value取值如下：

●true：Tp是引用类型。

●false：Tp不是引用类型。
