# aclUpdateDataBuffer

> **Section**: 1.28.5.6


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

更新 aclDataBuffer 中数据的内存及大小。

更新 aclDataBuffer 后，之前 aclDataBuffer 中存放数据的内存如果不使用，需及时释 放，否则可能会导致内存泄漏。

## 函数原型

## 参数说明

## 返回值说明

aclError aclUpdateDataBuffer(aclDataBuffer *dataBuffer, void *data, size\_t size)

| 参数名        | 输入 / 输 出   | 说明                                                                                                                                                                                 |
|------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dataBuffer | 输入         | aclDataBuffer 类型的指针。 需提前调用 aclCreateDataBuffer 接口创建 aclDataBuffer 类型的数据。 该内存需由用户自行管理，调用 aclrtMalloc 接口 / aclrtFree 接口申请 / 释放内存，或调用 aclrtMallocHost 接口 / aclrtFreeHost 接口申请 / 释放内存。 |
| data       | 输入         | 存放数据内存地址的指针。                                                                                                                                                                       |
| size       | 输入         | 内存大小，单位 Byte 。 如果用户需要使用空 tensor ，则在申请内存时，内存大 小最小为 1Byte ，以保障后续业务正常运行。                                                                                                              |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
