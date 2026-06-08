# 函数： destroy\_context

> **Section**: 2.8.2


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 资源参考

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

销毁一个 Context ，释放 Context 的资源。只能销毁通过 acl.rt.create\_context 接口创建 的 Context 。

- C 函数原型

aclError aclrtDestroyContext(aclrtContext context)

- python 函数

ret = acl.rt.destroy\_context(context)

| 参数名     | 说明                           |
|---------|------------------------------|
| context | int ，指定需要销毁的 Context 对象指针地址。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

接口调用流程与示例，请参见运行时资源申请与释放、同步等待。
