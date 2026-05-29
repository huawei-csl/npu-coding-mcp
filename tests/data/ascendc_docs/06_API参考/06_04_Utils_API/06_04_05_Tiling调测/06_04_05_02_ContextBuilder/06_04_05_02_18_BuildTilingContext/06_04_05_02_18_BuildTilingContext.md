# BuildTilingContext

> **Section**: 6.4.5.2.18  
> **PDF Pages**: 3856–3856  

---

<!-- page 3856 -->

参数说明

参数输入/输出说明

workspace输入指向gert::ContinuousVector类的void*指针

返回值说明

当前ContextBuilder的对象。

约束说明

由于TilingContext与KernelContext、TilingParseContext内部数据排序不同，Workspace()只支持以调用BuildTilingContext()为前提来使用；其他场景建议用Outputs接口，否则发生未定义行为。

调用示例

```cpp
void AddWorkspaceData(gert::ContinuousVector *ws){    ......    auto builder = context_ascendc::ContextBuilder()                                    .Workspace(ws);                                    .BuildTilingContext();    ......}
```

## 6.4.5.2.18 BuildTilingContext

功能说明

构造KernelRunContextHolder的对象，该对象可通过GetContext接口获取TilingContext类型的对象。

函数原型

```cpp
std::shared_ptr<KernelRunContextHolder> BuildTilingContext()
```

参数说明

无

返回值说明

指向KernelRunContextHolder的共享指针。

约束说明

无

调用示例

```cpp
auto tilingContextHolder = context_ascendc::ContextBuilder().  .SetOpNameType(...,...)  .NodeIoNum(...)
```
