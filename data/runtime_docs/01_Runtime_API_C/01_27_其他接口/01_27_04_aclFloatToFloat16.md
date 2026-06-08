# aclFloatToFloat16

> **Section**: 1.27.4


## 产品支持情况

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

将fl oat （指fl oat32 ）类型的数据转换为 aclFloat16 类型的数据。

aclFloat16 aclFloatToFloat16(float value)

| 参数名   | 输入 / 输 出   | 说明      |
|-------|------------|---------|
| value | 输入         | 待转换的数据。 |

转换后的数据。

注意，由于 C 语言无fl oat16 类型，此处返回值使用 uint16\_t 对数据进行存储。若用户需 要打印，需自行将 uint16\_t 解释成fl oat16 进行打印，或者转成fl oat 进行打印。
