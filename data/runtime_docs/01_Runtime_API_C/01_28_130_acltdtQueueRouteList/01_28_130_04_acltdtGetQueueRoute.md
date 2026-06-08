# acltdtGetQueueRoute

> **Section**: 1.28.130.4


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

从队列路由配置数组中获取指定的队列路由配置信息。

aclError acltdtGetQueueRoute(const acltdtQueueRouteList *routeList, size\_t index, acltdtQueueRoute *route)

| 参数名       | 输入 / 输 出   | 说明                                                                          |
|-----------|------------|-----------------------------------------------------------------------------|
| routeList | 输入         | 队列路由配置数组。 需提前调用 acltdtCreateQueueRouteList 接口创建 acltdtQueueRouteList 类型的数据。 |
| index     | 输入         | 指定获取哪一个队列路由配置信息， index 编号从 0 开 始。                                           |
| route     | 输入 & 输 出   | 需添加的队列路由配置信息的指针。类型定义请参见 acltdtQueueRoute 。                                  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
