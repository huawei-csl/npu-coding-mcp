# aclrtDeviceTaskAbort

> **Section**: 1.15.12


须知：本接口为预留接口，暂不支持。

停止指定 Device 上的正在执行的任务，同时丢弃指定 Device 上已下发的任务。该接口 支持用户设置永久等待、或配置具体的超时时间，若配置具体的超时时间，调用本接 口超出超时时间，则接口返回报错。

aclError aclrtDeviceTaskAbort(int32\_t deviceId, uint32\_t timeout)

| 参数名      | 输入 / 输 出   | 说明                                                              |
|----------|------------|-----------------------------------------------------------------|
| deviceId | 输入         | Device ID 。 与 aclrtSetDevice 接口中 Device ID 保持一致。                |
| timeout  | 输入         | 超时时间。 取值说明如下： ● 0 ：表示永久等待； ● >0 ：配置具体的超时时间，单位是毫秒。最大超时时 间 36 分钟。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
