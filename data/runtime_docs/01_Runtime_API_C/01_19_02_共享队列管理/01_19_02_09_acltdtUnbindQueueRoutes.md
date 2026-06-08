# acltdtUnbindQueueRoutes

> **Section**: 1.19.2.9


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

解绑定数据队列路由关系。

aclError acltdtUnbindQueueRoutes(acltdtQueueRouteList *qRouteList)

| 参数名        | 输入 / 输 出   | 说明                                                                                                |
|------------|------------|---------------------------------------------------------------------------------------------------|
| qRouteList | 输入 / 输 出   | 路由关系数组的指针，接口调用完成后返回路由去绑定 结果。类型定义请参见 acltdtQueueRouteList 。 可先通过 acltdtQueryQueueRoutes 获取路由关系数 组。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

只有当所有队列关系解绑定成功，本接口才会返回成功；任何一条解绑定失败，本接 口返回失败，如果您需要知道具体哪个路由关系解绑定失败，您可以先调用 acltdtGetQueueRoute 接口从路由关系数组中获取每一个路由关系，再调用 acltdtGetQueueRouteParam 接口查询绑定关系状态。
