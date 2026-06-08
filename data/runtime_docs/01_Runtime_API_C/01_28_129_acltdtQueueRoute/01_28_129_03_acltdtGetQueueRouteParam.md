# acltdtGetQueueRouteParam

> **Section**: 1.28.129.3


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取队列路由配置的相关信息，例如源队列 ID 、目标队列 ID 等。

aclError acltdtGetQueueRouteParam(const acltdtQueueRoute *route, acltdtQueueRouteParamType type, size\_t len, size\_t *paramRetSize, void *param)

## 参数说明

## 返回值说明

| 参数名           | 输入 / 输 出   | 说明                                                                                                                                |
|---------------|------------|-----------------------------------------------------------------------------------------------------------------------------------|
| route         | 输入         | 队列路由配置信息的指针。 需提前调用 acltdtCreateQueueRoute 接口创建 acltdtQueueRoute 类型的数据。                                                            |
| type          | 输入         | 路由参数类型。类型定义请参见 acltdtQueueRouteParamType 。                                                                                        |
| len           | 输入         | 参数值的字节数。 ● 参数的类型为 *_UINT64 时，此处配置为 8 ； ● 参数的类型为 *_UINT32 时，此处配置为 4 ； ● 参数的类型为 *_PTR 时，若操作系统是 32 位，则此处 配置为 4 ；若操作系统是 64 位，则配置为 8 。 |
| paramRetSiz e | 输出         | 实际返回的参数值字节数的指针。                                                                                                                   |
| param         | 输出         | 指向参数值的指针。                                                                                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
