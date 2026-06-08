# acltdtSetQueueRouteQueryInfo

> **Section**: 1.28.132.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

设置路由关系查询条件。

aclError acltdtSetQueueRouteQueryInfo(acltdtQueueRouteQueryInfo *param, acltdtQueueRouteQueryInfoParamType type, size\_t len, const void *value)

| 参数名   | 输入 / 输 出   | 说明                                                                                       |
|-------|------------|------------------------------------------------------------------------------------------|
| param | 输入 & 输 出   | 队列路由关系查询条件的指针。 需提前调用 acltdtCreateQueueRouteQueryInfo 创建 acltdtQueueRouteQueryInfo 类型的数据。 |
| type  | 输入         | 参数类型。类型定义请参见 acltdtQueueRouteQueryInfoParamType 。                                        |

## 返回值说明

| 参数名   | 输入 / 输 出   | 说明                                                                                                                                      |
|-------|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| len   | 输入         | 参数值的字节数。 ● 属性参数的类型为 *_UINT64 时，此处配置为 8 ； ● 属性参数的类型为 *_UINT32 时，此处配置为 4 ； ● 属性参数的类型为 *_PTR 时，若操作系统是 32 位，则 此处配置为 4 ；若操作系统是 64 位，则配置为 8 。 |
| value | 输入         | 参数值的指针。                                                                                                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
