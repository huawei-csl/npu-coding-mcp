# aclrtMemGetAddressRange

> **Section**: 1.13.47


## 产品支持情况

## 功能说明

## 函数原型

| 参数名    | 输入 / 输 出   | 说明                                                                                     |
|--------|------------|----------------------------------------------------------------------------------------|
| handle | 输入         | 存放物理内存信息的 handle 。类型定义请参见 aclrtDrvMemHandle 。 查询通过 aclrtMallocPhysical 接口申请的物理内存属性信 息。 |
| prop   | 输出         | 物理内存属性信息。类型定义请参见 aclrtPhysicalMemProp 。                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

获取待查询地址所属内存块的起始地址以及内存块大小。

aclError aclrtMemGetAddressRange(void *ptr, void **pbase, size\_t *psize)

## 参数说明

## 返回值说明

## 参考信息

| 使用场景                                                                           | aclrtMemGetAddressRange 接口行为   |
|--------------------------------------------------------------------------------|--------------------------------|
| 查询通过 aclrtMalloc 接口或 aclrtMallocWithCfg 接口返回的 Device 内 存                       | 返回内存块的起始地址和内存大小                |
| 查询通过 aclrtMallocHost 接口或 aclrtMallocHostWithCfg 接口返回的 Host 内存                  | 返回内存块的起始地址和内存大小。               |
| 查询通过 aclrtReserveMemAddress 、 aclrtMallocPhysical 、 aclrtMapMem 等 接口映射过的虚拟内存地址 | 返回经过映射的内存块的起始地址和内 存大小          |
