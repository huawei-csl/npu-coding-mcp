# EnableBias

> **Section**: 15  
> **PDF Pages**: 2430–2430  

---

<!-- page 2430 -->

参数说明

表6-1085参数说明

参数名输入/输出

描述

flag输入是否使能切K轴。

●true：使能切K轴

●false：不使能切K轴

返回值说明

无

约束说明

●在算子中使用该接口时，获取C矩阵结果时仅支持输出到Global Memory。

●在算子中使用该接口时，需在Kernel侧代码中首次将C矩阵分片的结果写入GlobalMemory之前，先清零Global Memory，随后在获取C矩阵分片的结果时，再开启AtomicAdd累加。如果不预先清零Global Memory，可能会因为累加GlobalMemory中原始的无效数据而产生精度问题。

●在算子中使用该接口时，不支持Bias参与矩阵乘计算。

调用示例

完整的算子样例请参考多核切K场景的算子样例。

```cpp
auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
```

tiling.EnableMultiCoreSplitK(true);  // 使能切K轴

## ?.15. EnableBias

功能说明

设置Bias是否参与运算，设置的信息必须与Kernel侧保持一致。

函数原型

```cpp
int32_t EnableBias(bool isBiasIn = false)
```
