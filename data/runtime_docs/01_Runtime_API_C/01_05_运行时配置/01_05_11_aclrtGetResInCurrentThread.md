# aclrtGetResInCurrentThread

> **Section**: 1.5.11


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

获取当前线程可使用的 Device 资源。

## 函数原型

## 参数说明

## 返回值说明

## 功能说明

获取时，按照如下优先级返回 value ： Stream 级别的 Device 资源限制（调用 aclrtSetStreamResLimit 接口设置） &gt; 当前进程的 Device 资源限制（调用 aclrtSetDeviceResLimit 接口设置） &gt; AI 处理器硬件默认的资源限制

aclError aclrtGetResInCurrentThread(aclrtDevResLimitType type, uint32\_t *value)

| 参数名   | 输入 / 输 出   | 说明                              |
|-------|------------|---------------------------------|
| type  | 输入         | 资源类型，请参见 aclrtDevResLimitType 。 |
| value | 输出         | 资源数量。                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
