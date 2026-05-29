# EnQue

> **Section**: 5  
> **PDF Pages**: 1794–1795  

---

<!-- page 1794 -->

功能说明

释放Que中的指定Tensor。

函数原型

```cpp
template <typename T>__aicore__ inline void FreeTensor(LocalTensor<T>& tensor)
```

参数说明

表6-700模板参数说明

参数名说明

TTensor的数据类型。

表6-701参数说明

输入/输出

参数名称

含义

tensor输入待释放的Tensor。

约束说明

无

返回值说明

无

调用示例

// 使用FreeTensor释放通过AllocTensor分配的Tensor，注意配对使用AscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 2> que;int num = 4;int len = 1024;pipe.InitBuffer(que, num, len);AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();que.FreeTensor<half>(tensor1);

## ?.5. EnQue

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

<!-- page 1795 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

将Tensor push到队列。

函数原型

```cpp
template <typename T>__aicore__ inline bool EnQue(const LocalTensor<T>& tensor)
```

参数说明

表6-702模板参数说明

参数名说明

TTensor的数据类型。

表6-703参数说明

输入/输出

参数名称

含义

tensor输入指定的Tensor

约束说明

无

返回值说明

●true - 表示Tensor加入Queue成功

●false - 表示Queue已满，入队失败

调用示例

// 接口: EnQue TensorAscendC::TPipe pipe;AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
