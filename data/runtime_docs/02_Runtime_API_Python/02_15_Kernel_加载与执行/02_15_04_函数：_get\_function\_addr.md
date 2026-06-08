# 函数： get\_function\_addr

> **Section**: 2.15.4


## 产品支持情况

## 功能说明

## 函数原型

| 参数名     | 说明                                                                          |
|---------|-----------------------------------------------------------------------------|
| options | list ，加载算子二进制文件的可选参数，结构参考 aclrtBinaryLoadOptions ，若参数为空，可将 options 设置为 [] 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

根据核函数句柄获取 Device 侧算子起始地址。对于包含矩阵计算和矢量计算的算子， 一个算子有两个起始地址，分别在 Cube （矩阵）计算单元、 Vector （向量）计算单元 上执行，通过本接口可获取 Cube 计算单元、 Vector 计算单元上的算子起始地址。若通 过本接口获取到 aivAddr 为空，则表示该算子只在 Cube 计算单元上执行。

- C 函数原型 aclError aclrtGetFunctionAddr(aclrtFuncHandle funcHandle, void **aicAddr, void **aivAddr)
- python 函数
- aic\_addr, aiv\_addr, ret = acl.rt.get\_function\_addr(func\_handle)

## 参数说明

## 返回值说明

| 返回值      | 说明                                                                                                                                                                                                                                         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| aic_addr | int ， AI Core 或 Cube Core 上的算子起始地址。 ● 对于以下产品，此处返回的是 AI Core 上的算子起始地址。 Atlas 训练系列产品 Atlas 推理系列产品 ● 对于以下产品，此处返回的是 Cube Core 上的算子起始地址。 Atlas 350 加速卡 Atlas A3 训练系列产品 /Atlas A3 推理系列产品 Atlas A2 训练系列产品 /Atlas A2 推理系列产品 Atlas 200I/500 A2 推理产品 |
| aiv_addr | int ， Vector Core 上的算子起始地址。 若通过本接口获取到 aivAddr 为空，则表示该算子不在 Vector Core 上 执行。                                                                                                                                                                |
| ret      | int ，返回 0 表示成功，返回其他值表示失败。                                                                                                                                                                                                                  |
