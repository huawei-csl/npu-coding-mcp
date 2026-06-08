# acltdtGetSliceInfoFromItem

> **Section**: 1.19.1.8


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

用于输出 Tensor 分片信息。

使用场景： OutfeedEnqueueOpV2 算子由于其功能要求需申请 Device 上的大块内存存 放数据，在 Device 内存不足时，可能会导致内存申请失败，进而导致某些算子无法正 常执行，该场景下，用户可以调用本接口获取 Tensor 分片信息（分片数量、分片索 引），再根据分片信息拼接算子的 Tensor 数据。

aclError acltdtGetSliceInfoFromItem(const acltdtDataItem *dataItem, size\_t *sliceNum, size\_t* sliceId)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                      |
|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| dataItem | 输入         | acltdtDataItem 类型的指针。 acltdtDataItem 用于标识 一个业务上的 Tensor 。类型定义请参见 acltdtDataItem 。 需提前调用 acltdtCreateDataItem 接口创建 acltdtDataItem 类型的数据。 |
| sliceNum | 输出         | 单个 Tensor 被切片的数量。                                                                                                                       |
| sliceId  | 输出         | 被切片 Tensor 的数据段索引。                                                                                                                      |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
