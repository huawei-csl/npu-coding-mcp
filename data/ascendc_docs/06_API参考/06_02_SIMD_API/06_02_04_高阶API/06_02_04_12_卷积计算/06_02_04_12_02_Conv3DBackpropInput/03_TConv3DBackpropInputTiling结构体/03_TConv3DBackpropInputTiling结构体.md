# TConv3DBackpropInputTiling结构体

> **Section**: 3  
> **PDF Pages**: 3041–3043  

---

<!-- page 3041 -->

## ?.3. TConv3DBackpropInputTiling 结构体

TConv3DBackpropInputTiling结构体包含Conv3DBackpropInput算子规格信息及Tiling切分算法的相关参数，被传递给Conv3DBackpropInput Kernel侧，用于数据切分、数据搬运和计算等。TConv3DBackpropInputTiling结构体的参数说明见下表。

用户通过调用 GetTiling接口获取TConv3DBackpropInputTiling结构体，具体流程请参考 Conv3DBackpropInput Tiling使用说明。当前暂不支持用户自定义配置TConv3DBackpropInputTiling结构体中的参数。

表6-1407 TConv3DBackpropInputTiling 结构说明

参数名称说明

batch输入GradOutput的N，等于卷积正向输入Input的N。

cin输出GradInput的Channel，等于卷积正向输入Input的Channel。

cout输入GradOutput的Channel。

cout1输入GradOutput的C1，等于cout/c0。

cin1输出GradInput的C1，等于卷积正向输入Input的C1，等于cin/c0。

cout1G预留参数，用户无需感知。

cin1G预留参数，用户无需感知。

c0当前输入数据类型下C0的大小。该参数目前只支持取值为16。

c0Bits任意一个数除以c0等价的右移位数，例如c0=8则c0Bits=3，c0=16则c0Bits=4。

dout输入GradOutput的Depth大小，单位元素。

ho输入GradOutput的Height大小，单位元素。

wo输入GradOutput的Width大小，单位元素。

di输出GradInput的Depth大小，等于卷积正向输入Input的Depth大小，单位元素。

hi输出GradInput的Height大小，等于卷积正向输入Input的Height大小，单位元素。

wi输出GradInput的Width大小，等于卷积正向输入Input的Width大小，单位元素。

dk输入Weight的Depth大小，单位元素。

hk输入Weight的Height大小，单位元素。

wk输入Weight的Width大小，单位元素。

group预留参数，用户无需感知。

strideD卷积反向计算中Stride的Depth大小，单位元素。

strideH卷积反向计算中StrideHeight大小，单位元素。

<!-- page 3042 -->

参数名称说明

strideW卷积反向计算中StrideWidth大小，单位元素。

padFront卷积反向计算中输出矩阵GradInput Padding的Depth维度的前方向，单位元素。

padBack卷积反向计算中输出矩阵GradInput Padding的Depth维度的后方向，单位元素。

padUp卷积反向计算中输出矩阵GradInput Padding的Height维度的上方向，单位元素。

padDown卷积反向计算中输出矩阵GradInput Padding的Height维度的下方向，单位元素。

padLeft卷积反向计算中输出矩阵GradInput Padding的Width维度的左方向，单位元素。

padRight卷积反向计算中输出矩阵GradInput Padding的Width维度的右方向，单位元素。

backpropPadTail

预留参数，用户无需感知。

backpropPadUp

卷积反向计算中输入矩阵GradOutput Padding的Height维度的上方向，单位元素。

backpropPadDown

卷积反向计算中输入矩阵GradOutput Padding的Height维度的下方向，单位元素。

backpropPadLeft

卷积反向计算中输入矩阵GradOutput Padding的Width维度的左方向，单位元素。

backpropPadRight

卷积反向计算中输入矩阵GradOutput Padding的Width维度的右方向，单位元素。

dilationD卷积反向计算中Dilation的Depth大小，单位元素。

dilationH卷积反向计算中Dilation的Height大小，单位元素。

dilationW卷积反向计算中Dilation的Width大小，单位元素。

al0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

bl0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

cl0Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

al1Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

bl1Pbuffer1表示不使能DoubleBuffer，2表示使能DoubleBuffer。

singleCoreGroup

预留参数，用户无需感知。

singleCoreCout

单核M方向上计算cout数据量的大小。

<!-- page 3043 -->

参数名称说明

singleCoreCout1

单核上cout1的大小。

singleCoreCin1

单核上cin1的大小。

singleCoreDin

单核上Din的大小。

singleCoreHo

单核K方向上计算ho数据量的大小。

baseML0上M方向大小。

baseKL0上K方向大小。

baseNL0上N方向大小。

baseD预留参数，用户无需感知。

baseBatch预留参数，用户无需感知。

baseGroup预留参数，用户无需感知。

stepM特征矩阵在L1中缓存的buffer M方向上baseM的倍数。

stepN权重矩阵在L1中缓存的buffer N方向上baseN的倍数。

stepKa特征矩阵在L1中缓存的buffer K方向上baseK的倍数。

stepKb权重矩阵在L1中缓存的buffer K方向上baseK的倍数。

stepBatch预留参数，用户无需感知。

stepGroup预留参数，用户无需感知。

iterateOrder

预留参数，用户无需感知。

hf32Flag预留参数，用户无需感知。

initOutputFlag

预留参数，用户无需感知。

reserved预留参数，用户无需感知。

singleCoreBatch

预留参数，用户无需感知。

singleCoreM

单核M方向上需要计算的数据量大小。

singleCoreCin

单核N方向上计算cin数据量的大小。
