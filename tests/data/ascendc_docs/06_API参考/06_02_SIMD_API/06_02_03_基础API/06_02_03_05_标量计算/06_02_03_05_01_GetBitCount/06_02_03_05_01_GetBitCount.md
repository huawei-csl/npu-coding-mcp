# GetBitCount

> **Section**: 6.2.3.5.1  
> **PDF Pages**: 1721–1721  

---

<!-- page 1721 -->

enum class RoundMode {    CAST_NONE = 0,  // 在转换有精度损失时表示CAST_RINT模式，不涉及精度损失时表示不舍入    CAST_RINT,      // rint，四舍六入五成双舍入    CAST_FLOOR,     // floor，向负无穷舍入    CAST_CEIL,      // ceil，向正无穷舍入    CAST_ROUND,     // round，四舍五入舍入    CAST_TRUNC,     // trunc，向零舍入    CAST_ODD,       // Von Neumann rounding，最近邻奇数舍入    CAST_HYBRID,    // hybrid，目前特指输出结果是hif8数据时，会用到的一种随机舍入};

## 6.2.3.5 标量计算

## 6.2.3.5.1 GetBitCount

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

获取一个uint64_t类型数字的二进制中0或者1的个数。

函数原型

```cpp
template <int countValue> __aicore__ inline int64_t GetBitCount(uint64_t valueIn)
```

参数说明

表6-644模板参数说明

参数名描述

countValue指定统计0还是统计1的个数。

只能输入0或1。
