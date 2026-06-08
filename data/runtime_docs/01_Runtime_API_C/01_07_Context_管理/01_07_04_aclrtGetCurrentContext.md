# aclrtGetCurrentContext

> **Section**: 1.7.4


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

获取线程的 Context 。

如果用户多次调用 aclrtSetCurrentContext 接口设置当前线程的 Context ，则获取的是 最后一次设置的 Context 。

aclError aclrtGetCurrentContext(aclrtContext *context)

| 参数名     | 输入 / 输 出   | 说明                                      |
|---------|------------|-----------------------------------------|
| context | 输出         | 线程当前 Context 的指针。类型定义请参见 aclrtContext 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
