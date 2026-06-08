# aclFormat

> **Section**: 1.28.10


```
typedef enum { ACL_FORMAT_UNDEFINED = -1, ACL_FORMAT_NCHW = 0, ACL_FORMAT_NHWC = 1, ACL_FORMAT_ND = 2, ACL_FORMAT_NC1HWC0 = 3, ACL_FORMAT_FRACTAL_Z = 4, ACL_FORMAT_NC1HWC0_C04 = 12, ACL_FORMAT_HWCN = 16, ACL_FORMAT_NDHWC = 27, ACL_FORMAT_FRACTAL_NZ = 29, ACL_FORMAT_NCDHW = 30, ACL_FORMAT_NDC1HWC0 = 32, ACL_FRACTAL_Z_3D = 33, ACL_FORMAT_NC = 35, ACL_FORMAT_NCL = 47, ACL_FORMAT_FRACTAL_NZ_C0_16 = 50, ACL_FORMAT_FRACTAL_NZ_C0_32 = 51, ACL_FORMAT_FRACTAL_NZ_C0_2 = 52, ACL_FORMAT_FRACTAL_NZ_C0_4 = 53, ACL_FORMAT_FRACTAL_NZ_C0_8 = 54, } aclFormat;
```

各维度的含义如下： N （ Batch ）表示批量大小、 H （ Height ）表示特征图高度、 W （ Width ）表示特征图宽度、 C （ Channels ）表示特征图通道、 D （ Depth ）表示特征 图深度、 L 是特征图长度。

## aclFormat 各项含义如下：

- UNDEFINED ：未知格式，默认值。
- NCHW ： 4 维数据格式。
- NHWC ： 4 维数据格式。
- ND ：表示支持任意格式，除了 Square 、 Tanh 等这些单输入对自身处理的算子 外，其他算子需谨慎使用。
- NC1HWC0 ： 5 维数据格式。其中， C0 与微架构强相关，该值等于 cube 单元的 size ，例如 16 ； C1 是将 C 维度按照 C0 切分： C1=C/C0 ， 若结果不整除，最后一份 数据需要 padding 到 C0 。
- FRACTAL\_Z ：卷积的权重的格式。
- NC1HWC0\_C04 ： 5 维数据格式。其中， C0 固定为 4 ， C1 是将 C 维度按照 C0 切分： C1=C/C0 ， 若结果不整除，最后一份数据需要 padding 到 C0 。当前版本不支持。
- HWCN ： 4 维数据格式。
- NDHWC ： NDHWC 格式。对于 3 维图像就需要使用带 D （ Depth ）维度的格式。
- FRACTAL\_NZ ：内部分形格式。用户目前无需使用。
- NCDHW ： NCDHW 格式。对于 3 维图像就需要使用带 D （ Depth ）维度的格式。
- NDC1HWC0 ： 6 维数据格式。相比于 NC1HWC0 ，仅多了 D （ Depth ）维度。
- FRACTAL\_Z\_3D ： 3D 卷积权重格式，例如 Conv3D/MaxPool3D/AvgPool3D 这些算 子都需要这种格式来表达。
- NC ：

2 维数据格式。

- NCL ： 3 维数据格式。
- FRACTAL\_NZ\_C0\_[M] ：内部用于分形的特殊数据排布格式， [M] 代表 C0 的数值， 当前支持（ 2, 4, 8, 16, 32 ）。用户目前无需使用。

仅 Atlas 350 加速卡支持该类型。
