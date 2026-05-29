# CountBitsCntSameAsSignBit

> **Section**: 6.2.3.5.3  
> **PDF Pages**: 1723–1723  

---

<!-- page 1723 -->

参数说明

表6-646参数说明

参数名输入/输出

描述

valueIn输入被统计的二进制数字。

返回值说明

返回valueIn的前导0的个数。

约束说明

无

调用示例

uint64_t valueIn = 0x0fffffffffffffff;// 输出数据ans：4，二进制从最高位到第一个1一共有4个0int64_t ans = AscendC::CountLeadingZero(valueIn);

## 6.2.3.5.3 CountBitsCntSameAsSignBit

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

计算一个int64_t类型数字的二进制中，从最高数值位开始与符号位相同的连续比特位的个数。

当输入是-1（比特位全1）或者0（比特位全0）时，返回-1。

函数原型

```cpp
__aicore__ inline int64_t CountBitsCntSameAsSignBit(int64_t valueIn)
```
