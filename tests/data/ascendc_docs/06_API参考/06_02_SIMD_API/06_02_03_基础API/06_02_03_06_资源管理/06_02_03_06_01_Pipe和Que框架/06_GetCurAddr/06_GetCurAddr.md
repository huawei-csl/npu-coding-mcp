# GetCurAddr

> **Section**: 6  
> **PDF Pages**: 1765–1765  

---

<!-- page 1765 -->

表6-684参数说明

输入/输出

参数名称

含义

curAddr输入已分配的内存地址。

约束说明

无

返回值说明

无

调用示例

请参考调用示例。

## ?.6. GetCurAddr

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

获取当前已经被自定义TBufPool分配的地址，用户可以从该地址值开始向后分配内存块。

函数原型

```cpp
__aicore__ inline uint32_t GetCurAddr()
```

约束说明

无
