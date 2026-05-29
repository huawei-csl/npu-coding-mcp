# ShapeInfo

> **Section**: 6.2.6.1  
> **PDF Pages**: 3081–3081  

---

<!-- page 3081 -->

## 6.2.5 C API

详细介绍请参见昇腾官网商用版在线文档。

## 6.2.6 其他数据类型

## 6.2.6.1 ShapeInfo

功能说明

ShapeInfo用来存放LocalTensor或GlobalTensor的shape信息。

函数原型

●ShapeInfo结构定义struct ShapeInfo {public:    __aicore__ inline ShapeInfo();    __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[],        const uint8_t inputOriginalShapeDim, const uint32_t inputOriginalShape[], const DataFormat inputFormat);    __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[], const DataFormat inputFormat);    __aicore__ inline ShapeInfo(const uint8_t inputShapeDim, const uint32_t inputShape[]);    uint8_t shapeDim;    uint8_t originalShapeDim;    uint32_t shape[K_MAX_DIM];    uint32_t originalShape[K_MAX_DIM];    DataFormat dataFormat;};

●获取Shape中所有dim的累乘结果__aicore__ inline int GetShapeSize(const ShapeInfo& shapeInfo)

函数说明

表6-1443 ShapeInfo 结构参数说明

参数名称描述

shapeDim现有的shape维度。

shape现有的shape。

originalShapeDim

原始的shape维度。

originalShape原始的shape。

dataFormat数据排布格式，DataFormat类型，定义如下：enum class DataFormat : uint8_t {    ND = 0,    NZ,    NCHW,    NC1HWC0,    NHWC,};
