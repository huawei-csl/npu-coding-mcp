# hset\_flag &amp; hwait\_flag

> **Section**: 6.6.4


## 功能说明

## 接口原型

## 参数说明

为了减少同步延迟，提供了 hset 和 hwait 标志接口， hset\_flag 接口中的目的内存由接口 立即数指定，都放置在实际的生成者或消费者接口之前。这样可以在同步发生之前通 知硬件数据依赖的确切位置。接口的具体功能是，根据传入的内存和管道信息，在对 应接口完成相关内存的读写之后，立即获得该事件的型号，不必等待接口的其余部分 执行完成。

hset\_flag &amp; hwait\_flag 仅在 Cube 和 Fixpipe 之间（双向）、 Cube 和 Pipe MTE1 之间 （双向）使用。 hset\_flag 和 hwait\_flag 接口必须放置在相应的生产或消费接口之前， 其目标内存由接口的立即数 memory 指定，这样硬件可以在同步发生之前被告知数据 依赖关系的确切位置。

由于' set &amp; wait '标志必须成对出现，因此在循环体前后会插入多个'虚拟'的 ' set ' or ' wait '标志，接口引入了一个新的参数 v 来指示接口是否为虚拟接口。

void hset\_flag(pipe\_t pipe, pipe\_t tpipe, event\_t eventID, mem\_t memory, bool v) void hset\_flag(pipe\_t pipe, pipe\_t tpipe, uint64\_t eventID, mem\_t memory, bool v) void hwait\_flag(pipe\_t pipe, pipe\_t tpipe, uint64\_t eventID, mem\_t memory, bool v) void hwait\_flag(pipe\_t pipe, pipe\_t tpipe, event\_t eventID, mem\_t memory, bool v)

pipe\_t/event\_t 参数参考上一节。

表 6-33 hset/hwait 特有参数说明

| 参数名     | 说明                         |
|---------|----------------------------|
| memory  | 指定的依赖内存                    |
| v       | 虚拟指示器， 0 表示 valid ， 1 表示虚拟 |
| eventID | 2bit 事件 ID ，仅支持 4 个事件 ID 。 |

表 6-34 mem\_t 枚举量

| 枚举名   |   枚举值 |
|-------|-------|
| L1    |     0 |
| L0A   |     1 |
| L0B   |     2 |
| L0C   |     3 |
| UB    |     4 |
| BT    |     5 |

## 流水类型
