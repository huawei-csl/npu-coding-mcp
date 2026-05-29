# PairReduceSum

> **Section**: 6.2.3.3.6.10  
> **PDF Pages**: 1421–1424  

---

<!-- page 1421 -->

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●为了节省地址空间，您可以定义一个Tensor，供源操作数与目的操作数同时使用（即地址重叠），需要注意计算后的目的操作数数据不能覆盖未参与计算的源操作数，需要谨慎使用。

●对于Atlas 200I/500 A2 推理产品，若配置的mask/mask[]参数后，存在某个datablock里的任何一个元素都不参与计算，则该datablock内所有元素的和会填充为0返回。比如float场景下，当mask配置为32，即只计算前4个datablock，则后四个datablock内的和会返回0。

调用示例

●本样例中只展示Compute流程中的部分代码。

–BlockReduceSum-tensor高维切分计算样例-mask连续模式// 设定mask为最多的128个全部元素参与计算int32_t mask = 256/sizeof(half);// 每个repeat128个元素，一共128个元素。int repeat = 1;// dstLocal: 目的操作数tensor// srcLocal: 源操作数tensor// srcBlkStride = 1, 在一个repeat中，block间没有空隙。// dstRepStride = 1, srcRepStride = 8, repeat间没有空隙。AscendC::BlockReduceSum<half>(dstLocal, srcLocal, repeat, mask, 1, 1, 8);

–BlockReduceSum-tensor高维切分计算样例-mask逐bit模式// 设定mask为最多的128个全部元素参与计算uint64_t mask[2] = { UINT64_MAX, UINT64_MAX };// 每个repeat128个元素，一共128个元素。int repeat = 1;// dstLocal: 目的操作数tensor// srcLocal: 源操作数tensor// srcBlkStride = 1, 在一个repeat中，block间没有空隙。// dstRepStride = 1, srcRepStride = 8, repeat间没有空隙。AscendC::BlockReduceSum<half>(dstLocal, srcLocal, repeat, mask, 1, 1, 8);

结果示例如下：输入数据src_gm: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...  3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

输出数据dst_gm: [16, 32, ..., 48]

●针对不同场景合理使用归约指令可以带来性能提升，相关介绍请参考3.8.6.3 选择低延迟指令，优化归约操作性能，具体样例请参考ReduceCustom。

## 6.2.3.3.6.10 PairReduceSum

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

<!-- page 1422 -->

产品是否支持

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

PairReduceSum：相邻两个（奇偶）元素求和，例如（a1, a2, a3, a4, a5, a6...），相邻两个数据求和为（a1+a2, a3+a4, a5+a6, ......）。归约指令的总体介绍请参考2.5.2.3.2 如何使用归约计算API。

函数原型

●mask逐bit模式template <typename T, bool isSetMask = true>__aicore__ inline void PairReduceSum(const LocalTensor<T>& dst, const LocalTensor<T>& src, const int32_t repeatTime, const uint64_t mask[], const int32_t dstRepStride, const int32_t srcBlkStride, const int32_t srcRepStride)

●mask连续模式template <typename T, bool isSetMask = true>__aicore__ inline void PairReduceSum(const LocalTensor<T>& dst, const LocalTensor<T>& src, const int32_t repeatTime, const int32_t mask, const int32_t dstRepStride, const int32_t srcBlkStride, const int32_t srcRepStride)

参数说明

表6-397模板参数说明

参数名描述

T操作数数据类型。

Atlas 350 加速卡，支持的数据类型为：half/float

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持的数据类型为：half/float

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持的数据类型为：half/float

Atlas 200I/500 A2 推理产品，支持的数据类型为：half/float

Atlas 推理系列产品AI Core，支持的数据类型为：half/float

Atlas 训练系列产品，支持的数据类型为：half

<!-- page 1423 -->

参数名描述

isSetMask

是否在接口内部设置mask。

●true，表示在接口内部设置mask。

