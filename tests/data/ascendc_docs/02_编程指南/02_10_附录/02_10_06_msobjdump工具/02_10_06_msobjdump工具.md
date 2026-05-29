# msobjdump工具

> **Section**: 2.10.6  
> **PDF Pages**: 358–370  

---

<!-- page 358 -->

●API方式

获取kernel侧调试信息并解析成可读文件。函数原型如下。def show_kernel_debug_data(bin_file_path: str, output_path: str = './') -> None

其中，输入参数说明如下。函数无输出参数和返回值。

–bin_file_path：kernel侧调试信息落盘的bin文件或包含bin文件的目录路径，字符串类型。

–output_path：解析结果的保存路径，字符串类型，默认是当前接口调用脚本所在目录下。

调用示例参考如下代码。

```cpp
from show_kernel_debug_data import show_kernel_debug_datashow_kernel_debug_data(./input/dump_workspace.bin)
```

产物说明

工具解析结果文件目录结构如下。其中，dump_data目录是对DumpTensor、PrintTimeStamp接口解析的结果，index0对应DumpTensor接口中第二个参数desc=0时的打印，loop0表示切分后首个分块的数据打印。

├ ${output_path}├── PARSER_${timestamp}                     // ${timestamp}表示时间戳     ├── dump_data     │   ├── 0                             // core0解析结果     │   ├── core_0_index_0_loop_0.bin     // core0 desc0 progress0落盘信息     │   ├── core_0_index_0_loop_0.txt     // core0 desc0 progress0解析结果      ...     │   ├── core_0_index_2_loop_15.bin    // core0 desc2 progress15落盘信息     │   ├── core_0_index_2_loop_15.txt    // core0 desc2 progress15解析结果     │   └── time_stamp_core_0.csv         // 时间戳信息     │   ├── 1                             // core1解析结果     │   ├── 2                             // core2解析结果      ...              │   └── index_dtype.json              // index与数据类型的映射关系     └── parser.log                         // 解析日志，包括printf、ascendc_assert接口的打印信息

## 2.10.6 msobjdump 工具

本工具主要针对Kernel直调工程（NPU模式）、标准自定义算子工程、简易自定义算子工程编译生成的算子ELF文件（Executable and Linkable Format）提供解析和解压功能，并将结果信息以可读形式呈现，方便开发者直观获得kernel文件信息。

说明

●ELF文件是一种用于二进制文件、可执行文件、目标代码、共享库和核心转储的文件格式，包括常见的*.a、*.so文件等。ELF文件常见构成如下：

●ELF头部：描述了整个文件的组织结构，包括文件类型、机器类型、版本号等信息。

●程序头部表：描述了文件中各种段（segments）信息，包括程序如何加载到内存中执行的信息。

●节区头部表：描述了文件中各个节（sections）信息，包括程序的代码、数据、符号表等。

●工具使用过程中，若出现如下场景，请根据日志提示信息，分析排查问题。

●ELF文件未找到

●ELF文件权限错误

●ELF文件存在但不支持解析或解压

<!-- page 359 -->

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品√

Atlas 训练系列产品√

工具安装

步骤1安装msobjdump工具。

