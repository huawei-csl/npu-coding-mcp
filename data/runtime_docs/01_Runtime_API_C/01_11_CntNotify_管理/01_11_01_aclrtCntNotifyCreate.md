# aclrtCntNotifyCreate

> **Section**: 1.11.1


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

创建 CntNotify 。

CntNotify 通常也用于 Device 与 Device 之间的状态 / 动作通信通知。但 CntNotify 是利用 计数值实现任务间的同步，跟 Notify 的区别是， Notify 的计数值仅支持 1 ， CntNotify 的 计数值支持 [1~uint32\_t 最大值 ] 。

aclError aclrtCntNotifyCreate(aclrtCntNotify *cntNotify, uint64\_t flag)

| 参数名       | 输入 / 输 出   | 说明                                     |
|-----------|------------|----------------------------------------|
| cntNotify | 输出         | CntNotify 的指针。类型定义请参见 aclrtCntNotify 。 |
| flag      | 输入         | 预留参数，当前固定配置为 0 。                       |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
