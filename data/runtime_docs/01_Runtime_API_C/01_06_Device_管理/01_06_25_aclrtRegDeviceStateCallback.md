# aclrtRegDeviceStateCallback

> **Section**: 1.6.25


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

注册 Device 状态回调函数，不支持重复注册。

当 Device 状态发生变化时（例如调用 aclrtSetDevice 、 aclrtResetDevice 等接口）， Runtime 模块会触发该回调函数的调用。

aclError aclrtRegDeviceStateCallback(const char *regName, aclrtDeviceStateCallback callback, void *args)

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| regName  | 输入         | 注册名称，保持唯一，不能为空，输入保证字符串以 \0 结 尾。                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| callback | 输入         | 回调函数。若 callback 不为 NULL ，则表示注册回调函数；若 为 NULL ，则表示取消注册回调函数。 回调函数的函数原型为： typedef enum { ACL_RT_DEVICE_STATE_SET_PRE = 0, // 调用 set 接口（例如 aclrtSetDevice ）之前 ACL_RT_DEVICE_STATE_SET_POST, // 调用 set 接口（例如 aclrtSetDevice ）之后 ACL_RT_DEVICE_STATE_RESET_PRE, // 调用 reset 接口（例如 aclrtResetDevice ）之前 ACL_RT_DEVICE_STATE_RESET_POST, // 调用 reset 接口（例如 aclrtResetDevice ）之后 } aclrtDeviceState; typedef void (*aclrtDeviceStateCallback)(uint32_t devId, aclrtDeviceState state, void *args); |
| args     | 输入         | 待传递给回调函数的用户数据的指针。                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
