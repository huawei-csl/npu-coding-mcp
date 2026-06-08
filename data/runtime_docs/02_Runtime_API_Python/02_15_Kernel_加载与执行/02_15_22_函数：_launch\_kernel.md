# 函数： launch\_kernel

> **Section**: 2.15.22


## 产品支持情况

对于同一个 bin\_handle ，首次调用 acl.rt.binary\_get\_function 接口时，会默认将 bin\_handle 关联的算子二进制数据拷贝至当前 Context 对应的 Device 上。

- C 函数原型

aclError aclrtBinaryGetFunction(const aclrtBinHandle binHandle, const char *kernelName, aclrtFuncHandle *funcHandle)

- python 函数

func\_handle, ret= acl.rt.binary\_get\_function(bin\_handle, kernel\_name)

| 参数名         | 说明                                                           |
|-------------|--------------------------------------------------------------|
| bin_handle  | int ，指向算子二进制的 handle 。调用 acl.rt.binary_load 接口获取 binHandle 。 |
| kernel_name | str ， kernel 名称。                                             |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

该接口是异步接口，调用接口成功仅表示任务下发成功，不表示任务执行成功。调用 该接口后，需调用同步等待接口（例如， acl.rt.synchronize\_stream ）确保任务已执 行完成。
