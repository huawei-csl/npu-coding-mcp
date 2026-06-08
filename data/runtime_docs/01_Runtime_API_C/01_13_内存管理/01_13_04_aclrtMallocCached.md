# aclrtMallocCached

> **Section**: 1.13.4


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

在 Device 上申请 size 大小的线性内存，通过 *devPtr 返回已分配内存的指针，该接口在 任何场景下申请的内存都是支持 Cache 缓存。

使用 aclrtMallocCached 接口申请的内存与使用 aclrtMalloc 接口申请的内存是等价 的，都支持 Cache 缓存，不需要用户处理 CPU 与 NPU 之间的 Cache 一致性。

aclError aclrtMallocCached(void **devPtr, size\_t size, aclrtMemMallocPolicy policy)

| 参数名    | 输入 / 输 出   | 说明                                                                                                            |
|--------|------------|---------------------------------------------------------------------------------------------------------------|
| devPtr | 输出         | ' Device 上已分配内存的指针'的指针。                                                                                       |
| size   | 输入         | 申请内存的大小，单位 Byte 。 size 不能为 0 。                                                                                |
| policy | 输入         | 内存分配规则。类型定义请参见 aclrtMemMallocPolicy 。 若配置的内存分配规则超出 aclrtMemMallocPolicy 取值范 围， size≥2M 时，按大页申请内存，否则按普通页申请内 存。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
