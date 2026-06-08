# aclrtSynchronizeStreamWithTimeout

> **Section**: 1.8.10


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

阻塞 Host 侧当前线程直到指定 Stream 中的所有任务都完成，该接口是在 aclrtSynchronizeStream 接口基础上进行了增强，支持用户设置超时时间，当应用程 序异常时可根据所设置的超时时间自行退出。

aclError aclrtSynchronizeStreamWithTimeout(aclrtStream stream, int32\_t timeout)

| 参数名     | 输入 / 输 出   | 说明                                                                                     |
|---------|------------|----------------------------------------------------------------------------------------|
| stream  | 输入         | 指定需要完成所有任务的 Stream 。类型定义请参见 aclrtStream 。                                              |
| timeout | 输入         | 接口的超时时间。 取值说明如下： ● -1 ：表示永久等待，和接口 aclrtSynchronizeStream 功 能一样； ● >0 ：配置具体的超时时间，单位是毫秒。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
