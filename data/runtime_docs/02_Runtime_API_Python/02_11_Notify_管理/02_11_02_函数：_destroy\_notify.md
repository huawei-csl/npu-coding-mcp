# 函数： destroy\_notify

> **Section**: 2.11.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁 Notify 。

- C 函数原型

aclError aclrtDestroyNotify(aclrtNotify notify)

- python 函数

ret = acl.rt.destroy\_notify(notify)

| 参数名    | 说明                  |
|--------|---------------------|
| notify | int ， Notify 的指针地址。 |

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
