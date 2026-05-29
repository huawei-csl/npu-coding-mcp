# EnableMultiCoreSplitK

> **Section**: 14  
> **PDF Pages**: 2429–2429  

---

<!-- page 2429 -->

参数说明

表6-1084参数说明

参数名输入/输出

描述

baseMIn输入设置固定的baseM，默认值为-1，表示不设置固定baseM，由tiling函数进行计算。

baseNIn输入设置固定的baseN，默认值为-1，表示不设置固定baseN，由tiling函数进行计算。

baseKIn输入当前仅支持取值为-1，暂不支持设置其它值。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

●baseM*baseN个输出元素所占的存储空间大小不能超过L0C Buffer大小，即baseM * baseN * sizeof(C_TYPE) <= L0CSize。

●baseM需要小于等于singleM按16个元素向上对齐后的值（如ceil(singleM/16)*16），baseN需要小于等于singleN以C0_size个元素向上对齐的值，其中singleM为单核内M轴长度，singleN为单核内N轴长度，half/bfloat16_t数据类型的C0_size为16，float数据类型的C0_size为8，int8_t数据类型的C0_size为32，int4b_t数据类型的C0_size为64。例如singleM=12，则baseM需要小于等于16，同时baseM需要满足分形对齐的要求，所以baseM只能取16；如果baseM取其他超过16的值，获取Tiling将失败。

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
```

tiling.SetFixSplit(16, 16, -1);  // 设置固定的baseM、baseN

## ?.14. EnableMultiCoreSplitK

功能说明

多核场景，通过该接口使能切K轴。不调用该接口的情况下，默认不切K轴。在GetTiling接口调用前使用。

函数原型

```cpp
void EnableMultiCoreSplitK(bool flag)
```
