# aclrtGetStreamResLimit

> **Section**: 1.5.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取指定 Stream 的 Device 资源限制。

若没有调用 aclrtSetStreamResLimit 接口设置 Device 资源限制，则调用本接口获取到 的 Device 资源限制优先级为：当前进程的 Device 资源限制（调用 aclrtSetDeviceResLimit 接口设置） &gt; AI 处理器硬件默认的资源限制

aclError aclrtGetStreamResLimit(aclrtStream stream, aclrtDevResLimitType type, uint32\_t *value)

| 参数名    | 输入 / 输 出   | 说明                                                        |
|--------|------------|-----------------------------------------------------------|
| stream | 输入         | 指定 Stream 。类型定义请参见 aclrtStream 。 若传入 NULL ，则表示默认 Stream 。 |

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                              |
|-------|------------|---------------------------------|
| type  | 输入         | 资源类型，请参见 aclrtDevResLimitType 。 |
| value | 输出         | 资源限制的大小。                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
