# aclrtNotifySetImportPidInterServer

> **Section**: 1.10.9


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

设置共享 Notify 的进程白名单。

该接口仅针对针对 Atlas A3 训练系列产品 /Atlas A3 推理系列产品中的超节点产品，

aclError aclrtNotifySetImportPidInterServer(aclrtNotify notify, aclrtServerPid *serverPids, size\_t num)

| 参数名        | 输入 / 输 出   | 说明                                                                                          |
|------------|------------|---------------------------------------------------------------------------------------------|
| notify     | 输入         | 指定 Notify 。类型定义请参见 aclrtNotify 。 必须先调用 aclrtNotifyGetExportKey 接口获取指定 Notify 的共享名称，再作为入参传入。 |
| serverPids | 输入         | 白名单信息数组。类型定义请参见 aclrtServerPid 。                                                            |
| num        | 输入         | serverPids 数组的大小。                                                                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
