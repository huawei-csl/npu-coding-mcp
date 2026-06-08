# aclrtSetStreamOverflowSwitch

> **Section**: 1.8.5


## 产品支持情况

## 功能说明

## 函数原型

销毁 Stream ，销毁通过 aclrtCreateStream 或 aclrtCreateStreamWithConfig 接口创 建的 Stream ，若 Stream 上有未完成的任务，不会等待任务完成，直接强制销毁 Stream 。

aclError aclrtDestroyStreamForce(aclrtStream stream)

| 参数名    | 输入 / 输出   | 说明                                 |
|--------|-----------|------------------------------------|
| stream | 输入        | 待销毁的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

饱和模式下，对接上层训练框架时（例如 PyTorch ），针对指定 Stream ，打开或关闭溢 出检测开关，关闭后无法通过溢出检测算子获取任务是否溢出。

aclError aclrtSetStreamOverflowSwitch(aclrtStream stream, uint32\_t flag)

## 参数说明

## 返回值说明

## 约束说明

| 参数名    | 输入 / 输 出   | 说明                                |
|--------|------------|-----------------------------------|
| stream | 输入         | 待操作 Stream 。类型定义请参见 aclrtStream 。 |
| flag   | 输入         | 溢出检测开关，取值范围如下： ● 0 ：关闭 ● 1 ：打开    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 在调用本接口前，可调用 aclrtSetDeviceSatMode 接口设置饱和模式。
- 调用该接口打开或关闭溢出检测开关后，仅对后续新下发的任务生效，已下发的 任务仍维持原样。
