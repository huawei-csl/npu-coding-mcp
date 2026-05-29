# SetUserDefInfo

> **Section**: 6.2.4.2.1.46  
> **PDF Pages**: 2399–2399  

---

<!-- page 2399 -->

约束说明

●该接口仅支持在分离架构下使用，否则返回随机值。

●在分离架构中，AIV核的ID会在REGIST_MATMUL_OBJ()接口内部自动初始化和赋值。因此，需要在调用REGIST_MATMUL_OBJ()接口之后，再调用本接口，以获取正确的ID。

●若在算子程序中调用SetSubBlockIdx()后， GetSubBlockIdx()接口将返回由SetSubBlockIdx接口设置的ID值。

调用示例

```cpp
typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
 typedef AscendC::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
```

AscendC::Matmul<aType, bType, cType, biasType, CFG_NORM> mm;REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);mm.GetSubBlockIdx(); // 获取子核ID

## 6.2.4.2.1.46 SetUserDefInfo

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

使能模板参数MatmulCallBackFunc（自定义回调函数）时，设置算子tiling地址，用于回调函数使用，该接口仅需调用一次。

函数原型

```cpp
__aicore__ inline void SetUserDefInfo(const uint64_t tilingPtr)
```
