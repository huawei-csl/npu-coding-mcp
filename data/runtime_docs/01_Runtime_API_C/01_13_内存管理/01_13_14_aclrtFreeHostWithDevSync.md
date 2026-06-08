# aclrtFreeHostWithDevSync

> **Section**: 1.13.14


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

释放通过 aclrtMallocHost 接口或 aclrtMallocHostWithCfg 接口申请的 Host 内存。

本接口内部会进行隐式的 Device 同步，并等待使用该内存的任务完成。

aclError aclrtFreeHostWithDevSync(void *hostPtr)

| 参数名     | 输入 / 输 出   | 说明        |
|---------|------------|-----------|
| hostPtr | 输入         | 待释放内存的指针。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
