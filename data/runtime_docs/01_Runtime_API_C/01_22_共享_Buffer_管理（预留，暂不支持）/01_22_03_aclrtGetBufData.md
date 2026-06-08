# aclrtGetBufData

> **Section**: 1.22.3


## 功能说明

## 函数原型

## 参数说明

## 返回值说明

获取共享 Buffer 的数据区指针和数据区长度，用户可以使用此指针填入数据。

接口调用顺序：调用 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请到共享 Buffer 后，因 此需由用户调用 aclrtGetBufData 接口获取共享 Buffer 的内存指针及长度后，再自行向 内存中填充有效数据，然后再调用 aclrtSetBufDataLen 接口设置共享 Buffer 中有效数 据的长度，且长度必须小于 aclrtGetBufData 获取到的 size 大小。

aclError aclrtGetBufData(const aclrtMbuf buf, void **dataPtr, size\_t *size)

| 参数名     | 输入 / 输 出   | 说明                                                                         |
|---------|------------|----------------------------------------------------------------------------|
| buf     | 输入         | 共享 Buffer ，类型定义请参见 aclrtMbuf 。 须通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请获得。 |
| dataPtr | 输出         | 数据区指针（ Device 侧地址）。                                                        |
| size    | 输出         | 数据区的长度，单位为 Byte 。                                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
