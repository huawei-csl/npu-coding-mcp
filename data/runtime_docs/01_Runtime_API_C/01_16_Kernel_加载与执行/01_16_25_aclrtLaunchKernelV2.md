# aclrtLaunchKernelV2

> **Section**: 1.16.25


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

指定任务下发的配置信息，并启动对应算子的计算任务。异步接口。

aclError aclrtLaunchKernelV2(aclrtFuncHandle funcHandle, uint32\_t numBlocks, const void *argsData, size\_t argsSize, aclrtLaunchKernelCfg *cfg, aclrtStream stream)

| 参数名        | 输入 / 输 出   | 说明                                                                                                              |
|------------|------------|-----------------------------------------------------------------------------------------------------------------|
| funcHandle | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。                                                                                 |
| numBlocks  | 输入         | 指定核函数将会在几个核上执行。                                                                                                 |
| argsData   | 输入         | 存放核函数所有入参数据的 Device 内存地址指针。 内存申请接口请参见 1.13 内存管理。 注意，执行本接口下发任务的 Device 需与 argsData 中使 用的 Device 内存要是同一个 Device 。 |
| argsSize   | 输入         | argsData 参数值的大小，单位为 Byte 。                                                                                      |
| cfg        | 输入         | 任务下发的配置信息。类型定义请参见 aclrtLaunchKernelCfg 。 不指定配置时，此处可传 NULL 。                                                     |
| stream     | 输入         | 指定执行任务的 Stream 。类型定义请参见 aclrtStream 。                                                                           |

## 返回值说明

## 参考资源

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

下表的几个接口都用于启用对应算子的计算任务，但功能和使用方式有所不同：

| 接口                             | 核函数参数值的传 入方式                        | 核函数参数值的 存放位置   | 是否可指定任务 下发的配置信息   |
|--------------------------------|-------------------------------------|----------------|-------------------|
| aclrtLaunchKernel              | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 否                 |
| aclrtLaunchKernelV 2           | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 是                 |
| aclrtLaunchKernelW ithConfig   | 在接口中指定参数 列表句柄 aclrtArgsHandle       | Host 内存        | 是                 |
| aclrtLaunchKernelW ithHostArgs | 在接口中指定存放 核函数所有入参数 据的 Host 内存地址 指针   | Host 内存        | 是                 |
