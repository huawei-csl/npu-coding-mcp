# LoadDataUnzip

> **Section**: 6.2.3.2.1.4  
> **PDF Pages**: 1009–1009  

---

<!-- page 1009 -->

## 6.2.3.2.1.4 LoadDataUnzip

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

将GM上的数据解压并搬运到A1/B1/B2上。执行该API前需要执行LoadUnzipIndex加载压缩索引表。

函数原型

```cpp
template <typename T>__aicore__ inline void LoadDataUnzip(const LocalTensor<T>& dst, const GlobalTensor<T>& src)
```

参数说明

表6-180参数说明

参数名称输入/输出

含义

dst输出目的操作数，类型为LocalTensor，支持的TPosition为A1/B1/B2。

LocalTensor的起始地址需要保证：TPosition为A1/B1时，32字节对齐；TPosition为B2时，512B对齐。

支持的数据类型为：int8_t。

src输入源操作数，类型为GlobalTensor。数据类型需要与dst保持一致。

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。
