# 函数： set\_device

> **Section**: 2.7.1


## 产品支持情况

获取当前线程可使用的 Device 资源。

获取时，按照如下优先级返回 value ： Stream 级别的 Device 资源限制（调用 acl.rt.set\_stream\_res\_limit 接口设置） &gt; 当前进程的 Device 资源限制（调用 acl.rt.set\_device\_res\_limit 接口设置） &gt;AI 处理器硬件默认的资源限制。

- C 函数原型 aclError aclrtGetResInCurrentThread(aclrtDevResLimitType type, uint32\_t *value)
- python 函数

value, ret = acl.rt.get\_res\_in\_current\_thread(type)

| 参数名   | 说明                                                                          |
|-------|-----------------------------------------------------------------------------|
| type  | int ，资源类型，当前支持 Cube Core 、 Vector Core ，具体请参见新增 数据结构 aclrtDevResLimitType 。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

## 资源参考

| 产品                     | 是否支持   |
|------------------------|--------|
| Atlas 200I/500 A2 推理产品 | √      |

调用本接口会隐式创建默认 Context ，该默认 Context 中包含一个默认 Stream 。在同一 个进程的多个线程中，如果调用 aclrtSetDevice 接口并指定相同的 Device 用于计算，那 么这些线程将共享同一个默认 Context 。

但 Atlas 推理系列产品的 EP 标准形态除外，其隐式创建的默认 Context 中包含两个 Stream ：一个默认 Stream 和一个执行内部同步的 Stream 。

- C 函数原型

aclError aclrtSetDevice(int32\_t deviceId)

- python 函数

ret = acl.rt.set\_device(device\_id)

| 参数名       | 说明                                                                                                   |
|-----------|------------------------------------------------------------------------------------------------------|
| device_id | int ， Device 设备号。 用户调用 acl.rt.get_device_count 接口获取可用的 Device 数量后，取 值范围： [0, ( 可用的 Device 数量 - 1)] 。 |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

如果多次调用 acl.rt.set\_device 接口而不调用 acl.rt.reset\_device 接口释放本进程使用 的 Device 资源，功能上不会有问题，因为在进程退出时也会释放本进程使用的 Device 资源。建议 acl.rt.set\_device 接口和 acl.rt.reset\_device 接口配对使用，在不使用 Device 上资源时，通过调用 acl.rt.reset\_device 接口及时释放本进程使用的 Device 资 源。

在不同进程或线程中支持调用 acl.rt.set\_device 接口指定同一个 Device 用于运算。在同 一个进程中的多个线程中，如果调用 acl.rt.set\_device 接口指定同一个 Device 用于运 算，这时隐式创建的默认 Context 是同一个。

接口调用流程与示例，请参见运行时资源申请与释放、同步等待。
