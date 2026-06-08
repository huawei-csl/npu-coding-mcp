# aclrtBinaryGetDevAddress

> **Section**: 1.16.6


## 产品支持情况

## 功能说明

函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取算子二进制数据在 Device 上的内存地址及内存大小。

aclError aclrtBinaryGetDevAddress(const aclrtBinHandle binHandle, void **binAddr, size\_t *binSize)

| 参数名       | 输入 / 输 出   | 说明                                                                                                                 |
|-----------|------------|--------------------------------------------------------------------------------------------------------------------|
| binHandle | 输入         | 算子二进制句柄。类型定义请参见 aclrtBinHandle 。 调用 aclrtBinaryLoadFromFile 接口或 aclrtBinaryLoadFromData 接口获取算子二进制句柄， 再将其作为入参传入本接口。 |

## 返回值说明

| 参数名     | 输入 / 输 出   | 说明                                                                                                                                       |
|---------|------------|------------------------------------------------------------------------------------------------------------------------------------------|
| binAddr | 输出         | 算子二进制数据在 Device 上的内存地址。 如果加载算子二进制时设置了懒加载标识（将 aclrtBinaryLoadOptions.aclrtBinaryLoadOption.isLazyL oad 设置为 1 ），那么调用本接口获取到的 binAddr 为空 指针。 |
| binSize | 输出         | 算子二进制数据的大小，单位 Byte 。                                                                                                                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
