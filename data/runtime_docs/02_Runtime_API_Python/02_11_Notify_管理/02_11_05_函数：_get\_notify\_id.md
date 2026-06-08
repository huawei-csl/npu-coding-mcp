# 函数： get\_notify\_id

> **Section**: 2.11.5


## 产品支持情况

## 功能说明

## 函数原型

| 参数名     | 说明                                                    |
|---------|-------------------------------------------------------|
| timeout | int ，等待的超时时间。 取值说明如下： 0 ：表示永久等待。 >0: 配置具体的超时时间，单位是毫秒。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取指定 Notify 的 ID 。

- C 函数原型 aclError aclrtGetNotifyId(aclrtNotify notify, uint32\_t *notifyId)
- python 函数

notify\_id, ret = acl.rt.get\_notify\_id(notify)

## 参数说明

## 返回值说明

| 返回值       | 说明                        |
|-----------|---------------------------|
| notify_id | int ，获取的 Notify ID 。      |
| ret       | int ，返回 0 表示成功，返回其他值表示失败。 |
