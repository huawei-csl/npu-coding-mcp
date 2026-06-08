# 函数： binary\_load\_from\_file

> **Section**: 2.15.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

从文件加载并解析算子二进制文件，输出指向算子二进制的 binHandle 。

对于 AI Core 算子，若使用本接口加载并解析算子二进制文件，需配套使用 acl.rt.launch\_kernel\_with\_config 接口下发计算任务。

## ● C 函数原型

aclError aclrtBinaryLoadFromFile(const char* binPath, aclrtBinaryLoadOptions *options, aclrtBinHandle *binHandle)

## ● python 函数

bin\_handle, ret = acl.rt.binary\_load\_from\_file(bin\_path, options)

| 参数名      | 说明                                                                          |
|----------|-----------------------------------------------------------------------------|
| bin_path | str ，算子二进制文件（ .o 文件）的路径，要求绝对路径。对于 AI CPU 算子，该参数支持传算子信息库文件（ .json ）。         |
| options  | list ，加载算子二进制文件的可选参数，结构参考 aclrtBinaryLoadOptions ，若参数为空，可将 options 设置为 [] 。 |

| 返回值        | 说明               |
|------------|------------------|
| bin_handle | int ，标识算子二进制的句柄。 |

## 约束说明

针对某一型号的产品，编译生成的算子二进制文件，必须在相同型号的产品上使用。
