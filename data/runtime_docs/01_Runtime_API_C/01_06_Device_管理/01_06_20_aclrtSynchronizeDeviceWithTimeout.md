# aclrtSynchronizeDeviceWithTimeout

> **Section**: 1.6.20


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品           | 是否支持   |
|--------------|--------|
| Atlas 训练系列产品 | √      |

阻塞当前线程，直到与当前线程绑定的 Context 所对应的 Device 完成运算。该接口是在 aclrtSynchronizeDevice 接口基础上进行了增强，支持用户设置超时时间，当应用程 序异常时可根据所设置的超时时间自行退出，超时退出时本接口返回 ACL\_ERROR\_RT\_STREAM\_SYNC\_TIMEOUT 。

多 Device 场景下，调用该接口等待的是当前 Context 对应的 Device 。

aclError aclrtSynchronizeDeviceWithTimeout(int32\_t timeout)

| 参数名     | 输入 / 输 出   | 说明                                                                                     |
|---------|------------|----------------------------------------------------------------------------------------|
| timeout | 输入         | 接口的超时时间。 取值说明如下： ● -1 ：表示永久等待，和接口 aclrtSynchronizeDevice 功 能一样； ● >0 ：配置具体的超时时间，单位是毫秒。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
