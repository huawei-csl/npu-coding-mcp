# FreeTensor

> **Section**: 3  
> **PDF Pages**: 1786–1786  

---

<!-- page 1786 -->

## ?.3. FreeTensor

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

释放TSCM中的指定Tensor。

函数原型

```cpp
template <typename T>__aicore__ inline void FreeTensor(LocalTensor<T>& tensor)
```

参数说明

输入/输出

参数名称

含义

tensor输入待释放的Tensor

约束说明

无

返回值说明

无

调用示例

参考调用示例。