工具跟随CANN软件包发布（参考环境准备完成CANN安装），其路径默认为“${INSTALL_DIR}/tools/msobjdump”，其中${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

步骤2设置环境变量。

●root用户安装Ascend-cann-toolkit包时source /usr/local/Ascend/cann/set_env.sh

●非root用户安装Ascend-cann-toolkit包时source ${HOME}/Ascend/cann/set_env.sh

步骤3检查工具是否安装成功。

执行如下命令，若能正常显示--help或-h信息，则表示工具环境正常，功能可正常使用。msobjdump -h

**----结束**

命令格式

●解析ELF文件的命令msobjdump --dump-elf <elf_file> [--verbose]

<!-- page 360 -->

表2-46参数说明

可选/必选

参数（区分大小写）

说明

--dump-elf<elf_file>，-d

必选解析ELF文件中包含的device信息，如文件名、文件类型、文件长度、符号表等，并终端打屏显示。

<elf_file>表示待解析ELF文件路径，如/home/op_api/lib_api.so。支持两种打印模式：

简单打印：默认仅打印部分device信息。

全量打印：与--verbose配套使用，开启全量device信息打屏显示。

不同工程打印字段信息不同，具体参见表2-49和表2-50。

--verbose，-V可选必须与--dump-elf配套使用，用于开启ELF文件中全量打印device信息功能。

●解压ELF文件的命令msobjdump --extract-elf <elf_file> [--out-dir <out_path>]

表2-47参数说明

可选/必选

参数（区分大小写）

说明

--extract-elf<elf_file>，-e

必选解压ELF文件中包含的device信息，并按原始文件夹规则落盘到输出路径下。

<elf_file>表示待解压ELF文件路径，如/home/op_api/lib_api.so。

默认路径：解压结果文件默认落盘到当前执行路径下。

自定义路径：可与--out-dir配套使用，设置落盘路径。

--out-dir<out_path>，-o

可选必须与--extract-elf配套使用，用于设置解压文件的落盘路径。

<out_path>为落盘文件目录，如/home/extract/。

请注意：msobjdump支持多用户并发调用，但需要指定不同的--out-dir，否则可能出现落盘内容被覆盖的问题。

●获取ELF文件列表的命令msobjdump --list-elf <elf_file>

<!-- page 361 -->

表2-48参数说明

可选/必选

参数（区分大小写）

说明

--list-elf<elf_file>，-l

可选获取ELF文件中包含的device信息文件列表，并打印显示。

<elf_file>表示待打印的ELF文件路径，如/home/op_api/lib_api.so。

表2-49 ELF 解析字段说明（Kernel 直调工程）

字段名含义是否必选

打印说明

VERSION表示版本号。是不设置--verbose，默认打印。

TYPECOUNT

表示ELF文件中包含的kernel文件个数。是不设置--verbose，默认打印。

ELF FILE${id}

表示ELF文件中包含的kernel文件名，${id}表示kernel文件序号。

是不设置--verbose，默认打印。

kernel文件名的命名规则如下：

按${sec_prefix}_${file_index}_${kernel_type}.o拼接，其中${sec_prefix}为section段名（工具根据“.ascend.kernel”关键字搜索获取），${file_index}表示文件编号，${kernel_type}表示kernel类型。

KERNELLEN

表示kernel文件的长度。是不设置--verbose，默认打印。

KERNELTYPE

表示kernel类型，映射关系为{0 : 'mix', 1: 'aiv', 2:'aic'}。

否不设置--verbose，默认打印。

ASCENDMETA

表示算子执行时核间同步、Cube/Vector核占比（task_ration）等信息。

否不设置--verbose，默认打印。

若没有获取到该信息，默认显示None。

elf heardinfos

包括ELF Header、Section Headers、Key toFlags、Program Headers、Symbol表等信息。

否设置--verbose，开启全量打印。

<!-- page 362 -->

表2-50 ELF 解析字段说明（标准/简易自定义算子工程）

字段名含义是否必选

打印说明

.ascend.meta. ${id}

表示算子kernel函数名称，其中${id}表示meta信息的索引值。

是不设置--verbose，默认打印。

VERSION表示版本号。是不设置--verbose，默认打印。

DEBUG调试相关信息，包含如下两部分内容：

否不设置--verbose，默认打印。

debugBufSize：调试信息需要的内存空间。

debugOptions：调试开关状态。取值如下：

0：调试开关关闭。

1：通过DumpTensor、printf打印进行调试。

2：通过assert断言进行调试。

4：通过时间戳打点功能进行调试。

8：通过内存越界检测进行调试。

DYNAMIC_PARAM

算子kernel函数是否启用动态参数。取值分别为：

否不设置--verbose，默认打印。

0：关闭动态参数模式。

1：开启动态参数模式。

OPTIONAL_PARAM

否不设置--verbose，默认打印。

可选参数信息，包含如下两部分内容：

optionalInputMode：可选输入在算子kernel函数中是否需要占位。取值分别为：

0：可选输入不占位。

1：可选输入占位。

optionalOutputMode：可选输出在算子kernel函数中是否需要占位。取值分别为：

0：可选输出不占位。

1：可选输出占位。

KERNEL_TYPE

表示kernel函数运行时core类型，取值参见表表2-51。

否不设置--verbose，默认打印。

CROSS_CORE_SYNC

表示硬同步syncall类型。

否不设置--verbose，默认打印。

USE_SYNC：使用硬同步。

NO_USE_SYNC：不使用硬同步。

<!-- page 363 -->

字段名含义是否必选

打印说明

MIX_TASK_RATION

表示kernel函数运行时的Cube核/Vector核占比分配类型。

否不设置--verbose，默认打印。

DETERMINISTIC_INFO

否不设置--verbose，默认打印。

表示算子是否为确定性计算。

0：不确定计算。

1：确定性计算。

BLOCK_NUM

否不设置--verbose，默认打印。

表示算子执行核数，该字段当前暂不支持，只打印默认值0xFFFFFFFF。

FUNCTION_ENTRY

算子TilingKey的值。否不设置--verbose，默认打印。

elf heardinfos

包括ELF Header、Section Headers、Key toFlags、Program Headers、Symbol表等信息。

否设置--verbose，开启全量打印。

表2-51 kernel type 信息

**KERNEL_TYPE说明**

AICORE该参数为预留参数，当前版本暂不支持。

算子执行时仅会启动AI Core，比如用户在host侧设置blocknum为5，则会启动5个AI Core。

AIC算子执行时仅启动AI Core上的Cube核：比如用户在host侧设置blocknum为10，则会启动10个Cube核。

AIV算子执行时仅启动AI Core上的Vector核：比如用户在host侧设置blocknum为10，则会启动10个Vector核。

MIX_AIC_MAINAIC、AIV混合场景下，设置核函数的类型为MIX ，算子执行时会同时启动AI Core上的Cube核和Vector核，比如用户在host侧设置blocknum为10，且设置task_ration为1：2，则会启动10个Cube核和20个Vector核。

MIX_AIV_MAINAIC、AIV混合场景下，使用了多核控制相关指令时，设置核函数的类型为MIX，算子执行时会同时启动AI Core上的Cube核和Vector核，比如用户在host侧设置blocknum为10，且设置task_ration为1：2，则会启动10个Vector核和20个Cube核。

<!-- page 364 -->

**KERNEL_TYPE说明**

AIC_ROLLBACK算子执行时会同时启动AI Core和Vector Core，此时AI Core会当成Cube Core使用。

AIV_ROLLBACK算子执行时会同时启动AI Core和Vector Core，此时AI Core会当成Vector Core使用。

使用样例（Kernel 直调算子工程）

以MatMulInvocationNeo算子为例（NPU模式），假设${cmake_install_dir}为算子Cmake编译产物根目录，目录结构如下（仅为示例，具体以实际算子工程为准），类似CMake编译配置文件编写。

out├── lib│   ├── libascendc_kernels_npu.so├── include│   ├── ascendc_kernels_npu│           ├── aclrtlaunch_matmul_custom.h│           ├── aclrtlaunch_triple_chevrons_func.h......

工具对编译生成的库文件（如*.so、*.a等）进行解析和解压，功能实现命令样例如下：

●解析包含device信息的库文件

支持两种打印方式，请按需选取，解析字段含义参见表2-49。

–简单打印msobjdump --dump-elf ${cmake_install_dir}/out/libascendc_kernels_npu.so

执行上述命令，终端打印基础device信息，示例如下：

===========================[VERSION]: 1[TYPE COUNT]: 1===========================[ELF FILE 0]: ascendxxxb1_ascendc_kernels_npu_0_mix.o[KERNEL TYPE]: mix[KERNEL LEN]: 511560[ASCEND META]: None

–全量打印msobjdump --dump-elf ${cmake_install_dir}/out/libascendc_kernels_npu.so --verbose

执行上述命令，终端打印所有device信息，示例如下：

===========================[VERSION]: 1[TYPE COUNT]: 1===========================[ELF FILE 0]: ascendxxxb1_ascendc_kernels_npu_0_mix.o[KERNEL TYPE]: mix[KERNEL LEN]: 511560[ASCEND META]: None====== [elf heard infos] ======ELF Header:  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  Class:                             ELF64  Data:                              2's complement, little endian  Version:                           1 (current)  OS/ABI:                            UNIX - System V  ABI Version:                       0  Type:                              EXEC (Executable file)  Machine:                           <unknown>: 0x1029

<!-- page 365 -->

```cpp
Version:                           0x1  Entry point address:               0x0  Start of program headers:          64 (bytes into file)  Start of section headers:          510280 (bytes into file)  Flags:                             0x940000  Size of this header:               64 (bytes)  Size of program headers:           56 (bytes)  Number of program headers:         2  Size of section headers:           64 (bytes)  Number of section headers:         20  Section header string table index: 18
Section Headers:  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al  [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0  [ 1] .text             PROGBITS        0000000000000000 0000b0 010a08 00  AX  0   0  4   .....................................................................................  [19] .strtab           STRTAB          0000000000000000 071278 00b6cb 00      0   0  1Key to Flags:  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),  L (link order), O (extra OS processing required), G (group), T (TLS),  C (compressed), x (unknown), o (OS specific), E (exclude),  D (mbind), p (processor specific)
There are no section groups in this file.
Program Headers:  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align  LOAD           0x0000b0 0x0000000000000000 0x0000000000000000 0x010aa8 0x010aa8 R E 0x1000  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0......
```

●解压包含device信息的库文件并落盘msobjdump --extract-elf ${cmake_install_dir}/out/libascendc_kernels_npu.so

执行上述命令，默认在当前执行路径下落盘ascendxxxb1_ascendc_kernels_npu_0_mix.o文件。

●获取包含device信息的库文件列表msobjdump --list-elf ${cmake_install_dir}/out/libascendc_kernels_npu.so

执行上述命令，终端会打印所有文件，屏显信息形如：

```cpp
ELF file    0: ascendxxxb1_ascendc_kernels_npu_0_mix.o
```

使用样例（标准/简易自定义算子工程）

以下面的算子工程为例（仅为示例，具体以实际算子工程为准），假设${cmake_install_dir}为算子Cmake编译产物根目录，目录结构如下，类似算子编译。

├── op_api│   ├── include│       ├── aclnn_acos_custom.h│       ├── aclnn_matmul_leakyrelu_custom.h│       ├── .........│   ├── lib│       ├── libcust_opapi.so

工具对编译生成的库文件（如*.so、*.a等）进行解析和解压，功能实现命令样例如下：

●解析包含device信息的库文件

支持两种打印方式，请按需选取，解析字段含义参见表2-50。

–简单打印msobjdump --dump-elf ${cmake_install_dir}/op_api/lib/libcust_opapi.so

执行上述命令，终端打印基础device信息，示例如下：

<!-- page 366 -->

```cpp
.ascend.meta META INFOVERSION: 1DEBUG: debugBufSize=0, debugOptions=0DYNAMIC_PARAM: dynamicParamMode=0OPTIONAL_PARAM: optionalInputMode=1, optionalOutputMode=1.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_1KERNEL_TYPE: AIVDETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 1.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_2_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 2.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_3_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 3.....................................ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_1KERNEL_TYPE: AIVDETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 1.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_2_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 2.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_3_mix_aivKERNEL_TYPE: MIX_AIV_MAINDETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 3
```

–全量打印msobjdump --dump-elf ${cmake_install_dir}/op_api/lib/libcust_opapi.so --verbose

执行上述命令，终端打印基础device信息，示例如下：

```cpp
.ascend.meta META INFOVERSION: 1DEBUG: debugBufSize=0, debugOptions=0DYNAMIC_PARAM: dynamicParamMode=0OPTIONAL_PARAM: optionalInputMode=1, optionalOutputMode=1.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_1KERNEL_TYPE: AIVDETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 1.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_2_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 2.ascend.meta. [0]: AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26_3_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 3.....................................ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_1KERNEL_TYPE: AIVDETERMINISTIC_INFO: 1
```

<!-- page 367 -->

BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 1.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_2_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]DETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 2.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_3_mix_aivKERNEL_TYPE: MIX_AIV_MAINDETERMINISTIC_INFO: 1BLOCK_NUM: 0xFFFFFFFFFUNCTION_ENTRY: 3....................................===== [elf heard infos] in ascendxxx_acos_custom_AcosCustom_da824ede53d7e754f85c14b9446ec2fc.o =====:ELF Header:  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  Class:                             ELF64  Data:                              2's complement, little endian  Version:                           1 (current)  OS/ABI:                            UNIX - System V  ................................................  Size of program headers:           56 (bytes)  Number of program headers:         3  Size of section headers:           64 (bytes)  Number of section headers:         9  Section header string table index: 7Section Headers:  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al  [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0    .....................................................................................  [ 8] .strtab           STRTAB          0000000000000000 00529b 000119 00      0   0  1Key to Flags:  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),  L (link order), O (extra OS processing required), G (group), T (TLS),  C (compressed), x (unknown), o (OS specific), E (exclude),  D (mbind), p (processor specific)................................................

