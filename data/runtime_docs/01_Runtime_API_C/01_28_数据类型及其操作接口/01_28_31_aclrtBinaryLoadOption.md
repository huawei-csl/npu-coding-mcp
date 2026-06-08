# aclrtBinaryLoadOption

> **Section**: 1.28.31


typedef struct { aclrtBinaryLoadOptionType type; aclrtBinaryLoadOptionValue value; } aclrtBinaryLoadOption;

加载算子二进制文件时，每个参数是由参数类型 aclrtBinaryLoadOption.type 及其对应 的参数值 aclrtBinaryLoadOption.value 组成，例如， aclrtBinaryLoadOption.type 为 ACL\_RT\_BINARY\_LOAD\_OPT\_LAZY\_LOAD 时， aclrtBinaryLoadOption.value 需根据 isLazyLoad 的取值来配置。

aclrtBinaryLoadOption.type 的定义请参见 aclrtBinaryLoadOptionType 。

aclrtBinaryLoadOption.value 的定义请参见 aclrtBinaryLoadOptionValue 。
