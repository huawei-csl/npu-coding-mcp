# aclrtMemSetAccess

> **Section**: 1.13.43


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

设置内存的访问权限。

aclError aclrtMemSetAccess(void* virPtr, size\_t size, aclrtMemAccessDesc* desc, size\_t count)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名    | 输入 / 输 出   | 说明                                                         |
|--------|------------|------------------------------------------------------------|
| virPtr | 输入         | 虚拟内存的起始地址。 必须与 aclrtMapMem 接口的 virPtr 地址相同。                |
| size   | 输入         | 虚拟内存的长度。 必须与 aclrtMapMem 接口的 size 相同。                      |
| desc   | 输入         | 内存访问的配置信息，包含内存访问保护标志、内存所 在位置等。类型定义请参见 aclrtMemAccessDesc 。 |
| count  | 输入         | desc 数组长度。                                                 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见进程间通信。
