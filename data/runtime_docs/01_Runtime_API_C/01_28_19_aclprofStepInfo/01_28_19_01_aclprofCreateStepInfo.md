# aclprofCreateStepInfo

> **Section**: 1.28.19.1


## 产品支持情况

## 功能说明

## 约束说明

## 函数原型

## 返回值

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

创建 aclprofStepInfo 对象，用于描述迭代信息。

- 使用 aclprofDestroyStepInfo 接口销毁 aclprofStepInfo 类型的数据，如不销毁会导 致内存未被释放。
- 与 aclprofDestroyStepInfo 接口配对使用，先调用 aclprofCreateStepInfo 接口再 调用 aclprofDestroyStepInfo 接口。

aclprofStepInfo* aclprofCreateStepInfo()

- 返回 aclprofStepInfo 类型的指针，表示成功。
- 返回 nullptr ，表示失败。

## 说明

同一个 aclprofStepInfo 对象、同一个 tag 只能设置一次，否则 Profiling 解析会出错。
