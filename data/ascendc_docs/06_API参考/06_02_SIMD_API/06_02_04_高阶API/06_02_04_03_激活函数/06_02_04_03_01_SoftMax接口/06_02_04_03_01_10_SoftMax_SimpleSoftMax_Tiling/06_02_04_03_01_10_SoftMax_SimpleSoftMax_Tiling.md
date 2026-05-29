# SoftMax/SimpleSoftMax Tiling

> **Section**: 6.2.4.3.1.10  
> **PDF Pages**: 2521–2521  

---

<!-- page 2521 -->

```cpp
tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());
    context->GetRawTilingData()->SetDataSize(tiling.GetDataSize());
    context->SetTilingKey(1);
    return ge::GRAPH_SUCCESS;}} // namespace optiling
```

步骤3对应的kernel侧通过在核函数中调用GET_TILING_DATA获取TilingData，继而将TilingData中的SoftMax Tiling信息传入SoftMax接口参与计算。完整的kernel侧样例请参考调用示例。

extern "C" __global__ __aicore__ void func_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling){    GET_TILING_DATA(tilingData, tiling);    KernelFunc op;    op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum,tilingData.SoftMaxTiling);    if (TILING_KEY_IS(1)) {        op.Process();    }}

**----结束**

## 6.2.4.3.1.10 SoftMax/SimpleSoftMax Tiling

功能说明

用于获取SoftMax/SimpleSoftMax Tiling参数。

函数原型

●获取Kernel接口计算所需最大/最小临时空间的接口uint32_t GetSoftMaxMaxTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isReuseSource)uint32_t GetSoftMaxMinTmpSize(const ge::Shape& srcShape, const uint32_t dataTypeSize, const bool isReuseSource)

●Tiling计算接口

–AscendC::optiling命名空间下的计算接口void SoftMaxTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, optiling::SoftMaxTiling& softmaxTiling)

–AscendC命名空间下的计算接口void SoftMaxTilingFunc(const ge::Shape& srcShape, const uint32_t dataTypeSize, const uint32_t localWorkSpaceSize, AscendC::tiling::SoftMaxTiling& softmaxTiling)

参数说明

表6-1131 SoftMax/SimpleSoftMax GetSoftMaxMaxTmpSize/GetSoftMaxMinTmpSize 接口参数列表

接口输入/输出

功能

srcShape输入输入srcTensor的shape信息。

dataTypeSize

输入参与计算的max和sum的数据类型，比如half=2。
