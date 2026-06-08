# 函数： get\_error\_code\_from\_exception\_info

> **Section**: 2.14.7


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取异常信息中的错误码。该接口与 acl.rt.set\_exception\_info\_callback 接口配合使 用。

- C 函数原型 uint32\_t aclrtGetErrorCodeFromExceptionInfo(const aclrtExceptionInfo *info)
- python 函数
- ret = acl.rt.get\_error\_code\_from\_exception\_info(info)

| 参数名   | 说明                                                                                                                                                              |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| info  | int ，异常信息 aclrtExceptionInfo 的指针地址。 在执行任务之前调用 acl.rt.set_exception_info_callback 接口，系 统会将产生异常的任务 ID 、 Stream ID 、线程 ID 、 Device ID 、错误 码存放在 aclExceptionInfo 中。 |

## 返回值说明

| 返回值   | 说明                                                                      |
|-------|-------------------------------------------------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败，返回值为 ' 0xFFFFFFFF '（以十六进制为例）时表示 Device 异常。 |
