# SIMT BuiltIn关键字

> **Section**: 2.4.2  
> **PDF Pages**: 162–168  

---

<!-- page 162 -->

内置变量

变量名对应API功能

block_numGetBlockNum当前任务配置的核数，用于代码内部的多核逻辑控制等。

block_idxGetBlockIdx当前核的索引，用于代码内部的多核逻辑控制及多核偏移量计算等。

通常，建议用户使用内置变量对应的API获取所需值，不建议用户直接使用内置变量。因为内置变量反映的是单个硬件资源的配置信息，对于软件栈整合硬件资源、扩展硬件的功能，内置变量的值与实际语义可能不符。

例如，在Atlas 推理系列产品中，当启用KERNEL_TYPE_MIX_VECTOR_CORE时，算子会同时运行在AI Core和Vector Core上。此时，block_idx在这两种核心上都是从0开始计数，用户无法直接通过block_idx来切分数据和控制多核逻辑。而GetBlockIdx在Vector Core上对block_idx增加偏移量（AI Core的block_num），从而保证返回的值能够正确反映多核环境下的实际逻辑。

## SIMD 与SIMT 混合编程场景

SIMD与SIMT混合编程场景中，SIMT VF的入口函数使用__simt_vf__进行标识，通过在SIMD的__aicore__函数中使用asc_vf_call调用SIMT入口函数。被SIMT VF入口函数调用的函数使用__simt_callee__进行标识。

●__simt_vf__

函数标记宏，用于标记SIMT VF入口函数，函数无返回值。使用asc_vf_call接口调用SIMT VF入口函数，启动VF子任务。__simt_vf__ inline void KernelAdd(__gm__ float* x, __gm__ float* y, __gm__ float* z)

__simt_vf__标记的SIMT VF函数支持的参数类型如下。__simt_vf__的使用示例请参考编程示例。

–指针类型：__ubuf__ *、__gm__ *；

–标量类型：bool、int8_t、uint8_t、int16_t、uint16_t、half、bfloat16、int32_t、uint32_t、float、int64_t、uint64_t。

●__simt_callee__

函数标记宏，用于标记SIMT VF非入口函数，函数可以有返回值，允许被SIMT VF入口函数或其他非入口函数调用。

```cpp
__simt_callee__ inline float add(float x, float y)
```

Ascend C为SIMT编程、SIMD与SIMT混合编程提供了布尔、整形、浮点型的标量数据类型和短向量数据类型，提供了用于表达线程块、线程网格三维信息的内置变量。关于内置数据格式的详细说明请参见内置数据类型，内置变量请参见内置变量。

## 2.4.2 SIMT BuiltIn 关键字

函数执行空间限定符

函数执行空间限定符（Function Execution Space Qualifier）指示函数是在Host侧执行还是在Device侧执行，以及能被调用的空间范围。

<!-- page 163 -->

表2-19函数执行空间限定符概览

函数执行空间限定符执行空间允许调用函数空间

**HostDeviceHostDevice**

__host__，无限定符√x√x

__aicore__x√x√

__global__x√√x

__global__修饰的函数是核函数入口，有以下使用约束：

●函数返回类型必须为void，不能是class、struct或者union的成员函数。

●不支持递归调用。

●对__global__函数的调用是异步的，调用后即返回Host侧的主机线程。

●只能被Host侧函数调用，在Device上执行。

__aicore__修饰的函数只能在Device侧执行，只能被__global__函数，或者其他__aicore__函数调用。

__host__修饰的函数只能在Host侧被调用和执行。

内存空间限定符

使用内存空间限定符__ubuf__来表示动、静态内存，静态内存的大小在编译期是确定的，动态内存的大小在核函数执行时确定。

注意

当前版本暂未支持动、静态内存，请关注后续版本。

●静态内存通过数组分配：__ubuf__ half staticBuf[1024];

●动态内存通过以下方式申请使用：extern __ubuf__ half dynamicBuf[]; 动态内存的实际内存大小需要在核函数启动时配置，详见核函数配置。

内置变量

●dim3

用于指定和获取线程网格（grid）、线程块（block）在x、y、z维度上的内置结构体。

