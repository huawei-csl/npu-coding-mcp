# GetCosTmpBufferFactorSize

> **Section**: 6.2.4.1.5.3  
> **PDF Pages**: 2025–2025  

---

<!-- page 2025 -->

```cpp
AscendC::GetCosMaxMinTmpSize(shape, 2, false, maxValue, minValue);AscendC::CosConfig config;config.algo = AscendC::CosAlgo::RADIAN_REDUCTION;AscendC::GetCosMaxMinTmpSize(config, shape, 2, false, maxValue, minValue);
```

## 6.2.4.1.5.3 GetCosTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCount和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

●算子实现需要调用Cos接口，开发者为其预留currBuff大小的空间，利用GetCosTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCount / typeSize**

●算子实现需要调用两个kernel侧API KernelIntf1、KernelIntf2，利用两个GetXxxTmpBufferFactorSize（其中Xxx为需要调用的两个高阶API）接口的两组输出值(maxLiveNodeCount、extraBuf)以及当前现有的临时空间，推导单次最大计算元素数量currentShapeSize为：

**currentShapeSize1 = (currBuff - extraBuf1) / maxLiveNodeCount1 /typeSize**

**currentShapeSize2 = (currBuff - extraBuf2) / maxLiveNodeCount2 /typeSize**

**currentShapeSize = min(currentShapeSize1, currentShapeSize2)**

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

函数原型

```cpp
void GetCosTmpBufferFactorSize(const uint32_t typeSize, uint32_t& maxLiveNodeCount, uint32_t& extraBuf)
void GetCosTmpBufferFactorSize(const CosConfig& config, const uint32_t typeSize, uint32_t& maxLiveNodeCount, uint32_t& extraBuf)
```

参数说明

表6-838参数列表

参数名输入/输出

功能

config输入该参数仅支持Atlas 350 加速卡。

Cos接口的相关配置信息。该参数的配置必须与CosKernel接口模板参数config的配置保持一致。

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。
