# acltdtSetBufDataLen

> **Section**: 1.19.3.7


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

设置共享 Buffer 中有效数据的长度。

接口调用顺序：调用 acltdtAllocBuf 或 acltdtCopyBufRef 接口申请到共享 Buffer 后， 因此需由用户调用 acltdtGetBufData 接口获取共享 Buffer 的内存指针及长度后，再自 行向内存中填充有效数据，然后再调用 acltdtSetBufDataLen 接口设置共享 Buffer 中有 效数据的长度，且长度必须小于 acltdtGetBufData 获取到的 size 大小。

aclError acltdtSetBufDataLen(acltdtBuf buf, size\_t len)

| 参数名   | 输入 / 输 出   | 说明                                                                              |
|-------|------------|---------------------------------------------------------------------------------|
| buf   | 输入         | 共享 Buffer 指针。类型定义请参见 acltdtBuf 。 须通过 acltdtAllocBuf 或 acltdtCopyBufRef 接口申请获 得。 |
| len   | 输入         | 有效数据的长度，单位为 Byte 。                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
