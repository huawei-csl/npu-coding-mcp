# set\_flag &amp; wait\_flag

> **Section**: 6.6.3


## 功能说明

## 接口原型

## 参数说明

## 流水类型

set\_flag 和 wait\_flag 是一对接口。任何 wait\_flag 接口都会等待直到一个具有相同事 件 ID 的 set\_flag 被执行。对于每一种流水线组合，都有从 0 到 7 的事件 ID 。 set\_flag 只是设置位，不会阻塞同一流水中的下一个接口。当 set\_flag 之前的所有接口已完成 提交，则会触发相应的 wait\_flag 。

值得注意的是，不允许有两个具有相同 ID 、流水和触发器对但没有相应 wait\_flag 的 set\_flag 。例如：

set\_flag(PIPE\_M, PIPE\_V, 0); set\_flag(PIPE\_M, PIPE\_V, 0);  // 非法

void set\_flag(pipe\_t pipe, pipe\_t tpipe, uint64\_t pipeID); void set\_flag(pipe\_t pipe, pipe\_t tpipe, event\_t pipeID); void wait\_flag(pipe\_t pipe, pipe\_t tpipe, uint64\_t pipeID); void wait\_flag(pipe\_t pipe, pipe\_t tpipe, event\_t pipeID);

pipe\_t 类型见上一节。在这个接口中， pipe\_t 不能为 PIPE\_ALL 。

## 表 6-32 同步接口对参数说明

| 参数名    | 说明                       |
|--------|--------------------------|
| pipe   | 需要等待完成的流水                |
| tpipe  | 等待完成后才能触发的流水             |
| pipeID | 3bit 事件 ID ，仅支持 7 个事件 ID |

PIPE\_S
