# aclrtBinaryLoadFromFile

> **Section**: 1.16.2


## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

从文件加载并解析算子二进制文件，输出指向算子二进制的 binHandle 。

对于 AI Core 算子，若使用本接口加载并解析算子二进制文件，需配套使用 aclrtLaunchKernelWithConfig 、 aclrtLaunchKernelV2 或 aclrtLaunchKernelWithHostArgs 接口下发计算任务。

aclError aclrtBinaryLoadFromFile(const char* binPath, aclrtBinaryLoadOptions *options, aclrtBinHandle *binHandle)

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

| 参数名       | 输入 / 输 出   | 说明                                                                 |
|-----------|------------|--------------------------------------------------------------------|
| binPath   | 输入         | 算子二进制文件（ *.o 文件）的路径，要求绝对路径。 对于 AI CPU 算子，该参数支持传算子信息库文件 （ *.json ）。 |
| options   | 输入         | 加载算子二进制文件的可选参数。类型定义请参见 aclrtBinaryLoadOptions 。                    |
| binHandle | 输出         | 标识算子二进制的句柄。类型定义请参见 aclrtBinHandle 。                                |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

针对某一型号的产品，编译生成的算子二进制文件，必须在相同型号的产品上使用。

接口调用示例，参见 AI Core 自定义算子加载。
