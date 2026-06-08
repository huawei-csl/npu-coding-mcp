# 函数： update\_data\_buffer

> **Section**: 2.19.10.6


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

更新 aclDataBuffer 中数据的内存及大小。

更新 aclDataBuffer 后，之前 aclDataBuffer 中存放数据的内存如果不使用，需及时释 放，否则可能会导致内存泄漏。

## ● C 函数原型

aclError aclUpdateDataBuffer(aclDataBuffer *dataBuffer, void *data, size\_t size)

- python 函数

ret = acl.update\_data\_buffer(data\_buffer, data, size)

| 参数名         | 说明                                                                                                                                                                                                        |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data_buffer | int ， aclDataBuffer 类型的指针地址。 需提前调用 acl.create_data_buffer 接口创建 aclDataBuffer 类型 的数据。 该内存需由用户自行管理，调用 acl.rt.malloc 接口 / acl.rt.free 接 口申请 / 释放内存，或调用 acl.rt.malloc_host 接口 / acl.rt.free_host 接口申请 / 释放内存。 |

## 返回值说明

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |
