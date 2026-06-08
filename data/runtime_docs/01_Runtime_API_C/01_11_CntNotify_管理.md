# CntNotify 管理

> **Section**: 1.11


aclError aclrtNotifyImportByKey(aclrtNotify *notify, const char *key, uint64\_t flags)

| 参数名    | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| notify | 输出         | Notify 指针。类型定义请参见 aclrtNotify 。                                                                                                                                                                                                                                                                                                                                                                       |
| key    | 输入         | Notify 共享名称。 必须先调用 aclrtNotifyGetExportKey 接口获取指定 Notify 的共享名称，再作为入参传入。                                                                                                                                                                                                                                                                                                                               |
| flags  | 输入         | 是否开启两个 Device 之间的数据交互。 取值为如下宏： ● ACL_RT_NOTIFY_IMPORT_FLAG_DEFAULT ：默认值， 关闭两个 Device 之间的数据交互。 配置为该值时，需单独调用 aclrtDeviceEnablePeerAccess 接口开启两个 Device 之间 的数据交互。 ● ACL_RT_NOTIFY_IMPORT_FLAG_ENABLE_PEER_ACCES S ：开启两个 Device 之间的数据交互。 配置为该值时，则无需调用 aclrtDeviceEnablePeerAccess 接口。 宏的定义如下： #define ACL_RT_NOTIFY_IMPORT_FLAG_DEFAULT 0x0UL #define ACL_RT_NOTIFY_IMPORT_FLAG_ENABLE_PEER_ACCESS 0x02UL |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

昇 腾虚拟化实例场景不支持该操作。
