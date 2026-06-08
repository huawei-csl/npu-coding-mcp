# aclrtMemRetainAllocationHandle

> **Section**: 1.13.45


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

根据虚拟内存地址获取物理内存信息的 handle 。

若多次调用本接口，则需相应地调用相同次数的 aclrtFreePhysical 来释放物理内存 handle 。

若调用接口时返回 ACL\_ERROR\_RT\_FEATURE\_NOT\_SUPPORT ，这表示底层驱动不支 持该特性，需将驱动包升级到 26.0.RC1 或更高版本。您可以单击 Link ，在'固件与驱 动'页面下载对应版本的驱动安装包，并参照其文档进行安装和升级。

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。
