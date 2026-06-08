# aclrtSetDeviceTaskAbortCallback

> **Section**: 1.15.16


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

调用本接口注册回调函数，用于在调用 aclrtDeviceTaskAbort 接口前后触发该回调函 数。不支持重复注册。

aclError aclrtSetDeviceTaskAbortCallback(const char *regName, aclrtDeviceTaskAbortCallback callback, void *args)

| 参数名     | 输入 / 输 出   | 说明                              |
|---------|------------|---------------------------------|
| regName | 输入         | 注册名称，保持唯一，不能为空，输入保证字符串以 \0 结 尾。 |

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                |
|----------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| callback | 输入         | 回调函数。若 callback 不为 NULL ，则表示注册回调函数；若 为 NULL ，则表示取消注册回调函数。 回调函数的函数原型为： typedef enum { ACL_RT_DEVICE_TASK_ABORT_PRE = 0, ACL_RT_DEVICE_TASK_ABORT_POST, } aclrtDeviceTaskAbortStage; typedef int32_t (*aclrtDeviceTaskAbortCallback)(int32_t deviceId, aclrtDeviceTaskAbortStage stage, uint32_t timeout, void *args); 此处的 timeout 表示期望回调函数执行的最长时间。 |
| args     | 输入         | 待传递给回调函数的用户数据的指针。                                                                                                                                                                                                                                                                                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
