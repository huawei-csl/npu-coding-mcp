# aclprofSubscribeConfig

> **Section**: 1.28.21


| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

销毁通过 aclprofCreateStepInfo 接口创建的 aclprofStepInfo 类型的数据。

- 与 aclprofCreateStepInfo 接口配对使用，先调用 aclprofCreateStepInfo 接口再调 用 aclprofDestroyStepInfo 接口。
- 同一 aclprofStepInfo 数据重复调用 aclprofDestroyStepInfo 接口，会出现重复释放 内存的报错。

void aclprofDestroyStepInfo(aclprofStepInfo* stepinfo)
