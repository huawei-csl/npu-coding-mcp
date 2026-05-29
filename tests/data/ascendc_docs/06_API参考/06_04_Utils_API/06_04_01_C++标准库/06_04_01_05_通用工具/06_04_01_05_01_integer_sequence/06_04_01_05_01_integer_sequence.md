# integer_sequence

> **Section**: 6.4.1.5.1  
> **PDF Pages**: 3758–3758  

---

<!-- page 3758 -->

EXPECT_EQ(Zero::value, 0);EXPECT_EQ(One::value, 1);EXPECT_EQ(Large::value, 0xFFFFFFFF);// 验证类型定义EXPECT_TRUE((AscendC::Std::is_same<typename Zero::value_type, size_t>::value));EXPECT_TRUE((AscendC::Std::is_same<typename Zero::type, Zero>::value));EXPECT_TRUE((AscendC::Std::is_same<Zero, AscendC::Std::integral_constant<size_t, 0>>::value));// 验证()操作符重载EXPECT_EQ(Zero()(), 0);EXPECT_EQ(One()(), 1);EXPECT_EQ(Large()(), 0xFFFFFFFF);

●Int特化类型的运算// 加法static_assert((AscendC::Std::Int<5>::value + AscendC::Std::Int<3>::value) == 8, "Addition failed");// 乘法static_assert((AscendC::Std::Int<4>::value * AscendC::Std::Int<6>::value) == 24, "Multiplication failed");// 比较static_assert(AscendC::Std::Int<10>::value > AscendC::Std::Int<5>::value, "Comparison failed");static_assert(AscendC::Std::Int<7>::value != AscendC::Std::Int<77>::value, "Equality check failed");

## 6.4.1.5 通用工具

## 6.4.1.5.1 integer_sequence

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

index_sequence是Ascend C提供的一个类模板，用于生成一个编译时的整数序列，适用于模板元编程。

make_index_sequence是Ascend C提供的一个模板，通常使用make_index_sequence创建一个index_sequence类型的对象，用于生成一个从0到N-1的整数序列。

函数原型

```cpp
template<size_t... Idx>using index_sequence = IntegerSequence<size_t, Idx...>;
template<size_t N>using make_index_sequence = MakeIntegerSequence<size_t, N>;
```
