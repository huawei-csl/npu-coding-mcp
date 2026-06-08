# 函数： malloc\_host\_with\_cfg

> **Section**: 2.12.34


## 产品支持情况

- C 函数原型

aclError aclrtMallocForTaskScheduler(void **devPtr, size\_t size, aclrtMemMallocPolicy policy, aclrtMallocConfig *cfg)

- python 函数

dev\_ptr, ret = acl.rt.malloc\_for\_task\_scheduler(size, policy, cfg)

| 参数名    | 说明                                                                                          |
|--------|---------------------------------------------------------------------------------------------|
| size   | int ，申请内存的大小，单位 Byte 。 size 不能为 0 。                                                         |
| policy | int ，内存分配规则。 若配置的内存分配规则超出 2.19.41 aclrtMemMallocPolicy 取值范 围， size≥2M 时，按大页申请内存，否则按普通页申请内存。 |
| cfg    | dict ，内存配置信息。不指定配置时，此处可传空字典，具体请参见 2.19.35 aclrtMallocConfig 。                               |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值      | 说明                            |
|----------|-------------------------------|
| host_ptr | int ，指向 Host 上已分配内存的指针地址。     |
| ret      | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
