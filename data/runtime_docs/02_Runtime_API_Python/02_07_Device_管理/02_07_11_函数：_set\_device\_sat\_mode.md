# 函数： set\_device\_sat\_mode

> **Section**: 2.7.11


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询当前运行环境的芯片版本。

- C 函数原型 const char *aclrtGetSocName()
- python 函数
- name = acl.get\_soc\_name()

无

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

调用该接口成功后，后续在该 Device 上新创建的 Stream 按设置的模式生效，对之前已 创建的 Stream 不生效。
