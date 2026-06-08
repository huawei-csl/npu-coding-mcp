# aclrtCopyBufRef

> **Section**: 1.22.8


## 功能说明

## 函数原型

## 参数说明

对共享 Buffer 数据区的引用拷贝，创建并返回一个新的 Mbuf 管理结构指向相同的数据 区。

aclError aclrtCopyBufRef(const aclrtMbuf buf, aclrtMbuf *newBuf)

| 参数名    | 输入 / 输 出   | 说明                                                                                    |
|--------|------------|---------------------------------------------------------------------------------------|
| buf    | 输入         | 共享 Buffer 。类型定义请参见 aclrtMbuf 。 共享 Buffer 可通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申 请获得。 |
| newBuf | 输出         | 返回一个新的共享 Buffer ，指向相同的数据区。类型定义请 参见 aclrtMbuf 。                                        |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
