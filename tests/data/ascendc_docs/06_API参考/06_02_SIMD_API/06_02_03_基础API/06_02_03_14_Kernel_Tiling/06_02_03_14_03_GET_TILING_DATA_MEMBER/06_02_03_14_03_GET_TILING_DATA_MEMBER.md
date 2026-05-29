# GET_TILING_DATA_MEMBER

> **Section**: 6.2.3.14.3  
> **PDF Pages**: 1980–1980  

---

<!-- page 1980 -->

约束说明

●本函数需在算子Kernel代码处使用，并且传入的tiling_data参数不需要声明类型。

●暂不支持Kernel直调工程。

调用示例

extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling){    KernelAdd op;    if (TILING_KEY_IS(1)) {        GET_TILING_DATA_WITH_STRUCT(Add_Struct_Special, tilingData, tiling); // 使用算子指定注册的结构体    op.Init(x, y, z, tilingData.totalLengthSpecial, tilingData.tileNumSpecial);    } else {        GET_TILING_DATA(tilingData, tiling);   // 使用算子默认注册的结构体    op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum);    }    if (TILING_KEY_IS(1)) {        op.Process();    }  else  if (TILING_KEY_IS(2)) {        op.Process();    } else  if (TILING_KEY_IS(3)) {        op.Process();    }}

## 6.2.3.14.3 GET_TILING_DATA_MEMBER

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

用于获取tiling结构体的成员变量。

函数原型

```cpp
GET_TILING_DATA_MEMBER(struct_name, mem_name, tiling_data, tiling_arg)
```
