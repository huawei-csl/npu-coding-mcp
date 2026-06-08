# aclrtGetBufChainNum

> **Section**: 1.22.11


## 功能说明

函数原型

## 参数说明

## 返回值说明

从 Mbuf 链表中获取共享 Buffer 的个数。

aclError aclrtGetBufChainNum(aclrtMbuf headBuf, uint32\_t *num)

| 参数名     | 输入 / 输 出   | 说明                                         |
|---------|------------|--------------------------------------------|
| headBuf | 输入         | Mbuf 链表中的第一个共享 Buffer 。类型定义请参见 aclrtMbuf 。 |
| num     | 输出         | 共享 Buffer 的个数。                             |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
