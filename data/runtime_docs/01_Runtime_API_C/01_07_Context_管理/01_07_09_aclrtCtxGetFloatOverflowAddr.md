# aclrtCtxGetFloatOverflowAddr

> **Section**: 1.7.9


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | √      |
| Atlas 训练系列产品 | √      |

饱和模式下，获取保存溢出标记的 Device 内存地址，该内存地址后续需作为 Workspace 参数传递给 AI Core 算子。

aclError aclrtCtxGetFloatOverflowAddr(void **overflowAddr)

| 参数名           | 输入 / 输 出   | 说明                   |
|---------------|------------|----------------------|
| overflowAdd r | 输出         | 保存溢出标记的 Device 内存地址。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
