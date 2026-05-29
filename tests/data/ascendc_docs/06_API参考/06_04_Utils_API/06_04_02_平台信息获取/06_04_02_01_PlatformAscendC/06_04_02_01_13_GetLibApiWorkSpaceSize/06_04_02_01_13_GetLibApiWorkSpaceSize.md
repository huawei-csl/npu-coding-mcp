# GetLibApiWorkSpaceSize

> **Section**: 6.4.2.1.13  
> **PDF Pages**: 3769–3769  

---

<!-- page 3769 -->

返回值说明

无

约束说明

无

调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t l2_bw;
    ascendcPlatform.GetCoreMemBw(platform_ascendc::CoreMemType::L2, l2_bw);    // ...    return ret;}
```

## 6.4.2.1.13 GetLibApiWorkSpaceSize

功能说明

获取AscendC API需要的workspace空间大小。

函数原型

```cpp
uint32_t GetLibApiWorkSpaceSize(void) const
```

参数说明

无

返回值说明

返回uint32_t数据类型的结果，该结果代表当前系统workspace的大小，单位为字节。

约束说明

无

调用示例

// 用户自定义的tiling函数static ge::graphStatus TilingFunc(gert::TilingContext* context){    AddApiTiling tiling;    ...    size_t usrSize = 256; // 设置用户需要使用的workspace大小。    // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。    auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());    uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();    size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。    currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。    ...}
