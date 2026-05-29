# GetMrgSortResult

> **Section**: 6.2.3.3.9.7  
> **PDF Pages**: 1478–1480  

---

<!-- page 1478 -->

参数名称含义

repeatTimes

迭代次数，每一次源操作数和目的操作数跳过四个队列总长度。取值范围：repeatTimes∈[1,255]。

repeatTimes参数生效是有条件的，需要同时满足以下四个条件：

●src包含四条队列并且validBit=15

●四个源队列的长度一致

●四个源队列连续存储

●ifExhaustedSuspension = False

返回值说明

无

约束说明

●当存在score[i]与score[j]相同时，如果i>j，则score[j]将首先被选出来，排在前面。

●每次迭代内的数据会进行排序，不同迭代间的数据不会进行排序。

●需要注意此函数排序的队列非region proposal结构。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

// 对8个已排好序的队列进行合并排序，repeatTimes = 2，数据连续存放// 每个队列包含32个(score,index)的8Bytes结构// 最后输出对score域的256个数完成排序后的结果AscendC::MrgSort4Info params;params.elementLengths[0] = 32;params.elementLengths[1] = 32;params.elementLengths[2] = 32;params.elementLengths[3] = 32;params.ifExhaustedSuspension = false;params.validBit = 0b1111;params.repeatTimes = 2;

AscendC::MrgSortSrcList<float> srcList;srcList.src1 = workLocal[0];srcList.src2 = workLocal[64]; // workLocal为float类型，每个队列占据256Bytes空间srcList.src3 = workLocal[128];srcList.src4 = workLocal[192];

```cpp
AscendC::MrgSort<float>(dstLocal, srcList, params);outQueueDst.EnQue<float>(dstLocal);outQueueDst.FreeTensor(dstLocal);
```

## 6.2.3.3.9.7 GetMrgSortResult

产品支持情况

产品是否支持

Atlas 350 加速卡√

<!-- page 1479 -->

产品是否支持

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取MrgSort已经处理过的队列里的Region Proposal个数，并依次存储在四个出参中。

本接口和MrgSort相关指令的配合关系如下：

●配合MrgSort4指令使用，获取MrgSort4指令处理过的队列里的Region Proposal个数。使用时，需要将MrgSort4中的MrgSort4Info.ifExhaustedSuspension参数配置为true，该配置模式下某条队列耗尽后，MrgSort4指令即停止。

以上说明适用于如下型号：

Atlas 推理系列产品AI Core

●配合MrgSort指令使用，获取MrgSort指令处理过的队列里的Region Proposal个数。使用时，需要将MrgSort中的MrgSort4Info.ifExhaustedSuspension参数配置为true，该配置模式下某条队列耗尽后，MrgSort指令即停止。

以上说明适用于如下型号：

Atlas 350 加速卡

Atlas A3 训练系列产品/Atlas A3 推理系列产品

Atlas A2 训练系列产品/Atlas A2 推理系列产品

Atlas 200I/500 A2 推理产品

函数原型

```cpp
__aicore__ inline void GetMrgSortResult(uint16_t &mrgSortList1, uint16_t &mrgSortList2, uint16_t &mrgSortList3, uint16_t &mrgSortList4)
```

参数说明

表6-434参数说明

参数名输入/输出

描述

mrgSortList1输出类型为uint16_t，表示MrgSort第一个队列里已经处理过的Region Proposal个数。

<!-- page 1480 -->

参数名输入/输出

描述

mrgSortList2输出类型为uint16_t，表示MrgSort第二个队列里已经处理过的Region Proposal个数。

mrgSortList3输出类型为uint16_t，表示MrgSort第三个队列里已经处理过的Region Proposal个数。

mrgSortList4输出类型为uint16_t，表示MrgSort第四个队列里已经处理过的Region Proposal个数。

返回值说明

无

约束说明

无

调用示例

●配合MrgSort指令使用示例。

```cpp
uint16_t elementLengths[4] = { 0 };uint32_t sortedNum[4] = { 0 };elementLengths[0] = 32;elementLengths[1] = 32;elementLengths[2] = 32;elementLengths[3] = 32;uint16_t validBit = 0b1111;
AscendC::MrgSortSrcList<float> srcList;srcList.src1 = workLocal[0];srcList.src2 = workLocal[32 * 1 * 2];srcList.src3 = workLocal[32 * 2 * 2];srcList.src4 = workLocal[32 * 3 * 2];
AscendC::MrgSort4Info mrgSortInfo(elementLengths, true, validBit, 1);AscendC::MrgSort(dstLocal, srcList, mrgSortInfo);
uint16_t mrgRes1 = 0;uint16_t mrgRes2 = 0;uint16_t mrgRes3 = 0;uint16_t mrgRes4 = 0;AscendC::GetMrgSortResult(mrgRes1, mrgRes2, mrgRes3, mrgRes4);
```

输出示例:

srcList： [  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.  16.  17.  18.  19.  20.  21.  22.  23.  24.  25.  26.  27.  28.  29.  30.  31.  32.  33.  34.  35.  36.  37.  38.  39.  40.  41.  42.  43.  44.  45.  46.  47.  48.  49.  50.  51.  52.  53.  54.  55.  56.  57.  58.  59.  60.  61.  62.  63.  64.  65.  66.  67.  68.  69.  70.  71.  72.  73.  74.  75.  76.  77.  78.  79.  80.  81.  82.  83.  84.  85.  86.  87.  88.  89.  90.  91.  92.  93.  94.  95.  96.  97.  98.  99. 100. 101. 102. 103. 104. 105. 106. 107. 108. 109. 110. 111. 112. 113. 114. 115. 116. 117. 118. 119. 120. 121. 122. 123. 124. 125. 126. 127. 128.]workLocal: [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
