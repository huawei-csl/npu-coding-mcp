# aclrtcDestroyProg

> **Section**: 6.4.8.4  
> **PDF Pages**: 3873–3873  

---

<!-- page 3873 -->

```cpp
#include "kernel_operator.h"#include "my_const_a.h"#include "my_const_b.h"
extern "C" __global__ __aicore__ void hello_world(GM_ADDR x){    KERNEL_TASK_TYPE_DEFAULT(KERNEL_TYPE_AIC_ONLY);    *x = *x + MY_CONST_A + MY_CONST_B;})"""";const char* headerSrcA = R"(#ifndef CONST_A_H#define CONST_A_Hconst int MY_CONST_A = 100;#endif // CONST_A_H)";const char* includeNameA = "my_const_a.h";
const char* headerSrcB = R"(#ifndef CONST_B_H#define CONST_B_Hconst int MY_CONST_B = 50;#endif // CONST_B_H)";
const char* includeNameB = "my_const_b.h";const char* headersArray[] = { headerSrcA, headerSrcB };const char* includeNameArray[] = { includeNameA, includeNameB };aclError result = aclrtcCreateProg(&prog, src, "hello_world", 2,  headersArray,  includeNameArray);
```

## 6.4.8.4 aclrtcDestroyProg

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

销毁编译程序的实例。

函数原型

```cpp
aclError aclrtcDestroyProg(aclrtcProg *prog)
```
