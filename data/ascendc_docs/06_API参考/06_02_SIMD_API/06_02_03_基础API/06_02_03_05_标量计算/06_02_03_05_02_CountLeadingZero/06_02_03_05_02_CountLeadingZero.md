# CountLeadingZero

> **Section**: 6.2.3.5.2  
> **PDF Pages**: 1722–1722  

---

<!-- page 1722 -->

表6-645参数说明

参数名输入/输出

描述

valueIn输入被统计的二进制数字。

返回值说明

valueIn中0或者1的个数。

约束说明

无

调用示例

uint64_t valueIn = 0xffff;    // 二进制格式中有16个1constexpr int countValue = 1;    // 统计valueIn二进制格式中1的个数// 输出数据oneCount: 16int64_t oneCount = AscendC::GetBitCount<countValue>(valueIn);

## 6.2.3.5.2 CountLeadingZero

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

计算一个uint64_t类型数字前导0的个数（二进制从最高位到第一个1一共有多少个0）。

函数原型

```cpp
__aicore__ inline int64_t CountLeadingZero(uint64_t valueIn)
```