dim3由3个无符号整数组成，结构体定义为{dimx，dimy，dimz}，用于指定3个不同维度的大小，三维总数为dimx * dimy * dimz。开发者可以通过如下方式创建dim3结构。dim3(x); // 创建一维结构，dimy和dimz为默认值1dim3(x, y); // 创建二维结构，dimz为默认值1dim3(x, y, z); // 创建三维结构

当前提供了以下仅在Device上可用的dim3结构的内置变量：

<!-- page 164 -->

●gridDim

内置全局变量，只能在核函数中使用，表示整个计算任务在各个维度上分别由多少个线程块构成。

–gridDim.x是x维度上的线程块数量。

–gridDim.y是y维度上的线程块数量，目前只能返回1。

–gridDim.z是z维度上的线程块数量，目前只能返回1。

●blockDim

内置全局变量，在核函数中可以直接使用，用于获取线程块中配置的线程的三维层次结构，即启动VF时配置的dim3结构体实例值。blockDim.x，blockDim.y，blockDim.z分别表示线程块中三个维度的线程数。

●blockIdx

内置全局变量，只能在核函数中使用，用于获取块索引。表示当前线程所在的线程块在整个网格中的位置坐标。

–blockIdx.x的范围是0到gridDim.x - 1。

–blockIdx.y的范围是0到gridDim.y - 1，目前只能返回0。

–blockIdx.z的范围是0到gridDim.z - 1，目前只能返回0。

●threadIdx

内置全局变量，在核函数中可以直接使用，用于获取当前线程在线程块内部的索引。threadIdx.x，threadIdx.y，threadIdx.z分别表示当前线程在3个维度的索引，threadIdx.x的范围为[0, blockDim.x)，threadIdx.y的范围为[0, blockDim.y)，threadIdx.z的范围为[0, blockDim.z)。线程块内线程的索引与线程ID对应关系如下：

–对于一维线程块，其线程ID为threadIdx.x。

–对于二维线程块，其线程ID为（threadIdx.x + threadIdx.y * blockDim.x）。

–对于三维线程块，其线程ID为（threadIdx.x + threadIdx.y * blockDim.x +threadIdx.z * blockDim.x * blockDim.y）。

当前提供了以下仅在Device上可用的int类型的内置变量：

●warpSize

运行时变量，表示一个线程束（warp）中的线程数量，当前为固定值32。

内置数据类型

目前提供了一系列适用于Device侧的数据类型，包括标量和短向量。短向量是由多个元素组成的简单向量。

表2-20标量数据类型

数据类型描述Size（bit）

类型

取值范围

bool布尔类型，占8比特，全0时代表false，否则代表true。

8true, flase

布尔型

<!-- page 165 -->

uint8_tunsigned char8[0, 255]

整形

int8_tsigned char8[-128, 127]

uint16_tunsigned short16[0, 65535]

int16_tsigned short16[-32768, 32767]

uint32_tunsigned int32[0, 4294967295]

int32_tsigned int32[-2147483648,2147483647]

uint64_tunsigned long64[0,18446744073709551615]

int64_tsigned long64[-9223372036854775808,9223372036854775807]

float8_e4m3_t符号位宽1，指数位宽4，尾数位宽3

8[26 - 29, 29 - 26]

浮点型

float8_e5m2_t符号位宽1，指数位宽5，尾数位宽2

8[213 - 216, 216 -213]

8点域编码决定数据精度与取值范围

hifloat8_t符号位宽1，点域位宽2，指数与尾数位宽由点域编码决定

half符号位宽1，指数位宽5，尾数位宽10

16[25 - 216, 216 - 25]

bfloat16_t符号位宽1，指数位宽8，尾数位宽7

16[2120 - 2128, 2128 -2120]

float符号位宽1，指数位宽8，尾数位宽23

32[2104 - 2128, 2128 -2104]

短向量数据类型分为Vector X2、Vector X4，表示一个短向量变量有2、4个元素，当前支持的类型分布如下：

元素数据类型Vector X2Vector X4

unsigned charuchar2uchar4

signed charchar2char4

unsigned short (16bit)ushort2ushort4

signed short (16bit)short2short4

