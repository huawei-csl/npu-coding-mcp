# aclrtDestroyContext

> **Section**: 1.7.2


## 产品支持情况

Atlas Context

中包含两个

Stream

：一个默

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

销毁 Context ，释放 Context 的资源。只能销毁通过 aclrtCreateContext 接口创建的 Context 。

aclError aclrtDestroyContext(aclrtContext context)

| 参数名     | 输入 / 输 出   | 说明                                   |
|---------|------------|--------------------------------------|
| context | 输入         | 需销毁的 Context 。类型定义请参见 aclrtContext 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
