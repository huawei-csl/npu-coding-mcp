# is_floating_point

> **Section**: 6.4.1.4.6  
> **PDF Pages**: 3729–3729  

---

<!-- page 3729 -->

```cpp
AscendC::Std::is_integral::value:0AscendC::Std::is_integral::value:0
```

## 6.4.1.4.6 is_floating_point

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

在程序编译时，检测一个类型是否为浮点类型，可以用于在编译时进行类型检查和条件处理。

函数原型

```cpp
template <typename T>struct is_floating_point;
```

参数说明

表6-1932模板参数说明

参数名含义

T需要检测的类型，包括基本数据类型、修饰类型等。

约束说明

无

返回值说明

is_floating_point的静态常量成员value用于获取返回的布尔值，is_floating_point<Tp>::value取值如下：

●true：Tp是浮点类型。

●false：Tp不是浮点类型。
