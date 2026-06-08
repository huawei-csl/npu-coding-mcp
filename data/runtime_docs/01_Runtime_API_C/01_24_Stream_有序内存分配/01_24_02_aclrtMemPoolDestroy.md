# aclrtMemPoolDestroy

> **Section**: 1.24.2


须知：预留接口，暂不支持。

销毁通过 aclrtMemPoolCreate 接口创建的内存池。

aclError aclrtMemPoolDestroy(const aclrtMemPool memPool)

| 参数名     | 输入 / 输 出   | 说明                           |
|---------|------------|------------------------------|
| memPool | 输入         | 内存池实例。类型定义请参见 aclrtMemPool 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
