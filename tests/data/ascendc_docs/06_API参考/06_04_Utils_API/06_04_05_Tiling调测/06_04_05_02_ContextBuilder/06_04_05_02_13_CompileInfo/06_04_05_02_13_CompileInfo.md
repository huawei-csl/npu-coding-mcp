# CompileInfo

> **Section**: 6.4.5.2.13  
> **PDF Pages**: 3852–3852  

---

<!-- page 3852 -->

调用示例

```cpp
context_ascendc::ContextBuilder builder;auto builder    .NodeIoNum(1,1)    .IrInstanceNum({1})    .AddAttr("attr_1", 1)    .AddAttr("attr_2", true)    .AddAttr("attr_3", "stringValue")    .AddAttr("attr_4", 1.f)    .AddAttr("attr_5", {1})    .AddAttr("attr_6", {false})    .AddAttr("attr_7", {"stringValue"})    .AddAttr("attr_8", {1.f})    .AddAttr("attr_9", {{1, 2}, {3, 4}})
```

## 6.4.5.2.13 CompileInfo

功能说明

将指向CompileInfo的指针传入TilingContext

函数原型

```cpp
ContextBuilder &CompileInfo(void *compileInfo)
```

参数说明

参数输入/输出说明

compileInfo输入指向CompileInfo的void指针

返回值说明

当前ContextBuilder的对象。

约束说明

由于TilingContext与KernelContext、TilingParseContext内部数据排序不同，CompileInfo()只支持以调用BuildTilingContext()为前提来使用；其他场景建议用Outputs接口，否则发生未定义行为。

调用示例

void AddCompileInfo(TilingParseContext *tilingParseContext){    ......    void *compilerInfo = *tilingParseContext->GetOutputPointer<void **>(0);    auto kernelContextHolder = context_ascendc::ContextBuilder()                                    ...... // 增加算子输入输出接口的调用                                    .CompileInfo(compileInfo)                                    .BuildTilingContext();    ......}
