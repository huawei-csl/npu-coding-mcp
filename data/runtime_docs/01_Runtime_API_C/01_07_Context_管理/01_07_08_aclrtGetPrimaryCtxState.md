# aclrtGetPrimaryCtxState

> **Section**: 1.7.8


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

获取默认 Context 的状态。

aclError aclrtGetPrimaryCtxState(int32\_t deviceId, uint32\_t *flags, int32\_t *active)

| 参数名      | 输入 / 输出   | 说明                                                                                                                    |
|----------|-----------|-----------------------------------------------------------------------------------------------------------------------|
| deviceId | 输入        | 获取指定 Device 下的默认 Context 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数 量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数 量 -1)] |
| flags    | 输出        | 预留参数。当前固定传 NULL 。                                                                                                     |
| active   | 输出        | 存放默认 Context 状态的指针。 状态值如下： ● 0 ：未激活 ● 1 ：激活                                                                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
