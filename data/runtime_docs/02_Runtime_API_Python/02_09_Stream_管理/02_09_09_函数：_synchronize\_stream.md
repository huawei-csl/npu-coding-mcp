# 函数： synchronize\_stream

> **Section**: 2.9.9


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 资源参考

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

阻塞应用程序运行，直到指定 Stream 中的所有任务都完成。

- C 函数原型

aclError aclrtSynchronizeStream(aclrtStream stream)

- python 函数

ret = acl.rt.synchronize\_stream(stream)

| 参数名    | 说明                               |
|--------|----------------------------------|
| stream | int ，指定需要完成所有任务的 Stream 对象的指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

接口调用示例，参见关于 Stream 间任务的同步等待（通过 Event 实现）。
