# pipe\_barrier

> **Section**: 6.6.2


## 功能说明

屏障接口是一种同步机制，确保在它之后发出的接口，必须等到同一流水线中所有先 前的接口都已完成并提交后，才能继续执行。

注意，所有接口都会经过 pipe S ，因此 pipe\_barrier(PIPE\_S) 会引发错误。 pipe\_barrier(PIPE\_ALL) 会等待所有流水线中的所有先前接口的提交。

void pipe\_barrier(pipe\_t pipe);

表 6-31 pipe\_t 枚举量

| 枚举名       |   枚举值 |
|-----------|-------|
| PIPE_S    |     0 |
| PIPE_V    |     1 |
| PIPE_M    |     2 |
| PIPE_MTE1 |     3 |

## 接口原型

## 参数说明

## 流水类型

| 枚举名       |   枚举值 |
|-----------|-------|
| PIPE_MTE2 |     4 |
| PIPE_MTE3 |     5 |
| PIPE_ALL  |     6 |
| PIPE_FIX  |    10 |

PIPE\_S
