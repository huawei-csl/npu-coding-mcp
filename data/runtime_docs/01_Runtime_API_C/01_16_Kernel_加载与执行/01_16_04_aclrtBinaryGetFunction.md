# aclrtBinaryGetFunction

> **Section**: 1.16.4


## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

根据核函数名称，查找到对应的核函数，并使用 funcHandle 表达。

对于同一个 binHandle ，首次调用 aclrtBinaryGetFunction 接口时，会默认将 binHandle 关联的算子二进制数据拷贝至当前 Context 对应的 Device 上。

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

接口调用示例，参见 AI Core 自定义算子加载。
