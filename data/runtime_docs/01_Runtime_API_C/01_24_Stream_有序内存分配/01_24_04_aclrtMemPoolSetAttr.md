# aclrtMemPoolSetAttr

> **Section**: 1.24.4


须知：预留接口，暂不支持。

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

设置属性值。

多次对同一个内存池的同一个属性值进行设置，以最后一次为准。

aclError aclrtMemPoolSetAttr(aclrtMemPool memPool, aclrtMemPoolAttr attr, void *value)

| 参数名     | 输入 / 输 出   | 说明                                          |
|---------|------------|---------------------------------------------|
| memPool | 输入         | 内存池实例。类型定义请参见 aclrtMemPool 。                |
| attr    | 输入         | 指定属性。类型定义请参见 aclrtMemPoolAttr 。             |
| value   | 输入         | 指向写入属性值地址的指针，写入的数据，其类型需要 与 attr 处指定属性的类型相同。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
