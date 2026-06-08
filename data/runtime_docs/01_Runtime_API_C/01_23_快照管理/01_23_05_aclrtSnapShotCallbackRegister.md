# aclrtSnapShotCallbackRegister

> **Section**: 1.23.5


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 推理系列产品 | ☓      |
| Atlas 训练系列产品 | ☓      |

注册一个回调函数，该回调函数将在快照操作的不同阶段被调用。不支持重复注册。

aclError aclrtSnapShotCallbackRegister(aclrtSnapShotStage stage, aclrtSnapShotCallBack callback, void *args)

| 参数名      | 输入 / 输 出   | 说明                                                                                                                  |
|----------|------------|---------------------------------------------------------------------------------------------------------------------|
| stage    | 输入         | 指定触发回调的快照阶段。类型定义请参见 aclrtSnapShotStage 。                                                                            |
| callback | 输入         | 指向回调函数的指针。当指定的快照阶段到达时，系统将自 动调用此函数。 函数定义如下： typedef uint32_t (*aclrtSnapShotCallBack)(int32_t deviceId, void* args); |
| args     | 输入         | 用户自定义参数指针，在回调函数调用时传递，可以为 NULL ，表示不需要传递额外参数。                                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
