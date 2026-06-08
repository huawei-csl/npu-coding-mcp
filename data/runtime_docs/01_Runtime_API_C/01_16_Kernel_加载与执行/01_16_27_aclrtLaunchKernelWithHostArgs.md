# aclrtLaunchKernelWithHostArgs

> **Section**: 1.16.27


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

aclError aclrtLaunchKernelWithHostArgs(aclrtFuncHandle funcHandle, uint32\_t numBlocks, aclrtStream stream, aclrtLaunchKernelCfg *cfg, void *hostArgs, size\_t argsSize, aclrtPlaceHolderInfo *placeHolderArray, size\_t placeHolderNum)

| 参数名        | 输入 / 输 出   | 说明                                                          |
|------------|------------|-------------------------------------------------------------|
| funcHandle | 输入         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。                             |
| numBlocks  | 输入         | 指定核函数将会在几个核上执行。                                             |
| stream     | 输入         | 指定执行任务的 Stream 。类型定义请参见 aclrtStream 。                       |
| cfg        | 输入         | 任务下发的配置信息。类型定义请参见 aclrtLaunchKernelCfg 。 不指定配置时，此处可传 NULL 。 |

## 返回值说明

## 接口调用示例

## 参考资源

| 参数名               | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                            |
|-------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hostArgs          | 输入         | 存放核函数所有入参数据的 Host 内存地址指针。                                                                                                                                                                                                                                                                                                     |
| argsSize          | 输入         | hostArgs 参数值的大小，单位为 Byte 。                                                                                                                                                                                                                                                                                                    |
| placeHolder Array | 输入         | placeholder 参数数组。 aclrtPlaceHolderInfo 定义如下： typedef struct { uint32_t addrOffset; uint32_t dataOffset; } aclrtPlaceHolderInfo; 成员变量说明如下： ● addrOffset ： placeholder 指向的数据区拷贝到 Device 后，其真实 Device 内存地址在 launch 时需要刷新到 hostArgs 中，该参数用于指定需刷新的位置偏移 ● dataOffset ： placeholder 指向的数据区需拷贝到 Device 侧，该参数用于指定数据区基于 hostArgs 的地 址偏移 |
| placeHolder Num   | 输入         | placeholder 参数数组的大小。                                                                                                                                                                                                                                                                                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见 AI Core 自定义算子加载。

下表的几个接口都用于启用对应算子的计算任务，但功能和使用方式有所不同：

| 接口                           | 核函数参数值的传 入方式                        | 核函数参数值的 存放位置   | 是否可指定任务 下发的配置信息   |
|------------------------------|-------------------------------------|----------------|-------------------|
| aclrtLaunchKernel            | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 否                 |
| aclrtLaunchKernelV 2         | 在接口中指定存放 核函数所有入参数 据的 Device 内存地 址指针 | Device 内存      | 是                 |
| aclrtLaunchKernelW ithConfig | 在接口中指定参数 列表句柄 aclrtArgsHandle       | Host 内存        | 是                 |

| 接口                             | 核函数参数值的传 入方式                      | 核函数参数值的 存放位置   | 是否可指定任务 下发的配置信息   |
|--------------------------------|-----------------------------------|----------------|-------------------|
| aclrtLaunchKernelW ithHostArgs | 在接口中指定存放 核函数所有入参数 据的 Host 内存地址 指针 | Host 内存        | 是                 |
