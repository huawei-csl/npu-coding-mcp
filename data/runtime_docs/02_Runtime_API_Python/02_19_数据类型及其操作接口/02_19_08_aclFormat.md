# aclFormat

> **Section**: 2.19.8


| 数据格式                       | 说明          |
|----------------------------|-------------|
| ACL_FORMAT_UNDEF INED = -1 | 未知数据类型，默认值。 |

| 数据格式                         | 说明                                                                                                      |
|------------------------------|---------------------------------------------------------------------------------------------------------|
| ACL_FORMAT_NCHW = 0          | NCHW 格式。                                                                                                |
| ACL_FORMAT_NHWC = 1          | NHWC 格式。                                                                                                |
| ACL_FORMAT_ND = 2            | 表示支持任意格式，除了 Square 、 Tanh 等这些单输入对自 身处理的算子外，其他算子需谨慎使用。                                                   |
| ACL_FORMAT_NC1H WC0 = 3      | 5 维数据格式。其中， C0 与微架构强相关，该值等于 cube 单元的 size ，例如 16 ； C1 是将 C 维度按照 C0 切分： C1=C/C0 ，若结果不整除，最后一份数据需要填充到 C0 。 |
| ACL_FORMAT_FRACTA L_Z = 4    | 卷积的权重的格式。                                                                                               |
| ACL_FORMAT_NC1H WC0_C04 = 12 | 5 维数据格式。其中， C0 固定为 4 ， C1 是将 C 维度按照 C0 切 分： C1=C/C0 ，若结果不整除，最后一份数据需要 padding 到 C0 。当前版本不支持。             |
| ACL_FORMAT_HWCN = 16         | HWCN 格式。                                                                                                |
| ACL_FORMAT_NDHW C = 27       | NDHWC 格式。对于 3 维图像就需要使用带 D （ Depth ）维 度的格式。                                                              |
| ACL_FORMAT_FRACTA L_NZ = 29  | 内部格式，用户目前无需使用。                                                                                          |
| ACL_FORMAT_NCDH W= 30        | NCDHW 格式。对于 3 维图像就需要使用带 D （ Depth ）维 度的格式。                                                              |
| ACL_FORMAT_NDC1H WC0 = 32    | 6 维数据格式。相比于 NC1HWC0 ，仅多了 D （ Depth ）维 度。                                                                |
| ACL_FRACTAL_Z_3D = 33        | 3D 卷积权重格式，例如 Conv3D/MaxPool3D/AvgPool3D 这些算子均需以这种格式来表达。                                                 |
| ACL_FORMAT_NC = 35           | 2 维数据格式。                                                                                                |
| ACL_FORMAT_NCL = 47          | 3 维数据格式。                                                                                                |

## 说明

各维度的含义如下： N （ Batch ）表示批量大小、 H （ Height ）表示特征图高度、 W （ Width ）表 示特征图宽度、 C （ Channels ）表示特征图通道、 D （ Depth ）表示特征图深度。
