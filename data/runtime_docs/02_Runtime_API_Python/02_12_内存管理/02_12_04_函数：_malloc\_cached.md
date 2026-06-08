# 函数： malloc\_cached

> **Section**: 2.12.4


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

申请 Device 上的内存，该接口在任何场景下申请的内存都是支持 cache 缓存。在 Device 上申请 size 大小的线性内存，通过 dev\_ptr 返回已分配内存的指针地址。

使用 acl.rt.malloc\_cached 接口申请的内存与使用 acl.rt.malloc 接口申请的内存是等价 的，都支持 cache 缓存，不需要用户处理 cpu 与 npu 之间的 cache 一致性。

调用媒体数据处理的接口前，若需要申请 Device 上的内存存放输入或输出数据，需调 用 acl.media.dvpp\_malloc 申请内存。

- C 函数原型 aclError aclrtMallocCached(void **devPtr, size\_t size, aclrtMemMallocPolicy policy)
- python 函数

dev\_ptr, ret = acl.rt.malloc\_cached(size, policy)

| 参数名    | 说明                                                                                         |
|--------|--------------------------------------------------------------------------------------------|
| size   | int ，申请内存的大小，单位 Byte 。 size 不能为 0 。                                                        |
| policy | int ，内存分配规则。 若配置的内存分配规则超出 2.19.41 aclrtMemMallocPolicy 取值范 围， size≥2M 时，按大页申请内存，否则按普通页申请内存 |

| 返回值     | 说明                            |
|---------|-------------------------------|
| dev_ptr | int ，指向 Device 上已分配内存的指针地址。   |
| ret     | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

## 约束说明

其它约束与 acl.rt.malloc 接口相同。

2.12.5

## 函数： mem\_flush

## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

将 cache 中的数据刷新到 DDR 中并将 cache 中的内容设置成无效。

该版本用户无需处理 CPU 与 NPU 之间的 cache 一致性，无需调用该接口。

- C 函数原型

aclError aclrtMemFlush(void *devPtr, size\_t size)

- python 函数

ret = acl.rt.mem\_flush(dev\_ptr, size)

| 参数名     | 说明                                               |
|---------|--------------------------------------------------|
| dev_ptr | int ，待fl ush 的 DDR 内存起始地址。                       |
| size    | int ，待fl ush 的 DDR 内存大小，单位 Byte 。' size '不能为 0 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
