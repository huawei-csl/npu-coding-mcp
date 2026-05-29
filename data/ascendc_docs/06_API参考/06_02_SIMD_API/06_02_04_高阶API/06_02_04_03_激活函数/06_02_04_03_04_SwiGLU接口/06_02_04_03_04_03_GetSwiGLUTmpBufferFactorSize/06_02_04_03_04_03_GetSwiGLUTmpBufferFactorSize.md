# GetSwiGLUTmpBufferFactorSize

> **Section**: 6.2.4.3.4.3  
> **PDF Pages**: 2552–2552  

---

<!-- page 2552 -->

参数名输入/输出

描述

minValue输出SwiGLU接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

isReuseSource

输入是否复用源操作数输入的空间，与kernel侧接口一致。

返回值说明

无

约束说明

无

调用示例

// 输入shape信息为1024;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t max;uint32_t min;AscendC::GetSwiGLUMaxMinTmpSize(shape, 2, max, min, false);

## 6.2.4.3.4.3 GetSwiGLUTmpBufferFactorSize

功能说明

kernel侧SwiGLU接口的计算需要开发者预留/申请临时空间，最大临时空间（maxTmpBuffer）和输入所占空间（inputSize * typeSize）存在以下关系：

**maxTmpBuffer = maxLiveNodeCount * inputSize * typeSize + extraBuffer**

其中maxLiveNodeCount表示最大临时空间是输入所占空间的多少倍；extraBuffer表示使用的额外临时空间大小。

该接口用于获取maxLiveNodeCount和extraBuffer，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuffer可以推算算子单次最大计算元素数量。

示例如下：

算子实现需要调用SwiGLU接口，开发者为其预留currBuff大小的空间，利用GetSwiGLUTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuffer输出值，反推SwiGLU算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuffer) / maxLiveNodeCount / typeSize**

函数原型

```cpp
void GetSwiGLUTmpBufferFactorSize(const uint32_t typeSize, uint32_t& maxLiveNodeCount, uint32_t& extraBuffer)
```
