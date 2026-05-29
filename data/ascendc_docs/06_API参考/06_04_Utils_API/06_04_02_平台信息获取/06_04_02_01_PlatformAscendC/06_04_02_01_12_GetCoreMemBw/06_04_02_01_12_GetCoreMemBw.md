# GetCoreMemBw

> **Section**: 6.4.2.1.12  
> **PDF Pages**: 3768–3768  

---

<!-- page 3768 -->

参数说明

参数输入/输出说明

memType输入硬件存储空间类型。

size输出对应类型的存储空间大小，单位：字节。

返回值说明

无

约束说明

无

调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t ub_size, l1_size;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);    // ...    return ret;}
```

## 6.4.2.1.12 GetCoreMemBw

功能说明

获取硬件平台存储空间的带宽大小。硬件存储空间类型定义如下：

enum class CoreMemType {    L0_A = 0, // 预留参数，暂不支持    L0_B = 1, // 预留参数，暂不支持    L0_C = 2, // 预留参数，暂不支持    L1 = 3,   // 预留参数，暂不支持    L2 = 4,    UB = 5,   // 预留参数，暂不支持    HBM = 6,    RESERVED};

函数原型

```cpp
void GetCoreMemBw(const CoreMemType &memType, uint64_t &bwSize) const
```

参数说明

参数输入/输出说明

memType输入硬件存储空间类型。

bwSize输出对应硬件的存储空间的带宽大小。单位是Byte/cycle，cycle代表时钟周期。
