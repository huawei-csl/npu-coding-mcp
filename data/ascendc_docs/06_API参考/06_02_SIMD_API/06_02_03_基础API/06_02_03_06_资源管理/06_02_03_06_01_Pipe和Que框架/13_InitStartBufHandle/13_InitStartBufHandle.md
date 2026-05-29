# InitStartBufHandle

> **Section**: 13  
> **PDF Pages**: 1805–1805  

---

<!-- page 1805 -->

## ?.13. InitStartBufHandle

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

设置TQue/TBuf的起始内存块指针、内存块的个数、每一块内存块的大小。

函数原型

```cpp
__aicore__ inline void InitStartBufHandle(TBufHandle startBufhandle, uint8_t num, uint32_t len)
```

参数说明

表6-708参数说明

输入/输出

参数名称

含义

startBufhandle

输入TQue/TBuf的起始内存块指针，数据类型为TBufHandle（实际为uint8_t*）。

num输入分配内存块的个数。

len输入每一个内存块的大小，单位为Bytes。

约束说明

●TQue、TBuf类继承自TQueBind类，所以TQue、TBuf对象也可使用该接口。

●该接口目前只提供给自定义TBufPool初始化TQue、TBuf的内存块时使用。

●当使用TBuf对象调用该接口时，入参num必须为1。

返回值说明

无
