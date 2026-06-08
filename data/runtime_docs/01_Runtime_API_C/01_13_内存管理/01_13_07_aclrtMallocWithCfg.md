# aclrtMallocWithCfg

> **Section**: 1.13.7


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

在 Device 上分配 size 大小的线性内存，并通过 *devPtr 返回已分配内存的指针，且内存 首地址 64 字节对齐。

与 aclrtMalloc 接口相比，本接口在申请内存时，还可以指定内存相关的配置信息。

使用本接口申请的内存，需要通过 aclrtFree 接口或 aclrtFreeWithDevSync 接口释放 内存。

aclError aclrtMallocWithCfg(void **devPtr, size\_t size, aclrtMemMallocPolicy policy, aclrtMallocConfig *cfg)

| 参数名    | 输入 / 输 出   | 说明                                                                                                            |
|--------|------------|---------------------------------------------------------------------------------------------------------------|
| devPtr | 输出         | ' Device 上已分配内存的指针'的指针。                                                                                       |
| size   | 输入         | 申请内存的大小，单位 Byte 。 size 不能为 0 。                                                                                |
| policy | 输入         | 内存分配规则。类型定义请参见 aclrtMemMallocPolicy 。 若配置的内存分配规则超出 aclrtMemMallocPolicy 取 值范围， size≥2M 时，按大页申请内存，否则按普通页 申请内存。 |
| cfg    | 输入         | 内存配置信息。类型定义请参见 aclrtMallocConfig 。 不指定配置时，此处可传 NULL 。                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
