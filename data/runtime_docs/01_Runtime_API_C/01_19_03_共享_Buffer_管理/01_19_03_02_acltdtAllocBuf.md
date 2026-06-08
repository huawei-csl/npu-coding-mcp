# acltdtAllocBuf

> **Section**: 1.19.3.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

申请共享 Buffer 内存。

使用 acltdtAllocBuf 接口申请内存后，数据区的长度为 size 参数的大小，在用户还未填 入有效数据前，该内存的有效数据长度初始值为 0 ，可在用户向内存中填入有效数据 后，再通过 acltdtSetBufDataLen 接口设置有效数据长度。

使用 acltdtAllocBuf 接口申请的内存，需要通过 acltdtFreeBuf 接口释放内存。

aclError acltdtAllocBuf(size\_t size, uint32\_t type, acltdtBuf *buf)

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                   |
|-------|------------|--------------------------------------------------------------------------------------------------------------------------------------|
| size  | 输入         | 用于指定数据区的内存大小，单位 Byte ，不能超过 4G 。                                                                                                      |
| type  | 输入         | 共享 Buffer 内存类型，支持设置如下枚举值。 typedef enum { ACL_TDT_NORMAL_MEM = 0, ACL_TDT_DVPP_MEM } acltdtAllocBufType; 当前仅支持设置 ACL_TDT_NORMAL_MEM 。 |
| buf   | 输出         | 申请成功，输出共享 Buffer 。类型定义请参见 acltdtBuf 。                                                                                                |

## 返回值说明

## 约束说明

对于 Atlas 200I/500 A2 推理产品，仅支持在 Ascend RC 形态下使用该接口。
