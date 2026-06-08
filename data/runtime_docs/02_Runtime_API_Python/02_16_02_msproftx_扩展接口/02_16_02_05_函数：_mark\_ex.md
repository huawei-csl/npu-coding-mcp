# 函数： mark\_ex

> **Section**: 2.16.2.5


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

acl.prof.mark\_ex 打点接口。

## 功能说明

- C 函数原型

aclError aclprofMark(void *stamp)

- python 函数

ret = acl.prof.mark(stamp)

| 参数名   | 说明                                                                       |
|-------|--------------------------------------------------------------------------|
| stamp | int ， Stamp 指针地址，指代 msproftx 事件标记。指定 2.16.2.2 函 数： create_stamp 接口的指针地址。 |

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |

## 函数原型

## 参数说明

## 返回值说明

## 资源参考

与 acl.prof.finalize 接口配对使用，先调用 acl.prof.init 接口再调用 acl.prof.finalize 接 口。
