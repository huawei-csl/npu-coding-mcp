# aclrtHostGetDevicePointer

> **Section**: 1.13.59


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

获取由 aclrtHostRegister 接口或 aclrtHostRegisterV2 接口注册映射的 Device 内存地 址。映射后的 Device 内存地址不能用于内存操作，例如内存复制。

aclError aclrtHostGetDevicePointer(void *pHost, void **pDevice, uint32\_t flag)

| 参数名     | 输入 / 输 出   | 说明                                         |
|---------|------------|--------------------------------------------|
| pHost   | 输入         | 通过 aclrtHostRegisterV2 接口注册映射的 Host 内存地 址。 |
| pDevice | 输出         | Host 内存映射成的 Device 内存地址。                   |
| flag    | 输入         | 预留参数，当前固定配置为 0 。                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
