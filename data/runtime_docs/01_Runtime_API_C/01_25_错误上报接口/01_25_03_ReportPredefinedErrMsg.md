# ReportPredefinedErrMsg

> **Section**: 1.25.3


## 函数功能

## 函数原型

用于上报 CANN 预定义好的用户类错误信息。

- 不带参数的错误码信息：

int32\_t ReportPredefinedErrMsg(const char *error\_code)

- 带参数的错误码信息：

int32\_t ReportPredefinedErrMsg(const char *error\_code, const std::vector&lt;const char *&gt; &amp;key, const std::vector&lt;const char *&gt; &amp;value)

## 针对该接口，还提供了封装该接口的宏 REPORT\_PREDEFINED\_ERR\_MSG ，宏定义如 下：

```
#define REPORT_PREDEFINED_ERRMSG_CHOOSER(_1, _2, _3, NAME, ...) NAME #define REPORT_PREDEFINED_ERRMSG_1PARAMS(error_code) error_message::ReportPredefinedErrMsg(error_code) #define REPORT_PREDEFINED_ERRMSG_3PARAMS(error_code, key, value)                                                       \ error_message::ReportPredefinedErrMsg((error_code), (key), (value)) #define REPORT_PREDEFINED_ERR_MSG (...)                                                                                 \ REPORT_PREDEFINED_ERRMSG_CHOOSER(__VA_ARGS__, REPORT_PREDEFINED_ERRMSG_3PARAMS, ,                                    \ REPORT_PREDEFINED_ERRMSG_1PARAMS)(__VA_ARGS__)
```

## 参数说明

## 返回值

| 参数名         | 输入 / 输 出   | 说明                                                                                                                                               |
|-------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| error_co de | 输入         | 错误码以 6 位字符形式体现，例如 E10001 ，其中，第 1 位表 示级别，分为 E 、 W 、 I ，分别表示错误、告警、提示类；第 2 位表示模块；后 4 位表示错误码， 0000~8999 为用户类错 误。 CANN 预定义好的用户类错误可参见《故障处理》中的'错 误码参考'。 |
| key         | 输入         | 预定义的参数。 每个错误码支持的参数可查看 error_code.json 文件中的 Arglist 字段。                                                                                           |
| value       | 输入         | 参数 key 中参数对应的实际值。 这些实际值会替换 error_code.json 文件中 ErrMessage 字段的 占位符，得到最终的错误码信息。                                                                    |

- 0 ：成功。

- -1 ：失败。
