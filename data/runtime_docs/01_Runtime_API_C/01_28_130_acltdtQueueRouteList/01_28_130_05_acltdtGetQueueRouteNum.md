# acltdtGetQueueRouteNum

> **Section**: 1.28.130.5


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

从队列路由配置数组中获取路由数量。

size\_t acltdtGetQueueRouteNum(const acltdtQueueRouteList *routeList)

| 参数名       | 输入 / 输 出   | 说明                                                                          |
|-----------|------------|-----------------------------------------------------------------------------|
| routeList | 输入         | 队列路由配置数组。 需提前调用 acltdtCreateQueueRouteList 接口创建 acltdtQueueRouteList 类型的数据。 |

返回路由数量。
