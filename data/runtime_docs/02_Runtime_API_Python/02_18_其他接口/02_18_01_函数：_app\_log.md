# 函数： app\_log

> **Section**: 2.18.1


## 产品支持情况

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

将日志记录到系统相应的日志文件中。

- C 函数原型 ACL\_APP\_LOG(aclLogLevel logLevel, const char *message)
- python 函数

acl.app\_log(log\_level, message)

## 功能说明

## 函数原型

## ● 场景举例：

- -两次模型执行，需要设置不同的 Dump 配置信息，接口调用顺序： acl.init 接 口 --&gt; acl.mdl.init\_dump 接口 --&gt; acl.mdl.set\_dump 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; acl.mdl.finalize\_dump 接口 --&gt; 模型卸载 --&gt; acl.mdl.init\_dump 接口 --&gt; acl.mdl.set\_dump 接口 --&gt; 模型加载 --&gt; 模型 执行 --&gt; acl.mdl.finalize\_dump 接口 --&gt; 模型卸载 --&gt; 执行其它任务 --&gt; acl.finalize 接口
- -同一个模型执行两次，第一次需要 Dump ，第二次无需 Dump ，接口调用顺 序： acl.init 接口 --&gt; acl.mdl.init\_dump 接口 --&gt; acl.mdl.set\_dump 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; acl.mdl.finalize\_dump 接口 --&gt; 模型卸载 --&gt; 模 型加载 --&gt; 模型执行 --&gt; 执行其它任务 --&gt; acl.finalize 接口

## 参数说明

## 返回值说明

| 参数名       | 说明                                                            |
|-----------|---------------------------------------------------------------|
| log_level | int ，设定日志级别。 ● 0 ： DEBUG ● 1 ： INFO ● 2 ： WARNING ● 3 ： ERROR |
| message   | str ，记录的日志信息。                                                 |

无
