# aclrtMemPoolCreate

> **Section**: 1.24.1


须知：预留接口，暂不支持。

## 功能说明

## 函数原型

创建内存池。

aclError aclrtMemPoolCreate(aclrtMemPool *memPool, const aclrtMemPoolProps *poolProps)

## 参数说明

## 返回值说明

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 参数名       | 输入 / 输 出   | 说明                                |
|-----------|------------|-----------------------------------|
| memPool   | 输出         | 内存池实例。类型定义请参见 aclrtMemPool 。      |
| poolProps | 输入         | 内存池配置。类型定义请参见 aclrtMemPoolProps 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
