# SetLoadDataRepeat

> **Section**: 6.2.3.2.1.10  
> **PDF Pages**: 1028–1029  

---

<!-- page 1028 -->

功能说明

设置Load3D时A1/B1边界值。

如果Load3D指令在处理源操作数时，源操作数在A1/B1上的地址超出设置的边界，则会从A1/B1起始地址开始读取数据。

函数原型

```cpp
__aicore__ inline void SetLoadDataBoundary(uint32_t boundaryValue)
```

参数说明

表6-191参数说明

参数名称输入/输出

含义

boundaryValue

输入边界值。

Load3Dv1指令：单位是32字节。

Load3Dv2指令：单位是字节。

约束说明

●用于Load3Dv1时，boundaryValue的最小值是16（单位：32字节）；用于Load3Dv2时，boundaryValue的最小值是1024（单位：字节）。

●如果使用SetLoadDataBoundary接口设置了边界值，配合Load3D指令使用时，Load3D指令的A1/B1初始地址要在设置的边界内。

●如果boundaryValue设置为0，则表示无边界，可使用整个A1/B1。

●操作数地址对齐要求请参见通用地址对齐约束。

调用示例

参考调用示例。

## 6.2.3.2.1.10 SetLoadDataRepeat

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Corex

<!-- page 1029 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

用于设置Load3Dv2接口的repeat参数。设置repeat参数后，可以通过调用一次Load3Dv2接口完成多个迭代的数据搬运。

函数原型

```cpp
__aicore__ inline void SetLoadDataRepeat(const LoadDataRepeatParam& repeatParams)
```

参数说明

表6-192参数说明

参数名称输入/输出

含义

repeatParams

输入设置Load3Dv2接口的repeat参数，类型为LoadDataRepeatParam。

具体定义请参考${INSTALL_DIR}/include/ascendc/basic_api/interface/kernel_struct_mm.h，${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。

参数说明请参考表6-193。

表6-193 LoadDataRepeatParam 结构体参数说明

参数名称含义

repeatTime

height/width方向上的迭代次数，取值范围：repeatTime ∈[0,255] 。默认值为1。
