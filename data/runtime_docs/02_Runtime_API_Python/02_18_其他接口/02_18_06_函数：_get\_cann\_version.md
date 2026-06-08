# 函数： get\_cann\_version

> **Section**: 2.18.6


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询 CANN 软件包版本号。

- C 函数原型

aclError aclsysGetCANNVersion(aclCANNPackageName name, aclCANNPackageVersion *version)

- python 函数

version, ret = acl.get\_cann\_version(name)

| 参数名   | 说明                                                                                    |
|-------|---------------------------------------------------------------------------------------|
| name  | int ，指定要查询的软件包，具体请参见 2.19.3 aclCANNPackageName 。若指定要查询的软件包没有安装，则本接 口返回报错，错误码 100003 。 |

| 返回值     | 说明                                                      |
|---------|---------------------------------------------------------|
| version | dict ， CANN 软件包版本号，具体请参见 2.19.4 aclCANNPackageVersion 。 |
| ret     | int ，返回 0 表示成功，返回其他值表示失败，请参见 2.19.1 aclError 。          |
