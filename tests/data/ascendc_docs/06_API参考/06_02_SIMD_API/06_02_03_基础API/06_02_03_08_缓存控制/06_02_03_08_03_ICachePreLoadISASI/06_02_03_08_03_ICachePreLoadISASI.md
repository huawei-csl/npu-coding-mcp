# ICachePreLoad(ISASI)

> **Section**: 6.2.3.8.3  
> **PDF Pages**: 1862–1862  

---

<!-- page 1862 -->

}// 由于首地址非64B对齐，调用1条指令，只会刷新起始地址至64B字节对齐的部分，即前4个数AscendC::DataCacheCleanAndInvalid<uint64_t, AscendC::CacheLine::SINGLE_CACHE_LINE, AscendC::DcciDst::CACHELINE_OUT>(global);// 需要再次调用DataCacheCleanAndInvalid指令，刷新后4个数AscendC::DataCacheCleanAndInvalid<uint64_t, AscendC::CacheLine::SINGLE_CACHE_LINE, AscendC::DcciDst::CACHELINE_OUT>(global[4]);// 示例3：SINGLE_CACHE_LINE 模式，假设mmAddr_为0x40（64B对齐），多核处理场景（本样例仅做示例说明，便于开发者理解使用限制，非正常使用样例）AscendC::GlobalTensor<uint64_t> global;global.SetGlobalBuffer((__gm__ uint64_t*)mmAddr_);global.SetValue(AscendC::GetBlockIdx(), AscendC::GetBlockIdx());// 算子中多核操作虽然不在同一个地址，但在同一个Cache Line, 会出现数据的随机覆盖，和通用CPU的行为不同// 调用DataCacheCleanAndInvalid指令后，由于多核操作的时间不一致，最终结果存在随机性，后执行的核会覆盖前面核的结果AscendC::DataCacheCleanAndInvalid<uint64_t, AscendC::CacheLine::SINGLE_CACHE_LINE, AscendC::DcciDst::CACHELINE_OUT>(global);// 示例4：ENTIRE_DATA_CACHE 模式，假设mmAddr_为0x20（非64B对齐）// 本样例仅做示例说明，便于开发者理解使用限制，非正常使用样例AscendC::GlobalTensor<uint64_t> global;global.SetGlobalBuffer((__gm__ uint64_t*)mmAddr_ + AscendC::GetBlockIdx() * 1024);for( int i = 0; i < 8; i++) {   global.SetValue(i, AscendC::GetBlockIdx());}// 刷新整个Data Cache，性能较差AscendC::DataCacheCleanAndInvalid<uint64_t, AscendC::CacheLine::ENTIRE_DATA_CACHE, AscendC::DcciDst::CACHELINE_OUT>(global);

## 6.2.3.8.3 ICachePreLoad(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

从指令所在DDR地址预加载指令到ICache中。

函数原型

```cpp
__aicore__ inline void ICachePreLoad(const int64_t preFetchLen)
```
