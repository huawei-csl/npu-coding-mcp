# aclrtRegisterCpuFunc

> **Section**: 1.16.14


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

若使用 aclrtBinaryLoadFromData 接口加载 AI CPU 算子二进制数据，还需配合使用本 接口注册 AI CPU 算子信息，得到对应的 funcHandle 。

本接口只用于 AI CPU 算子，其它算子会返回报错 ACL\_ERROR\_RT\_PARAM\_INVALID 。

aclError aclrtRegisterCpuFunc(const aclrtBinHandle handle, const char *funcName, const char *kernelName, aclrtFuncHandle *funcHandle)

| 参数名        | 输入 / 输 出   | 说明                                                                                     |
|------------|------------|----------------------------------------------------------------------------------------|
| handle     | 输入         | 算子二进制句柄。类型定义请参见 aclrtBinHandle 。 调用 aclrtBinaryLoadFromData 接口获取算子二进制句 柄，再将其作为入参传入本接口。 |
| funcName   | 输入         | 执行 AI CPU 算子的入口函数。不能为空。                                                                |
| kernelName | 输入         | AI CPU 算子的 opType 。不能为空。                                                               |
| funcHandle | 输出         | 函数句柄。类型定义请参见 aclrtFuncHandle 。                                                         |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
