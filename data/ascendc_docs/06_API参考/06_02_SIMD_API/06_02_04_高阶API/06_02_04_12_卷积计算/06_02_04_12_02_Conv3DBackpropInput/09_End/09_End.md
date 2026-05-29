# End

> **Section**: 9  
> **PDF Pages**: 3037–3037  

---

<!-- page 3037 -->

函数原型

```cpp
template <bool sync = true>__aicore__ inline void GetTensorC(const AscendC::GlobalTensor<DstT> &output, uint8_t enAtomic = 0, bool enSequentialWrite = false)
```

参数说明

表6-1404模板参数说明

参数名描述

sync预留参数，用户无需感知。

表6-1405接口参数说明

参数名输入/输出

描述

output输入将计算结果搬至Global Memory的GM地址。

enAtomic输入预留参数，用户无需感知。

enSequentialWrite

输入预留参数，用户无需感知。

返回值说明

无

约束说明

GetTensorC接口必须在Iterate后进行调用，完成卷积反向实现，调用顺序如下。while (Iterate()) {       GetTensorC(); }

调用示例

```cpp
while (gradInput_.Iterate()) {       gradInput_.GetTensorC(gradInputGm_[offsetC_]); }
```

## ?.9. End

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√
