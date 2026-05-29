# SetShapeInfo

> **Section**: 6.2.2.2.10  
> **PDF Pages**: 845–845  

---

<!-- page 845 -->

产品是否支持

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品√

功能说明

根据输入的offset偏移返回新的GlobalTensor。

函数原型

```cpp
__aicore__ inline GlobalTensor operator[](const uint64_t offset) const
```

参数说明

表6-72参数说明

参数名输入/输出

描述

offset输入偏移offset个元素。

返回值说明

指定偏移量的GlobalTensor。

约束说明

无。

调用示例

// operator[]使用方法, aGlobal[4]为从起始地址开始偏移量为4的新tensorauto gmA = aGlobal[4];// 示例结果如下：// 输入数据(aGlobal): [1 2 3 4 5 6 ... 100]// 输出数据(gmA ): [5 6 7 8 ... 100]

## 6.2.2.2.10 SetShapeInfo

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√
