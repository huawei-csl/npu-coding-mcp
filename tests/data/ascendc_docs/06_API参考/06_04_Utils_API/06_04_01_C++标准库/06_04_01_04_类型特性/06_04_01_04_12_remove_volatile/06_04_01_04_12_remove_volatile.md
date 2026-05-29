# remove_volatile

> **Section**: 6.4.1.4.12  
> **PDF Pages**: 3738–3738  

---

<!-- page 3738 -->

约束说明

无

返回值说明

remove_const是一个结构体，其提供一个嵌套类型type，表示移除const限定符后的类型。通过remove_const<Tp>::type来访问该类型。

调用示例

```cpp
// Test non-const typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<int>::type, int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<double>::type, double>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<char>::type, char>));
// Test const typeascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<const int>::type, int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<const double>::type, double>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const<const char>::type, char>));
ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const_t<int>, int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const_t<double>, double>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const_t<const int>, int>));ascendc_assert((AscendC::Std::is_same_v<AscendC::Std::remove_const_t<const double>, double>));
```

## 6.4.1.4.12 remove_volatile

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

在程序编译时，对传入的模板参数类型移除volatile限定符，可以用于在编译时进行类型转换。

函数原型

```cpp
template <typename Tp>struct remove_volatile;
```
