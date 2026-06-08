# aclAppLog

> **Section**: 1.27.1


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

将日志记录到日志文件中。

acl 接口还提供了 ACL\_APP\_LOG 宏，封装 aclAppLog 接口，推荐用户调用 ACL\_APP\_LOG 宏，传入日志级别、日志描述、 fmt 中的可变参数。

#define ACL\_APP\_LOG(level, fmt, ...) \ aclAppLog(level, \_\_FUNCTION\_\_, \_\_FILE\_\_, \_\_LINE\_\_, fmt, ##\_\_VA\_ARGS\_\_)

void aclAppLog(aclLogLevel logLevel, const char *func, const char *file, uint32\_t line, const char *fmt, ...)

| 参数名      | 输入 / 输 出   | 说明                                                                                               |
|----------|------------|--------------------------------------------------------------------------------------------------|
| logLevel | 输入         | 日志级别。 typedef enum { ACL_DEBUG = 0, ACL_INFO = 1, ACL_WARNING = 2, ACL_ERROR = 3, } aclLogLevel; |
| func     | 输入         | 表示用户在哪个接口中调用 aclAppLog 接口，固定配置为 __FUNCTION__                                                     |
| file     | 输入         | 表示用户在哪个文件中调用 aclAppLog 接口，固定配置为 __FILE__                                                         |
| line     | 输入         | 表示用户在哪一行中调用 aclAppLog 接口，固定配置为 __LINE__                                                          |
| fmt      | 输入         | 日志描述。 在调用格式化函数时， fmt 中参数的类型、个数必须与实际 参数类型、个数保持一致。                                                 |
| ...      | 输入         | fmt 中的可变参数，根据日志内容添加。                                                                             |

无

## 调用示例

// 若 fmt 中存在可变参数，需提前定义 uint32\_t modelId = 1; ACL\_APP\_LOG(ACL\_INFO, "load model success, modelId is %u", modelId);
