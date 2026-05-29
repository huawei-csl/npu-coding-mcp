# is_convertible

> **Section**: 6.4.1.4.1  
> **PDF Pages**: 3721–3721  

---

<!-- page 3721 -->

## 6.4.1.4.1 is_convertible

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

is_convertible是定义于<type_traits>头文件的一个类型转换检查工具，它提供了一种在程序编译时进行类型转换检查的机制：判断两个类型之间是否可以进行隐式转换并返回结果布尔值。本接口可应用在模板元编程、函数重载决议以及静态断言等场景，用于在程序编译阶段捕获潜在的类型转换错误，避免发生运行时错误。

函数原型

```cpp
template <typename From, typename To>struct is_convertible;
```

参数说明

表6-1927模板参数说明

参数名含义

From源类型，即需要进行转换的原始类型。

To目标类型，即需要转换到的目标类型。

约束说明

源类型和目标类型均不支持抽象类和多态类型。

返回值说明

is_convertible的静态常量成员value用于获取返回的布尔值，is_convertible<From,To>::value取值如下：

●true：From类型的对象可以隐式转换为To类型。
