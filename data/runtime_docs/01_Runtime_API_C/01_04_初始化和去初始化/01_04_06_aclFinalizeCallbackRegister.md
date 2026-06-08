# aclFinalizeCallbackRegister

> **Section**: 1.4.6


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

注册去初始化回调函数。

在 aclFinalize 接口之前调用本接口，在去初始化时触发回调函数的调用。

aclError aclFinalizeCallbackRegister(aclRegisterCallbackType type, aclFinalizeCallbackFunc cbFunc, void *userData)

| 参数名      | 输入 / 输 出   | 说明                                                                               |
|----------|------------|----------------------------------------------------------------------------------|
| type     | 输入         | 注册类型，按照不同的功能区分，请参见 aclRegisterCallbackType 。                                     |
| cbFunc   | 输入         | 去初始化回调函数。 回调函数定义如下： typedef aclError (*aclFinalizeCallbackFunc)(void *userData); |
| userData | 输入         | 待传递给回调函数的用户数据的指针。                                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
