# aclprofMarkEx

> **Section**: 1.21.2.5


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

aclprofMarkEx 打点接口。

调用此接口向配置的 Stream 流上下发打点任务，用于标识 Host 侧打点与 Device 侧打点 任务的关系。

aclError aclprofMarkEx(const char *msg, size\_t msgLen, aclrtStream stream)

| 参数名    | 输入 / 输 出   | 说明                              |
|--------|------------|---------------------------------|
| msg    | 输入         | 打点信息字符串指针。类型定义请参见 aclrtStream 。 |
| msgLen | 输入         | 字符串长度。最大支持 127 字符。              |
| stream | 输入         | 指定 Stream 。                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
