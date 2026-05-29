# SetCommEngine

> **Section**: 6.2.4.11.2.15  
> **PDF Pages**: 2985–2985  

---

<!-- page 2985 -->

返回值说明

●0表示设置成功。

●非0表示设置失败。

约束说明

本接口仅在Atlas A3 训练系列产品/Atlas A3 推理系列产品上通信类型为HCCL_CMD_BATCH_WRITE时生效。

调用示例

```cpp
const char *groupName = "testGroup";uint32_t opType = HCCL_CMD_BATCH_WRITE;std::string algConfig = "BatchWrite=level0:fullmesh";uint32_t reduceType = HCCL_REDUCE_SUM;AscendC::Mc2CcTilingConfig mc2CcTilingConfig(groupName, opType, algConfig, reduceType);mc2CcTilingConfig.SetQueueNum(2U);
```

## 6.2.4.11.2.15 SetCommEngine

功能说明

设置通信任务使用的通信引擎。

函数原型

```cpp
uint32_t SetCommEngine(uint8_t commEngine)
```

参数说明

表6-1385参数说明

参数名输入/输出

描述

commEngine

输入通信引擎。uint8_t类型，该参数的取值范围请参考：《HCCL集合通信库》>接口参考中HcclCommConfig接口的hcclOpExpansionMode参数取值说明。

返回值说明

●0表示设置成功。

●非0表示设置失败。

约束说明

无

调用示例

```cpp
static ge::graphStatus AllToAllVCustomTilingFunc(gert::TilingContext *context){    AllToAllVCustomV3TilingData *tiling = context->GetTilingData<AllToAllVCustomV3TilingData>();
```
