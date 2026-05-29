# ProposalExtract

> **Section**: 6.2.3.3.9.2  
> **PDF Pages**: 1464–1465  

---

<!-- page 1464 -->

## 6.2.3.3.9.2 ProposalExtract

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

与ProposalConcat功能相反，从Region Proposals内将相应位置的单个元素抽取后重排，每次迭代处理16个Region Proposals，抽取16个元素后连续排列。

函数原型

```cpp
template <typename T>__aicore__ inline void ProposalExtract(const LocalTensor<T>& dst, const LocalTensor<T>& src, const int32_t repeatTime, const int32_t modeNumber)
```

参数说明

表6-422模板参数说明

参数名描述

T操作数数据类型。

Atlas 训练系列产品，支持的数据类型为：half

Atlas 推理系列产品AI Core，支持的数据类型为：half/float

表6-423参数说明

参数名称输入/输出

含义

dst输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

<!-- page 1465 -->

参数名称输入/输出

含义

src输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

LocalTensor的起始地址需要32字节对齐。

源操作数的数据类型需要与目的操作数保持一致。

repeatTime

输入重复迭代次数，int32_t类型，每次迭代完成16个RegionProposals的元素抽取并排布到16个元素里，下次迭代跳至相邻的下一组16个Region Proposals和下一组16个元素。取值范围：repeatTime∈[0,255]。

modeNumber

输入抽取位置参数，取值范围：modeNumber∈[0, 5]，int32_t类型，仅限于以下配置：

●0 – 从x1抽取

●1 – 从y1抽取

●2 – 从x2抽取

●3 – 从y2抽取

●4 – 从score抽取

●5 – 从label抽取

返回值说明

无

约束说明

●用户需保证src中存储的proposal数目大于等于实际所需数目，否则会存在tensor越界错误。

●用户需保证dst中存储的元素大于等于实际所需数目，否则会存在tensor越界错误。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

●接口使用样例// repeatTime = 2, modeNumber = 4, 把32个Region Proposal中的score域元素抽取出来排列成32个连续元素AscendC::ProposalExtract(dstLocal, srcLocal, 2, 4);

示例结果输入数据(src_gm):因为moodel=4，第一个元素33.3的起始位置是4。每个Region Proposal占用连续8个half/float类型的元素。这里使用的类型是half。后续被抽取的每个元素间隔8个元素。repeat为2，每次迭代完成16个元素，共计32个元素[ 0.      0.      0.      0.   33.3    0.      0.      0.      0.      0.      0.      0.  67.56   0.      0.      0.      0.      0.      0.      0.  68.5    0.      0.      0.      0.      0.      0.      0.  -11.914 0.      0.      0.      0.      0.      0.      0.
