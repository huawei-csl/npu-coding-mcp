# aclrtSynchronizeDevice

> **Section**: 1.6.19


## 产品支持情况

## 功能说明

函数原型

参数说明

返回值说明

## 接口调用示例

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

阻塞当前线程，直到与当前线程绑定的 Context 所对应的 Device 完成运算。

aclError aclrtSynchronizeDevice(void)

无

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见显式同步。
