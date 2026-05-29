# SetSysWorkSpace

> **Section**: 2  
> **PDF Pages**: 1812–1812  

---

<!-- page 1812 -->

}// 结束矩阵乘操作mm.End();

## ?.2. SetSysWorkSpace

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

框架需要使用的workspace称之为系统workspace。6.2.4.2.1 Matmul Kernel侧接口等高阶API需要系统workspace，所以在使用该类API时，需要调用该接口，设置系统workspace的指针。采用工程化算子开发方式或者kernel直调方式（开启HAVE_WORKSPACE编译选项）时，不需要开发者手动设置，框架会自动设置。其他场景下，需要开发者调用SetSysWorkSpace进行设置。

在kernel侧调用该接口前，需要在host侧调用GetLibApiWorkSpaceSize获取系统workspace的大小，并在host侧设置workspacesize大小。样例如下：

// 用户自定义的tiling函数static ge::graphStatus TilingFunc(gert::TilingContext* context){    AddApiTiling tiling;    ...    size_t usrSize = 256; // 设置用户需要使用的workspace大小。    // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。    auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());    uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();    size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。    currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。    ...}

函数原型

```cpp
__aicore__ inline void SetSysWorkspace(GM_ADDR workspace)
```
