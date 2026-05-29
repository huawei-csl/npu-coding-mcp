# SetAType

> **Section**: 4  
> **PDF Pages**: 2419–2419  

---

<!-- page 2419 -->

约束条件说明

kaStepIter_ % kbStepIter_ = 0或者kbStepIter_% kaStepIter_ = 0

MDL模板K方向循环搬运要求Ka和Kb方向迭代次数为倍数关系

kaStepIter_ = CeilDiv(tiling_->singleCoreK_,tiling_->baseK * tiling_->stepKa)

kaStepIter_ ：Ka方向循环搬运迭代次数

kbStepIter_ = CeilDiv(tiling_->singleCoreK_,tiling_->baseK * tiling_->stepKb)

kbStepIter_ ：Kb方向循环搬运迭代次数

●性能调优推荐取值

根据Tiling调优经验，部分TCubeTiling参数值或取值方式推荐如下：

–base块推荐(baseM, baseN, baseK)：(128, 256, 64)

–dbL0A / dbL0B = 2

–depthA1 / (stepM * stepKa) = 2

–depthB1 / (stepN * stepKb) = 2

–优先设置参数stepKa/stepKb，使得K方向全载，再考虑M方向或N方向全载

## ?.4. SetAType

功能说明

设置A矩阵的位置，数据格式，数据类型，是否转置等信息，这些信息需要和kernel侧的设置保持一致。

函数原型

```cpp
int32_t SetAType(TPosition pos, CubeFormat type, DataType dataType, bool isTrans = false)
```

参数说明

表6-1075参数说明

参数名输入/输出

描述

pos输入A矩阵所在的buffer位置，可设置为：TPosition::GM,TPosition::VECOUT, TPosition::TSCM。

type输入A矩阵的数据格式，可设置为：CubeFormat::ND，CubeFormat::NZ，CubeFormat::VECTOR

dataType输入A矩阵的数据类型，可设置为：DataType::DT_FLOAT/DataType::DT_FLOAT16/DataType::DT_BFLOAT16/DataType::DT_INT8/DataType::DT_INT4/DataType::DT_FLOAT8_E4M3FN/DataType::DT_FLOAT8_E5M2/DataType::DT_HIFLOAT8。
