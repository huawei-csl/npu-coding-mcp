# aclDestroyDataBuffer

> **Section**: 1.28.5.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

销毁通过 aclCreateDataBuffer 接口创建的 aclDataBuffer 类型的数据。

此处仅销毁 aclDataBuffer 类型的数据，调用 aclCreateDataBuffer 接口创建 aclDataBuffer 类型数据时传入的 data 的内存需由用户自行释放。

aclError aclDestroyDataBuffer(const aclDataBuffer *dataBuffer)

| 参数名        | 输入 / 输 出   | 说明                        |
|------------|------------|---------------------------|
| dataBuffer | 输入         | 待销毁的 aclDataBuffer 类型的指针。 |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
