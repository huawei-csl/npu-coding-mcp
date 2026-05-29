# 如何使用workspace

> **Section**: 2.10.9.3  
> **PDF Pages**: 393–393  

---

<!-- page 393 -->

if (workspace == nullptr) {        return;    }    GM_ADDR usr = AscendC::GetUserWorkspace(workspace);    KernelAdd op;    op.Init(x, y, z, tilingData.numBlocks, tilingData.totalLength, tilingData.tileNum);    KERNEL_TASK_TYPE_DEFAULT(KERNEL_TYPE_MIX_VECTOR_CORE); // 使能VectorCore    if (TILING_KEY_IS(1)) {        op.Process1();    } else if (TILING_KEY_IS(2)) {        op.Process2();    }    // ...}

2.完成host侧tiling开发时，设置的numBlocks代表的是AI Core和Vector Core的总数，比如用户在host侧设置numBlocks为10，则会启动总数为10的AI Core和Vector Core；为保证启动Vector Core，设置数值应大于AI Core的核数。您可以通过6.4.2.1.7 GetCoreNumAic接口获取AI Core的核数，6.4.2.1.9GetCoreNumVector接口获取Vector Core的核数。如下代码片段，分别为使用kernel直调工程和自定义算子工程时的设置样例，此处设置为AI Core和VectorCore的总和，表示所有AI Core和Vector Core都启动。

–kernel直调工程auto ascendcPlatform = platform_ascendc::PlatformAscendCManager::GetInstance();auto totalCoreNum = ascendcPlatform.GetCoreNumAic();// ASCENDXXX请替换为实际的版本型号if (ascendcPlatform.GetSocVersion() == platform_ascendc::SocVersion::ASCENDXXX) {   totalCoreNum = totalCoreNum + ascendcPlatform.GetCoreNumVector();}...kernel_name<<<totalCoreNum , l2ctrl, stream>>>(argument list);

–自定义算子工程// 配套的host侧tiling函数示例：ge::graphStatus TilingFunc(gert::TilingContext* context){        // 使能VectorCore，将numBlocks置为AI Core中vector核数 + Vector Core中的vector核数    auto ascendcPlatform = platform_ascendc::PlatformAscendC(platformInfo);    auto totalCoreNum = ascendcPlatform.GetCoreNumAic();    // ASCENDXXX请替换为实际的版本型号    if (ascendcPlatform.GetSocVersion() == platform_ascendc::SocVersion::ASCENDXXX) {       totalCoreNum = totalCoreNum + ascendcPlatform.GetCoreNumVector();    }    context->SetBlockDim(totalCoreNum);}

说明

●请参考Ascend C API中具体API支持的型号，来判断API接口是否支持Atlas 推理系列产品Vector Core。

●支持Vector Core后，因为AI Core和Vector Core会分别执行，通过不同的任务进行调度，所以不支持核间同步指令，如IBSet、IBWait、SyncAll等。

●算子计算溢出（输入inf/nan或计算结果超出范围）时，需注意AI Core和Vector Core结果表现不一致，AI Core仅支持饱和模式，Vector Core仅支持inf/nan模式。

## 2.10.9.3 如何使用workspace

workspace是设备侧Global Memory上的一块内存。workspace内存分为两部分：系统workspace和用户workspace。

●系统workspace：Ascend C API需要预留的workspace内存
