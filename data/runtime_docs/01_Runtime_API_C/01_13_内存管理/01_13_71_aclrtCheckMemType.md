# aclrtCheckMemType

> **Section**: 1.13.71


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |
| Atlas 推理系列产品           | √      |
| Atlas 训练系列产品           | √      |

检查 Device 内存类型。

aclError aclrtCheckMemType(void** addrList, uint32\_t size, uint32\_t memType, uint32\_t *checkResult, uint32\_t reserve)

| 参数名         | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| addrList    | 输入         | Device 内存地址数组。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| size        | 输入         | addrList 数组大小。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| memType     | 输入         | Device 内存类型。若 addrList 数组中有多种不同类型的内 存地址，则 memType 处需配置为多种内存类型位或，例 如配置为： RT_MEM_MASK_DEV_TYPE &#124; RT_MEM_MASK_DVPP_TYPE 当前支持设置为如下宏： ● ACL_RT_MEM_TYPE_DEV ：表示调用 aclrtMalloc 、 aclrtMallocWithCfg 等接口申请的 Device 内存。 ● ACL_RT_MEM_TYPE_DVPP ：表示 DVPP 专用的 Device 内存，可调用相关内存申请接口（例如 hi_mpi_dvpp_malloc ）申请该内存。 Atlas 350 加速 卡中不再有单独的 DVPP Device 内存类型，而是当做 普通 Device 内存处理。 ● ACL_RT_MEM_TYPE_RSVD ：表示调用 aclrtReserveMemAddress 接口预留的虚拟内存。 宏定义如下： #define ACL_RT_MEM_TYPE_DEV (0X2U) #define ACL_RT_MEM_TYPE_DVPP (0X8U) #define ACL_RT_MEM_TYPE_RSVD (0X10U) |
| checkResult | 输出         | 检查 addrList 数组中内存地址类型与 memType 处是否匹 配。 ● 1 ：匹配 ● 0 ：不匹配                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| reserve     | 输入         | 预留参数，当前固定配置为 0 。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## 返回值说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
