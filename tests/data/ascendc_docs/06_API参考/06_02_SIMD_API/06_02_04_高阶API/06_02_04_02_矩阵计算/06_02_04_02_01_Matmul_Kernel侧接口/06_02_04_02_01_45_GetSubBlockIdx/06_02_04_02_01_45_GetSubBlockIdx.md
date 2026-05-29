# GetSubBlockIdx

> **Section**: 6.2.4.2.1.45  
> **PDF Pages**: 2398–2398  

---

<!-- page 2398 -->

调用示例

```cpp
typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
```

MatmulImpl<aType, bType, cType, biasType, CFG_NORM> mm;mm.SetSubBlockIdx(0);  // 子核ID设置为0

## 6.2.4.2.1.45 GetSubBlockIdx

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

获取当前AIV核的ID。分离架构下，一个AI Core由Cube Core（AIC）和Vector Core（AIV）按照一定比例1：N进行组合，其中N个AIV的子核ID分别为0, 1, ..., N-1。

Matmul::GetSubBlockIdx()与基础API接口AscendC::GetSubBlockIdx()的区别在于，Matmul::GetSubBlockIdx()用于获取当前AIV核在当前AI Core分组中的ID，而AscendC::GetSubBlockIdx()获取的是AIV核在所有AI Core分组中的逻辑ID。例如，有10组AI Core，AIC与AIV的比例为1:2，共20个AIV核。调用Matmul::GetSubBlockIdx()时，20个AIV的获取结果依次为0, 1, 0, 1, 0, 1, ..., 0, 1。调用AscendC::GetSubBlockIdx()时，20个AIV的获取结果依次为0, 1, 2, 3, 4, 5, ..., 18, 19。

函数原型

```cpp
__aicore__  inline uint8_t GetSubBlockIdx()
```

参数说明

无

返回值说明

当前AIV核的ID。
