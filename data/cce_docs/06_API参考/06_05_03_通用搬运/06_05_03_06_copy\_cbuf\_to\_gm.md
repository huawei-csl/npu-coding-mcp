# copy\_cbuf\_to\_gm

> **Section**: 6.5.3.6


## 功能说明

从 L1 读取数据写入到 GM 中。

## 接口原型

## 参数说明

## 流水类型

## 用例

void copy\_cbuf\_to\_gm(\_\_gm\_\_ void *dst, \_\_cbuf\_\_ void *src, uint8\_t sid, uint16\_t nBurst, uint16\_t lenBurst, uint16\_t srcGap, uint16\_t dstGap);

参数含义见表 1 通用搬运指令参数说明。

PIPE\_MTE3

```
// input 为 64 维的 float 向量 extern "C" __global__ __aicore__ void move( __gm__ float* __restrict__ input,    // 输入数据指针 __gm__ float* __restrict__ output    // 输出数据指针 ) { // 分配 CBuffer 内存区域 __cbuf__ float* input_cb = (__cbuf__ float*)get_imm(0); // 将全局内存的数据搬入 L1 copy_gm_to_cbuf(input_cb, input, 0, 1, 8, 0, 0, pad_t::PAD_NONE); // 等待输入数据搬运完成 set_flag(PIPE_MTE2, PIPE_MTE3, EVENT_ID0); wait_flag(PIPE_MTE2, PIPE_MTE3, EVENT_ID0); // 将 L1 的结果写回全局内存 copy_cbuf_to_gm(output, input_cb, 0, 1, 8, 0, 0); // 等待所有操作完成 pipe_barrier(PIPE_ALL); }
```

## copy\_cbuf\_to\_gm 参数解释：

- 1 、 dst: output ；
- 2 、 src: input\_cb ；
- 3 、 sid: 无需关注，设置为 0 即可；
- 4 、 nBurst: 所有数据作为整块搬运，故设为 1 ；
- 5 、 lenBurst: 搬运总字节数为 64 * 4 = 256 ，以 32B 为单位，故为 8 。
- 6 、 srcGap: 由于是单个数据块搬运，所以间隙为 0 。
- 7 、 dstGap: 由于是单个数据块搬运，所以间隙为 0 。
