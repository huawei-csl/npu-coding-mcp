# SetLoadDataPaddingValue

> **Section**: 6.2.3.2.1.11  
> **PDF Pages**: 1030–1030  

---

<!-- page 1030 -->

参数名称含义

repeatStride

height/width方向上的前一个迭代与后一个迭代起始地址的距离，取值范围：n∈[0, 65535]，默认值为0。

●repeatMode为0，repeatStride的单位为16个元素。

●repeatMode为1，repeatStride的单位和具体型号有关。下文中的data_type指Load3Dv2中源操作数的数据类型。Atlas 350 加速卡，repeatStride的单位为32/sizeof(data_type)个元素。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，repeatStride的单位为32/sizeof(data_type)个元素。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，repeatStride的单位为32/sizeof(data_type)个元素。

Atlas 200I/500 A2 推理产品，repeatStride的单位为64/sizeof(data_type)个元素。

repeatMode

控制repeat迭代的方向，取值范围：k∈[0, 1] 。默认值为0。

0：迭代沿height方向；

1：迭代沿width方向。

调用示例

参考调用示例

## 6.2.3.2.1.11 SetLoadDataPaddingValue

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

用于调用Load3Dv1接口/Load3Dv2接口时设置Pad填充的数值。Load3Dv1/Load3Dv2的模板参数isSetPadding设置为true时，用户需要通过本接口设置Pad填充的数值，设置为false时，本接口设置的填充值不生效。
