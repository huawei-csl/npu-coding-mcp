# aclrtSetBufDataLen

> **Section**: 1.22.7


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

设置共享 Buffer 中有效数据的长度。

接口调用顺序：调用 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请到共享 Buffer 后，因 此需由用户调用 aclrtGetBufData 接口获取共享 Buffer 的内存指针及长度后，再自行向 内存中填充有效数据，然后再调用 aclrtSetBufDataLen 接口设置共享 Buffer 中有效数 据的长度，且长度必须小于 aclrtGetBufData 获取到的 size 大小。

aclError aclrtSetBufDataLen(aclrtMbuf buf, size\_t len)

| 参数名   | 输入 / 输 出   | 说明                                                                         |
|-------|------------|----------------------------------------------------------------------------|
| buf   | 输入         | 共享 Buffer ，类型定义请参见 aclrtMbuf 。 须通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请获得。 |
| len   | 输入         | 有效数据的长度，单位为 Byte 。                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
