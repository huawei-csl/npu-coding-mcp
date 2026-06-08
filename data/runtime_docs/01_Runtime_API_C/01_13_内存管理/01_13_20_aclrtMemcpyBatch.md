# aclrtMemcpyBatch

> **Section**: 1.13.20


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | ☓      |

## 实现批量内存复制。

本接口中的 Host 内存支持锁页内存（例如通过 aclrtMallocHost 接口申请的内存）、非 锁页内存（通过 malloc 接口申请的内存）。

aclError aclrtMemcpyBatch(void **dsts, size\_t *destMaxs, void **srcs, size\_t *sizes, size\_t numBatches, aclrtMemcpyBatchAttr *attrs, size\_t *attrsIndexes, size\_t numAttrs, size\_t *failIndex)

| 参数名           | 输入 / 输 出   | 说明                                                                                                                                                                                    |
|---------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dsts          | 输入         | 目的内存地址数组。                                                                                                                                                                             |
| destMax s     | 输入         | 内存复制最大长度数组，用于存放每一段要复制的内存的最 大长度，单位 Byte 。                                                                                                                                              |
| srcs          | 输入         | 源内存地址数组。                                                                                                                                                                              |
| sizes         | 输入         | 内存复制长度数组，用于存放每一段要复制的内存大小，单 位 Byte 。                                                                                                                                                   |
| numBatc hes   | 输入         | dsts 、 srcs 和 sizes 数组的长度。                                                                                                                                                            |
| attrs         | 输入         | 内存复制属性数组。类型定义请参见 aclrtMemcpyBatchAttr 。                                                                                                                                               |
| attrsInde xes | 输入         | 内存复制属性索引数组，用于指定 attrs 数组中每个条目适用 的复制范围。 attrs[k] 中指定的属性将应用于从 attrsIndexes[k] 到 attrsIndexes[k+1] - 1 的复制操作，同时 attrs[numAttrs-1] 将应用于从 attrsIndexes[numAttrs-1] 到 numBatches - 1 的复制操作。 |
| numAttrs      | 输入         | attrs 和 attrsIndexes 数组的长度。                                                                                                                                                           |
| failIndex     | 输出         | 用于发生错误时指示出错的复制项下标（仅支持对内存属性 和复制方向的校验）。若错误不涉及特定复制操作，该值将 为 SIZE_MAX 。                                                                                                                    |

## 返回值说明

## 约束说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

- 批次内的内存拷贝是无序的，不会按照数组中元素的顺序拷贝。
- 将 srcs 中指定的数据复制到 dsts 中指定的内存区域，每个复制操作的大小由 sizes 指 定， dsts 、 srcs 、 sizes 这三个数组必须具有 numBatches 指定的相同长度。
- 批处理中的每个复制操作必须与 attrs 数组中指定的属性集相关联， attrs 数组中的 每个条目可应用于多个复制操作，具体通过 attrsIndexes 数组指定对应属性条目生 效的起始复制索引。 attrs 和 attrsIndexes 这两个数组必须具有 numAttrs 指定的相 同长度。例如：若批处理包含 dsts/srcs/sizes 列出的 10 个复制操作，其中前 6 个使 用一组属性，后 4 个使用另一组属性，则 numAttrs 为 2 ， attrsIndexes 为 {0,6} ， attrs 包含两组属性。注意， attrsIndexes 的首个条目必须为 0 ，且每个条目必须大 于前一个条目，最后一个条目应小于 numBatches 。此外 numAttrs 必须小于等于 numBatches 。
- 批量内存复制的方向仅支持'从 Host 到 Device '或者'从 Device 到 Host '中的一 种。
