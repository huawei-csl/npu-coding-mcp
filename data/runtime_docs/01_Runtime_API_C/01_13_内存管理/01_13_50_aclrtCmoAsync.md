# aclrtCmoAsync

> **Section**: 1.13.50


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
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

实现 Device 上的 Cache 内存操作。异步接口。

aclError aclrtCmoAsync(void *src, size\_t size, aclrtCmoType cmoType, aclrtStream stream)

| 参数名     | 输入 / 输出   | 说明                                                                          |
|---------|-----------|-----------------------------------------------------------------------------|
| src     | 输入        | 待操作的 Device 内存地址。 只支持本 Device 上的 Cache 内存操作。                                |
| size    | 输入        | 待操作的 Device 内存大小，单位 Byte 。                                                  |
| cmoType | 输入        | Cache 内存操作类型。类型定义请参见 aclrtCmoType 。 当前仅支持 ACL_RT_CMO_TYPE_PREFETCH （内存预 取）。 |
| stream  | 输入        | 执行内存操作任务的 Stream 。类型定义请参见 aclrtStream 。                                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
