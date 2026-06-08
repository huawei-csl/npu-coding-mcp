# aclGetDataBufferAddr

> **Section**: 1.28.5.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取 aclDataBuffer 类型中的数据的内存地址。

void *aclGetDataBufferAddr(const aclDataBuffer *dataBuffer)

| 参数名        | 输入 / 输 出   | 说明                                                                       |
|------------|------------|--------------------------------------------------------------------------|
| dataBuffer | 输入         | aclDataBuffer 类型的指针。 需提前调用 aclCreateDataBuffer 接口创建 aclDataBuffer 类型的数据。 |

返回 aclDataBuffer 类型中的数据的内存地址。
