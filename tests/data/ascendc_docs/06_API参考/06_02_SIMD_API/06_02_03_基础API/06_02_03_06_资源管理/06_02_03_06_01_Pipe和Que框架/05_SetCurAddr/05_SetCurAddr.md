# SetCurAddr

> **Section**: 5  
> **PDF Pages**: 1764–1764  

---

<!-- page 1764 -->

函数原型

```cpp
__aicore__ inline TBufHandle GetBufHandle(uint8_t offset)
```

表6-683参数说明

输入/输出

参数名称

含义

offset输入内存块的index值

约束说明

offset值不可超出EXTERN_IMPL_BUFPOOL中定义的BUFID_SIZE大小，用户可根据需要添加校验。

返回值说明

指定的内存块，类型为TBufHandle。

调用示例

请参考调用示例。

## ?.5. SetCurAddr

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

设置自定义TBufPool已经被分配完的地址，比如初始化时一共申请了32k的内存大小，给某一个TQue分配了8K，则需要调用该接口以保证后续的内存块从8K开始分配。

函数原型

```cpp
__aicore__ inline void SetCurAddr(uint32_t curAddr)
```
