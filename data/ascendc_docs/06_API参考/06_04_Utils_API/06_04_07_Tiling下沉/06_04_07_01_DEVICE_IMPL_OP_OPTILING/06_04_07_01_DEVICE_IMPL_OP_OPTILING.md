# DEVICE_IMPL_OP_OPTILING

> **Section**: 6.4.7.1  
> **PDF Pages**: 3869–3869  

---

<!-- page 3869 -->

```cpp
context->SetBlockDim(NUM_BLOCKS);
    tiling.set_totalLength(totalLength);
    tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());
    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());
    ASCENDC_TPL_SEL_PARAM(context, D_T_X, D_T_Y, D_T_Z, TILE_NUM, IS_SPLIT);
    size_t *currentWorkspace = context->GetWorkspaceSizes(1);
    currentWorkspace[0] = 0;
    return ge::GRAPH_SUCCESS;}
```

## 6.4.7 Tiling 下沉

## 6.4.7.1 DEVICE_IMPL_OP_OPTILING

功能说明

在Tiling下沉场景中，该宏定义用于生成Tiling下沉的注册类，再通过调用注册类的成员函数来注册需要下沉的Tiling函数。

函数原型

```cpp
namespace optiling {using SinkTilingFunc = std::function<ge::graphStatus(gert::TilingContext *context)>;
```

class DeviceOpImplRegisterImpl;// 开发者仅关注Tiling成员函数class DeviceOpImplRegister {public:  DeviceOpImplRegister(const char *opType);~DeviceOpImplRegister();  DeviceOpImplRegister(DeviceOpImplRegister &&other) noexcept;  DeviceOpImplRegister(const DeviceOpImplRegister &other);  DeviceOpImplRegister &operator=(const DeviceOpImplRegister &) = delete;  DeviceOpImplRegister &operator=(DeviceOpImplRegister &&) = delete;  DeviceOpImplRegister &Tiling(SinkTilingFunc func);

```cpp
// ...};}  // namespace optiling
#define DEVICE_IMPL_OP_OPTILING(optype)                                                                      \  static optiling::DeviceOpImplRegister VAR_UNUSED g_deviceOpImplRegister##optype =                                    \      optiling::DeviceOpImplRegister(#optype)#endif
```

参数说明

表6-1965 DEVICE_IMPL_OP_OPTILING 参数说明

参数输入/输出说明

optype输入需要注册Tiling函数的OpType（算子类型）。
