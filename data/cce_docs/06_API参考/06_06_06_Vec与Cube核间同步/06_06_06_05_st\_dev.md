# st\_dev

> **Section**: 6.6.6.5


## 功能说明

## 接口原型

## 参数说明

## 流水类型

FFTS 同步接口。 将数据（包括模式和标志 ID ）从寄存器存储到目标地址。

st\_dev 将 src 中的数据（其中 src 的高 8 位代表 mode ，低 8 位代表fl ag\_id ）写入目标地址 dst+offset 。 wait\_flag\_dev (int64\_t flagID) ，判断fl agID 对应的 counter 是否为 0 ，如 果是则本接口后的所有接口都被阻塞，直至fl agID 对应 counter 不为 0 。每一个fl agID 都 有对应的 counter ，每一次调用 st\_dev ，该fl agID 对应的 counter 都会自增 1 ，每一次调 用 wait\_flag\_dev ，该fl agID 对应的 counter 都会减 1 。 mode 有效范围为 0-2 ，fl agID 有 效范围为 0-15 ，每个fl agID 对应的 counter 有效范围为 0-15 ，如果fl agID 或 counter 超过 有效范围，会出现异常。

void st\_dev(int8\_t src, \_\_gm\_\_ int8\_t *dst, int16\_t offset);

void st\_dev(float src, \_\_gm\_\_ float *dst, int16\_t offset);

void st\_dev(half src, \_\_gm\_\_ half *dst, int16\_t offset);

void st\_dev(int32\_t src, \_\_gm\_\_ int32\_t *dst, int16\_t offset);

void st\_dev(int64\_t src, \_\_gm\_\_ int64\_t *dst, int16\_t offset);

## 表 6-39 参数说明

| 参数名    | 说明   | 取值范围             | 单位   |
|--------|------|------------------|------|
| src    | 源寄存器 | /                | /    |
| dst    | 目的地址 | /                | /    |
| offset | 偏移量  | [-32768 ,327 67] | B    |

PIPE\_S
---
