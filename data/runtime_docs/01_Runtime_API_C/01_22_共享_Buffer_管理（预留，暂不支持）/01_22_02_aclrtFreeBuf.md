# aclrtFreeBuf

> **Section**: 1.22.2


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

释放通过 aclrtAllocBuf 接口申请的共享 Buffer 。

aclError aclrtFreeBuf(aclrtMbuf buf)

| 参数名   | 输入 / 输 出   | 说明                                 |
|-------|------------|------------------------------------|
| buf   | 输入         | 待释放的共享 Buffer 。类型定义请参见 aclrtMbuf 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
