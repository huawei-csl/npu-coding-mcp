# 函数： cmo\_async

> **Section**: 2.12.31


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | x      |
| Atlas 推理系列产品                      | x      |
| Atlas 200I/500 A2 推理产品            | x      |

实现 Device 上的 Cache 内存操作。

- C 函数原型

aclError aclrtCmoAsync(void *src, size\_t size, aclrtCmoType cmoType, aclrtStream stream)

- python 函数

ret = acl.rt.cmo\_async(src, size, cmo\_type, stream)

| 参数名     | 说明                                                                                |
|---------|-----------------------------------------------------------------------------------|
| src     | int ，待操作的 Device 内存的地址。                                                           |
| size    | int ，待操作的 Device 内存大小，单位 Byte 。                                                   |
| cmoType | int ， Cache 内存操作类型。参考 2.19.17 aclrtCmoType 当前仅支持 ACL_RT_CMO_TYPE_PREFETCH （内存预取）。 |
| stream  | int ，指定 stream 。                                                                  |

## 返回值说明

## 约束说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

Atlas 训练系列产品不支持该接口。

Atlas 推理系列产品不支持该接口。

Atlas 200I/500 A2 推理产品不支持该接口。
