# Profiling 数据采集接口

> **Section**: 2.16.1


启动对应 Kernel 的计算任务。仅支持 Ascend C 自定义算子。

## ● C 函数原型

aclError aclrtLaunchKernel(aclrtFuncHandle funcHandle, uint32\_t numBlocks, const void *argsData, size\_t argsSize, aclrtStream stream)

## ● python 函数

ret = acl.rt.launch\_kernel(func\_handle, num\_blocks, args\_data, args\_size, stream)

| 参数名         | 说明                                                                                         |
|-------------|--------------------------------------------------------------------------------------------|
| func_handle | int ，调用 acl.rt.binary_get_function 接口根据 kernel_name 获取 func_handle 。                       |
| num_blocks  | int ，指定核函数将会在几个核上执行。                                                                       |
| args_data   | int ，存放 Kernel 所有入参数据的 Device 内存地址指针。内存申请接 口请参见 2.12 内存管理。                                 |
| args_size   | int ， argsData 参数值的大小，单位为 Byte 。                                                           |
| stream      | int ，指定执行任务的 Stream ，可复用已创建的 Stream 节省资源或调 用 acl.rt.create_stream 接口创建 Stream ，再作为入参在此处传入。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
