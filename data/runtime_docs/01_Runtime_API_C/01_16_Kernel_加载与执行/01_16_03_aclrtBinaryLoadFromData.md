# aclrtBinaryLoadFromData

> **Section**: 1.16.3


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

从内存加载并解析算子二进制数据，输出指向算子二进制的 binHandle 。

调用本接口用于加载 AI CPU 算子信息（ aclrtBinaryLoadOption.type 包含 ACL\_RT\_BINARY\_LOAD\_OPT\_CPU\_KERNEL\_MODE ）时，还需配合使用 aclrtRegisterCpuFunc 接口注册 AI CPU 算子。

## 函数原型

## 参数说明

## 返回值说明

注意，系统仅将算子加载至当前 Context 所对应的 Device 上，因此在调用 aclrtLaunchKernelWithConfig 接口启动算子计算任务时，所在的 Device 必须与算子 加载时的 Device 相同。

aclError aclrtBinaryLoadFromData(const void *data, size\_t length, const aclrtBinaryLoadOptions *options, aclrtBinHandle *binHandle)

| 参数名       | 输入 / 输 出   | 说明                                              |
|-----------|------------|-------------------------------------------------|
| data      | 输入         | 存放算子二进制数据的 Host 内存地址，不能为空。                      |
| length    | 输入         | 算子二进制数据的内存大小，必须大于 0 ，单位 Byte 。                  |
| options   | 输入         | 加载算子二进制文件的可选参数。类型定义请参见 aclrtBinaryLoadOptions 。 |
| binHandle | 输出         | 标识算子二进制的句柄。类型定义请参见 aclrtBinHandle 。             |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
