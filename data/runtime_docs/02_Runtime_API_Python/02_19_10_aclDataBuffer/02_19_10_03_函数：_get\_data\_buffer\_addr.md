# 函数： get\_data\_buffer\_addr

> **Section**: 2.19.10.3


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

获取 aclDataBuffer 类型中的数据的内存地址。

- C 函数原型 void *aclGetDataBufferAddr(const aclDataBuffer *dataBuffer)
- python 函数

output = acl.get\_data\_buffer\_addr(data\_buffer)

| 参数名         | 说明                                                                                   |
|-------------|--------------------------------------------------------------------------------------|
| data_buffer | int ，表示 aclDataBuffer 的指针地址。 需提前调用 acl.create_data_buffer 接口创建 aclDataBuffer 类型 的数据。 |

## 返回值说明

| 返回值    | 说明                               |
|--------|----------------------------------|
| output | int ， aclDataBuffer 类型中的数据的指针地址。 |
