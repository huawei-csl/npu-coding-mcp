# 函数： value\_wait

> **Section**: 2.12.42


## 产品支持情况

## 功能说明

## 函数原型

| 参数名      | 说明                                                                                                 |
|----------|----------------------------------------------------------------------------------------------------|
| dev_addr | int ， Device 侧内存地址。 此处需用户提前申请 Device 内存（例如调用 acl.rt.malloc 接口）， dev_addr 要求 8 字节对齐，有效内存位宽为 64bit 。 |
| value    | int ，需向内存中写入的数据。                                                                                   |
| flag     | int ，预留参数，当前固定设置为 0 。                                                                              |
| stream   | int ，指定 stream 。此处支持传 0 ，表示使用默认 Stream 。                                                           |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

等待指定内存中的数据满足一定条件后解除阻塞。

- C 函数原型

aclError aclrtValueWait(void* devAddr, uint64\_t value, uint32\_t flag, aclrtStream stream)

- python 函数

ret = acl.rt.value\_wait(devAddr, value, flag, stream)

## 参数说明

## 返回值说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
