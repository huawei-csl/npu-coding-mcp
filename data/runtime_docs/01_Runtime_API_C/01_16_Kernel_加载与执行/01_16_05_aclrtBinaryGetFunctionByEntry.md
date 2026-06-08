# aclrtBinaryGetFunctionByEntry

> **Section**: 1.16.5


须知：本接口为预留接口，暂不支持。

## 功能说明

## 函数原型

## 参数说明

aclError aclrtBinaryGetFunction(const aclrtBinHandle binHandle, const char *kernelName, aclrtFuncHandle *funcHandle)

| 参数名        | 输入 / 输 出   | 说明                                                                                                                 |
|------------|------------|--------------------------------------------------------------------------------------------------------------------|
| binHandle  | 输入         | 算子二进制句柄。类型定义请参见 aclrtBinHandle 。 调用 aclrtBinaryLoadFromFile 接口或 aclrtBinaryLoadFromData 接口获取算子二进制句柄， 再将其作为入参传入本接口。 |
| kernelName | 输入         | 核函数名称。                                                                                                             |
| funcHandle | 输出         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。                                                                                    |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

根据 Function Entry 获取核函数句柄。

对于同一个 binHandle ，首次调用 aclrtBinaryGetFunctionByEntry 接口时，会默认将 binHandle 关联的算子二进制数据拷贝至当前 Context 对应的 Device 上。

aclError aclrtBinaryGetFunctionByEntry(aclrtBinHandle binHandle, uint64\_t funcEntry, aclrtFuncHandle *funcHandle)

| 参数名       | 输入 / 输 出   | 说明                                                                                                                 |
|-----------|------------|--------------------------------------------------------------------------------------------------------------------|
| binHandle | 输入         | 算子二进制句柄。类型定义请参见 aclrtBinHandle 。 调用 aclrtBinaryLoadFromFile 接口或 aclrtBinaryLoadFromData 接口获取算子二进制句柄， 再将其作为入参传入本接口。 |

## 返回值说明

| 参数名        | 输入 / 输 出   | 说明                              |
|------------|------------|---------------------------------|
| funcEntry  | 输入         | 标识核函数的关键字。                      |
| funcHandle | 输出         | 核函数句柄。类型定义请参见 aclrtFuncHandle 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
