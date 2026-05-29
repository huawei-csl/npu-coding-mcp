# GetConcatTmpSize

> **Section**: 6.2.4.7.4  
> **PDF Pages**: 2805–2805  

---

<!-- page 2805 -->

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

请参见6.2.4.7.11 MrgSort的调用示例。

## 6.2.4.7.4 GetConcatTmpSize

功能说明

获取Concat接口所需的临时空间大小。

函数原型

```cpp
uint32_t GetConcatTmpSize(const platform_ascendc::PlatformAscendC &ascendcPlatform, const uint32_t elemCount, const uint32_t dataTypeSize)
```

参数说明

表6-1289接口参数列表

参数名输入/输出

描述

ascendcPlatform

输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。

elemCount输入输入元素个数。

dataTypeSize

输入输入数据大小（单位为字节）。

返回值说明

Concat接口所需的临时空间大小。

约束说明

无

调用示例

```cpp
fe::PlatFormInfos platform_info;auto plat = platform_ascendc::PlatformAscendC(&platform_info);const uint32_t elemCount = 128;AscendC::GetConcatTmpSize(plat, elemCount, 2);
```
