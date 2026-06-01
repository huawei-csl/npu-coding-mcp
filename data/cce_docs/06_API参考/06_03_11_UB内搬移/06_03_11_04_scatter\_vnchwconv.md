# scatter\_vnchwconv

> **Section**: 6.3.11.4


## 功能说明

这是将 NCHW 格式转换为 NC1HWC0 格式的接口。在此接口中， MASK 寄存器无效。

如果是 b8 数据， C0=32 ，如果是 b32/b16 数据， C0=16 。

对于 b32 类型：在源向量中，从每个 32B 块中提取 4B ，然后将它们组合成新的块。

for (e=0; e&lt;16; e=e+2)

for (k=0; k&lt;8; k++) dst[e][k] = src[k][e/2] dst[e+1][k] = src[k+8][e/2]

## 接口原型

## 参数类型

对于 b16 类型：在源向量中，从每个 32B 块中提取 2B ，然后将它们组合成新的块。 for (e=0; e&lt;16; e=e+2) for (k=0; k&lt;16; k++) dst[e][k] = src[k][e]

对于 b8 类型，在源向量中，从每个 32B 块中提取 1B ，然后将它们组合成新的块，并且 可以通过 dstHighHalf 与 srcHighHalf 参数指定是从地址的高半段取还是低半段取。

dstHighHalf = 0, srcHighHalf = 0: for (e=0; e&lt;16; e++) for (k=0; k&lt;16; k++) dst[e][k].B = src[k][e].B dstHighHalf = 1, srcHighHalf = 0 for (e=0; e&lt;16; e++) for (k=0; k&lt;16; k++) dst[e][k+16].B = src[k][e].B dstHighHalf = 0, srcHighHalf = 1 for (e=0; e&lt;16; e++) for (k=0; k&lt;16; k++) dst[e][k].B = src[k][e+16].B dstHighHalf = 1, srcHighHalf = 1 for (e=0; e&lt;16; e++) for (k=0; k&lt;16; k++) dst[e][k+16].B = src[k][e+16].B

该接口不支持 MASK 配置。

// 相同接口的不同原型区别在于源地址和目的地址的数据类型不同 void scatter\_vnchwconv\_b32(ub\_addr8\_t dst, ub\_addr8\_t src, uint8\_t repeat, uint16\_t dstStride, uint16\_t

srcStride);

void scatter\_vnchwconv\_b8(ub\_addr8\_t dst, ub\_addr8\_t src, uint8\_t repeat, uint16\_t dstStride, uint16\_t srcStride, bool dstHighHalf, bool srcHighHalf);

void scatter\_vnchwconv\_b16(ub\_addr8\_t dst, ub\_addr8\_t src, uint8\_t repeat, uint16\_t dstStride, uint16\_t srcStride);

| 参数名   | 说明                                                                                                      | 取值范围   | 单位   |
|-------|---------------------------------------------------------------------------------------------------------|--------|------|
| dst   | dst 是目标向量地址寄存器 VAd ， VAd 用于存储写入目 标数据（ NC1HWC0 格 式）的 UB 地址信息。一次 使用两个寄存器（ VAd ， VAd+1 ），共指向 512B 的 UB 地址。 | /      | /    |
| src   | src 是目标向量地址寄存器 VAn ， VAn 用于读取目标数 据（ NCHW 格式）的 UB 地 址信息。一次使用两个寄存 器（ VAn ， VAn+1 ），共指 向 512B 的 UB 地址。     | /      | /    |

## 流水类型

| 参数名         | 说明                                                                                                           | 取值范围        | 单位   |
|-------------|--------------------------------------------------------------------------------------------------------------|-------------|------|
| repeat      | 迭代次数。 例如 repeat=3 时，例 dst 地 址依次为 VAd[i] 、 VAd[i] +dstStride 、 VAd[i] +2*dstStride VA[n] 就是 VA 第 n 个元 素。      | [0, 2^8-1]  | /    |
| srcStride   | 源地址的块级步长（对 VAn 和 VAn+1 生效）。                                                                                  | [0, 2^16-1] | 32B  |
| dstStride   | 目标地址的块级步长（对 VAd 和 VAd+1 生效）。                                                                                 | [0, 2^16-1] | 32B  |
| dstHighHalf | dstHighHalf = 0 ：将提取 的数据存储到目标数据 32B 块的低半段（ 0~15 索 引）。 dstHighHalf = 1 ：将提取 的数据存储到目标数据 32B 块的高半段（ 16~31 索 引）。 | [0, 1]      | /    |
| srcHighHalf | srcHighHalf = 0 ：从源数 据 32B 块的低半段（ 0~15 索引）提取数据。 srcHighHalf = 1 ：从源数 据 32B 块的高半段 （ 16~31 索引）提取数 据。           | [0,1]       | /    |

VA 有 VA0-VA7 。 VA0 有 128 位，存储 UB 块的地址。 VA0 被分为 8 个块指针，每个指针指 向一个 32B 的块，共 256B 。

（ VAn ， VAd ）∈ [VA0-VA7]

参数表中的 Stride 均指代相邻两个首地址间的步长。

PIPE\_V
