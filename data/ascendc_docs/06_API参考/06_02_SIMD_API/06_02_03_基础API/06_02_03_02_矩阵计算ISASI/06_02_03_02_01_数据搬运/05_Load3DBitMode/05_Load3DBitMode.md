# Load3DBitMode

> **Section**: 5  
> **PDF Pages**: 1002–1006  

---

<!-- page 1002 -->

## ?.5. Load3DBitMode

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品x

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

Load3D用于完成image to column操作，将多维feature map转为二维矩阵。支持如下数据通路：A1->A2; B1->B2。

函数原型

```cpp
template <TPosition Dst, TPosition Src, typename T>__aicore__ inline void LoadData(const LocalTensor<T>& dst, const LocalTensor<T>& src,const Load3DBitModeParam& loadDataParams)
```

参数说明

表6-173模板参数说明

参数名称含义

T源操作数和目的操作数的数据类型。

●Load3DBitMode接口：Atlas 350 加速卡，支持数据类型为：uint8_t/int8_t/fp8_e4m3fn_t/fp8_e5m2_t/hifloat8_t/half/bfloat16_t/uint32_t/int32_t/float

Src源操作数存储的逻辑位置（TPosition），仅Load3DBitMode接口使用。

Dst目的操作数存储的逻辑位置（TPosition），仅Load3DBitMode接口使用。

<!-- page 1003 -->

表6-174通用参数说明

参数名称输入/输出

含义

dst输出目的操作数，类型为LocalTensor。

数据连续排列顺序由目的操作数所在TPosition决定，具体约束如下：

●A2：ZZ格式/NZ格式；

●B2：ZN格式；

●A1/B1：无格式要求，一般情况下为NZ格式。

src输入源操作数，类型为LocalTensor或GlobalTensor。

数据类型需要与dst保持一致。

loadDataParams

输入LoadData参数结构体，类型为：

●Load3DBitModeParam，具体参考表6-175

