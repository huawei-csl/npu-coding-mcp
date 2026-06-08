# aclrtCmoAsyncWithDesc

> **Section**: 1.13.55


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

使用内存描述符（二级指针方式）操作 Device 上的 Cache 内存。异步接口。

aclError aclrtCmoAsyncWithDesc(void *cmoDesc, aclrtCmoType cmoType, aclrtStream stream, const void *reserve)

| 参数名     | 输入 / 输 出   | 说明                                                                                     |
|---------|------------|----------------------------------------------------------------------------------------|
| cmoDesc | 输入         | Cache 内存描述符地址指针， Device 侧内存地址。 此处需先调用 aclrtCmoSetDesc 接口设置内存描述符，再将 内存描述符地址指针作为入参传入本接口。 |
| cmoType | 输入         | Cache 内存操作类型。类型定义请参见 aclrtCmoType 。 当前仅支持 ACL_RT_CMO_TYPE_PREFETCH （内存预取）。             |
| stream  | 输入         | 执行内存操作任务的 Stream 。类型定义请参见 aclrtStream 。                                                |
| reserve | 输入         | 预留参数。当前固定传 NULL 。                                                                      |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
