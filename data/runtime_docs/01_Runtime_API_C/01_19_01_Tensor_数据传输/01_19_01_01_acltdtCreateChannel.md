# acltdtCreateChannel

> **Section**: 1.19.1.1


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

创建 acltdtChannelHandle 类型的数据，表示可以用于向 Device 发送数据或是从 Device 接收数据的通道。通道使用完成后，需及时依次调用 acltdtStopChannel 、 acltdtDestroyChannel 接口释放通道资源。

对于 Atlas 训练系列产品，仅支持在 昇 腾虚拟化实例场景下使用本接口。

acltdtChannelHandle *acltdtCreateChannel(uint32\_t deviceId, const char *name)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                   |
|----------|------------|------------------------------------------------------------------------------------------------------|
| deviceId | 输入         | Device ID 。 用户调用 aclrtGetDeviceCount 接口获取可用的 Device 数量后，这个 Device ID 的取值范围： [0, ( 可用的 Device 数量 -1)] |
| name     | 输入         | 队列通道名称的指针。                                                                                           |

- 返回 acltdtChannelHandle 类型的指针，表示成功。
- 返回 nullptr ，表示失败。
