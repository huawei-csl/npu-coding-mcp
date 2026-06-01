# copy\_cbuf\_to\_bt

> **Section**: 6.5.11.1


## 功能说明

## 参数说明

## 接口原型

## 流水类型

如果矩阵运算涉及乘加两种运算，此时加法计算的偏置向量需要搬运到偏置表（ bias table ）中。

该接口将 mad 需要的偏置数据从 L1 缓存移动到偏置表缓冲区。偏置表缓冲区的大小为 1KB 。

表 6-29 偏置表搬运参数说明

| 参数名          | 说明                                                  | 取值范围        | 单位   |
|--------------|-----------------------------------------------------|-------------|------|
| dst          | 目的地址， 64B 对齐， uint64_t 类型， 代表首地址。                   | /           | /    |
| src          | 源地址， 32B 对齐。                                        | /           | /    |
| convCont rol | 如果启用， L1 中的数据将被视为 FP16 格式，并在写入偏置表缓冲区之前转 换为 FP32 格式。 | [0, 1]      | /    |
| nBurst       | 搬运数据块数量。                                            | [2, 2^12-1] | elem |
| lenBurst     | 数据块长度。                                              | [0, 2^16-1] | 64B  |
| sourceGa p   | 两个相邻源数据块之间的间隙大小。                                    | [0, 2^16-1] | 32B  |
| dstGap       | 两个相邻目的数据块之间的间隙大 小。                                  | [0, 2^16-1] | 64B  |

srcGap/dstGap ：表示两次搬运之间的 gap ，即上一个 burst 的尾地址跟下一个 burst 的 首地址之间的距离；

void copy\_cbuf\_to\_bt(uint64\_t dst, \_\_cbuf\_\_ void *src, uint16\_t convControl, uint16\_t nBurst, uint16\_t lenBurst, uint16\_t sourceGap, uint16\_t dstGap);

PIPE\_MTE1
