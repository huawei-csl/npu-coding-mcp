# aclrtGetBufFromChain

> **Section**: 1.22.10


## 功能说明

## 函数原型

## 参数说明

从 Mbuf 链表中获取第 index 个共享 Buffer 。

aclError aclrtGetBufFromChain(aclrtMbuf headBuf, uint32\_t index, aclrtMbuf *buf)

| 参数名     | 输入 / 输 出   | 说明                                         |
|---------|------------|--------------------------------------------|
| headBuf | 输入         | Mbuf 链表中的第一个共享 Buffer 。类型定义请参见 aclrtMbuf 。 |
| index   | 输入         | Mbuf 链表中的索引（从 0 开始计数）。                     |
| buf     | 输出         | 输出第 index 个共享 Buffer 。类型定义请参见 aclrtMbuf 。  |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