unsigned intuint2uint4

<!-- page 166 -->

signed intint2int4

无符号的长整型 (64bit)ulonglong2ulonglong4

有符号的长整型 (64bit)longlong2longlong4

无符号的长整型 (32bit)ulong2ulong4

有符号的长整型 (32bit)long2long4

浮点型，1符号位，2指数位，1尾数位float4_e2m1x2_t-

浮点型，1符号位，1指数位，2尾数位float4_e1m2x2_t-

浮点型，1符号位，4指数位，3尾数位float8_e4m3x2_t-

浮点型，1符号位，5指数位，2尾数位float8_e5m2x2_t-

浮点型 hif8hifloat8x2_t-

浮点型，1符号位，5指数位，10尾数位half2-

浮点型，1符号位，8指数位，7尾数位bfloat16x2_t-

浮点型，1符号位，8指数位，23尾数位float2float4

表2-21短向量数据类型

数据类型内存大小（字节）

地址对齐（字节）

char2, uchar222

char4, uchar444

short2, ushort244

short4, ushort488

int2, uint288

int4, uint41616

long2，ulong288

long4，ulong41616

longlong2，ulonglong21616

longlong4，ulonglong43232

float288

float41616

float4_e2m1x2_t， float4_e1m2x2_t11

<!-- page 167 -->

float8_e4m3x2_t，float8_e5m2x2_t、hifloat8x2_t

22

half2，bfloat16x2_t44

运算符

SIMT编程提供了一系列运算符，用于执行数学运算。以下是支持的运算符列表。

表2-22 SIMT 编程支持的运算符列表

**half/bfloat16_t/float**

**half2/bfloat16x2_t**

**hifloat8_t**

**bool**

**int8_t/uint8_t/int16_t/uint16_t/int32_t/uint32_t/int64_t/uint64_t**

类别运算符

+x√√√x

算术运算符

-x√√√x

*x√√√x

/x√√√x

%x√xxx

++x√√√x

--x√√√x

- (取反)

x√√√x

<x√√xx

比较运算符

<=x√√xx

>x√√xx

>=x√√xx

==x√√xx

!=x√√xx

&x√xxx

位运算符

|x√xxx

^x√xxx

~x√xxx

<<x√xxx

>>x√xxx

<!-- page 168 -->

**half/bfloat16_t/float**

**half2/bfloat16x2_t**

**hifloat8_t**

**bool**

**int8_t/uint8_t/int16_t/uint16_t/int32_t/uint32_t/int64_t/uint64_t**

类别运算符

&&√√√xx

逻辑运算符

||√√√xx

!√√√xx

a ?b : c

√√√√x

条件运算符

运算符使用示例如下所示：// 加法运算res[idx] = x[idx] + y[idx];

// 取反运算x[idx] = (-x[idx]);

// 比较运算if (x[idx] > y[idx]) {    res[idx] = x[idx];} else {    res[idx] = y[idx];}

// 按位与运算res[idx] = x[idx] & y[idx];

// 逻辑或运算if (x[idx] || y[idx]) {    res[idx] = 1;}

// 条件运算res[idx] = x[idx] > y[idx] ? x[idx] : y[idx];

核函数配置

在调用__global__限定符修饰的函数时必须指定执行配置。执行配置通过在函数名后带括号的参数列表之间插入，形如：

```cpp
<<<grid_dim, block_dim, dynamic_mem_size, stream>>>
```

其中：

●grid_dim：int或dim3类型，用于指定网格（grid）的维度与规模，grid_dim.x *grid_dim.y * grid_dim.z等于启动的线程块总数。

●block_dim：int或dim3类型，用于指定每个线程块（block）的维度与规模，block_dim.x * block_dim.y * block_dim.z等于每个线程块包含的线程数。

●dynamic_mem_size：size_t类型，该参数指定除静态分配的内存外，本次调用为每个线程块动态分配的共享内存字节数。

●stream：aclrtStream类型指针，指定关联的流，用于维护异步操作的执行顺序。

以下示例展示了内核函数的声明与调用方式。// 声明__global__ void add_custom(float* x, float* y, float* z, uint64_t total_length);
