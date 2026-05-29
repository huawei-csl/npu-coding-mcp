# SetDoubleBuffer

> **Section**: 20  
> **PDF Pages**: 2435–2435  

---

<!-- page 2435 -->

## ?.20. SetDoubleBuffer

功能说明

设置A/B/C/Bias是否使能double buffer功能，以及是否需要做ND2NZ或者NZ2ND的转换，主要用于Tiling函数内部调优。

该接口为预留接口，当前版本暂不支持。

函数原型

```cpp
int32_t SetDoubleBuffer(bool a, bool b, bool c, bool bias, bool transND2NZ = true, bool transNZ2ND = true)
```

参数说明

表6-1091参数说明

参数名输入/输出

描述

a输入设置A矩阵是否开启double buffer。

b输入设置B矩阵是否开启double buffer。

c输入设置C矩阵是否开启double buffer。

bias输入设置Bias矩阵是否开启double buffer。

transND2NZ

输入设置是否需要ND2NZ。

transNZ2ND

输入设置是否需要NZ2ND。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

## ?.21. GetBaseM

功能说明

获取Tiling计算得到的baseM值。baseM参数的说明请参考表6-1072。

函数原型

```cpp
int32_t GetBaseM() const
```
