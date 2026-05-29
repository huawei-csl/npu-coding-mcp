# Init

> **Section**: 3  
> **PDF Pages**: 1735–1735  

---

<!-- page 1735 -->

```cpp
...    }private:    ...    TPipe* pipe;    ...};extern "C" __global__ __aicore__ void example_kernel(...) {    ...    TPipe pipe;
    KernelExample<float> op;
    op.Init(..., &pipe);    ...}
```

## ?.3. Init

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

用于内存和同步流水事件EventID的初始化。

函数原型

```cpp
__aicore__ inline void Init()
```

约束说明

重复申请释放tpipe，要与Destroy接口成对使用，tpipe如果要重复申请需要先Destroy释放后再Init。

返回值说明

无

调用示例

// 实例化一个浮点型的自定义算子对象KernelInit<float> op;uint32_t srcSize = 128;
