# aclrtCntNotifyWaitInfo

> **Section**: 1.28.40


```
typedef struct { aclrtCntNotifyWaitMode mode;  // Wait 的行为模式 uint32_t value; uint32_t timeout;             // 超时时间，单位是秒，其中， 0 表示永久等待 uint8_t  isClear;             // wait 解除阻塞后是否 CntNotify 的计数值自动清空为 0 ，取值： 1 表示清空， 0 表示不 清空 uint8_t rev[3]; } aclrtCntNotifyWaitInfo;
```

mode 结构体定义请参见 aclrtCntNotifyWaitMode 。
