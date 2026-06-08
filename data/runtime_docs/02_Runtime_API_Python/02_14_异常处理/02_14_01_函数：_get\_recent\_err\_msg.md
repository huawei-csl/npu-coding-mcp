# 函数： get\_recent\_err\_msg

> **Section**: 2.14.1


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

获取并清空与本接口在同一个线程中的其它 pyacl 接口调用失败时的错误描述信息。

获取进程级别、还是线程级别的错误描述信息由 acl.init 接口中的' err\_msg\_mode ' 配置控制，默认线程级别。

- C 函数原型

const char *aclGetRecentErrMsg()

- python 函数

msg = acl.get\_recent\_err\_msg()

无

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 建议在每次调用 pyacl 接口失败时都调用 acl.get\_recent\_err\_msg 接口，以便获取调 用 pyacl 接口异常时的错误描述信息，用于定位问题。
- 同一个线程中多次调用 acl.get\_recent\_err\_msg 接口后，只有最后一次调用 acl.get\_recent\_err\_msg 接口返回的错误描述字符串有效，之前

acl.get\_recent\_err\_msg 接口返回的错误描述字符串不能使用，否则可能导致内存 非法访问。

- 如果未在每次调用 pyacl 接口失败时调用 acl.get\_recent\_err\_msg 接口可能导致错误 信息堆积、丢失。
