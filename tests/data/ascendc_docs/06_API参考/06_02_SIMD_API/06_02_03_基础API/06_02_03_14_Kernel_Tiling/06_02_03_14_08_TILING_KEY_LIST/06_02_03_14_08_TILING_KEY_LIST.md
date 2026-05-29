# TILING_KEY_LIST

> **Section**: 6.2.3.14.8  
> **PDF Pages**: 1987–1987  

---

<!-- page 1987 -->

## 6.2.3.14.8 TILING_KEY_LIST

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

TILING_KEY_LIST函数用于在核函数中判断当前执行的TilingKey是否与Host侧配置的指定TilingKey匹配，从而标识满足TilingKey == key1或TilingKey == key2条件的分支逻辑。

函数原型

```cpp
TILING_KEY_LIST(key1,key2)
```

参数说明

参数输入/输出说明

key输入key表示某个核函数的分支，必须是非负整数。

约束说明

●TILING_KEY_LIST运用于if和else if分支，不支持else分支，即用TILING_KEY_LIST函数来表征N个分支，必须用N个TILING_KEY_LIST(key1,key2)来分别表示。

●支持传入两个TilingKey，每个TilingKey具备唯一性。

●使用该接口时，必须设置默认的Kernel类型，也可以为某个TilingKey单独配置Kernel类型，该配置会覆盖默认Kernel类型。Kernel类型仅支持配置为KERNEL_TYPE_MIX_AIC_1_1、KERNEL_TYPE_MIX_AIC_1_2。

●暂不支持Kernel直调工程。

调用示例

```cpp
extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *workspace, __gm__ uint8_t *tiling){    GET_TILING_DATA(tilingData, tiling);
```
