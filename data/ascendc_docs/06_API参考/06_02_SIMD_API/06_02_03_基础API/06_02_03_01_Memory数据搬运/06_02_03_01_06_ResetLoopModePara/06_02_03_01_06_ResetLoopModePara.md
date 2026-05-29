# ResetLoopModePara

> **Section**: 6.2.3.1.6  
> **PDF Pages**: 967–967  

---

<!-- page 967 -->

约束说明

●源操作数和目的操作数的起始地址需要保证32字节对齐。

●目的操作数的数据不能重叠，如果有重叠，硬件层面不会报错或者告警，同时也不能保证重叠数据的正确性；但是不同迭代可以交织，例如内层循环中相邻迭代目的操作数的数据块间的间隔可以小于相邻连续目的操作数的数据块的间隔。

●需要在每次使能loop mode并且设置loop mode的参数后通过ResetLoopModePara进行寄存器的复位，否则会影响到下一次对应通路的搬运的使用，引发异常。

调用示例

本示例中操作数数据类型为int8_t。AscendC::LocalTensor<int8_t> srcLocal = inQueueSrc.AllocTensor<int8_t>();AscendC::DataCopyExtParams copyParams{2, 48 * sizeof(int8_t), 0, 0, 0}; // 结构体DataCopyExtParams最后一个参数是rsv保留位AscendC::DataCopyPadExtParams<half> padParams{false, 0, 0, 0};AscendC::LoopModeParams loopParam2Ub {2, 2, 96, 128, 192, 288};AscendC::SetLoopModePara(loopParam2Ub, DataCopyMVType::OUT_TO_UB);AscendC::DataCopyPad<int8_t, PaddingMode::Compact>(srcLocal, srcGlobal, copyParams, padParams); // 从GM->VECIN搬运 48 * 2 * 2 * 2 = 384BytesAscendC::ResetLoopModePara(DataCopyMVType::OUT_TO_UB);AscendC::LoopModeParams loopParam2Gm {2, 2, 128, 96, 288, 192};AscendC::SetLoopModePara(loopParams2Gm, DataCopyMVType::UB_TO_OUT);DataCopyPad<T, PaddingMode::Compact>(dstGlobal, srcLocal, copyParams);AscendC::ResetLoopModePara(DataCopyMVType::UB_TO_OUT);

结果示例如下：

输入数据src0Global: [1 2 3 ... 384]输出数据dstGlobal:[1 2 3 ... 384]

## 6.2.3.1.6 ResetLoopModePara

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

重置loop mode的参数。与SetLoopModePara搭配使用，在使能loop mode并且设置loop mode的参数的数据搬运场景下，数据搬运结束后需要调用该函数来重置loopmode参数。
