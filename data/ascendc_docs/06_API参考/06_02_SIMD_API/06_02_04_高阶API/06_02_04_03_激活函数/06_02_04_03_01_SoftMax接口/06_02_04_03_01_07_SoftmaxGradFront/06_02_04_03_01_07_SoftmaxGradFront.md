# SoftmaxGradFront

> **Section**: 6.2.4.3.1.7  
> **PDF Pages**: 2510–2514  

---

<!-- page 2510 -->

[17.5      17.5      17.5      ... 20.       20.       20.      ]]输入数据(inMeanLocal/inExpSumLocal/inMaxLocal)：[[0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] ... [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5] [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5]]输出数据(dstLocal)：[[0.0049   0.004906 0.004913 ... 0.998    1.       1.      ] [0.00488  0.00489  0.00489  ... 0.996    0.996    1.      ] [0.004868 0.004868 0.004887 ... 0.996    0.996    1.      ] ... [0.004894 0.004894 0.004894 ... 1.       1.       1.      ] [0.00472  0.00472  0.00472  ... 1.       1.       1.      ] [0.004684 0.004684 0.004684 ... 1.       1.       1.      ]]

## 6.2.4.3.1.7 SoftmaxGradFront

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

将输入tensor[m0, m1, ...mt, n]（t大于等于0）的非尾轴长度相乘的结果看作m，则输入tensor的shape看作[m, n]。对输入tensor[m,n]按行做gradfront反向计算，计算公式如下：

![p2510_img001.png](../../../../images/p2510_img001.png)

当输入shape为ND格式时，内部的reduce过程按last轴进行；当输入shape为NZ格式时，内部的reduce过程按照last轴和first轴进行，reduce过程可以参考 SoftMax中的图示说明。

为方便理解，通过Python脚本实现的方式，表达其计算公式如下，其中dx、y是源操作数（输入），d为目的操作数（输出）。

```cpp
def softmax_grad_front(dx, y, is_fp16=False):    dx = dx.astype(np.float32)    y = y.astype(np.float32)
```

<!-- page 2511 -->

```cpp
d = (dx * y).sum(axis=-1, keepdims=True)  ###[1024,1]    if is_fp16:        d = d.astype(np.float16)    return d
```

实现原理

以float类型，ND格式，shape为[m, k]的输入Tensor为例，描述SoftmaxGradFront高阶API内部算法框图，如下图所示。

图6-84 SoftmaxGradFront 算法框图

![p2511_img001.png](../../../../images/p2511_img001.png)

计算过程分为如下几步，均在Vector上进行：

1.mul步骤：对输入x和y所有数据相乘，计算结果会保存到一个临时空间temp中；

2.reducesum步骤：对temp中的数据([m, k])每一行数据求和得到[m, 1]，计算结果保存到临时空间中；

3.broadcast步骤：对[m, 1]做一个按datablock为单位的填充，比如float类型下，把[m, 1]扩展成[m, 8]，并输出结果z。

函数原型

●接口框架申请临时空间template <typename T, bool isBasicBlock = false, bool isDataFormatNZ = false>__aicore__ inline void SoftmaxGradFront(const LocalTensor<T>& dstTensor, const LocalTensor<T>& gradTensor, const LocalTensor<T>& srcTensor, const SoftMaxTiling& tiling, const SoftMaxShapeInfo& softmaxShapeInfo = {})

