# aclrtRegStreamStateCallback

> **Section**: 1.8.18


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

注册 Stream 状态回调函数，不支持重复注册。

当 Stream 状态发生变化时（例如调用 aclrtCreateStream 、 aclrtDestroyStream 等接 口）， Runtime 模块会触发该回调函数的调用。此处的 Stream 包含显式创建的 Stream 以及默认 Stream 。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtRegStreamStateCallback(const char *regName, aclrtStreamStateCallback callback, void *args)

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                |
|----------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| regName  | 输入         | 注册唯一名称，不能为空，输入保证字符串以 \0 结尾。                                                                                                                                                                                                                                                                                                                                       |
| callback | 输入         | 回调函数。若 callback 不为 NULL ，则表示注册回调函数；若 为 NULL ，则表示取消注册回调函数。 回调函数的函数原型为： typedef enum { ACL_RT_STREAM_STATE_CREATE_POST = 1, // 调用 create 接口（例如 aclrtCreateStream ）之后 ACL_RT_STREAM_STATE_DESTROY_PRE, // 调用 destroy 接口（例如 aclrtDestroyStream ）之前 } aclrtStreamState; typedef void (*aclrtStreamStateCallback)(aclrtStream stm, aclrtStreamState state, void *args); |
| args     | 输入         | 待传递给回调函数的用户数据的指针。                                                                                                                                                                                                                                                                                                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
