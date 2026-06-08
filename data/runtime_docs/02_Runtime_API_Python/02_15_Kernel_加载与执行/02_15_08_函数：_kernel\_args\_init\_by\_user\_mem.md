# 函数： kernel\_args\_init\_by\_user\_mem

> **Section**: 2.15.8


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |

根据核函数句柄初始化参数列表，并获取标识参数列表的句柄。

与 acl.rt.kernel\_args\_init\_by\_user\_mem 接口的区别在于，调用本接口表示由系统管 理内存。

- C 函数原型

aclError aclrtKernelArgsInit(aclrtFuncHandle funcHandle, aclrtArgsHandle *argsHandle)

- python 函数

args\_handle, ret = acl.rt.kernel\_args\_init(func\_handle)

| 参数名         | 说明                                                               |
|-------------|------------------------------------------------------------------|
| func_handle | int ，核函数句柄。 调用 acl.rt.binary_get_function 获取核函数句柄，再将其作为入参 传入本接口。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 训练系列产品           | √      |
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

根据核函数句柄初始化参数列表，并获取标识参数列表的句柄。

与 acl.rt.kernel\_args\_init 接口的区别在于，调用本接口表示由用户管理内存。

- C 函数原型

aclError aclrtKernelArgsInitByUserMem(aclrtFuncHandle funcHandle, aclrtArgsHandle argsHandle, void *userHostMem, size\_t actualArgsSize)

## ● python 函数

ret = acl.rt.kernel\_args\_init\_by\_user\_mem(func\_handle, args\_handle, user\_host\_mem, actual\_args\_size)

| 参数名               | 说明                                                                                                   |
|-------------------|------------------------------------------------------------------------------------------------------|
| func_handle       | int ，核函数句柄。 调用 acl.rt.binary_get_function 获取核函数句柄，再将其作为入参 传入本接口。                                     |
| args_handle       | int ，参数列表句柄。 需提前调用 acl.rt.kernel_args_get_handle_mem_size 接口获取内 存大小，申请 Host 内存，再将 Host 内存地址作为入参传入此处。 |
| user_host_m em    | int ， Host 内存地址。 需提前调用 acl.rt.kernel_args_get_mem_size 接口获取内存大小， 申请 Host 内存，再将 Host 内存地址作为入参传入此处。    |
| actual_args_ size | int ，内存大小。 需提前调用 acl.rt.kernel_args_get_mem_size 接口获取内存大小， 再将其作为入参传入此处。                              |

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
