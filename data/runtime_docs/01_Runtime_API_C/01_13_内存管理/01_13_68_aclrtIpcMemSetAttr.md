# aclrtIpcMemSetAttr

> **Section**: 1.13.68


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

设置 IPC 共享内存的属性信息。

## 函数原型

## 参数说明

## 返回值说明

aclError aclrtIpcMemSetAttr(const char *key, aclrtIpcMemAttrType type, uint64\_t attr)

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                                                                                                          |
|-------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| key   | 输入         | 共享内存 key 。 必须先调用 aclrtIpcMemGetExportKey 接口获取共享内 存 key ，再作为入参传入。                                                                                                                                                            |
| type  | 输入         | 内存映射类型。类型定义请参见 aclrtIpcMemAttrType 。 当前支持配置为 ACL_RT_IPC_MEM_ATTR_ACCESS_LINK ，用于在跨片访 问时，指定双 die 之间是 SIO （ serial input/output ）通 道、还是 HCCS （ Huawei Cache Coherence System ）通 道。                                            |
| attr  | 输入         | 属性。 当前支持设置为如下宏： ● ACL_RT_IPC_MEM_ATTR_ACCESS_LINK_SIO ： SIO 通 道，默认该选项 ● ACL_RT_IPC_MEM_ATTR_ACCESS_LINK_HCCS ： HCCS 通道 宏的定义如下： #define ACL_RT_IPC_MEM_ATTR_ACCESS_LINK_SIO 0 #define ACL_RT_IPC_MEM_ATTR_ACCESS_LINK_HCCS 1 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
