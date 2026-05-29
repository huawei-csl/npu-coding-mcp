# ContextBuilder构造函数

> **Section**: 6.4.5.2.2  
> **PDF Pages**: 3844–3844  

---

<!-- page 3844 -->

```cpp
.Inputs(...)    .Outputs(...)    .BuildKernelRunContext();gert::KernelContext* tilingParseContext = kernelContextHolder->GetContext<gert::KernelContext>();
```

// 构造TilingContextauto tilingContextHolder = context_ascendc::ContextBuilder()    .SetOpNameType(...,...)    .NodeIoNum(...)    .IrInstanceNum(...)    .AddInputTd(...)    .AddOutputTd(...)    .AddAttr(...)    .BuildTilingContext(...);gert::TilingContext* tilingContext = tilingContextHolder->GetContext<gert::TilingContext>();

## 6.4.5.2.2 ContextBuilder 构造函数

功能说明

创建ContextBuilder对象时，初始化数据成员。

函数原型

```cpp
ContextBuilder()
```

参数说明

无。

约束说明

无。

## 6.4.5.2.3 KernelRunContextHolder 结构定义

功能说明

该结构体为ContextBuilder类最终的构造结果，可通过指定的接口获取内部算子信息或获取KernelContext类的对象。

函数原型

struct KernelRunContextHolder {    KernelRunContextHolder();~KernelRunContextHolder();    template<typename T>    T *GetContext() const    {        return reinterpret_cast<T*>(context);    }    gert::ComputeNodeInfo *MutableComputeNodeInfo()    {        return reinterpret_cast<gert::ComputeNodeInfo *>(computeNodeExtendHolder.get());    }    std::unique_ptr<ValueHolderImpl> valueHolder;    std::unique_ptr<uint8_t[]> computeNodeExtendHolder;    KernelRunContext *context {nullptr};};
