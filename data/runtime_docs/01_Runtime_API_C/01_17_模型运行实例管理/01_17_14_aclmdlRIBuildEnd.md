# aclmdlRIBuildEnd

> **Section**: 1.17.14


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

结束构建模型运行实例。

aclError aclmdlRIBuildEnd(aclmdlRI modelRI, void *reserve)

| 参数名     | 输入 / 输出   | 说明                                                                             |
|---------|-----------|--------------------------------------------------------------------------------|
| modelRI | 输入        | 模型运行实例。类型定义请参见 aclmdlRI 。 此处的 modelRI 需与 aclmdlRIBuildBegin 接口中的 modelRI 保持一致。 |
| reserve | 输入        | 预留参数。当前固定传 NULL 。                                                              |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
