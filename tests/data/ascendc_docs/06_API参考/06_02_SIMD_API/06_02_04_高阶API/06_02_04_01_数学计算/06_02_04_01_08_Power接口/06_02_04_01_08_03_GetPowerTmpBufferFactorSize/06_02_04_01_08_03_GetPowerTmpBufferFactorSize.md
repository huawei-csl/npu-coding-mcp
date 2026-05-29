# GetPowerTmpBufferFactorSize

> **Section**: 6.2.4.1.8.3  
> **PDF Pages**: 2044–2044  

---

<!-- page 2044 -->

●Power(dstTensor, srcTensor1, srcTensor2)样例// srcTensor1、srcTensor2输入shape信息均为512;算子输入的数据类型为float;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape shape(shape_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetPowerMaxMinTmpSize(shape, shape, false, 4, false, maxValue, minValue);

●Power(dstTensor, srcTensor1, scalarValue)样例// srcTensor1输入shape信息为128*128，scalarValue的shape为1;算子输入的数据类型为half;不允许修改源操作数std::vector<int64_t> shape1_vec = {128,128};std::vector<int64_t> shape2_vec = {1};ge::Shape shape1(shape1_vec);ge::Shape shape2(shape2_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetPowerMaxMinTmpSize(shape1, shape2, false, 2, false, maxValue, minValue);

●Power(dstTensor, scalarValue, srcTensor2)样例//scalarValue的shape为1，srcTensor2输入shape信息为128*128;算子输入的数据类型为float;不允许修改源操作数std::vector<int64_t> shape1_vec = {1};std::vector<int64_t> shape2_vec = {128,128};ge::Shape shape1(shape1_vec);ge::Shape shape2(shape2_vec);uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetPowerMaxMinTmpSize(shape1, shape2, false, 4, false, maxValue, minValue);

## 6.2.4.1.8.3 GetPowerTmpBufferFactorSize

功能说明

该接口用于获取maxLiveNodeCount和extraBuf，在固定空间大小的情况下，通过maxLiveNodeCount和extraBuf可以推算算子单次最大计算元素数量。maxLiveNodeCount表示临时空间是单次计算数据量所占空间的多少倍；extraBuf表示使用的额外临时空间大小。

推算示例如下：

算子实现需要调用Power接口，开发者为其预留currBuff大小的空间，利用GetPowerTmpBufferFactorSize接口得到maxLiveNodeCount、extraBuf输出值，可推导算子单次最大计算元素数量为：

**currentShapeSize = (currBuff - extraBuf) / maxLiveNodeCount / typeSize**

注意上文中的currBuff表示接口计算可用的空间，需要去除用户输入输出等空间；另外，接口获取的maxLiveNodeCount值可能为0，计算时需要判断该值非0，避免除零错误。

函数原型

```cpp
void GetPowerTmpBufferFactorSize(const bool baseIsTensor, const bool expIsTensor, const bool typeIsInt, const uint32_t typeSize, uint32_t& maxLiveNodeCount, uint32_t& extraBuffer)
```
