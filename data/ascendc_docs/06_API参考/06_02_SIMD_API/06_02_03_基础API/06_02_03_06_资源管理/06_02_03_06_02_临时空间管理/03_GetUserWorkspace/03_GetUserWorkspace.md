# GetUserWorkspace

> **Section**: 3  
> **PDF Pages**: 1813–1813  

---

<!-- page 1813 -->

参数说明

表6-714接口参数说明

参数名称输入/输出

描述

workspace输入核函数传入的workspace的指针，包括系统workspace和用户使用的workspace。

约束说明

无

返回值说明

无

调用示例

template<typename aType, typename bType, typename cType, typename biasType>__aicore__ inline void MatmulLeakyKernel<aType, bType, cType, biasType>::Init(    GM_ADDR a, GM_ADDR b, GM_ADDR bias, GM_ADDR c, GM_ADDR workspace, const TCubeTiling& tiling, float alpha){    // 融合算子的初始化操作    // ...    // workspace为核函数传入的GM指针，用于设置系统workspace    AscendC::SetSysWorkspace(workspace);    if (GetSysWorkSpacePtr() == nullptr) {        return;    }    // 后续Matmul指令    ...}

## ?.3. GetUserWorkspace

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√
