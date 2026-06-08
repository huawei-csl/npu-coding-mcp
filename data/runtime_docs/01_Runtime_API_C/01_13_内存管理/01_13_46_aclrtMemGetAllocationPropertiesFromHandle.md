# aclrtMemGetAllocationPropertiesFromHandle

> **Section**: 1.13.46


## 产品支持情况

## 功能说明

## 函数原型

aclError aclrtMemRetainAllocationHandle(void* virPtr, aclrtDrvMemHandle *handle)

| 参数名    | 输入 / 输 出   | 说明                                                   |
|--------|------------|------------------------------------------------------|
| virPtr | 输入         | '已分配的虚拟内存地址的指针'的指针。 必须与 aclrtMapMem 接口的 virPtr 地址相同。 |
| handle | 输出         | 存放物理内存信息的 handle 。类型定义请参见 aclrtDrvMemHandle 。        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据物理内存信息的 handle 查询其内存属性信息。

aclError aclrtMemGetAllocationPropertiesFromHandle(aclrtDrvMemHandle handle, aclrtPhysicalMemProp* prop)

## 参数说明

## 返回值说明

## 约束说明

Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。
