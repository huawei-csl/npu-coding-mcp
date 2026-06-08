# 函数： destroy\_stream\_force

> **Section**: 2.9.4


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

- 调用 acl.rt.destroy\_stream 接口销毁指定 Stream 时，需确保该 Stream 在当前 Context 下。
- 调用 acl.rt.destroy\_stream 接口销毁指定 Stream 时，需确保其它接口没有正在使 用该 Stream 。

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁指定 Stream ，销毁通过 acl.rt.create\_stream 或

acl.rt.create\_stream\_with\_config 接口创建的 Stream ，若 Stream 上有未完成的任 务，不会等待任务完成，直接强制销毁 Stream 。

- C 函数原型

aclError aclrtDestroyStreamForce(aclrtStream stream)

- python 函数

ret = acl.rt.destroy\_stream\_force(stream)

| 参数名    | 说明                      |
|--------|-------------------------|
| stream | int ，待销毁的 Stream 的指针地址。 |

## 返回值说明

## 约束说明

调用本接口销毁指定 Stream 时，需确保该 Stream 在当前 Context 下。
