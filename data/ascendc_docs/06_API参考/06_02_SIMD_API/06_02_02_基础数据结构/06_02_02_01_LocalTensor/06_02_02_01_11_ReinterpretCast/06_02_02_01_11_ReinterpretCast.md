# ReinterpretCast

> **Section**: 6.2.2.1.11  
> **PDF Pages**: 826–826  

---

<!-- page 826 -->

## 6.2.2.1.11 ReinterpretCast

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

将当前Tensor重解释为用户指定的新类型，转换后的Tensor与原Tensor地址及内容完全相同，Tensor的大小（字节数）保持不变。

函数原型

```cpp
template <typename CAST_T> __aicore__ inline LocalTensor<CAST_T> ReinterpretCast() const
```

参数说明

表6-59模板参数说明

参数名描述

CAST_T用户指定的新类型。

返回值说明

重解释转换后的Tensor。

约束说明

无

调用示例

// 示例// input_local为int32_t 类型，包含16个元素(64字节)for (int32_t i = 0; i < 16; ++i) {    inputLocal.SetValue(i, i); // 对inputLocal中第i个位置进行赋值为i}