上述结构体参数定义请参考${INSTALL_DIR}/include/ascendc/basic_api/interface/kernel_struct_mm.h，${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。

表6-175 Load3DBitModeParam 类参数说明

参数名称含义

config0uint64_t类型，与Load3DBitModeConfig0位域（bit-field）结构体类型参数config0BitMode组成联合体（union），初始化为0，可以使用类对象的GetConfig0()函数获取其值。

config0BitMode

Load3DBitModeConfig0位域（bit-field）结构体类型，参数参考表6-176，与config0组成联合体（union）。

config1uint64_t类型，与Load3DBitModeConfig1位域（bit-field）结构体类型参数config1BitMode组成联合体（union），初始化为0，可以使用类对象的GetConfig1()函数获取其值。

config1BitMode

Load3DBitModeConfig1位域（bit-field）结构体类型，参数参考表6-177，与config1组成联合体（union）。

Load3DBitModeParam类参数设计思想说明：

联合体（union）是一种特殊的数据结构，允许在相同的内存位置存储不同的数据类型。union的所有成员共享同一块内存空间，大小由最大成员决定，同一时间只能使用一个成员。

位域（bit-field）是一种特殊的类成员，允许精确控制结构体中成员变量所占用的内存位数。结构体中成员变量从上到下对应内存中从低位到高位。

Load2DBitModeParam类使用union与bit-field方法，采用bit位表达参数类型，使用bit-field结构体自动处理入参的bit位数，并利用union的特性实现多参数融合传递，仅需传递一个入参即可包含全部所需信息，对应底层接口仅需要接收一个参数。同时，

<!-- page 1004 -->

当需要修改参数中某一bit位的值时，仅需要通过循环和位运算即可实现，不需要重新传入参数，减少了scalar计算，实现性能提升。

Load2DBitModeParam类可以直接使用LoadData2DParamsV2结构体类型对象初始化：

```cpp
template <typename T>__aicore__ inline Load3DBitModeParam(const LoadData3DParamsV2<T> &loadData3DParams_);
```

也可以使用各参数的Set函数修改参数值，并且由于使用了联合体，还可以对congfig0和config1直接进行逐bit位修改来修改参数。

表6-176 Load3DBitModeConfig0 结构体参数说明

参数名称含义

kStep该指令在目的操作数width维度的传输长度，如果不覆盖最右侧的分形，对于half类型，应为16的倍数，对于int8_t/uint8_t应为32的倍数；覆盖的情况则无倍数要求。取值范围: kStep∈[1, 65535] 。

（与表6-171中的kExtension含义相同）

该参数是位域结构体的最低位参数，占用16bit，可以使用Load3DBitModeParam类对象的SetKExtension()函数设置其值，使用GetKExtension()函数获取其值。

mStep该指令在目的操作数height维度的传输长度，如果不覆盖最下侧的分形，对于half/int8_t/uint8_t，应为16的倍数；覆盖的情况则无倍数要求。取值范围：mStep∈[1, 65535] 。

（与表6-171中的mExtension含义相同）

该参数是位域结构体的第二低位参数，占用16bit，可以使用Load3DBitModeParam类对象的SetMExtension()函数设置其值，使用GetMExtension()函数获取其值。

kPos该指令在目的操作数width维度的起点，对于half类型，应为16的倍数，对于int8_t/uint8_t应为32的倍数。取值范围[0, 65535] 。默认为0。

（与表6-171中的kStartPt含义相同）

该参数是位域结构体的第三低位参数，占用16bit，可以使用Load3DBitModeParam类对象的SetKStartPt()函数设置其值，使用GetKStartPt()函数获取其值。

mPos该指令在目的操作数height维度的起点，如果不覆盖最下侧的分形，对于half/int8_t/uint8_t，应为16的倍数；覆盖的情况则无倍数要求。取值范围[0, 65535] 。默认为0。

（与表6-171中的mStartPt含义相同）

该参数是位域结构体的最高位参数，占用16bit，可以使用Load3DBitModeParam类对象的SetMStartPt()函数设置其值，使用GetMStartPt()函数获取其值。

<!-- page 1005 -->

表6-177 Load3DBitModeConfig1 结构体参数说明

参数名称含义

strideW卷积核在源操作数width维度滑动的步长，取值范围：strideW∈[1,63] 。

（与表6-171中的strideW含义相同）

该参数是位域结构体的最低位参数，占用6bit，可以使用Load3DBitModeParam类对象的SetStrideW()函数设置其值，使用GetStrideW()函数获取其值。

strideH卷积核在源操作数height 维度滑动的步长，取值范围：strideH∈[1,63] 。

（与表6-171中的strideH含义相同）

该参数是位域结构体的第二低位参数，占用6bit，可以使用Load3DBitModeParam类对象的SetStrideH()函数设置其值，使用GetStrideH()函数获取其值。

Wk卷积核width，取值范围：Wk∈[1, 255] 。

（与表6-171中的filterW含义相同）

该参数是位域结构体的第三低位参数，占用8bit，可以使用Load3DBitModeParam类对象的SetFilterW()函数设置其值，使用GetFilterW()函数获取其值。

Hk卷积核height，取值范围：Hk∈[1, 255] 。

（与表6-171中的filterH含义相同）

该参数是位域结构体的第四低位参数，占用8bit，可以使用Load3DBitModeParam类对象的SetFilterH()函数设置其值，使用GetFilterH()函数获取其值。

dilationW卷积核width膨胀系数，取值范围：dilationW∈[1, 255] 。

（与表6-171中的dilationFilterW含义相同）

该参数是位域结构体的第五低位参数，占用8bit，可以使用Load3DBitModeParam类对象的SetDilationFilterW()函数设置其值，使用GetDilationFilterW()函数获取其值。

dilationH卷积核height膨胀系数，取值范围：dilationH∈[1, 255]。

（与表6-171中的dilationFilterH含义相同）

该参数是位域结构体的第六低位参数，占用8bit，可以使用Load3DBitModeParam类对象的SetDilationFilterH()函数设置其值，使用GetDilationFilterH()函数获取其值。

filterW是否在filterW的基础上将卷积核width增加256 个元素。true，增加；false，不增加。

（与表6-171中的filterSizeW含义相同）

该参数是位域结构体的第七低位参数，占用1bit，可以使用Load3DBitModeParam类对象的SetFilterSizeW()函数设置其值，使用GetFilterSizeW()函数获取其值。

<!-- page 1006 -->

参数名称含义

filterH是否在filterH的基础上将卷积核height增加256个元素。true，增加；false，不增加。

（与表6-171中的filterSizeH含义相同）

该参数是位域结构体的第八低位参数，占用1bit，可以使用Load3DBitModeParam类对象的SetFilterSizeH()函数设置其值，使用GetFilterSizeH()函数获取其值。

transpose是否启用转置功能，对整个目标矩阵进行转置，支持数据类型为bool，仅在目的TPosition为A2，且源操作数为half类型时有效。默认为false。

●true：启用

●false：不启用

（与表6-171中的enTranspose含义相同）

该参数是位域结构体的第九低位参数，占用1bit，可以使用Load3DBitModeParam类对象的SetTranspose()函数设置其值，使用GetTranspose()函数获取其值。

fmatrixCtrl表示LoadData3DV2指令从左矩阵还是右矩阵获取FeatureMap的属性描述，与 SetFmatrix配合使用，当前只支持设置为false，默认值为false。

●true：从右矩阵中获取FeatureMap的属性描述；

●false：从左矩阵中获取FeatureMap的属性描述。

（与表6-171中的fMatrixCtrl含义相同）

该参数是位域结构体的第十低位参数，占用1bit，可以使用Load3DBitModeParam类对象的SetFmatrixCtrl()函数设置其值，使用GetFmatrixCtrl()函数获取其值。

sizeChannel源操作数的通道数，取值范围：channelSize∈[1, 63] 。

channelSize的取值要求为：对于uint32_t/int32_t/float，channelSize可取值为4，N * 8，N * 8 + 4；对于half/bfloat16，channelSize可取值为4，8，N * 16，N * 16 + 4，N * 16 + 8；对于int8_t/uint8_t，channelSize可取值为4，8，16， 32 * N，N * 32 +4，N * 32 + 8，N * 32 + 16；对于int4b_t，ChannelSize可取值为8，16，32，N * 64，N * 64 + 8，N * 64 + 16，N * 64 + 32。N为正整数。

（与表6-171中的channelSize含义相同）

该参数是位域结构体的最高位参数，占用16bit，可以使用Load3DBitModeParam类对象的SetChannelSize()函数设置其值，使用GetChannelSize()函数获取其值。

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。
