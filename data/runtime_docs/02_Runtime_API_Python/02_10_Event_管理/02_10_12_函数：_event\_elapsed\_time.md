# 函数： event\_elapsed\_time

> **Section**: 2.10.12


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

统计两个 Event 之间的耗时。

- C 函数原型

aclError aclrtEventElapsedTime(float *ms, aclrtEvent startEvent, aclrtEvent endEvent)

- python 函数

ms, ret = acl.rt.event\_elapsed\_time(start, end)

| 参数名   | 说明                       |
|-------|--------------------------|
| start | int ，指定起始 Event 对象的指针地址。 |
| end   | int ，指定结尾 Event 对象的指针地址。 |

## 返回值说明

## 约束说明

接口调用顺序：调用 acl.rt.create\_event / acl.rt.create\_event\_with\_flag 接口创建 event--&gt; 调用 acl.rt.record\_event 接口在同一个 stream 中记录起始 event 、结尾 event--&gt; 调用 acl.rt.synchronize\_stream 接口阻塞应用程序运行，直到指定 Stream 中的所有 任务都完成 --&gt; 调用 acl.rt.event\_elapsed\_time 接口统计两个 Event 之间的耗时。
