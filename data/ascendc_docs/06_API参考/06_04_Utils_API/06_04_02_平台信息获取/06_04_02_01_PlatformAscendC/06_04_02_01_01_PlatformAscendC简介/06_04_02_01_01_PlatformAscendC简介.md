# PlatformAscendC简介

> **Section**: 6.4.2.1.1  
> **PDF Pages**: 3759–3759  

---

<!-- page 3759 -->

参数说明

表6-1951模板参数说明

参数名含义

...Idx表示序列的形参包。

size_t，在64位系统中为long unsigned int，非64位系统中为unsigned int。

N生成的整数序列的大小。

size_t，在64位系统中为long unsigned int，非64位系统中为unsigned int。

约束说明

●N的范围为[0, 64]。

●index_sequence作为序列，长度最大为64。

返回值说明

无

调用示例

生成并打印一个长度为5的整数序列。

template<size_t... Is> __aicore__  inline void PrintIndexSequence(AscendC::Std::index_sequence<Is...>) {   ((AscendC::printf(" Is:%lu", Is)), ...);}__aicore__ inline void Process(){    PrintIndexSequence(AscendC::Std::make_index_sequence<5>{}); // 打印结果: 0，1，2，3，4    PrintIndexSequence(AscendC::Std::index_sequence<0,1,2,10,8000>{}); // 打印结果: 0，1，2，10, 8000}

## 6.4.2 平台信息获取

## 6.4.2.1 PlatformAscendC

## 6.4.2.1.1 PlatformAscendC 简介

在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

需要包含的头文件

使用该功能需要包含"tiling/platform/platform_ascendc.h"头文件。样例如下：#include "tiling/platform/platform_ascendc.h"
