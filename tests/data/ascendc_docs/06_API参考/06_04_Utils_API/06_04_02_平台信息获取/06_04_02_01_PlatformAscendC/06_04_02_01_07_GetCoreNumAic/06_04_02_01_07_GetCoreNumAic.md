# GetCoreNumAic

> **Section**: 6.4.2.1.7  
> **PDF Pages**: 3764–3764  

---

<!-- page 3764 -->

参数说明

无

返回值

●对于RegBase硬件平台芯片架构，返回当前硬件平台Vector计算单元位宽。

●对于非RegBase硬件平台芯片架构，返回0 。

约束说明

无

调用示例

```cpp
void GetLayerNormMaxMinTmpSize(...){       platform_ascendc::PlatformAscendC* platform = platform_ascendc::PlatformAscendCManager::GetInstance();        ...        const uint32_t vecLenB32 = platform->GetVecRegLen() / LAYERNORM_SIZEOF_FLOAT;
        const uint32_t vecLenB16 = platform->GetVecRegLen() / LAYERNORM_SIZEOF_HALF;        ...}
```

## 6.4.2.1.7 GetCoreNumAic

功能说明

获取当前硬件平台AI Core中Cube核数。若AI Core的架构为Cube、Vector分离模式，返回Cube Core的核数；耦合模式返回AI Core的核数。

函数原型

```cpp
uint32_t GetCoreNumAic(void) const
```

参数说明

无

返回值说明

Atlas 训练系列产品，耦合模式，返回AI Core的核数

Atlas 推理系列产品，耦合模式，返回AI Core的核数

Atlas A2 训练系列产品/Atlas A2 推理系列产品，分离模式，返回Cube Core的核数

Atlas A3 训练系列产品/Atlas A3 推理系列产品，分离模式，返回Cube Core的核数

Atlas 350 加速卡，分离模式，返回Cube Core的核数

约束说明

无
