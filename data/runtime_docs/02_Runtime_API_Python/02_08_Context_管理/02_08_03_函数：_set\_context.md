# 函数： set\_context

> **Section**: 2.8.3


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

设置线程的 Context 。

- C 函数原型

aclError aclrtSetCurrentContext(aclrtContext context)

- python 函数

ret = acl.rt.set\_context(context)

| 参数名     | 说明                         |
|---------|----------------------------|
| context | int ，线程当前的 Context 对象指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 支持以下场景：
- -如果在某线程（例如： thread1 ）中调用 acl.rt.create\_context 接口显式创建 一个 Context （例如： ctx1 ），则可以不调用 acl.rt.set\_context 接口指定该线 程的 Context ，系统默认将 ctx1 作为 thread1 的 Context 。

- -如果没有调用 acl.rt.create\_context 接口显式创建 Context ，则系统将默认 Context 作为线程的 Context ，此时，不能通过 acl.rt.destroy\_context 接口来 释放默认 Context 。
- -如果多次调用 acl.rt.set\_context 接口设置线程的 Context ，以最后一次为准。
- 若给线程设置的 Context 所对应的 Device 已经被复位，则不能将该 Context 设置为 线程的 Context ，否则会导致业务异常。
- 推荐在某一线程中创建的 Context ，在该线程中使用。若在线程 A 中调用 acl.rt.create\_context 接口创建 Context ，在线程 B 中使用该 Context ，则需由用户 自行保证两个线程中同一个 Context 下同一个 Stream 中任务执行的顺序。
