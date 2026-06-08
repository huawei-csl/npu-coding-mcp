# aclFinalize

> **Section**: 1.4.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 接口调用示例

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

去初始化函数，用于释放进程内 acl 接口使用的相关资源。

对于涉及 Device 业务日志回传到 Host 的场景，本接口默认增加 2000ms 延时（实际最大 延时可达 2000ms ），以确保 ERROR 级别和 EVENT 级别日志完整回传，防止不丢失。您 可以将 ASCEND\_LOG\_DEVICE\_FLUSH\_TIMEOUT 环境变量设置为 0 （命令示例： export ASCEND\_LOG\_DEVICE\_FLUSH\_TIMEOUT=0 环境变量的详细描述请参见《环境变量参

），来取消该默认延时。关于 ASCEND\_LOG\_DEVICE\_FLUSH\_TIMEOUT 考》中的'日志 &gt; ASCEND\_LOG\_DEVICE\_FLUSH\_TIMEOUT '。

aclError aclFinalize()

无

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

应用进程退出前，应确保已调用 aclFinalize 或 aclFinalizeReference 接口完成去初始 化，否则可能会导致异常，例如应用进程退出时有异常报错。

不建议在析构函数中调用 aclFinalize 或 aclFinalizeReference 接口，否则在进程退出时 可能由于单例析构顺序未知而导致进程异常退出的问题。

接口调用示例，参见初始化。
