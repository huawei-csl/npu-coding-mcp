# aclrtMemsetAsync

> **Section**: 1.13.16


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

初始化内存，将内存中的内容设置为指定的值。

要初始化的内存支持在 Host 侧或 Device 侧，系统根据地址判定是 Host 还是 Device 。如 果 Host 内存不是用 acl 接口（例如 aclrtMallocHost ）申请的，将会导致未定义的行为。

aclError aclrtMemset(void *devPtr, size\_t maxCount, int32\_t value, size\_t count)

| 参数名       | 输入 / 输 出   | 说明                      |
|-----------|------------|-------------------------|
| devPtr    | 输入         | 内存起始地址的指针。              |
| maxCou nt | 输入         | 内存的最大长度，单位 Byte 。       |
| value     | 输入         | 设置的值。                   |
| count     | 输入         | 需要设置为指定值的内存长度，单位 Byte 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

初始化内存，将内存中的内容设置为指定的值。异步接口。

要初始化的内存支持在 Host 侧或 Device 侧，系统根据地址判定是 Host 还是 Device 。如 果 Host 内存不是用 acl 接口（例如 aclrtMallocHost ）申请的，将会导致未定义的行为。

aclError aclrtMemsetAsync(void *devPtr, size\_t maxCount, int32\_t value, size\_t count, aclrtStream stream)

| 参数名       | 输入 / 输 出   | 说明                                         |
|-----------|------------|--------------------------------------------|
| devPtr    | 输入         | 内存起始地址的指针。                                 |
| maxCou nt | 输入         | 内存的最大长度，单位 Byte 。                          |
| value     | 输入         | 设置的值。                                      |
| count     | 输入         | 需要设置为指定值的内存长度，单位 Byte 。                    |
| stream    | 输入         | 指定执行内存初始化任务的 Stream 。类型定义请参见 aclrtStream 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
