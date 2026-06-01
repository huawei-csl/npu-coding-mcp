# copy\_gm\_to\_cbuf

> **Section**: 6.5.3.5


## 功能说明

## 接口原型

从 GM 读取数据写入到 L1 中，并对数据做填补。

void copy\_gm\_to\_cbuf(\_\_cbuf\_\_ void *dst, \_\_gm\_\_ void *src, uint8\_t sid, uint16\_t nBurst, uint16\_t lenBurst, uint16\_t srcGap, uint16\_t dstGap, pad\_t padMode);

## 参数说明

参数含义见表 1 通用搬运指令参数说明。

## padMode 说明：

padMode 等于 0 ，表示无 padding ，当不等于 0 时， padMode 设置通过 set\_padding(config) 完成数据 padding 。 padMode 详见表 1 填充模式对照。

void set\_padding(uint64\_t config);

- config[63:32] 默认为 0 ；
- 对于 b32 padding data ， config[31:0] 生效；
- 对于 b16 padding data ，只需设置 config[15:0] ，其余 bit 设置为 0 ；
- 对于 b8 padding data ，需要将 config[15:8] 和 config[7:0] 设置为 padding data ， 其余 bit 设置为 0 ；
- 对于 b4 padding data ，需要将 config[15:12] 、 config[11:8] 、 config[7:4] 、 config[3:0] 设置为 padding data ，其余 bit 设置为 0 ；

## 表 6-20 填充模式对照

| pad Mod e 枚 举名   |   pad Mo de 枚 举 值 | pad 模式描述                                                                                                                                                                                           |
|------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAD _NO NE       |                 0 | 无 padding                                                                                                                                                                                          |
| PAD _M ODE 1     |                 1 | ● lenBurst 必须设置为 1 （单位 32Bytes ），实际只从 GM 搬运 1Bytes 到 L1 ，然后在其后插入 31 个 config[7:0] （ set_padding 参数）合计 31Bytes 的数据写入 CBUF ； ● srcGap 必须设置为 0 ，表示每次 burst 搬运是从 GM 上连续读取； ● dstGap 单位不变，仍是 32Bytes 。  |
| PAD _M ODE 2     |                 2 | ● lenBurst 必须设置为 1 （单位 32Bytes ），实际只从 GM 搬运 2Bytes 到 L1 ，然后在其后插入 15 个 config[31:16] （ set_padding 参数）合 计 30Bytes 的数据写入 CBUF ● srcGap 必须设置为 0 ，表示每次 burst 搬运是从 GM 上连续读取； ● dstGap 单位不变，仍是 32Bytes 。 |
| PAD _M ODE 3     |                 3 | ● lenBurst 必须设置为 1 （单位 32Bytes ），实际只从 GM 搬运 4Bytes 到 L1 ，然后在其后插入 14 个 config[31:16] （ set_padding 参数）合 计 28Bytes 的数据写入 CBUF ● srcGap 必须设置为 0 ，表示每次 burst 搬运是从 GM 上连续读取； ● dstGap 单位不变，仍是 32Bytes 。 |

## 流水类型

| pad Mod e 枚 举名   |   pad Mo de 枚 举 值 | pad 模式描述                                                                                                                                                                                           |
|------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PAD _M ODE 4     |                 4 | ● lenBurst 必须设置为 1 （单位 32Bytes ），实际只从 GM 搬运 8Bytes 到 L1 ，然后在其后插入 12 个 config[31:16] （ set_padding 参数）合 计 24Bytes 的数据写入 CBUF ● srcGap 必须设置为 0 ，表示每次 burst 搬运是从 GM 上连续读取； ● dstGap 单位不变，仍是 32Bytes 。 |
| PAD _M ODE 5     |                 5 | ● lenBurst 必须设置为 1 （单位 32Bytes ），实际只从 GM 搬运 16Bytes 到 L1 ，然后在其后插入 8 个 config[31:16] （ set_padding 参数）合计 16Bytes 的数据写入 CBUF ● srcGap 必须设置为 0 ，表示每次 burst 搬运是从 GM 上连续读取； ● dstGap 单位不变，仍是 32Bytes 。  |
| PAD _M ODE 6     |                 6 | ● 从每个搬运的 32Bytes 中去除高位的 28Bytes ，只保留 4Bytes ，所以 从 GM 读取的 lenBurst * 32Bytes 长度的数据然后搬到 L1 上的是 lenBurst * 4Bytes ； ● CBUF 上每个 burst 连续存储，所以 dstGap 必须设置为 0 ； ● srcGap 单位仍是 32Bytes 。                 |
| PAD _M ODE 7     |                 7 | ● 从每个搬运的 32Bytes 中去除高位的 24Bytes ，只保留 8Bytes ，所以 从 GM 读取的 lenBurst * 32Bytes 长度的数据然后搬到 L1 上的是 lenBurst * 8Bytes ； ● CBUF 上每个 bust 连续存储，所以 dstGap 必须设置为 0 ； ● srcGap 单位仍是 32Bytes 。                  |
| PAD _M ODE 8     |                 8 | ● 从每个搬运的 32Bytes 中去除高位的 16Bytes ，只保留 16Bytes ，所 以从 GM 读取的 lenBurst * 32Bytes 长度的数据然后搬到 L1 上的是 lenBurst * 16Bytes ； ● CBUF 上每个 bust 连续存储，所以 dstGap 必须设置为 0 ； ● srcGap 单位仍是 32Bytes 。                |

PIPE\_MTE2
