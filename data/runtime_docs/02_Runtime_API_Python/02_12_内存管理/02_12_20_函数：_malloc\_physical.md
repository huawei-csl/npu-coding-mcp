# 函数： malloc\_physical

> **Section**: 2.12.20


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

申请 Host 或 Device 物理内存并返回一个物理内存 handle 。

本接口可配合 acl.rt.reserve\_mem\_address 接口（申请虚拟内存）、 acl.rt.map\_mem 接口（建立虚拟内存与物理内存之间的映射）使用，以便申请地址连 续的虚拟内存、最大化利用物理内存地址的目的。

本接口可配合 acl.rt.mem\_export\_to\_shareable\_handle 接口（导出物理内存 handle ）、 acl.rt.mem\_import\_from\_shareable\_handle （导入共享 handle ）使用， 用于实现多进程之间的物理内存共享。同时，也支持在共享物理内存时，使用虚拟内 存，请参见 acl.rt.mem\_export\_to\_shareable\_handle 接口处的说明。

Atlas 200/300/500 推理产品不支持该接口。

- C 函数原型

aclError aclrtMallocPhysical(aclrtDrvMemHandle *handle, size\_t size, const aclrtPhysicalMemProp *prop, uint64\_t flags)

## ● python 函数

handle, ret = acl.rt.malloc\_physical(size, prop, flags)

| 参数名   | 说明                                                                                                                        |
|-------|---------------------------------------------------------------------------------------------------------------------------|
| size  | int ，物理地址空间大小，单位 Byte 。 先调用 acl.rt.mem_get_allocation_granularity 接口获取内存申请粒 度，然后再调用本接口申请物理内存时 size 按获取到的内存申请粒度 对齐，以便节约内存。 |
| prop  | dict ，物理内存属性信息，具体请参见 2.19.42 aclrtPhysicalMemProp 。                                                                       |
| flags | int ，预留，当前仅支持设置为 0 。                                                                                                      |

## 返回值说明

## 约束说明

| 返回值    | 说明                            |
|--------|-------------------------------|
| handle | int ，存放物理内存信息的 handle 。       |
| ret    | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- Atlas 200I/500 A2 推理产品上， Ascend RC 形态不支持调用本接口。
- 针对 Atlas A3 训练系列产品 /Atlas A3 推理系列产品中的超节点产品，当内存所在 位置 prop["location"]["type"] = ACL\_MEM\_LOCATION\_TYPE\_HOST\_NUMA ，且 内存属性类型 prop["memAttr"] 为 P2P 选项（例如 ACL\_MEM\_P2P\_HUGE ）时，可 申请到的最大内存大小根据服务器型号、 Bios 版本会有所不同。建议通过 acl.rt.malloc\_physical 接口按内存规划尝试申请，以确认内存是否足够。
- 内存属性类型 prop["memAttr"] 当前仅支持如下选项：
- -ACL\_MEM\_NORMAL ：普通内存。
- -ACL\_MEM\_HUGE ： 2M 粒度对齐的大页内存。
- -ACL\_MEM\_HUGE1G ： 1G 粒度对齐的大页内存，仅支持 Device 。 仅 Atlas A3 训练系列产品 /Atlas A3 推理系列产品、 Atlas A2 训练系列产品 / Atlas A2 推理系列产品支持该类型。

其它型号当前不支持该类型。

- -ACL\_MEM\_P2P\_NORMAL ：用于 Device 间数据复制的普通内存。
- -ACL\_MEM\_P2P\_HUGE ：用于 Device 间数据复制的大页内存，内存申请粒度 为 2M 。
- -ACL\_MEM\_P2P\_HUGE1G ：用于 Device 间数据复制的大页内存，内存申请粒

仅 训练系列产品 推理系列产品中的部分互联形态支持该类

- 度为 1G ，仅支持 Device 。 Atlas A3 /Atlas A3 型，以接口实际返回情况为准。 其它型号当前不支持该类型。
- -ACL\_HBM\_MEM\_HUGE ： 2M 粒度对齐的大页内存。
- -ACL\_HBM\_MEM\_HUGE1G ： 1G 粒度对齐的大页内存，仅支持 Device 。 Atlas 350 加速卡支持该类型。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品、 Atlas A2 训练系列产品 / Atlas A2 推理系列产品支持该类型。

## 其它型号当前不支持该类型。

- -ACL\_HBM\_MEM\_NORMAL ：普通内存，接口内部会按照 ACL\_HBM\_MEM\_HUGE 类型申请大页内存。
- -ACL\_DDR\_MEM\_HUGE ：大页内存，仅支持 Host 内存。
- -ACL\_DDR\_MEM\_NORMAL ：普通内存，仅支持 Host 内存。
- -ACL\_DDR\_MEM\_P2P\_HUGE ：用于 Device 间数据复制的大页内存，仅支持 Host 内存。
- -ACL\_DDR\_MEM\_P2P\_NORMAL ：用于 Device 间数据复制的普通内存，仅支 持 Host 内存。
