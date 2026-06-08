# acltdtAddQueueRoute

> **Section**: 1.28.130.3


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

向队列路由配置数组中添加队列路由配置信息。

aclError acltdtAddQueueRoute(acltdtQueueRouteList *routeList, const acltdtQueueRoute *route)

| 参数名       | 输入 / 输 出   | 说明                                                                          |
|-----------|------------|-----------------------------------------------------------------------------|
| routeList | 输入 & 输 出   | 队列路由配置数组。 需提前调用 acltdtCreateQueueRouteList 接口创建 acltdtQueueRouteList 类型的数据。 |
| route     | 输入         | 需添加的队列路由配置信息的指针。 需提前调用 acltdtCreateQueueRoute 接口创建 acltdtQueueRoute 类型的数据。  |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
