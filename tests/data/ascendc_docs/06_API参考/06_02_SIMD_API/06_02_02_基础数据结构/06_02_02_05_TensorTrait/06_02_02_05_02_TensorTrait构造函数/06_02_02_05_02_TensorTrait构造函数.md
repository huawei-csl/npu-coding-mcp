# TensorTrait构造函数

> **Section**: 6.2.2.5.2  
> **PDF Pages**: 870–871  

---

<!-- page 870 -->

接口分类接口名称

基础API>矢量计算>类型转换

Cast、Truncate

基础API>矢量计算>归约计算

ReduceMax、BlockReduceMax、WholeReduceMax、ReduceMin、BlockReduceMin、WholeReduceMin、ReduceSum、BlockReduceSum、WholeReduceSum、RepeatReduceSum、PairReduceSum

基础API>矢量计算>数据转换

Transpose、TransDataTo5HD

基础API>矢量计算>数据填充

Brcb、Duplicate（仅支持不带scalar参数的接口）

基础API>矢量计算>离散与聚合

Gather、Gatherb、Scatter

基础API>矢量计算>数据重排（ISASI）

Interleave、DeInterleave

基础API>矢量计算>排序组合（ISASI）

ProposalConcat、ProposalExtract、RpSort16、MrgSort4、Sort32

## 6.2.2.5.2 TensorTrait 构造函数

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

根据输入的Layout对象，实例化TensorTrait对象。

函数原型

```cpp
__aicore__ inline TensorTrait(const LayoutType& t = {})
```

<!-- page 871 -->

参数说明

参数名输入/输出描述

t输入输入的Layout对象。输入的数据类型LayoutType，需满足约束说明。

返回值说明

无

约束说明

无

调用示例

●TensorTrait使用示例// TensorTrait使用示例为基于googletest的UT示例

// MakeTensorTrait方法创建TensorTraitAscendC::Shape<int,int,int> shape = AscendC::MakeShape(10, 20, 30);AscendC::Stride<int,int,int> stride = AscendC::MakeStride(1, 100, 200);auto layoutMake = AscendC::MakeLayout(shape, stride);    auto tensorTraitMake = AscendC::MakeTensorTrait<float, AscendC::TPosition::VECIN>(layoutMake);

```cpp
EXPECT_EQ(AscendC::Std::get<0>(tensorTraitMake.GetLayout().GetShape()), 10);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitMake.GetLayout().GetShape()), 20);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitMake.GetLayout().GetShape()), 30);EXPECT_EQ(AscendC::Std::get<0>(tensorTraitMake.GetLayout().GetStride()), 1);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitMake.GetLayout().GetStride()), 100);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitMake.GetLayout().GetStride()), 200);
```

// 构造函数方法创建TensorTraitusing TensorTraitType = AscendC::TensorTrait<half, AscendC::TPosition::VECCALC, AscendC::Layout<AscendC::Shape<int, int, int>, AscendC::Stride<int, int, int>>>;TensorTraitType tensorTraitInit(layoutMake);

```cpp
EXPECT_EQ(AscendC::Std::get<0>(tensorTraitInit.GetLayout().GetShape()), 10);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitInit.GetLayout().GetShape()), 20);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitInit.GetLayout().GetShape()), 30);EXPECT_EQ(AscendC::Std::get<0>(tensorTraitInit.GetLayout().GetStride()), 1);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitInit.GetLayout().GetStride()), 100);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitInit.GetLayout().GetStride()), 200);
EXPECT_EQ(AscendC::Std::get<0>(tensorTraitInit.GetShape()), 10);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitInit.GetShape()), 20);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitInit.GetShape()), 30);EXPECT_EQ(AscendC::Std::get<0>(tensorTraitInit.GetStride()), 1);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitInit.GetStride()), 100);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitInit.GetStride()), 200);
```

// SetLayout方法设置TensorTraitTensorTraitType tensorTraitSet;tensorTraitSet.SetLayout(layoutMake);

```cpp
EXPECT_EQ(AscendC::Std::get<0>(tensorTraitSet.GetLayout().GetShape()), 10);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitSet.GetLayout().GetShape()), 20);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitSet.GetLayout().GetShape()), 30);EXPECT_EQ(AscendC::Std::get<0>(tensorTraitSet.GetLayout().GetStride()), 1);EXPECT_EQ(AscendC::Std::get<1>(tensorTraitSet.GetLayout().GetStride()), 100);EXPECT_EQ(AscendC::Std::get<2>(tensorTraitSet.GetLayout().GetStride()), 200);
```
