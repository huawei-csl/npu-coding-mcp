# aclrtMallocHostWithCfg

> **Section**: 1.13.12


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

申请 Host 内存（该内存是锁页内存），由系统保证内存首地址 64 字节对齐。

与 aclrtMallocHost 接口相比，本接口在申请内存时，还可以指定内存相关的配置信 息。

通过本接口申请的内存，需要通过 aclrtFreeHost 接口或 aclrtFreeHostWithDevSync 接口释放内存。

针对 Ascend RC 形态、 Control CPU 开放形态， Host 与 Device 是合一的，所以申请 Host 内存也等同于申请 Device 内存。此外，申请内存时，按普通页申请。如果需要 64 字节 对齐的首地址，用户需自行处理对齐问题。

aclError aclrtMallocHostWithCfg(void **ptr, uint64\_t size, aclrtMallocConfig *cfg)

| 参数名   | 输入 / 输 出   | 说明                                                    |
|-------|------------|-------------------------------------------------------|
| ptr   | 输出         | '已分配内存的指针'的指针。                                        |
| size  | 输入         | 申请内存的大小，单位 Byte 。 size 不能为 0 。                        |
| cfg   | 输入         | 内存配置信息。类型定义请参见 aclrtMallocConfig 。 不指定配置时，此处可传 NULL 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
