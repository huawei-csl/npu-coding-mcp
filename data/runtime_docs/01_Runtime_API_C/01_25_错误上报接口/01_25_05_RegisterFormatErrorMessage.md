# RegisterFormatErrorMessage

> **Section**: 1.25.5


## 函数功能

## 函数原型

## 参数说明

## 返回值

按照规定的 json 格式，调用本接口给 CANN 注册预定义的错误码信息后，再调用 ReportPredefinedErrMsg 接口上报错误码。

int32\_t RegisterFormatErrorMessage(const char *error\_msg, size\_t error\_msg\_len)

同时为了方便使用，封装了宏 REG\_FORMAT\_ERROR\_MSG ，用户可直接使用该宏注 册，该宏直接定义静态变量注册，进程加载时就会完成注册。

#define REG\_FORMAT\_ERROR\_MSG (error\_msg, error\_msg\_len) \

REG\_FORMAT\_ERROR\_MSG\_UNIQ\_HELPER((error\_msg), (error\_msg\_len), \_\_COUNTER\_\_) #define REG\_FORMAT\_ERROR\_MSG\_UNIQ\_HELPER(error\_msg, error\_msg\_len, counter) \ REG\_FORMAT\_ERROR\_MSG\_UNIQ((error\_msg), (error\_msg\_len), counter) #define REG\_FORMAT\_ERROR\_MSG\_UNIQ(error\_msg, error\_msg\_len, counter) \ static const auto register\_error\_msg\_##counter ATTRIBUTE\_USED = []() -&gt; int32\_t { \ return error\_message::RegisterFormatErrorMessage((error\_msg), (error\_msg\_len)); \ }()

| 参数名            | 输入 / 输 出   | 说明                                             |
|----------------|------------|------------------------------------------------|
| error_ms g     | 输入         | 错误码信息，可一次注册多个错误码。 错误码信息需按 json 格式组织，示例请参见调用示例。 |
| error_ms g_len | 输入         | error_msg 长度，不包含末尾的 '\0' 。                     |

- 0 ：成功。

- -1 ：失败。

## 调用示例

error\_msg 错误码信息需按照 json 格式组织， error\_info\_list 是一个包含错误信息对象的 数组，至少需要包含一个元素，其中各字段含义如下：

- errClass ：错误分类。
- errTitle ：错误标题。
- ErrCode ：错误码。注意不要与当前已有的错误码重复，已有的错误码请参见《故 障处理》中的'错误码参考'。
- ErrMessage ：错误消息，可以包含格式化占位符 (%s) 。
- Arglist ：参数列表，用于说明 ErrMessage 中占位符对应的参数，参数列表长度与 ErrMessage 里格式化占位符个数必须相等。
- suggestion ：建议信息，包含：
- -Possible Cause ：可能的原因。
- -Solution ：解决方法。

```
#include <string> #include "base/err_msg.h" const std::string error_msg = R"( { "error_info_list": [ { "errClass": "GE Errors", "errTitle": "Invalid_Dynamic_Shape_Argument", "ErrCode": "E10018", "ErrMessage": "Value [%s] for shape [%s] is invalid. When [--dynamic_batch_size] is included, only batch size N can be -1 in [--input_shape].", "Arglist": "shape,index", "suggestion": { "Possible Cause": "When [--dynamic_batch_size] is included, only batch size N can be -1 in the shape.", "Solution": "Try again with a valid [--input_shape] argument. Make sure that non-batch size axes are not -1." } }, { "errClass": "GE Errors", "errTitle": "Invalid_--input_shape_Argument", "ErrCode": "E10019", "ErrMessage": "When [--dynamic_image_size] is included, only the height and width axes can be -1 in [--input_shape].", "Arglist": "", "suggestion": { "Possible Cause": "When [--dynamic_image_size] is included, only the height and width axes can be -1 in the shape.", "Solution": "Try again with a valid [--input_shape] argument. Make sure that axes other than height and width are not -1." } } ] } )"; REG_FORMAT_ERROR_MSG(error_msg.c_str(), error_msg.size());
```
