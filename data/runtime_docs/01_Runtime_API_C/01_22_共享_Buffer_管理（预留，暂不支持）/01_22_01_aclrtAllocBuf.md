# aclrtAllocBuf

> **Section**: 1.22.1


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

申请指定大小的共享 Buffer 。

aclError aclrtAllocBuf(aclrtMbuf *buf, size\_t size)

| 参数名   | 输入 / 输 出   | 说明                                 |
|-------|------------|------------------------------------|
| buf   | 输出         | 申请到的共享 Buffer 。类型定义请参见 aclrtMbuf 。 |
| size  | 输入         | 用于指定数据区的内存大小，单位 Byte ，不能超过 4G 。    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
