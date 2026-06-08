# aclrtFreePhysical

> **Section**: 1.13.29


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

释放通过 aclrtMallocPhysical 接口申请的物理内存。

如果物理内存与虚拟内存之间存在映射关系，则此处不会实际释放物理内存。只有在 调用 aclrtUnmapMem 接口取消该物理内存与虚拟内存的映射之后，物理内存才会被 真正释放。

aclError aclrtFreePhysical(aclrtDrvMemHandle handle)

| 参数名    | 输入 / 输 出   | 说明                                             |
|--------|------------|------------------------------------------------|
| handle | 输入         | 待释放的物理内存信息 handle 。类型定义请参见 aclrtDrvMemHandle 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。

接口调用示例，参见虚拟内存管理。
