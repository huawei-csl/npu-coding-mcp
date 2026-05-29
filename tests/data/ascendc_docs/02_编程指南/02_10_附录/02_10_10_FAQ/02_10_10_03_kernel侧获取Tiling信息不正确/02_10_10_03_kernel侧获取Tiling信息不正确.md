# kernel侧获取Tiling信息不正确

> **Section**: 2.10.10.3  
> **PDF Pages**: 402–402  

---

<!-- page 402 -->

AscendC::LocalTensor<T> local1 = que0.AllocTensor<T>();AscendC::LocalTensor<T> local2 = que1.AllocTensor<T>();AscendC::LocalTensor<T> local3 = que2.AllocTensor<T>();AscendC::LocalTensor<T> local4 = que3.AllocTensor<T>();// 第5个AllocTensor会出现资源分配失败，同一个TPosition上同时Alloc出来的Tensor数量超出了4个的限制AscendC::LocalTensor<T> local5 = que4.AllocTensor<T>();

处理步骤

如果确实有多块buffer使用，可以将多个buffer合并到一块buffer，通过偏移使用。样例如下：

// 此时建议通过以下方法解决：// 如果确实有多块buffer使用, 可以将多个buffer合并到一块buffer, 通过偏移使用pipe.InitBuffer(que0, 1, len * 3);pipe.InitBuffer(que1, 1, len * 3);/* * 分配出3块内存大小的LocalTensor, local1的地址为que0中buffer的起始地址， * local2的地址为local1的地址偏移len后的地址，local3的地址为local1的地址偏移 * len * 2的地址 */int32_t offset1 = len;int32_t offset2 = len * 2;AscendC::LocalTensor<T> local1 = que0.AllocTensor<T>();AscendC::LocalTensor<T> local2 = local1[offset1];AscendC::LocalTensor<T> local3 = local1[offset2];

## 2.10.10.3 kernel 侧获取Tiling 信息不正确

现象描述

通过算子在kernel侧实现代码中添加PRINTF打印发现kernel侧获取的Tiling信息不正确。

比如下文样例，增加的打印代码如下：

```cpp
PRINTF("tiling_data.totalLength: %d tiling_data.tileNum: %d.\n", tiling_data.totalLength, tiling_data.tileNum);
```

打印的Tiling数据如下，全为0：

```cpp
tiling_data.totalLength: 0 tiling_data.tileNum: 0.
```

问题根因

kernel侧获取Tiling信息不正确的原因一般有以下两种：

●host侧计算Tiling的逻辑不正确

●kernel侧核函数的参数未按照正确顺序填写

处理步骤

步骤1参考如下示例，打印TilingData的数据，确认host侧序列化保存的TilingData是否正确。如果此时打印值有误，说明Tiling的计算逻辑可能不正确，需要进一步检查host侧Tiling实现代码，排查计算逻辑是否有误。

std::cout<<*reinterpret_cast<uint32_t *>(context->GetRawTilingData()->GetData())<<std::endl; //按照实际数据类型打印TilingData第一个参数值，如需确认其他值，取值指针向后偏移即可

步骤2如果上一步骤中打印的TilingData正确，需要排查kernel侧核函数的参数是否按照正确顺序填写。
