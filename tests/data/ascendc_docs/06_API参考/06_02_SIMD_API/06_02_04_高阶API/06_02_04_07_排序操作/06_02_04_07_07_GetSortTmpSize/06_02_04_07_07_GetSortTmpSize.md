# GetSortTmpSize

> **Section**: 6.2.4.7.7  
> **PDF Pages**: 2817–2817  

---

<!-- page 2817 -->

该样例适用于：

Atlas 350 加速卡

static constexpr AscendC::SortConfig config = {AscendC::SortType::RADIX_SORT, false};Sort<T, false, config>(dstLocal, dstIndexLocal, srcLocal, 1024);示例结果输入数据（srcGm）: 1024个half类型数据[1023 1022 ... 2 1 0]输入数据（srcIndexGm）: 1024个uint32_t类型数据[0 1 2 ... 1022 1023]输出数据（dstGm）:[0 1 2 ... 1022 1023]输出数据（dstIndexGm）:[1023 1022 ... 2 1 0]

## 6.2.4.7.7 GetSortTmpSize

功能说明

获取Sort接口所需的临时空间大小。

函数原型

```cpp
uint32_t GetSortTmpSize(const platform_ascendc::PlatformAscendC &ascendcPlatform, const uint32_t elemCount, const uint32_t dataTypeSize)
```

参数说明

表6-1296接口参数列表

参数名输入/输出

描述

ascendcPlatform

输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。

elemCount输入输入元素个数。

dataTypeSize

输入输入数据大小（单位为字节）。

返回值说明

Sort接口所需的临时空间大小。

约束说明

无

调用示例

```cpp
fe::PlatFormInfos platform_info;auto plat = platform_ascendc::PlatformAscendC(&platform_info);const uint32_t elemCount = 128;AscendC::GetSortTmpSize(plat, elemCount, 4);
```
