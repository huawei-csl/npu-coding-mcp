# aclprofPop

> **Section**: 1.21.2.7


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

msproftx 用于记录事件发生的时间跨度的结束时间。

调用此接口后， Profiling 自动在 Stamp 指针中记录采集结束的时间戳。

aclError aclprofPop()

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 与 1.21.2.6 aclprofPush 接口成对使用，表示时间跨度的开始和结束。
- 在 1.21.2.2 aclprofCreateStamp 接口和 1.21.2.10 aclprofDestroyStamp 接口之 间调用。
- 不能跨线程调用。若需要跨线程可使用 1.21.2.8 aclprofRangeStart / 1.21.2.9 aclprofRangeStop 接口。
