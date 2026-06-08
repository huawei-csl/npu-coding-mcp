# aclrtLaunchKernelWithConfig

> **Section**: 1.16.26


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

指定任务下发的配置信息，并启动对应算子的计算任务。异步接口。

## 函数原型

## 参数说明

## 返回值说明

## 参考资源

若使用本接口下发 AI Core 算子的计算任务，需配套使用 aclrtBinaryLoadFromFile 接 口加载并解析算子二进制文件。

aclError aclrtLaunchKernelWithConfig(aclrtFuncHandle funcHandle, uint32\_t numBlocks, aclrtStream stream, aclrtLaunchKernelCfg *cfg, aclrtArgsHandle argsHandle, void *reserve)

| 参数名        | 输入 / 输 出   | 说明                                                          |
|------------|------------|-------------------------------------------------------------|
| funcHandle | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。                             |
| numBlocks  | 输入         | 指定核函数将会在几个核上执行。                                             |
| stream     | 输入         | 指定执行任务的 Stream 。类型定义请参见 aclrtStream 。                       |
| cfg        | 输入         | 任务下发的配置信息。类型定义请参见 aclrtLaunchKernelCfg 。 不指定配置时，此处可传 NULL 。 |
| argsHandle | 输入         | 参数列表句柄。类型定义请参见 aclrtArgsHandle 。                            |
| reserve    | 输入         | 预留参数。当前固定传 NULL 。                                           |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

下表的几个接口都用于启用对应算子的计算任务，但功能和使用方式有所不同：

| 接口                           | 核函数参数值的传 入方式                        | 核函数参数值的 存放位置   | 是否可指定任务 下发的配置信息   |
|------------------------------|-------------------------------------|----------------|-------------------|
| aclrtLaunchKernel            | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 否                 |
| aclrtLaunchKernelV 2         | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 是                 |
| aclrtLaunchKernelW ithConfig | 在接口中指定参数 列表句柄 aclrtArgsHandle       | Host 内存        | 是                 |

| 接口                             | 核函数参数值的传 入方式                      | 核函数参数值的 存放位置   | 是否可指定任务 下发的配置信息   |
|--------------------------------|-----------------------------------|----------------|-------------------|
| aclrtLaunchKernelW ithHostArgs | 在接口中指定存放 核函数所有入参数 据的 Host 内存地址 指针 | Host 内存        | 是                 |
