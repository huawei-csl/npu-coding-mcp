# GetTaskRatio

> **Section**: 6.2.3.13.3  
> **PDF Pages**: 1971–1971  

---

<!-- page 1971 -->

// 避免代码中直接的硬件条件判断（如使用ASCEND_IS_AIV或ASCEND_IS_AIC）    Async<EngineType::AIC, aicOperation>(a, b, bias, c, workspace, tiling, &pipe);    Async<EngineType::AIV, aivOperation>(c, tiling, &pipe);}__aicore__ inline void aicOperation(GM_ADDR a, GM_ADDR b, GM_ADDR bias, GM_ADDR c, GM_ADDR workspace, const TCubeTiling &tiling, AscendC::TPipe *pipe) {    MatmulLeakyKernel<half, half, float, float> matmulLeakyKernel;    matmulLeakyKernel.Init(a, b, bias, c, workspace, tiling, pipe);    REGIST_MATMUL_OBJ(pipe, GetSysWorkSpacePtr(), matmulLeakyKernel.matmulObj, &matmulLeakyKernel.tiling);    matmulLeakyKernel.Process(pipe);}

```cpp
__aicore__ inline void aivOperation(GM_ADDR c, const TCubeTiling &tiling, AscendC::TPipe *pipe) {    LeakyReluKernel<float> leakyReluKernel;
    leakyReluKernel.Init(c, tiling, pipe);
    leakyReluKernel.Process(pipe);}
```

## 6.2.3.13.3 GetTaskRatio

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

分离模式下，获取一个AI Core上Cube Core（AIC）或者Vector Core（AIV）的数量与AI Core数量的比例。耦合模式下，固定返回1。

函数原型

```cpp
__aicore__ inline int64_t GetTaskRatio()
```

参数说明

无

返回值说明

●针对分离模式，不同Kernel类型下（通过6.2.3.14.12 设置Kernel类型接口设置），在AIC和AIV上调用该接口的返回值如下：
