# aclrtGetBufDataLen

> **Section**: 1.22.6


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

获取共享 Buffer 中有效数据的长度。

通过 aclrtSetBufDataLen 接口设置共享 Buffer 中有效数据的长度后，可调用本接口获 取有效数据的长度，否则，通过本接口获取到的长度为 0 。

aclError aclrtGetBufDataLen(aclrtMbuf buf, size\_t *len)

| 参数名   | 输入 / 输 出   | 说明                                                                         |
|-------|------------|----------------------------------------------------------------------------|
| buf   | 输入         | 共享 Buffer ，类型定义请参见 aclrtMbuf 。 须通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请获得。 |
| len   | 输出         | 有效数据的长度，单位为 Byte 。                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
