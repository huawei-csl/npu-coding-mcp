# aclprofDestroySubscribeConfig

> **Section**: 1.28.21.2


## 产品支持情况

## 功能说明

## 约束说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

销毁通过 aclprofCreateSubscribeConfig 接口创建的 aclprofSubscribeConfig 类型的数 据。

- 与 aclprofCreateSubscribeConfig 接口配对使用，先调用 aclprofCreateSubscribeConfig 接口再调用 aclprofDestroySubscribeConfig 接口。
- 同一 aclprofSubscribeConfig 指针重复调用 aclprofDestroySubscribeConfig 接口， 会出现重复释放内存的报错。

aclError aclprofDestroySubscribeConfig(const aclprofSubscribeConfig *profSubscribeConfig)

![Figure](../../images/figure_6470.png)

**[Image: figure_6470.png (210x60, 8.5KB)]**

## 返回值说明

| 参数名                  | 输入 / 输 出   | 说明                                                                  |
|----------------------|------------|---------------------------------------------------------------------|
| profSubscrib eConfig | 输入         | 待销毁的 aclprofSubscribeConfig 类型的指针。类型定义 请参见 aclprofSubscribeConfig 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