●false，表示在接口外部设置mask，开发者需要使用 SetVectorMask接口设置mask值。这种模式下，本接口入参中的mask值必须设置为占位符MASK_PLACEHOLDER。

表6-398参数说明

参数名称输入/输出

含义

dst输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

src输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

repeatTime

输入迭代次数。取值范围为[0, 255]。

关于该参数的具体描述请参考2.5.2.2.2 高维切分API。

mask/mask[]

输入mask用于控制每次迭代内参与计算的元素。

●逐bit模式：可以按位控制哪些元素参与计算，bit位的值为1表示参与计算，0表示不参与。mask为数组形式，数组长度和数组元素的取值范围和操作数的数据类型有关。当操作数为16位时，数组长度为2，mask[0]、mask[1]∈[0, 264-1]并且不同时为0；当操作数为32位时，数组长度为1，mask[0]∈(0, 264-1]；当操作数为64位时，数组长度为1，mask[0]∈(0, 232-1]。

例如，mask=[8, 0]，8=0b1000，表示仅第4个元素参与计算。

●连续模式：表示前面连续的多少个元素参与计算。取值范围和操作数的数据类型有关，数据类型不同，每次迭代内能够处理的元素个数最大值不同。当操作数为16位时，mask∈[1, 128]；当操作数为32位时，mask∈[1, 64]；当操作数为64位时，mask∈[1, 32]。

dstRepStride

输入目的操作数相邻迭代间的地址步长。以一个repeat归约后的长度为单位。PairReduce完成后，一个repeat的长度减半。即单位为128Byte。

注意，此参数值Atlas 训练系列产品不支持配置0。

<!-- page 1424 -->

参数名称输入/输出

含义

srcBlkStride

输入单次迭代内datablock的地址步长。详细说明请参考dataBlockStride。

srcRepStride

输入源操作数相邻迭代间的地址步长，即源操作数每次迭代跳过的datablock数目。详细说明请参考repeatStride。

返回值说明

无

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●如果两两相加的两个元素mask位未配置（即当前两个元素不参与运算），对于Atlas 200I/500 A2 推理产品，对应的目的操作数中的值会置为0，对于其他产品型号，对应的目的操作数中的值不会变化。比如float场景下对64个数使用当前指令，mask配置为62，表示最后两个元素不参与运算，对于Atlas 200I/500 A2 推理产品，目的操作数中最后一个值会返回0；对于其他产品型号，目的操作数中最后一个值不会变化。

调用示例

本样例中只展示Compute流程中的部分代码。

●PairReduceSum-tensor高维切分计算样例-mask连续模式// 设定mask为最多的128个全部元素参与计算int32_t mask = 256/sizeof(half);// 每个repeat128个元素，一共128个元素。int repeat = 1;// dstLocal: 目的操作数tensor// srcLocal: 源操作数tensor// srcBlkStride = 1, 在一个repeat中，block间没有空隙。// dstRepStride = 1, srcRepStride = 8, repeat间没有空隙。AscendC::PairReduceSum<half>(dstLocal, srcLocal, repeat, mask, 1, 1, 8);

●PairReduceSum-tensor高维切分计算样例-mask逐bit模式// 设定mask为最多的128个全部元素参与计算uint64_t mask[2] = { UINT64_MAX, UINT64_MAX };// 每个repeat128个元素，一共128个元素。int repeat = 1;// dstLocal: 目的操作数tensor// srcLocal: 源操作数tensor// srcBlkStride = 1, 在一个repeat中，block间没有空隙。// dstRepStride = 1, srcRepStride = 8, repeat间没有空隙。AscendC::PairReduceSum<half>(dstLocal, srcLocal, repeat, mask, 1, 1, 8);

●示例结果输入数据src_gm：[1, 1, 1, -1, 2, 2, -1, 2,  3, 3, 3, -1, 4, 4, -2, 4,....]输出数据dst_gm：[2, 0, 4, 1, 6, 2, 8, 2, ....]
