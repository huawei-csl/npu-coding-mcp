# AllocTensor

> **Section**: 2  
> **PDF Pages**: 1785–1785  

---

<!-- page 1785 -->

```cpp
qIn.FreeTensor(ubLocal);}
```

## ?.2. AllocTensor

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

从TSCM中分配tensor，tensor所占大小为InitBuffer时设置的每块内存长度。注意，分配的tensor内容并非全0，可能会是随机值。

函数原型

```cpp
template <typename T>__aicore__ inline LocalTensor<T> AllocTensor()
```

参数说明

无

约束说明

无

返回值说明

LocalTensor对象。

调用示例

AscendC::TPipe pipe;AscendC::TSCM<AscendC::TPosition::VECIN, 1> tscm;int num = 4;int len = 1024;pipe.InitBuffer(tscm, num, len); // InitBuffer分配内存块数为4，每块大小为1024BytesAscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>(); // AllocTensor分配Tensor长度为1024Bytesque.EnQue(tensor1);tensor1 = que.DeQue<half>();que.FreeTensor(tensor1);
