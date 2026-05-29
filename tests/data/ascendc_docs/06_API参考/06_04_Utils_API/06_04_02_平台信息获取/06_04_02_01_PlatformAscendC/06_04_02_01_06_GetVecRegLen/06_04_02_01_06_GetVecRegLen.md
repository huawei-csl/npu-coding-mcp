# GetVecRegLen

> **Section**: 6.4.2.1.6  
> **PDF Pages**: 3763–3763  

---

<!-- page 3763 -->

参数说明

无

返回值

当前硬件平台架构号的枚举类。该枚举类和AI处理器型号的对应关系请通过CANN软件安装后文件存储路径下include/platform/soc_spec.h头文件获取。

产品NPU_ARCH

Atlas 350 加速卡DAV_3510

Atlas A3 训练系列产品/AtlasA3 推理系列产品

DAV_2201

Atlas A2 训练系列产品/AtlasA2 推理系列产品

DAV_2201

Atlas 200I/500 A2 推理产品DAV_3002

Atlas 推理系列产品AI CoreDAV_2002

Atlas 推理系列产品VectorCore

DAV_2002

Atlas 训练系列产品DAV_1001

约束说明

无

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto npuArch = ascendcPlatform.GetCurNpuArch();    // 根据所获得的版本型号自行设计Tiling策略    // DAV_XXX请替换为实际的架构号    if (socVersion == NpuArch::DAV_XXXX) {        // ...    }    return ret;}

## 6.4.2.1.6 GetVecRegLen

功能说明

获取当前硬件平台芯片架构Vec计算单元位宽。

函数原型

```cpp
uint32_t GetVecRegLen(void) const
```
