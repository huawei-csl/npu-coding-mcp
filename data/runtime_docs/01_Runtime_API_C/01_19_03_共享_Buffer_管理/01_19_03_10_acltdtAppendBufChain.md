# acltdtAppendBufChain

> **Section**: 1.19.3.10


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | ☓      |
| Atlas 训练系列产品 | ☓      |

将某个共享 Buffer 内存添加到共享 Buffer 链表中。共享 Buffer 链最大支持 128 个共享 Buffer 。共享 Buffer 可通过 acltdtAllocBuf 或 acltdtCopyBufRef 接口申请获得。

aclError acltdtAppendBufChain(acltdtBuf headBuf, acltdtBuf buf)

| 参数名     | 输入 / 输 出   | 说明                                              |
|---------|------------|-------------------------------------------------|
| headBuf | 输入         | 共享 Buffer 链头部的第一个共享 Buffer 。类型定义请参见 acltdtBuf 。 |
| buf     | 输入         | 待添加的共享 Buffer 。类型定义请参见 acltdtBuf 。              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