===== [elf heard infos] in ascendxxx_matmul_leakyrelu_custom_MatmulLeakyreluCustom_e052bee3255764ac919095f3bdf83389.o =====:ELF Header:  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  Class:                             ELF64  Data:                              2's complement, little endian  Version:                           1 (current)  ................................................  Section header string table index: 6Section Headers:  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al  [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0  [ 1] .text             PROGBITS        0000000000000000 0000e8 007ed8 00  AX  0   0  4  [ 2] .data             PROGBITS        0000000000008000 0080e8 000008 00  WA  0   0 256  [ 3] .comment          PROGBITS        0000000000000000 0080f0 000043 01  MS  0   0  1  [ 4] .bl_uninit        NOBITS          0000000000000000 008133 000020 00      0   0  1  [ 5] .symtab           SYMTAB          0000000000000000 008138 0000c0 18      7   1  8  [ 6] .shstrtab         STRTAB          0000000000000000 0081f8 00003b 00      0   0  1  [ 7] .strtab           STRTAB          0000000000000000 008233 0000ec 00      0   0  1  ................................................

●解压包含device信息的库文件并落盘msobjdump --extract-elf ${cmake_install_dir}/op_api/lib/libcust_opapi.so

执行上述命令，默认在当前执行路径下保存解压文件，产物目录如下：

