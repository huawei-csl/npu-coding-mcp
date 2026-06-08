# aclrtDestroyGroupInfo

> **Section**: 1.18.6


## 产品支持情况

## 功能说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | ☓      |

根据实际支持的 Group 数量创建 aclrtGroupInfo 类型的连续内存块，并返回对应指针。

如需销毁 aclrtGroupInfo 类型的数据，请参见 aclrtDestroyGroupInfo 。

不支持在 Atlas 推理系列产品 Ascend EP 形态下调用本接口。

aclrtGroupInfo *aclrtCreateGroupInfo()

无

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

销毁 aclrtGroupInfo 类型的数据，释放相关的内存。只能销毁通过 aclrtCreateGroupInfo 接口创建的 aclrtGroupInfo 类型。

不支持在 Atlas 推理系列产品 Ascend EP 形态下调用本接口。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtDestroyGroupInfo(aclrtGroupInfo *groupInfo)

| 参数名       | 输入 / 输 出   | 说明                           |
|-----------|------------|------------------------------|
| groupInfo | 输入         | 待销毁的 aclrtGroupInfo 类型数据的指针。 |

返回 0 表示成功，非零表示失败，请参见 1.28.1 aclError 。
