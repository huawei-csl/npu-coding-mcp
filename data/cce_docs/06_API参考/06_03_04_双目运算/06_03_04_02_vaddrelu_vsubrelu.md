# vaddrelu/vsubrelu

> **Section**: 6.3.4.2


## 功能说明

## 接口原型

计算每个向量元素的加法或减法后施加 ReLU 函数，计算公式如下：

// vaddrelu [dst] = ReLU([src0] + [src1]) // vsubrelu [dst] = ReLU([src0] - [src1])

以 block （ 32Byte ）为单位完成计算，一次完成 8 个 block 的计算。

上述接口均支持通过 MASK 控制哪些元素参与计算。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同 // vaddrelu

## 参数说明

## 流水类型
