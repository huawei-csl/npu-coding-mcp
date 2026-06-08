# 函数： destroy\_stream

> **Section**: 2.9.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁指定 Stream ，销毁通过 acl.rt.create\_stream 或

acl.rt.create\_stream\_with\_config 接口创建的 Stream ，若 Stream 上有未完成的任 务，会等待任务完成后再销毁 Stream 。

- C 函数原型

aclError aclrtDestroyStream(aclrtStream stream)

- python 函数

ret = acl.rt.destroy\_stream(stream)

| 参数名    | 说明                      |
|--------|-------------------------|
| stream | int ，待销毁的 Stream 的指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 调用 acl.rt.destroy\_stream 接口销毁指定 Stream 前，需要先调用 acl.rt.synchronize\_stream 接口确保 Stream 中的任务都已完成。

## 资源参考

接口调用流程与示例，请参见运行时资源申请与释放、同步等待。
