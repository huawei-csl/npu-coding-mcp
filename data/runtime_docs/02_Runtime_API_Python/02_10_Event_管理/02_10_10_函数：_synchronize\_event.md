# 函数： synchronize\_event

> **Section**: 2.10.10


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

阻塞当前线程运行直到 Event 捕获的所有任务都执行完成。具体见 acl.rt.record\_event 接口参考 Event 捕获的细节。

- C 函数原型

aclError aclrtSynchronizeEvent(aclrtEvent event)

- python 函数

ret = acl.rt.synchronize\_event(event)

| 参数名   | 说明                         |
|-------|----------------------------|
| event | int ，指定需等待的 Event 对象的指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

接口调用示例，参见关于 Event 的同步等待。
