# 函数： destroy\_data\_buffer

> **Section**: 2.19.10.2


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

销毁 aclDataBuffer 类型的数据。

此处仅销毁 aclDataBuffer 类型的数据，调用 acl.create\_data\_buffer 接口创建 aclDataBuffer 类型数据时传入的 data 的内存需由用户自行释放。

- C 函数原型

aclError aclDestroyDataBuffer(const aclDataBuffer *dataBuffer)

- python 函数

ret = acl.destroy\_data\_buffer(data\_buffer)

| 参数名         | 说明                           |
|-------------|------------------------------|
| data_buffer | int ，表示 aclDataBuffer 的指针地址。 |

## 返回值说明

| 返回值   | 说明                                  |
|-------|-------------------------------------|
| ret   | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |
