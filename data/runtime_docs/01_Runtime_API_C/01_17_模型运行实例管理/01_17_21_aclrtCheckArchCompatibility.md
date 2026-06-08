# aclrtCheckArchCompatibility

> **Section**: 1.17.21


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据 AI 处理器版本判断算子指令是否兼容。

aclError aclrtCheckArchCompatibility(const char *socVersion, int32\_t *canCompatible)

## 参数说明

## 返回值说明

| 参数名            | 输入 / 输 出   | 说明                     |
|----------------|------------|------------------------|
| socVersio n    | 输入         | AI 处理器版本。              |
| canCom patible | 输出         | 是否兼容， 1 表示兼容， 0 表示不兼容。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
