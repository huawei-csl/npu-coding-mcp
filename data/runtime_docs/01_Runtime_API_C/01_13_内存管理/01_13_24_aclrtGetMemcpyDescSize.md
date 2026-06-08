# aclrtGetMemcpyDescSize

> **Section**: 1.13.24


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

获取当前 Device 的内存复制描述符占用的内存大小。

本接口需与其它关键接口配合使用，以便实现内存复制，详细描述请参见 aclrtMemcpyAsyncWithDesc 。

aclError aclrtGetMemcpyDescSize(aclrtMemcpyKind kind, size\_t *descSize)

| 参数名      | 输入 / 输 出   | 说明                                                                                           |
|----------|------------|----------------------------------------------------------------------------------------------|
| kind     | 输入         | 内存复制的类型。类型定义请参见 aclrtMemcpyKind 。 当前仅支持 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE ，表示 Device 内的内存复制。 |
| descSize | 输出         | 内存大小，单位 Byte 。                                                                               |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
