# 函数： create\_step\_info

> **Section**: 2.16.4.2


## 产品支持情况

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 推理系列产品           | √      |
| Atlas 200I/500 A2 推理产品 | √      |

利用单算子加载与执行接口实现训练的场景下，使用本接口用于标记迭代开始与结束 时间，为后续 Profiling 解析提供迭代标识，以便以迭代为粒度展示性能数据。

- C 函数原型

aclError aclprofGetStepTimestamp(aclprofStepInfo* stepInfo, aclprofStepTag tag, aclrtStream stream)

- python 函数

ret =acl.prof.get\_step\_timestamp(stepinfo, tag, stream)

| 参数名      | 说明                                                                       |
|----------|--------------------------------------------------------------------------|
| stepinfo | int ，指定迭代信息。需提前调用 acl.prof.create_step_info 接口创 建 aclprofStepInfo 类型的数据。 |
| tag      | int ，用于标记迭代开始或结束。在迭代开始时传入 ACL_STEP_START ，迭代结束时需传入 ACL_STEP_END 。        |
| stream   | int ，指定 Stream 。                                                         |

| 产品            | 是否支持   |
|---------------|--------|
| Atlas 350 加速卡 | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

创建 aclprofStepInfo 对象，用于描述迭代信息。

- C 函数原型

aclprofStepInfo* aclprofCreateStepInfo(void)

- python 函数

info = acl.prof.create\_step\_info()

无

| 返回值   | 说明                                                                           |
|-------|------------------------------------------------------------------------------|
| info  | int ， aclprofStepInfo 类型指针地址。 ● 返回 aclprofStepInfo 类型，表示成功。 ● 返回 None ，表示失败。 |

- 使用 acl.prof.destroy\_step\_info 接口销毁 aclprofStepInfo 类型的数据，如不销毁会 导致内存未被释放。
- 与 acl.prof.destroy\_step\_info 接口配对使用，先调用 acl.prof.create\_step\_info 接 口再调用 acl.prof.destroy\_step\_info 接口。
- 同一个 aclprofStepInfo 对象、同一个 tag 只能设置一次，否则 Profiling 解析会出 错。
