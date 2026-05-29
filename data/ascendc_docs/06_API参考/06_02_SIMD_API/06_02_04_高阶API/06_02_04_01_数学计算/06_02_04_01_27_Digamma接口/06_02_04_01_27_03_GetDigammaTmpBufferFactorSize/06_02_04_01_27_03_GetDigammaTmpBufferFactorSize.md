# GetDigammaTmpBufferFactorSize

> **Section**: 6.2.4.1.27.3  
> **PDF Pages**: 2146–2146  

---

<!-- page 2146 -->

## 6.2.4.1.27.3 GetDigammaTmpBufferFactorSize

功能说明

kernel侧Digamma接口的计算需要开发者预留/申请临时空间，最大临时空间（maxTmpBuffer）和输入所占空间（inputSize * typeSize）存在以下关系：

**maxTmpBuffer = maxLiveNodeCount * inputSize * typeSize + extraBuffer**

其中maxLiveNodeCount表示最大临时空间是输入所占空间的多少倍；extraBuffer表示使用的额外临时空间大小。

该接口用于获取maxLiveNodeCount和extraBuffer，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuffer可以推算算子单次最大计算元素数量；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

示例如下：

算子实现需要调用Digamma接口，开发者为其预留currBuff大小的空间，利用GetDigammaTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuffer输出值，反推Digamma算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuffer) / maxLiveNodeCount / typeSize**

函数原型

```cpp
void GetDigammaTmpBufferFactorSize(const uint32_t typeSize, uint32_t& maxLiveNodeCount, uint32_t& extraBuffer)
```

参数说明

表6-930参数列表

参数名输入/输出

功能

typeSize输入输入的数据类型大小，单位为字节。比如输入的数据类型为half，此处应传入2。

maxLiveNodeCount

输出最大存活节点数，最大临时空间是输入所占空间的多少倍。

extraBuffer输出使用的额外临时空间大小，单位为字节。

返回值说明

无

约束说明

当利用maxLiveNodeCount，extraBuffer反推出的currentShapeSize * typeSize <256B时，currentShapeSize按照256B/typeSize的值向上取整。
