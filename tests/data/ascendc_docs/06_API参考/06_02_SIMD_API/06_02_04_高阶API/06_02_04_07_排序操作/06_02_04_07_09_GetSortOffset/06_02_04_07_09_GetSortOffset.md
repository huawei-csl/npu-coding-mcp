# GetSortOffset

> **Section**: 6.2.4.7.9  
> **PDF Pages**: 2819–2819  

---

<!-- page 2819 -->

参数名输入/输出

描述

maxValue输出Sort接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。最大空间大小为0表示计算不需要临时空间。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出Sort接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。最小空间大小为0表示计算不需要临时空间。

返回值说明

无

约束说明

无

调用示例

完整的调用样例请参考6.2.4.1.49 更多样例。// 输入shape信息为1024;算子输入的数据类型为uint32_t;不允许修改源操作数std::vector<int64_t> shape_vec = {1024};ge::Shape srcShape(shape_vec);ge::DataType valueType = ge::DT_UINT32;ge::DataType indexType = ge::DT_UINT32;bool isDescend = true;bool hasSrcIndex = false;bool hasDstIndex = false;bool isReuseSource = false;AscendC::SortConfig config;config.type = AscendC::SortType::RADIX_SORT;config.isDescend = isDescend;config.hasSrcIndex = hasSrcIndex;config.hasDstIndex = hasDstIndex;uint32_t maxValue = 0;uint32_t minValue = 0;AscendC::GetSortMaxMinTmpSize(srcShape, valueType, indexType, isReuseSource, config, maxValue, minValue);

## 6.2.4.7.9 GetSortOffset

功能说明

根据元素位置，获取Sort数据中的对应偏移量（单位为字节）。
