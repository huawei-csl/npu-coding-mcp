# LoadTilingLibrary

> **Section**: 6.4.5.1.4  
> **PDF Pages**: 3843–3843  

---

<!-- page 3843 -->

## 6.4.5.1.4 LoadTilingLibrary

功能说明

根据输入的路径，加载对应的Tiling动态库。开发者基于工程化算子开发开发方式完成算子实现后，可通过算子包编译或算子动态库编译获取对应的Tiling动态库文件。

●算子包编译：Tiling实现对应的动态库为算子包部署目录下的liboptiling.so。具体路径可参考2.10.2.6.2 算子包部署。

●动态库编译：Tiling实现集成在算子动态库libcust_opapi.so中。具体路径可参考2.10.2.7 算子动态库和静态库编译。

函数原型

```cpp
bool LoadTilingLibrary(const char *tilingSoPath) const
```

参数说明

参数名输入/输出描述

tilingSoPath输入Tiling动态库的路径，支持相对路径与绝对路径。

返回值说明

true：Tiling动态库加载成功；false：Tiling动态库加载失败。具体错误可参考Log信息。

关于日志配置和查看，请参考《环境变量参考》中“辅助功能 > 日志”章节。

约束说明

无

调用示例

```cpp
context_ascendc::OpTilingRegistry tmpIns;bool flag = tmpIns.LoadTilingLibrary("/your/path/to/so_path/liboptiling.so");if (flag == false) {    std::cout << "Load tiling so failed" << std::endl;    ...        }// ...
```

## 6.4.5.2 ContextBuilder

## 6.4.5.2.1 简介

ContextBuilder类提供一系列的API接口，支持手动构造TilingContext类来验证Tiling函数以及KernelContext类用于TilingParse函数的验证。

调用示例

// 构造KernelContextauto kernelContextHolder = context_ascendc::ContextBuilder()
