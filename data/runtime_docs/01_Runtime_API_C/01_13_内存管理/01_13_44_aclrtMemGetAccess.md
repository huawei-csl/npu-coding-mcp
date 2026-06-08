# aclrtMemGetAccess

> **Section**: 1.13.44


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

获取内存的访问权限。

aclError aclrtMemGetAccess(void *virPtr, aclrtMemLocation *location, uint64\_t *flag)

## 参数说明

## 返回值说明

| 参数名      | 输入 / 输 出   | 说明                                                                                                                                                                                                                       |
|----------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| virPtr   | 输入         | 虚拟内存的起始地址。 必须与 aclrtMapMem 接口的 virPtr 地址相同。                                                                                                                                                                              |
| location | 输入         | 内存所在位置。类型定义请参见 aclrtMemLocation 。 当前仅支持将 aclrtMemLocation.type 设置为 ACL_MEM_LOCATION_TYPE_HOST 或 ACL_MEM_LOCATION_TYPE_DEVICE 。当 aclrtMemLocation.type 为 ACL_MEM_LOCATION_TYPE_HOST 时， aclrtMemLocation.id 无效，固定设置为 0 即可。 |
| flag     | 输出         | 内存访问保护标志。                                                                                                                                                                                                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
