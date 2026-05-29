# GetSFFValue

> **Section**: 6.2.3.5.4  
> **PDF Pages**: 1724–1724  

---

<!-- page 1724 -->

参数说明

表6-647参数说明

参数名输入/输出

描述

valueIn输入输入数据，数据类型int64_t。

返回值说明

返回从最高数值位开始和符号位相同的连续比特位的个数。

约束说明

无

调用示例

int64_t valueIn = 0x0f00000000000000;// 输出数据(ans): 3，符号为0，第4位为1，则与最高位相同的bit数为3int64_t ans = AscendC::CountBitsCntSameAsSignBit(valueIn);

## 6.2.3.5.4 GetSFFValue

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

获取一个uint64_t类型数字的二进制表示中从最低有效位开始的第一个0或1出现的位置，如果没找到则返回-1。

函数原型

```cpp
template <int countValue> __aicore__ inline int64_t GetSFFValue(uint64_t valueIn)
```
