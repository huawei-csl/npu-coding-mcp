# aclrtGetBufUserData

> **Section**: 1.22.5


## 功能说明

## 函数原型

获取共享 Buffer 的私有数据区数据，偏移 offset 后，拷贝至用户申请的内存区域。当前 默认私有数据区大小是 96Byte ， offset+size 必须小于或等于 96Byte ，否则返回报错。

aclError aclrtGetBufUserData(const aclrtMbuf buf, void *dataPtr, size\_t size, size\_t offset)

## 参数说明

## 返回值说明

| 参数名     | 输入 / 输 出   | 说明                                                                         |
|---------|------------|----------------------------------------------------------------------------|
| buf     | 输入         | 共享 Buffer ，类型定义请参见 aclrtMbuf 。 须通过 aclrtAllocBuf 或 aclrtCopyBufRef 接口申请获得。 |
| dataPtr | 输出         | 存放用户数据的内存地址指针。                                                             |
| size    | 输入         | 用户数据的长度，单位为 Byte 。 数据长度小于或等于 96Byte 。                                      |
| offset  | 输入         | 地址偏移，单位为 Byte 。 偏移量小于或等于 96Byte 。                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
