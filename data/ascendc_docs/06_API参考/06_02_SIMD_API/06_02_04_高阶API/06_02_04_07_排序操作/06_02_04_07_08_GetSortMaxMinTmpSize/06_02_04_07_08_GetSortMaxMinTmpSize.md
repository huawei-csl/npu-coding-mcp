# GetSortMaxMinTmpSize

> **Section**: 6.2.4.7.8  
> **PDF Pages**: 2818–2818  

---

<!-- page 2818 -->

## 6.2.4.7.8 GetSortMaxMinTmpSize

功能说明

带SortConfig模板参数的kernel侧Sort接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小；

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。

函数原型

```cpp
void GetSortMaxMinTmpSize(const ge::Shape &srcShape, ge::DataType valueType, ge::DataType indexType, bool isReuseSource, const SortConfig &config, uint32_t &maxValue, uint32_t &minValue)
```

参数说明

表6-1297接口参数列表

参数名输入/输出

描述

srcShape输入输入的shape信息。

valueType输入输入、输出Value的数据类型。与Sort接口的模板参数T保持一致。

indexType输入输入、输出Index的数据类型。与Sort接口的模板参数U保持一致。

isReuseSource

输入是否复用源操作数输入的空间。与Sort接口的参数isReuseSource保持一致。

config输入Sort的相应配置：选择的排序算法，排序结果的升降序，输入输出是否带有索引数据。数据类型SortConfig，定义如下。其中的参数hasSrcIndex、hasDstIndex与使用的Sort接口是否带有输入索引、输出索引的情况保持一致；当前hasSrcIndex = true, hasDstIndex = false组合不支持。struct SortConfig {    SortType type = SortType::RADIX_SORT; // 排序算法    bool isDescend = false; // 是否降序排序，默认值为false，输出结果升序排序    bool hasSrcIndex = false; // 是否带有输入索引    bool hasDstIndex = false; // 是否带有输出索引};

其中，排序算法的数据类型SortType取值如下。enum class SortType {    RADIX_SORT,  // 使用基排序算法实现    MERGE_SORT   // 使用归并排序实现};
