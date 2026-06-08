# aclprofCreateStamp

> **Section**: 1.21.2.2


## 产品支持情况

## 功能说明

## 函数原型

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

创建 msproftx 事件标记。后续调用 aclprofMark 、 aclprofSetStampTraceMessage 、 aclprofPush 和 aclprofRangeStart 接口时需要以描述该事件的指针作为输入，表示记 录该事件发生的时间跨度。

void *aclprofCreateStamp()

- 返回 void 类型的指针，表示成功。
- 返回 nullptr ，表示失败。

## 约束说明

与 1.21.2.10 aclprofDestroyStamp 接口配对使用，需提前调用 1.21.1.4 aclprofStart 接口。