|-- config                                                               // 算子原型配置文件目录|    ├── ${soc_version}   |        ├── acos_custom.json                                  |        ├── matmul_leakyrelu_custom.json

<!-- page 368 -->

|        ├── .......                                             |-- ${soc_version}                                                    // AI处理器名|     ├── acos_custom                                               // 基础单算子编译文件*.o和对应的*.json文件|         ├── AcosCustom_da824ede53d7e754f85c14b9446ec2fc.json      // 命名规则：${op_type}_${parm_info}.json或${op_type}_${parm_info}.o，${parm_info}是基于算子输入/输出dtype、shape等信息生成的标识码|         ├── AcosCustom_da824ede53d7e754f85c14b9446ec2fc.o|         ├── AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26.json|         ├── AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26.o|     ├── matmul_leakyrelu_custom  |         ├── MatmulLeakyreluCustom_e052bee3255764ac919095f3bdf83389.json|         ├── MatmulLeakyreluCustom_e052bee3255764ac919095f3bdf83389.o|     ├── axpy_custom    |         ├── .....

以acos_custom算子编译产物解压为例：

–查看算子原型（acos_custom.json）{    "binList": [        {            "implMode": "high_performance",            "int64Mode": false,            "simplifiedKeyMode": 0,            "simplifiedKey": [......],            "staticKey": "96b2b4bb2e3xxx,ee37ce8796ef139dexxxx",            "inputs": [                {                    "name": "x",                    "index": 0,                    "dtype": "float32",                    "format": "ND",                    "paramType": "required",                    "shape": [                        -2                    ],                    "format_match_mode": "FormatAgnostic"                }            ],            "outputs": [                {                    "name": "y",                    "index": 0,                    "dtype": "float32",                    "format": "ND",                    "paramType": "required",                    "shape": [                        -2                    ],                    "format_match_mode": "FormatAgnostic"                }            ],            "attrs": [                {                    "name": "tmp",                    "dtype": "int",                    "value": 0                },                .........            ],            "opMode": "dynamic",            "optionalInputMode": "gen_placeholder",            "deterministic": "ignore",            "binInfo": {                "jsonFilePath": "ascendxxx/acos_custom/AcosCustom_da824ede53d7e754f85c14b9446ec2fc.json"            }        },        {            "implMode": "high_performance",

<!-- page 369 -->

```cpp
"int64Mode": false,            "simplifiedKeyMode": 0,            "simplifiedKey": [            ],            "staticKey": "27d6f997f2f3551axxxx,1385590c47affa578eb429xxx",            "inputs": [                {                    "name": "x",                    "index": 0,                    "dtype": "float16",                    "format": "ND",                    "paramType": "required",                    "shape": [                        -2                    ],                    "format_match_mode": "FormatAgnostic"                }            ],            "outputs": [                {                    "name": "y",                    "index": 0,                    "dtype": "float16",                    "format": "ND",                    "paramType": "required",                    "shape": [                        -2                    ],                    "format_match_mode": "FormatAgnostic"                }            ],            "attrs": [                {                    "name": "tmp",                    "dtype": "int",                    "value": 0                },                .........            ],            "opMode": "dynamic",            "optionalInputMode": "gen_placeholder",            "deterministic": "ignore",            "binInfo": {                "jsonFilePath": "ascendxxx/acos_custom/AcosCustom_dad9c8ca8fcbfd789010c8b1c0da8e26.json"            }        }    ]}
```

–解析${op_type}_${parm_info}.o文件获取.ascend.meta段信息。msobjdump --dump-elf ./AcosCustom_da824ede53d7e754f85c14b9446ec2fc.o

执行上述命令，终端屏显如下，字段与库文件解析类似，参见表2-50。

```cpp
.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_1KERNEL_TYPE: AIV.ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_2_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1].ascend.meta. [0]: AcosCustom_da824ede53d7e754f85c14b9446ec2fc_3_mix_aivKERNEL_TYPE: MIX_AIV_MAINMIX_TASK_RATION: [0:1]
```

–查看${op_type}_${parm_info}.json，直观获取device文件中算子信息。{    "binFileName": "AcosCustom_da824ede53d7e754f85c14b9446ec2fc",    "binFileSuffix": ".o",    "blockDim": -1,    "coreType": "MIX",

<!-- page 370 -->

"intercoreSync": 1,    "kernelName": "AcosCustom_da824ede53d7e754f85c14b9446ec2fc",    "magic": "RT_DEV_BINARY_MAGIC_ELF",    "memoryStamping": [],    "opParaSize": 24,    "parameters": [],    "sha256": "94e32d04fcaf435411xxxxxxxx",    "workspace": {        "num": 1,        "size": [            -1        ],        "type": [            0        ]    },    "kernelList": [        {            "tilingKey": 1,            "kernelType": "MIX_AIC",            "taskRation": "0:1",            "crossCoreSync": 0,            "kernelName": "AcosCustom_da824ede53d7e754f85c14b9446ec2fc_1"        },        .........    ],    "taskRation": "tilingKey",    "optionalInputMode": "gen_placeholder",    "debugOptions": "printf",    "debugBufSize": 78643200,    "compileInfo": {},    "supportInfo": {                                                        // 算子原型信息        "implMode": "high_performance",        "int64Mode": false,        "simplifiedKeyMode": 0,        "simplifiedKey": [......],        "staticKey": "96b2b4bb2e35fa3dxxx,ee37ce8796ef139dedxxxxxxxx",        "inputs": [            {                "name": "x",                "index": 0,                "dtype": "float32",                "format": "ND",                "paramType": "required",                "shape": [                    -2                ],                "format_match_mode": "FormatAgnostic"            }        ],        "outputs": [            {                "name": "y",                "index": 0,                "dtype": "float32",                "format": "ND",                "paramType": "required",                "shape": [                    -2                ],                "format_match_mode": "FormatAgnostic"            }        ],        "attrs": [            {                "name": "tmp",                "dtype": "int",                "value": 0            },
