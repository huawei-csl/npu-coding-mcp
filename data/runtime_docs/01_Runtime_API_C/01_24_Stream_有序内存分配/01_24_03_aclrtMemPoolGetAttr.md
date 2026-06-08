# aclrtMemPoolGetAttr

> **Section**: 1.24.3


须知：预留接口，暂不支持。

## 功能说明

## 函数原型

获取指定属性的值。

如果未通过 aclrtMemPoolSetAttr 接口设置相应属性，则获取该属性的默认值。

aclError aclrtMemPoolGetAttr(aclrtMemPool memPool, aclrtMemPoolAttr attr, void *value)

## 参数说明

## 返回值说明

| 参数名     | 输入 / 输 出   | 说明                                       |
|---------|------------|------------------------------------------|
| memPool | 输入         | 内存池实例。类型定义请参见 aclrtMemPool 。             |
| attr    | 输入         | 指定属性。类型定义请参见 aclrtMemPoolAttr 。          |
| value   | 输出         | 指向输出属性值地址的指针，该指针指向的类型需与 attr 处指定属性的类型相同。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
