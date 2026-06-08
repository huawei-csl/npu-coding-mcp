# aclrtCmoAsyncWithBarrier

> **Section**: 1.13.51


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

实现 Device 上的 Cache 内存操作，同时携带 barrierId ， barrierId 表示 Cache 内存操作的 屏障标识。异步接口。

aclError aclrtCmoAsyncWithBarrier(void *src, size\_t size, aclrtCmoType cmoType, uint32\_t barrierId, aclrtStream stream)

| 参数名       | 输入 / 输 出   | 说明                                                                                                                                                                          |
|-----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| src       | 输入         | 待操作的 Device 内存地址。 只支持本 Device 上的 Cache 内存操作。                                                                                                                                |
| size      | 输入         | 待操作的 Device 内存大小，单位 Byte 。                                                                                                                                                  |
| cmoType   | 输入         | Cache 内存操作类型。类型定义请参见 aclrtCmoType 。                                                                                                                                         |
| barrierId | 输入         | 屏障标识。 当 cmoType 为 ACL_RT_CMO_TYPE_INVALID 时， barrierId 有效，支持传入大于 0 的数字，配合 aclrtCmoWaitBarrier 接口使用，等待具有指定 barrierId 的 Invalid 内存操作任务执行完成。当 cmoType 为其它值时， barrierId 固定传 0 。 |
| stream    | 输入         | 执行内存操作任务的 Stream 。类型定义请参见 aclrtStream 。 此处只支持与模型绑定过的 Stream ，绑定模型与 Stream 需调用 aclmdlRIBindStream 接口。                                                                        |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
