# 函数： kernel\_args\_para\_update

> **Section**: 2.15.14


## 产品支持情况

## 功能说明

## 函数原型

| 参数名       | 说明        |
|-----------|-----------|
| data_size | int ，内存大小 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

通过 acl.rt.kernel\_args\_append 接口追加的参数，可调用本接口更新参数值。

## ● C 函数原型

aclError aclrtKernelArgsParaUpdate(aclrtArgsHandle argsHandle, aclrtParamHandle paramHandle, void *param, size\_t paramSize)

- python 函数

ret = acl.rt.kernel\_args\_para\_update(args\_handle, param\_handle, param, param\_size)

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
