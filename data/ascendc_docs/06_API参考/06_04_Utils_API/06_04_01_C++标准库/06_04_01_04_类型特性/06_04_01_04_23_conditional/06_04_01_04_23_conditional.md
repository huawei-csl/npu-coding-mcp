# conditional

> **Section**: 6.4.1.4.23  
> **PDF Pages**: 3754–3755  

---

<!-- page 3754 -->

```cpp
Container<int> integralContainer;
intResult = add(1, 2);AscendC::PRINTF("Integer result: %d\n", intResult);
```

doubleResult = add((float)1.5, (float)2.5);AscendC::PRINTF("float result: %f\n", doubleResult);// 执行结果：Integral type multiplicationResult of integral multiplication: 6Non-integral type multiplicationResult of non-integral multiplication: 8.750000Generic container.Integral container.Integral type addition.Integer result: 3Non-integral type addition.float result: -1.000000

## 6.4.1.4.23 conditional

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

conditional是定义在<type_traits>头文件里的一个类型特征工具，它在程序编译时根据一个布尔条件从两个类型中选择一个类型。本接口可应用在模板元编程中，用于根据不同的条件来灵活选择合适的类型，增强代码的通用性和灵活性。

conditional有一个嵌套的type成员，它的值取决于Bp的值：如果Bp为true，则conditional<Bp, If, Then>::type为If。如果Bp为false，则conditional<Bp, If,Then>::type为Then。

函数原型

```cpp
template <bool Bp, typename If, typename Then>struct conditional;
```

参数说明

表6-1949模板参数说明

参数名含义

Bp一个布尔常量表达式，作为选择类型的条件。

<!-- page 3755 -->

参数名含义

If当Bp为true时选择的类型。

Then当Bp为false时选择的类型。

约束说明

无

返回值说明

conditional的静态常量成员type用于获取返回值，conditional<Bp, If, Then>::type取值如下：

●If：Bp为true。

●Then：Bp为false。

调用示例

// 定义两个不同的类型struct TypeA {    __aicore__ inline static void print() {        AscendC::PRINTF("This is TypeA..\n");    }};

```cpp
struct TypeB {    __aicore__ inline static void print() {        AscendC::PRINTF("This is TypeB..\n");    }};
```

// 根据条件选择类型template <bool Condition>__aicore__ inline void selectType() {    using SelectedType = typename AscendC::Std::conditional<Condition, TypeA, TypeB>::type;    SelectedType::print();}

// 定义一个模板函数，根据条件选择不同的类型template <bool Condition>__aicore__ inline void selectOtherType() {    using SelectedType = typename std::conditional<Condition, int, float>::type;    if constexpr (std::is_same_v<SelectedType, int>) {        AscendC::PRINTF("Selected type is int.\n");    } else {        AscendC::PRINTF("Selected type is float.\n");    }}

// 条件为 true，选择 TypeAselectType<true>();// 条件为 false，选择 TypeBselectType<false>();

// 测试条件为 true 的情况selectOtherType<true>();// 测试条件为 false 的情况selectOtherType<false>();// 执行结果：This is TypeA..
