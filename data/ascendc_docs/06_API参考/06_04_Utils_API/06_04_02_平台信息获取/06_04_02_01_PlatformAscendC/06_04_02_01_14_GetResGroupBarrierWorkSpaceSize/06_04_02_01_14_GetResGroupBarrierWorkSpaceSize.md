# GetResGroupBarrierWorkSpaceSize

> **Section**: 6.4.2.1.14  
> **PDF Pages**: 3770–3770  

---

<!-- page 3770 -->

## 6.4.2.1.14 GetResGroupBarrierWorkSpaceSize

功能说明

获取6.2.3.12.2 GroupBarrier所需要的workspace空间大小。

函数原型

```cpp
uint32_t GetResGroupBarrierWorkSpaceSize(void) const
```

参数说明

无

返回值说明

当前GroupBarrier所需要的workspace大小。

约束说明

无。

调用示例

// 用户自定义的tiling函数static ge::graphStatus TilingFunc(gert::TilingContext* context){    AddApiTiling tiling;    ...    // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。    auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());    uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();    // 设置用户需要使用的workspace和GroupBarrier需要的大小作为usrWorkspace的总大小。    size_t usrSize = 256 + ascendcPlatform.GetResGroupBarrierWorkSpaceSize(); // 设置用户需要使用的workspace大小。    size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。    currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。    ...}

## 6.4.2.1.15 GetResCubeGroupWorkSpaceSize

功能说明

基于 CreateCubeResGroup进行AI Core分组计算需要传入workspace用于消息通信，在Host侧提供本接口用于获取CreateCubeResGroup所需要的workspace空间大小。

函数原型

```cpp
uint32_t GetResCubeGroupWorkSpaceSize(void) const
```

参数说明

无
