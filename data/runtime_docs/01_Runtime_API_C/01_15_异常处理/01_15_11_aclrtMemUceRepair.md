# aclrtMemUceRepair

> **Section**: 1.15.11


须知：本接口为预留接口，暂不支持。

## 功能说明

## 函数原型

修复内存 UCE 的错误虚拟地址。

aclError aclrtMemUceRepair(int32\_t deviceId, aclrtMemUceInfo *memUceInfoArray, size\_t arraySize)

## 参数说明

## 返回值说明

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 参数名              | 输入 / 输 出   | 说明                                               |
|------------------|------------|--------------------------------------------------|
| deviceId         | 输入         | Device ID 。 与 aclrtSetDevice 接口中 Device ID 保持一致。 |
| memUceInf oArray | 输入         | aclrtMemUceInfo 数组的指针。                           |
| arraySize        | 输入         | 传入 aclrtMemUceInfo 数组的长度。                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
