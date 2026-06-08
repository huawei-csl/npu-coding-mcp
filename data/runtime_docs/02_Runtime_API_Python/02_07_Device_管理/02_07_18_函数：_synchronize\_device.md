# 函数： synchronize\_device

> **Section**: 2.7.18


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 资源参考

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

阻塞应用程序运行，直到正在运算中的 Device 完成运算。

多 Device 场景下，调用该接口等待的是当前 Context 对应的 Device 。

- C 函数原型

aclError aclrtSynchronizeDevice(void)

- python 函数

ret = acl.rt.synchronize\_device()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 接口调用示例，参见关于 Device 的同步等待。
