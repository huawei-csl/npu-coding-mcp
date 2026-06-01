# set\_cmpmask

> **Section**: 6.3.3.1


CMPMASK(128bit) 作为向量选择运算接口 6.3.7.1 vsel 的选择寄存器。

## 功能说明

## 接口原型

## 流水类型

将 UB 中的 src 起始的 16B 连续地址存入 CMPMASK[127:0] 中。

void set\_cmpmask(\_\_ubuf\_\_ void *src)

PIPE\_V
