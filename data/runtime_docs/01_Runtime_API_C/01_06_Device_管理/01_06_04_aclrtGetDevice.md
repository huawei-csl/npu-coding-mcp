# aclrtGetDevice

> **Section**: 1.6.4


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取当前正在使用的 Device 的 ID 。

aclError aclrtGetDevice(int32\_t *deviceId)

## 参数说明

## 返回值说明

## 约束说明

如果没有提前指定计算设备（例如调用 aclrtSetDevice 接口），则调用 aclrtGetDevice 接口时，返回错误。
