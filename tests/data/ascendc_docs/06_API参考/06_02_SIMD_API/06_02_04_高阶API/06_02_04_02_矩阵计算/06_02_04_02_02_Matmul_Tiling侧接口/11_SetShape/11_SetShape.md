# SetShape

> **Section**: 11  
> **PDF Pages**: 2426–2426  

---

<!-- page 2426 -->

参数名输入/输出

描述

singleNIn输入设置的singleNIn大小，单位为元素，默认值为-1。-1表示不设置指定的singleNIn，该值由tiling函数自行计算。

singleKIn输入设置的singleKIn大小，单位为元素，默认值为-1。-1表示不设置指定的singleKIn，该值由tiling函数自行计算。

返回值说明

-1表示设置失败；0表示设置成功。

约束说明

●在MxMatmul场景中，如果A与B矩阵的位置同时为GM，对singleKIn没有特殊限制，在这种情况下，若scaleA和scaleB的K方向大小（即Ceil(singleKIn, 32)）为奇数，用户需自行在scaleA和scaleB的K方向补0至偶数。例如，当singleKIn为30时，Ceil(singleKIn, 32)为1，用户需要自行在scaleA和scaleB的K方向补0，使K方向为偶数。对于其它A、B矩阵逻辑位置的组合情况，即A与B矩阵的位置不同时为GM，singleKIn以32个元素向上对齐后的数值必须是32的偶数倍。

●在MxMatmul场景中，当输入数据类型为fp4x2_e2m1_t、fp4x2_e1m2_t时，内轴必须为偶数。

调用示例

auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform); tiling.SetShape(1024, 1024, 1024);  // 设置Matmul单次计算的形状tiling.SetSingleShape(1024, 1024, 1024);  // 设置单核计算的形状tiling.SetOrgShape(1024, 1024, 1024);

## ?.11. SetShape

功能说明

设置Matmul计算的形状m、n、k，该形状可以为原始完整矩阵或其局部矩阵，单位为元素。该形状的矩阵乘可以由单核或多核计算完成。

使用本接口时，有两种参数传入方式：

●传入Matmul计算的形状m、n、k，调用GetTiling接口时，按照m、n、k计算并返回Tiling参数。

●m、n、k中任意一个或多个参数位置传入-1，调用GetTiling接口时，该位置取SetOrgShape接口中设置的原始形状M、N、K或Ka/Kb，然后由接口内部计算最优Tiling参数。如下图所示，原始A矩阵的K方向最后一列为不参与计算的脏数据，在SetOrgShape接口中设置包含该列数据的原始形状，在本接口中设置Matmul计算的K方向大小，同时参数m、n设置为-1表示按照原始形状M、N计算Tiling。
