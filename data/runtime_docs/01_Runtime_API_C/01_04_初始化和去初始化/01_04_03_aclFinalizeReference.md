# aclFinalizeReference

> **Section**: 1.4.3


## 产品支持情况

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

去初始化函数，用于释放进程内 acl 接口使用的相关资源。

aclFinalizeReference 接口内部涉及引用计数的实现， aclInit 接口每被调用一次，则引 用计数加一， aclFinalizeReference 接口每被调用一次，则该引用计数减一，当引用计 数减到 0 时，才会真正去初始化。 aclFinalize 接口与本接口的区别在于，调用 aclFinalize 接口会将计数清零，直接去初始化。

aclError aclFinalizeReference(uint64\_t *refCount)

| 参数名      | 输入 / 输 出   | 说明                                                          |
|----------|------------|-------------------------------------------------------------|
| refCount | 输入 & 输 出   | 返回调用 aclFinalizeReference 后的引用计数。 若不需要获取引用计数，此处可传 nullptr 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

应用进程退出前，应确保已调用 aclFinalize 或 aclFinalizeReference 接口完成去初始 化，否则可能会导致异常，例如应用进程退出时有异常报错。

不建议在析构函数中调用 aclFinalize 或 aclFinalizeReference 接口，否则在进程退出时 可能由于单例析构顺序未知而导致进程异常退出的问题。
