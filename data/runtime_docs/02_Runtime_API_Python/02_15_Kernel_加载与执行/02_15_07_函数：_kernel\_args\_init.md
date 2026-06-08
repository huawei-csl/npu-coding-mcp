# 函数： kernel\_args\_init

> **Section**: 2.15.7


## 产品支持情况

若使用 acl.rt.binary\_load\_from\_data 接口加载 AI CPU 算子二进制数据，还需配合使 用本接口注册 AI CPU 算子信息，得到对应的 func\_handle 。本接口只用于 AI CPU 算 子，其它算子会返回报错 ACL\_ERROR\_RT\_PARAM\_INVALID 。

- C 函数原型

aclError aclrtRegisterCpuFunc(const aclrtBinHandle handle, const char *funcName, const char *kernelName, aclrtFuncHandle *funcHandle)

- python 函数

func\_handle, ret = acl.rt.register\_cpu\_func(bin\_handle, func\_name, kernel\_name)

| 参数名         | 说明                                                                      |
|-------------|-------------------------------------------------------------------------|
| bin_handle  | int ，算子二进制句柄。调用 acl.rt.binary_load_from_data 接口获 取算子二进制句柄，再将其作为入参传入本接口。 |
| func_name   | str ，执行 AI CPU 算子的入口函数。不能为空。                                            |
| kernel_name | str ， AI CPU 算子的 opType 。不能为空。                                          |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 返回值         | 说明                        |
|-------------|---------------------------|
| args_handle | int ，参数列表句柄。              |
| ret         | int ，返回 0 表示成功，返回其他值表示失败。 |
