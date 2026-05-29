# GetRuntimeUBSize

> **Section**: 6.2.3.13.5  
> **PDF Pages**: 1973–1973  

---

<!-- page 1973 -->

返回值说明

UB空间的大小，单位为byte。

约束说明

无

调用示例

本调用示例通过GetUBSizeInBytes获取的UB空间大小，来计算tileNum的值。

// 定义待处理的总数据长度 (元素个数)uint32_t totalLength = 16384;

// GetUBSizeInBytes() / sizeof(half) -> 计算 UB 能容纳多少个 half 类型元素// 除2 -> 预留 50% 的 UB 空间uint32_t tileLength = AscendC::GetUBSizeInBytes() / sizeof(half) / 2;// 防止分片大小超过实际数据总量if (totalLength < tileLength) {    tileLength = totalLength;}// 需要迭代的分片数量：16384 / 63488 = 1uint32_t tileNum = totalLength / tileLength;

## 6.2.3.13.5 GetRuntimeUBSize

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取运行时UB空间的大小，单位为byte。开发者根据UB的大小来计算循环次数等参数值。

函数原型

```cpp
__aicore__ inline uint32_t GetRuntimeUBSize()
```

参数说明

无
