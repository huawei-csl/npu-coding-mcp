# 函数： kernel\_args\_finalize

> **Section**: 2.15.15


## 产品支持情况

## 功能说明

## 函数原型

| 参数名           | 说明                              |
|---------------|---------------------------------|
| args_handle   | int ，参数列表句柄。                    |
| param_handl e | int ，参数句柄。                      |
| param         | int ，待追加参数值的内存地址。此处为 Host 内存地址。 |
| param_size    | int ，内存大小，单位 Byte 。             |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

在所有参数追加完成后，调用本接口以标识参数组装完毕。

- C 函数原型 aclError aclrtKernelArgsFinalize(aclrtArgsHandle argsHandle)
- python 函数
- ret = acl.rt.kernel\_args\_finalize(args\_handle)

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
