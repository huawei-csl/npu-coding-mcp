# WriteSpmBuffer

> **Section**: 13  
> **PDF Pages**: 1748–1750  

---

<!-- page 1748 -->

参数说明

参数名输入/输出

含义

workspace

输入workspace地址。

bufferSize

输入SPM Buffer的大小，单位是字节。

约束说明

无

返回值说明

无

调用示例

●暂存到workspace初始化AscendC::TPipe pipe;int len = 1024; // 设置spm buffer为1024个类型为T的数据workspace_gm.SetGlobalBuffer((__gm__ T *)usrWorkspace, len);  // 此处的usrWorkspace为用户自定义的workspaceauto gm = workspace_gm[AscendC::GetBlockIdx() * len];pipe.InitSpmBuffer(gm, len * sizeof(T));

●暂存到L1 Buffer初始化AscendC::TPipe pipe;int len = 1024; // 设置spm buffer为1024个类型为T的数据pipe.InitSpmBuffer(len * sizeof(T));

## ?.13. WriteSpmBuffer

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

<!-- page 1749 -->

功能说明

将需要溢出暂存的数据拷贝到SPM Buffer中。

函数原型

●适用于连续和不连续的数据暂存：template <typename T>__aicore__ inline void WriteSpmBuffer(const LocalTensor<T>& writeBuffer, const DataCopyParams& copyParams, int32_t writeOffset = 0)

●适用于连续的数据暂存：template <typename T>__aicore__ inline void WriteSpmBuffer(const LocalTensor<T>& writeBuffer, const int32_t writeSize, int32_t writeOffset = 0)

参数说明

表6-671接口参数说明

输入/输出

参数名称

含义

writeBuffer

输入需要溢出暂存的Local内存。

copyParams

输入搬运参数，DataCopyParams类型，DataCopyParams结构定义请参考表6-672。

writeSize

输入拷贝的元素个数。

writeOffset

输入拷贝到SPM Buffer的偏移，单位为字节。

表6-672 DataCopyParams 结构体参数定义

参数名称含义

blockCount

待搬运的连续传输数据块个数。uint16_t类型，取值范围：blockCount∈[1, 4095]。

blockLen待搬运的每个连续传输数据块长度，单位为DataBlock（32字节）。uint16_t类型，取值范围：blockLen∈[1, 65535]。

特殊情况：

●当dst位于C2PIPE2GM时，单位为128B。

●一般情况：当dst位于C2时，表示源操作数的连续传输数据块长度，单位为64B。针对Atlas 350 加速卡，当dst位于C2时，表示源操作数的连续传输数据长度，单位为32B。

<!-- page 1750 -->

参数名称含义

srcGap源操作数相邻连续数据块的间隔（前面一个数据块的尾与后面数据块的头的间隔），单位为DataBlock（32字节）。uint16_t类型，srcGap不要超出该数据类型的取值范围。

在L1 Buffer -> Fixpipe Buffer场景中，srcGap特指源操作数相邻连续数据块的间隔（前面一个数据块的头与后面数据块的头的间隔），单位为DataBlock（32字节）。uint16_t类型，srcGap不要超出该数据类型的取值范围。

dstGap目的操作数相邻连续数据块间的间隔（前面一个数据块的尾与后面数据块的头的间隔），单位为DataBlock（32字节）。uint16_t类型，dstGap不要超出该数据类型的取值范围。

特殊情况：

●当dst位于C2PIPE2GM时，单位为128B。

●一般情况：当dst位于C2时，表示源操作数的连续传输数据块长度，单位为64B。针对Atlas 350 加速卡，当dst位于C2时，表示源操作数的连续传输数据长度，单位为32B。

在L1 Buffer -> Fixpipe Buffer场景中，dstGap特指源操作数相邻连续数据块的间隔（前面一个数据块的头与后面数据块的头的间隔），单位为DataBlock（32字节）。uint16_t类型，dstGap不要超出该数据类型的取值范围。

约束说明

●暂存拷贝到L1时注意writeSize和writeOffset保证32字节对齐

●拷贝的内存不要超出初始化的SPM Buffer大小，否则会存在溢出踩踏等问题。

返回值说明

无

调用示例

●使用DataCopyParams搬运AscendC::TPipe pipe;int dataSize = 32; // 假设T为half类型，从ub上申请一块内存32 * sizeof(half)字节int offset = 32; // 拷贝到spmBuffer时偏移32字节AscendC::DataCopyParams copyParams{1, 2, 0, 0}; // 从ub上搬运一个连续传输数据块，一个数据块的长度为2个datablock，一个datablock为32bytes// writeLocal为SPM Buffer上的half类型的LocalTensorpipe.WriteSpmBuffer(writeLocal, copyParams, offset); // 将ub上的连续传输数据块搬运到SPM Bufferpipe.ReadSpmBuffer(writeLocal, copyParams, offset); // 将暂存在SPM Buffer的数据读回到local数据...// 当ub内存足够时，将暂存在SPM Buffer的数据块搬运回GM上，dstGlobal为half类型的GlobalTensorAscendC::DataCopy(dstGlobal, writeLocal, copyParams);

●使用writeSize连续搬运AscendC::TPipe pipe;int dataSize = 32; // 假设T为half类型，从ub上申请一块内存32 * sizeof(half)字节int offset = 32; // 拷贝到spmBuffer时偏移32字节;// writeLocal为SPM Buffer上的half类型的LocalTensorpipe.WriteSpmBuffer(writeLocal, dataSize, offset); // 将ub上的连续传输数据块搬运到SPM Bufferpipe.ReadSpmBuffer(writeLocal, dataSize, offset); // 将暂存在SPM Buffer的数据读回到local数据
