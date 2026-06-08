# aclrtAppendBufChain

> **Section**: 1.22.9


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

将共享 Buffer 添加到 Mbuf 链表中。共享 Buffer 链最大支持 128 个共享 Buffer 。共享 Buffer 可通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请获得。

aclError aclrtAppendBufChain(aclrtMbuf headBuf, aclrtMbuf buf)

| 参数名     | 输入 / 输 出   | 说明                                         |
|---------|------------|--------------------------------------------|
| headBuf | 输入         | Mbuf 链表中的第一个共享 Buffer 。类型定义请参见 aclrtMbuf 。 |
| buf     | 输入         | 待添加的共享 Buffer 。类型定义请参见 aclrtMbuf 。         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
