# 函数： notify\_import\_by\_key

> **Section**: 2.11.9


## 产品支持情况

## 功能说明

## 函数原型

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | x      |

在本进程中获取 key 的信息，并返回本进程可以使用的 Notify 指针地址。

本接口需与其它接口配合使用，以便实现多 Device 上不同进程间的任务同步，请参见 acl.rt.notify\_get\_export\_key 接口处的说明。

- C 函数原型 aclError aclrtNotifyImportByKey(aclrtNotify *notify, const char *key, uint64\_t flag)

## 参数说明

## 返回值说明

## 约束说明

## ● python 函数

notify, ret = acl.rt.notify\_import\_by\_key(key, flags)

| 参数名   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| key   | str ， Notify 共享名称。 必须先调用 acl.rt.notify_get_export_key 接口获取指定 Notify 的共享 名称，再作为参数传入。                                                                                                                                                                                                                                                                                                                                  |
| flags | int ，是否开启两个 Device 之间的数据交互。 取值为如下宏： ● ACL_RT_NOTIFY_IMPORT_FLAG_DEFAULT ：默认值，关闭两个 Device 之间的数据交互。 配置为该值时，需单独调用 acl.rt.device_enable_peer_access 接 口开启两个 Device 之间的数据交互。 ● ACL_RT_NOTIFY_IMPORT_FLAG_ENABLE_PEER_ACCESS ：开启两 个 Device 之间的数据交互。 配置为该值时，则无需调用 acl.rt.device_enable_peer_access 接 口。 宏的定义如下： #define ACL_RT_NOTIFY_IMPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_NOTIFY_IMPORT_FLAG_ENABLE_PEER_ACCESS 0x02UL |

| 返回值    | 说明                        |
|--------|---------------------------|
| notify | int ， Notify 指针。          |
| ret    | int ，返回 0 表示成功，返回其他值表示失败。 |

昇 腾虚拟化实例场景不支持该操作。
