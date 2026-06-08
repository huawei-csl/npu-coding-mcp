# 函数： destroy\_subscribe\_config

> **Section**: 2.16.3.3


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 训练系列产品           | √      |
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

销毁 aclprofSubscribeConfig 类型的数据，只能销毁通过 acl.prof.create\_subscribe\_config 接口创建的 aclprofSubscribeConfig 类型。

- C 函数原型 aclError aclprofDestroySubscribeConfig(const aclprofSubscribeConfig *profSubscribeConfig)
- python 函数

ret = acl.prof.destroy\_subscribe\_config(subscribe\_config)

| 参数名               | 说明                                        |
|-------------------|-------------------------------------------|
| subscribe_conf ig | int ，待销毁的 aclprofSubscribeConfig 类型的地址对象。 |

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |

- 与 acl.prof.create\_subscribe\_config 接口配对使用，先调用 acl.prof.create\_subscribe\_config 接口再调用 acl.prof.destroy\_subscribe\_config 接

口。

- 同一 aclprofSubscribeConfig 重复调用 acl.prof.destroy\_subscribe\_config 接口，会 出现重复释放内存的报错。
