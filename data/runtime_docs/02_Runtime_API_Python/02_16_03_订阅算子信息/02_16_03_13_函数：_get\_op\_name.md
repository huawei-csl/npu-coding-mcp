# 函数： get\_op\_name

> **Section**: 2.16.3.13


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

获取指定算子的算子名称。

建议用户新建一个线程，在新线程内调用该接口，否则可能阻塞主线程中的其它任务 调度。

acl.prof.get\_op\_name 和 acl.prof.get\_op\_name\_v2 接口功能一致，但 acl.prof.get\_op\_name\_v2 接口会获取算子名称长度，并分配相应的空间，不需要用户 传参来指定算子名称所需空间大小，建议优先使用 acl.prof.get\_op\_name\_v2 接口。

- C 函数原型

aclError aclprofGetOpName(const void *opInfo, size\_t opInfoLen, uint32\_t index, char *opName, size\_t opNameLen)

- python 函数

op\_name, ret = acl.prof.get\_op\_name(op\_info, op\_info\_len, index, op\_name\_len)

| 参数名         | 说明                                                                                        |
|-------------|-------------------------------------------------------------------------------------------|
| op_info     | int ，指定算子信息的内存地址。                                                                         |
| op_info_len | int ，算子信息的长度。                                                                             |
| index       | int ，指定获取第几个算子的算子名称。 用户调用 acl.prof.get_op_num 接口获取算子数量后，这个 index 的取值范围： [0, ( 算子数量 -1)] 。 |

## 返回值说明

| 返回值     | 说明                                  |
|---------|-------------------------------------|
| op_name | str ，算子名称。                          |
| ret     | int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。 |
