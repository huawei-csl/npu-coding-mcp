# set\_vector\_mask

> **Section**: 6.3.2.2


## 功能说明

## 接口原型

## 流水类型

配合向量计算进行 mask 设置，详见 6.3.1.2 Mask 规则说明

set\_vector\_mask\_dup(uint64\_t mask) ： Mask 高低位寄存器均设置为 mask 值

set\_vector\_mask(uint64\_t mask1, uint64\_t mask0) ： Mask 寄存器高位设置为 mask1 ，低位设置为 mask0

void set\_vector\_mask\_dup(uint64\_t mask) void set\_vector\_mask(uint64\_t mask1, uint64\_t mask0)

PIPE\_S
