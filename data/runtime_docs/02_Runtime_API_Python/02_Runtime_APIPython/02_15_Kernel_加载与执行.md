# Kernel 加载与执行

> **Section**: 2.15


| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取当前线程的 Runtime （运行时管理模块）错误码，获取后清空当前线程的错误 码，这时在线程中无新增错误码之前，调用本接口获取到的是表示成功的返回码 ACL\_SUCCESS 。

- C 函数原型

aclError aclrtGetLastError(aclrtLastErrLevel level)

- python 函数
- ret = acl.rt.get\_last\_error(level)

| 参数名   | 说明                                                     |
|-------|--------------------------------------------------------|
| level | int ，指定获取错误码的级别，当前仅支持线程级别。参考 2.19.29 aclrtLastErrLevel |
