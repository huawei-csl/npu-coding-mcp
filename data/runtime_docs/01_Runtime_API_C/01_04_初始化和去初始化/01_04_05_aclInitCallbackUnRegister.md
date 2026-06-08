# aclInitCallbackUnRegister

> **Section**: 1.4.5


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

若不需要触发回调函数的调用，可调用本接口取消注册回调函数。

aclError aclInitCallbackUnRegister(aclRegisterCallbackType type, aclInitCallbackFunc cbFunc)

| 参数名    | 输入 / 输 出   | 说明                                                                                                               |
|--------|------------|------------------------------------------------------------------------------------------------------------------|
| type   | 输入         | 注册类型，按照不同的功能区分，请参见 aclRegisterCallbackType 。                                                                     |
| cbFunc | 输入         | 初始化回调函数。 回调函数的函数原型为： typedef aclError (*aclInitCallbackFunc)(const char *configStr, size_t len, void *userData); |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
