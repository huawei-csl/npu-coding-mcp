# ReserveLocalMemory

> **Section**: 6.4.2.1.16  
> **PDF Pages**: 3771–3771  

---

<!-- page 3771 -->

返回值说明

当前CreateCubeResGroup所需要的workspace空间大小。

约束说明

无。

调用示例

// 用户自定义的tiling函数static ge::graphStatus TilingFunc(gert::TilingContext* context){    AddApiTiling tiling;    ...    // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。    auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());    uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();    // 设置用户需要使用的workspace和CreateCubeResGroup需要的大小作为usrWorkspace的总大小。    size_t usrSize = 256 + ascendcPlatform.GetResCubeGroupWorkSpaceSize();     size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。    currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。    ...}

## 6.4.2.1.16 ReserveLocalMemory

功能说明

该函数用于在Unified Buffer中预留指定大小的内存空间。调用该接口后，使用GetCoreMemSize可以获取实际可用的剩余Unified Buffer空间大小。

函数原型

```cpp
void ReserveLocalMemory(ReservedSize size)
```

参数说明

参数名输入/输出说明

ReservedSize

输入需要预留的空间大小。enum class ReservedSize {    RESERVED_SIZE_8K,  // 预留8 * 1024B空间    RESERVED_SIZE_16K, // 预留16 * 1024B空间    RESERVED_SIZE_32K, // 预留32 * 1024B空间};

返回值说明

无

约束说明

多次调用该函数时，仅保留最后一次调用的结果。
