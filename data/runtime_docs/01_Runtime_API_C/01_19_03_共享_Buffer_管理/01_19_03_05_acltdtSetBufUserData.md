# acltdtSetBufUserData

> **Section**: 1.19.3.5


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

设置共享 Buffer 的私有数据区数据，从用户内存拷贝到共享内存的私有数据区的指定偏 移位置，用于设置控制信息作为上下文传递。当前默认私有数据区大小是 96Byte ， offset+size 必须小于或等于 96Byte ，否则返回报错。

aclError acltdtSetBufUserData(acltdtBuf buf, const void *dataPtr, size\_t size, size\_t offset)

| 参数名     | 输入 / 输 出   | 说明                                    |
|---------|------------|---------------------------------------|
| buf     | 输出         | 共享 Buffer 指针。类型定义请参见 acltdtBuf 。      |
| dataPtr | 输入         | 存放用户数据的内存地址指针。                        |
| size    | 输入         | 用户数据的长度，单位为 Byte 。 数据长度小于或等于 96Byte 。 |
| offset  | 输入         | 地址偏移，单位为 Byte 。 偏移量小于或等于 96Byte 。     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
