# COPY_TILING_WITH_ARRAY

> **Section**: 6.2.3.14.6  
> **PDF Pages**: 1984–1984  

---

<!-- page 1984 -->

调用示例

```cpp
extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling){    KernelAdd op;
    GET_TILING_DATA_PTR_WITH_STRUCT(AddCustomTilingData, tilingDataPtr, tiling);
```

if ASCEND_IS_AIV {        COPY_TILING_WITH_STRUCT(VectorTilingStruct, tilingDataPtr->vectorTiling, vTilingStructPtr);   // Vector侧使用VectorTilingStruct        op.Init(x, y, z, vTilingStructPtr->totalLength, vTilingStructPtr->tileNum);        op.Process();    } else {        COPY_TILING_WITH_STRUCT(CubeTilingStruct, tilingDataPtr->cubeTiling, cTilingStructPtr); // Cube侧使用CubeTilingStruct    op.Init(x, y, z, *cTilingStructPtr);        op.Process();    }}

## 6.2.3.14.6 COPY_TILING_WITH_ARRAY

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

拷贝指定大小的数组内容到目标数组中，并返回指向拷贝后数组的指针。适用于拷贝一个结构体的数组成员变量的场景。该宏将指定数组拷贝至栈上，适用于频繁访问Tiling数据的场景，能够加快数据访问速度。

函数原型

```cpp
COPY_TILING_WITH_ARRAY(arr_type, arr_count, src_ptr, dst_ptr)
```

参数说明

参数输入/输出说明

arr_type输入指定要拷贝的数组类型。

arr_count输入指定要拷贝的数组大小。
