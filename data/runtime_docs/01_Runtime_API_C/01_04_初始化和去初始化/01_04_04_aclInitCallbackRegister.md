# aclInitCallbackRegister

> **Section**: 1.4.4


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

注册初始化回调函数。

若在 aclInit 接口之前调用本接口，则会在初始化时触发回调函数的调用；若在 aclInit 接口之后调用本接口，则会在注册时立即触发回调函数的调用。

aclError aclInitCallbackRegister(aclRegisterCallbackType type, aclInitCallbackFunc cbFunc, void *userData)

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                      |
|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type     | 输入         | 注册类型，按照不同的功能区分，请参见 aclRegisterCallbackType 。                                                                                                                                            |
| cbFunc   | 输入         | 初始化回调函数。 回调函数的函数原型为： typedef aclError (*aclInitCallbackFunc)(const char *configStr, size_t len, void *userData); configStr 跟 aclInit 接口中的 json 文件内容保持一致； len 表 示 json 文件内容的长度，单位 Byte 。 |
| userData | 输入         | 待传递给回调函数的用户数据的指针。                                                                                                                                                                       |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
