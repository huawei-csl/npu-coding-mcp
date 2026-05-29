# SetCurBufSize

> **Section**: 7  
> **PDF Pages**: 1766–1766  

---

<!-- page 1766 -->

返回值说明

当前已分配的内存地址。

调用示例

请参考调用示例。

## ?.7. SetCurBufSize

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

设置当前已经被自定义TBufPool分配的内存块个数。

函数原型

```cpp
__aicore__ inline void SetCurBufSize(uint8_t curBufSize)
```

约束说明

无

返回值说明

无

调用示例

请参考调用示例。
