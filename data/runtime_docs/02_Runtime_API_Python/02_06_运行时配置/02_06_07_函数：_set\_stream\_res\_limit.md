# 函数： set\_stream\_res\_limit

> **Section**: 2.6.7


## 产品支持情况

若没有调用 acl.rt.set\_stream\_res\_limit 接口设置 Device 资源限制，则调用本接口获取 到的 Device 资源限制优先级为：当前进程的 Device 资源限制（调用 acl.rt.set\_stream\_res\_limit 接口设置） &gt; AI 处理器硬件默认的资源限制。

## ● C 函数原型

aclError aclrtGetStreamResLimit(aclrtStream stream, aclrtDevResLimitType type, uint32\_t *value)

- python 函数

value, ret = acl.rt.get\_stream\_res\_limit(stream,  type)

| 参数名    | 说明                                                                          |
|--------|-----------------------------------------------------------------------------|
| stream | int ，指定 Stream, 若传入 0 ，则表示默认 Stream 。                                       |
| type   | int ，资源类型，当前支持 Cube Core 、 Vector Core ，具体请参见新增 数据结构 aclrtDevResLimitType 。 |

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

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
