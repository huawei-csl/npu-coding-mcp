# 函数： value\_write

> **Section**: 2.12.41


## 产品支持情况

## 功能说明

## 函数原型

| 参数名   | 说明                |
|-------|-------------------|
| ptr   | int ， Host 侧内存地址。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

向指定内存中写数据。

- C 函数原型 aclError aclrtValueWrite(void* devAddr, uint64\_t value, uint32\_t flag, aclrtStream stream)
- python 函数
- ret = acl.rt.value\_write(dev\_addr, value, flag, stream)

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
