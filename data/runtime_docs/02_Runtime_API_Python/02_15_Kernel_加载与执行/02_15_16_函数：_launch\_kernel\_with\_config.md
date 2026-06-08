# 函数： launch\_kernel\_with\_config

> **Section**: 2.15.16


## 产品支持情况

## 功能说明

## 函数原型

| 参数名         | 说明           |
|-------------|--------------|
| args_handle | int ，参数列表句柄。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

指定任务下发的配置信息，并启动对应算子的计算任务。异步接口。

若使用本接口下发 AI Core 算子的计算任务，需配套使用 acl.rt.binary\_load\_from\_file 接口加载并解析算子二进制文件。

- C 函数原型 aclError aclrtLaunchKernelWithConfig(aclrtFuncHandle funcHandle, uint32\_t numBlocks, aclrtStream stream, aclrtLaunchKernelCfg *cfg, aclrtArgsHandle argsHandle, void *reserve)
- python 函数
- ret = acl.rt.launch\_kernel\_with\_config(func\_handle, num\_blocks, stream, cfg, args\_handle, reserve)

## 参数说明

## 返回值说明

| 返回值   | 说明                        |
|-------|---------------------------|
| ret   | int ，返回 0 表示成功，返回其他值表示失败。 |
