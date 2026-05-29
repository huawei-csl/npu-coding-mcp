# SetDim

> **Section**: 26  
> **PDF Pages**: 2440–2440  

---

<!-- page 2440 -->

## ?.26. SetDim

功能说明

设置多核Matmul时，参与运算的核数。不同场景下的设置规则如下：

●纯Cube模式（只有矩阵计算）

SetDim设置当前AI处理器可用的核数，通过Tiling计算得到执行Matmul计算实际使用的核数，实际使用的核数小于等于AI处理器可用的核数。SetBlockDim按照实际使用的核数由用户进行配置，SetBlockDim加载的核全部用于Matmul API的计算。

●MIX模式（包含矩阵计算和矢量计算）

–分离模式：Matmul API都是从AIV侧发起的，调用Iterate计算时在AIV侧只会起到通知的作用，通知AIC去做矩阵计算，计算完成后AIC告知AIV计算完成，在开发者层面感知的是AIV的核数，SetDim设置为当前AI处理器可用的AIV核的数量，通过Tiling计算得到实际使用的AIV核数。SetBlockDim设置为实际使用的AI Core（AIC、AIV组合）的数量。例如，SetDim设置为40，表示可以使用40个AIV核发起多核Matmul运算，Tiling计算得到实际使用的AIV核数是20。当前AI处理器的AIC:AIV为1:2，则SetBlockDim设置为10，表示实际使用10个AI Core（AIC AIV的组合）。

–耦合模式：SetDim设置当前AI处理器可用的核数，通过Tiling计算得到实际使用的核数，实际使用的核数小于等于AI处理器可用的核数。SetBlockDim按照实际使用的核数由用户进行配置，SetBlockDim加载的核全部用于MatmulAPI的计算。

函数原型

```cpp
int32_t SetDim(int32_t dim)
```

参数说明

表6-1093参数说明

参数名输入/输出

描述

dim输入多核Matmul tiling计算时，可以使用的核数。注意，MIX模式下，该参数取值小于等于耦合模式下启动的AICore核数或者分离模式下启动的AIV核数。

返回值说明

-1表示设置失败； 0表示设置成功。

约束说明

无

调用示例

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
```
