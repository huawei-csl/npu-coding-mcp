# 函数： reset\_device\_force

> **Section**: 2.7.4


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

复位当前运算的 Device ，释放 Device 上的资源。释放的资源包括默认 Context 、默认 Stream 以及默认 Context 下创建的所有 Stream 。若默认 Context 或默认 Stream 下的任务 还未完成，系统会等待任务完成后再释放。

acl.rt.reset\_device\_force 接口可与 acl.rt.set\_device 接口配对使用，也可不与 aclrtSetDevice 接口配对使用，若不配对使用，一个进程中，针对同一个 Device ，调用 一次或多次 acl.rt.set\_device 接口后，仅需调用一次本接口可释放 Device 上的资源。

- # 与 acl.rt.set\_device 接口配对使用： acl.rt.set\_device(1) -&gt; acl.rt.reset\_device\_force(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device\_force(1)

# 与 acl.rt.set\_device 接口不配对使用：

acl.rt.set\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device\_force(1)

- C 函数原型

aclError aclrtResetDeviceForce(int32\_t deviceId)

- python 函数

ret=acl.rt.reset\_device\_force(device\_id)

| 参数名       | 说明                |
|-----------|-------------------|
| device_id | int ， Device 设备号。 |

## 返回值说明

## 约束说明

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

- 多线程场景下，针对同一个 Device ，如果每个线程中都调用 acl.rt.set\_device 接 口、 acl.rt.reset\_device\_force 接口，如下所示，线程 2 中的 acl.rt.reset\_device\_force 接口会返回报错，因为线程 1 中 acl.rt.reset\_device\_force 接口已经释放了 Device 1 的资源：

时间线

------------------------------------------------------------------------------&gt;

线程 1 ：

acl.rt.set\_device(1)  acl.rt.reset\_device\_force(1)

线程 2 ：

acl.rt.set\_device(1)                                acl.rt.reset\_device\_force(1)

多线程场景下，正确方式是应在线程执行的最后，调用一次 acl.rt.reset\_device\_force 释放 Device 资源，如下所示：

时间线

------------------------------------------------------------------------------&gt;

acl.rt.set\_device(1)                                acl.rt.reset\_device\_force(1)

线程 1 ：

acl.rt.set\_device(1)

线程 2 ：

- acl.rt.reset\_device 接口与 acl.rt.reset\_device\_force 接口可以混用，但混用时，若 两个 Reset 接口的调用次数、调用顺序不对，接口会返回报错。 # 混用时的正确方式：

# 两个 Reset 接口都分别与 Set 接口配对使用，且 acl.rt.reset\_device\_force 接口在 acl.rt.reset\_device 接口之后 acl.rt.set\_device(1) -&gt; acl.rt.reset\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device\_force(1) acl.rt.set\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device(1) -&gt; acl.rt.reset\_device\_force(1)

## # 混用时的错误方式：

# 当引用计数减到 0 时，会真正释放 Device 上的资源，此时再调用 acl.rt.reset\_device 或 acl.rt.reset\_device\_force 接口都会报错

# acl.rt.reset\_device 接口内部涉及引用计数的实现，当 acl.rt.reset\_device 接口每被调用一次，则该引用计 数减 1 ，

acl.rt.set\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device(1) -&gt; acl.rt.reset\_device(1) -&gt; acl.rt.reset\_device\_force(1)

# acl.rt.reset\_device\_force 接口在 acl.rt.reset\_device 接口之后，否则接口返回报错 acl.rt.set\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device\_force(1) -&gt; acl.rt.reset\_device(1)

acl.rt.set\_device(1) -&gt; acl.rt.set\_device(1) -&gt; acl.rt.reset\_device(1) -&gt; acl.rt.reset\_device\_force(1) -&gt; acl.rt.reset\_device\_force(1)
