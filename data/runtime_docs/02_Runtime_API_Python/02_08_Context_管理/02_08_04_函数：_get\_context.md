# 函数： get\_context

> **Section**: 2.8.4


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

获取线程的 Context 。

- C 函数原型

aclError aclrtGetCurrentContext(aclrtContext context)

- python 函数

context, ret = acl.rt.get\_context()

无

| 返回值     | 说明                         |
|---------|----------------------------|
| context | int ，表示创建的 Context 对象指针地址。 |

## 约束说明

如果用户多次调用 acl.rt.set\_context 接口设置当前线程的 Context ，则获取的是最后一 次设置的 Context 。