●通过sharedTmpBuffer入参传入临时空间template <typename T, bool isBasicBlock = false, bool isDataFormatNZ = false>__aicore__ inline void SoftmaxGradFront(const LocalTensor<T>& dstTensor, const LocalTensor<T>&

<!-- page 2512 -->

```cpp
gradTensor, const LocalTensor<T>& srcTensor, const LocalTensor<uint8_t>& sharedTmpBuffer, const SoftMaxTiling& tiling, const SoftMaxShapeInfo& softmaxShapeInfo = {})
```

由于该接口的内部实现中涉及复杂的计算，需要额外的临时空间来存储计算过程中的中间变量。临时空间支持接口框架申请和开发者通过sharedTmpBuffer入参传入两种方式。

●接口框架申请临时空间，开发者无需申请，但是需要预留临时空间的大小。

●通过sharedTmpBuffer入参传入，使用该tensor作为临时空间进行处理，接口框架不再申请。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。

接口框架申请的方式，开发者需要预留临时空间；通过sharedTmpBuffer传入的情况，开发者需要为tensor申请空间。临时空间大小BufferSize的获取方式如下：通过SoftmaxGrad Tiling接口中提供的GetSoftMaxGradMaxTmpSize/GetSoftMaxGradMinTmpSize接口获取所需最小和最大临时空间大小，最小空间可以保证功能正确，最大空间用于提升性能。

参数说明

表6-1127模板参数说明

参数名描述

T操作数的数据类型。

Atlas 350 加速卡，支持的数据类型为：half、float。

Atlas A3 训练系列产品/Atlas A3 推理系列产品，支持的数据类型为：half、float。

Atlas A2 训练系列产品/Atlas A2 推理系列产品，支持的数据类型为：half、float。

Atlas 200I/500 A2 推理产品，支持的数据类型为：half、float。

Atlas 推理系列产品AI Core，支持的数据类型为：half、float。

isBasicBlocksrcTensor和gradTensor的shape信息和Tiling切分策略满足基本块要求的情况下，可以使能该参数用于提升性能，默认不使能。是否满足基本块的要求，可以采用如下两种方式之一判断：

●srcTensor和dstTensor的shape信息[m,n]需要满足如下条件：

–尾轴长度n小于2048并且大于等于256/sizeof(T)（即half场景下n最小为128，float场景下n最小为64），同时n是64的倍数；

–非尾轴长度的乘积m为8的倍数。

●在Tiling实现中，通过调用IsBasicBlockInSoftMax判断Tiling切分策略是否满足基本块的切分要求。

针对Atlas 200I/500 A2 推理产品，该参数为预留参数，暂未启用，为后续的功能扩展做保留，保持默认值即可。

isDataFormatNZ当前输入输出的数据格式是否为NZ格式，默认数据格式为ND，即默认取值为false。

针对Atlas 200I/500 A2 推理产品，不支持配置为NZ格式。

<!-- page 2513 -->

表6-1128接口参数说明

描述

参数名输入/输出

dstTensor输出目的操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

last轴长度固定32Byte即一个datablock长度，并且该datablock中的所有数据为同一个值。比如half数据类型下，该datablock里的16个数均为相同的值，非last轴长度需要和srcTensor保持一致。

gradTensor输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

last轴长度需要32Byte对齐，gradTensor的shape与srcTensor的shape一致。

srcTensor输入源操作数。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

last轴长度需要32Byte对齐，srcTensor的shape与gradTensor的shape一致。

sharedTmpBuffer

输入临时空间。

类型为LocalTensor，支持的TPosition为VECIN/VECCALC/VECOUT。

该操作数的数据类型固定uint8_t。

用于接口内部复杂计算时存储中间变量，由开发者提供。

临时空间大小BufferSize的获取方式请参考 SoftmaxGradTiling接口。

tiling输入softmaxgradfront计算所需tiling信息，Tiling信息的获取请参考 SoftmaxGrad Tiling接口。

softmaxShapeInfo

输入srcTensor的shape信息。SoftMaxShapeInfo类型，具体定义如下：struct SoftMaxShapeInfo {    uint32_t srcM; // 非尾轴乘积长度    uint32_t srcK; // 尾轴长度，必须32Byte对齐    uint32_t oriSrcM; // 原始非尾轴乘积长度    uint32_t oriSrcK;  // 原始尾轴长度};

需要注意，当输入输出的数据格式为NZ格式时，尾轴长度为reduce轴长度即图6-79中的W0*W1，非尾轴为H0*H1。

返回值说明

无

<!-- page 2514 -->

约束说明

●操作数地址对齐要求请参见通用地址对齐约束。

●不支持sharedTmpBuffer与源操作数和目的操作数地址重叠。

●当参数softmaxShapeInfo中srcM != oriSrcM 或者 srcK != oriSrcK时，开发者需要对GM上的原始输入(oriSrcM, oriSrcK)在M或K方向补齐数据到(srcM, srcK)，补齐的数据会参与部分运算，在输入输出复用的场景下，API的计算结果会覆盖srcTensor中补齐的原始数据，在输入输出不复用的场景下，API的计算结果会覆盖dstTensor中对应srcTensor补齐位置的数据。

调用示例

完整算子样例请参考softmaxgradfront算子样例。// dstLocal: 存放SoftmaxGradFront计算结果的Tensor// gradLocal：存放SoftmaxGradFront计算的输入Tensor// srcLocal：存放SoftmaxGradFront计算的输入Tensor// sharedTmpBuffer: 存放SoftmaxGradFront计算过程中临时缓存的Tensor// softmaxTiling：存放SoftmaxGradFront计算所需Tiling信息，可通过SoftMaxGradTilingFunc接口获取

AscendC::SoftMaxShapeInfo softmaxInfo(    /* 非尾轴长度的乘积          */ srcM,     /* 尾轴长度，必须32Bytes对齐 */ srcK,     /* 原始非尾轴长度的乘积      */ oriSrcM,     /* 原始尾轴长度              */ oriSrcK);

// 通过sharedTmpBuffer入参传入临时空间AscendC::SoftmaxGradFront<T>(dstLocal, gradLocal, srcLocal, sharedTmpBuffer, softmaxTiling, softmaxInfo);// 接口框架申请临时空间AscendC::SoftmaxGradFront<T>(dstLocal, gradLocal, srcLocal, softmaxTiling, softmaxInfo);

结果示例如下：

输入数据(gradLocal)：[[-100.     -80.     -60.     -50.     -30.     -20.     -15.     -10.   ] [  -9.      -8.      -7.      -6.      -5.      -4.      -3.      -2.   ] [  -1.5     -1.      -0.8     -0.6     -0.5     -0.45    -0.4     -0.35 ] [  -0.3     -0.25    -0.2     -0.15    -0.1     -0.05    -0.01    -0.001] [   0.       0.001    0.01     0.05     0.1      0.15     0.2      0.25 ] [   0.3      0.35     0.4      0.45     0.5      0.6      0.8      1.   ] [   1.5      2.       3.       4.       5.       6.       7.       8.   ] [   9.      10.      15.      20.      30.      50.      60.      80.   ]]输入数据(srcLocal)：[[2. 2. 2. 2. 2. 2. 2. 2.] ... [2. 2. 2. 2. 2. 2. 2. 2.]]输出数据(dstLocal)：[[-730.   ] [ -88.   ] [ -11.2  ] [  -2.122] [   1.522] [   8.8  ] [  73.   ] [ 548.   ]]
