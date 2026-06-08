# 函数： kernel\_args\_get\_place\_holder\_buffer

> **Section**: 2.15.13


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

根据用户指定的内存大小，获取 param\_handle 占位符指向的内存地址。

## ● C 函数原型

aclError aclrtKernelArgsGetPlaceHolderBuffer(aclrtArgsHandle argsHandle, aclrtParamHandle paramHandle, size\_t dataSize, void **bufferAddr)

- python 函数

buffer\_addr, ret = acl.rt.kernel\_args\_get\_place\_holder\_buffer(args\_handle, param\_handle, data\_size)

| 参数名           | 说明                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------|
| args_handle   | int ，参数列表句柄。                                                                                  |
| param_handl e | int ，参数句柄。 此处的 param_handle 需与 acl.rt.kernel_args_append_place_holder 接口中的 param_handle 保持一致。 |

## 返回值说明

| 返回值         | 说明                                                           |
|-------------|--------------------------------------------------------------|
| buffer_addr | int ， param_handle 占位符指向的内存地址。 后续由用户管理该内存中的数据，但无需管理该内存的生命周期。 |
| ret         | int ，返回 0 表示成功，返回其他值表示失败。                                    |
