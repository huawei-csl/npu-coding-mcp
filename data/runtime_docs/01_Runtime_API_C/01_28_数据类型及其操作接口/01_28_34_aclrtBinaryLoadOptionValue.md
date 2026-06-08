# aclrtBinaryLoadOptionValue

> **Section**: 1.28.34


typedef union aclrtBinaryLoadOptionValue { uint32\_t isLazyLoad; uint32\_t magic; int32\_t cpuKernelMode; uint32\_t rsv[4]; } aclrtBinaryLoadOptionValue;

| 成员名称       | 描述                                                                                                                                                  |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| isLazyLoad | 指定解析算子二进制、注册算子后，是否加载算子到 Device 侧。 取值如下： ● 1 ：调用本接口时不加载算子到 Device 侧。 ● 0 ：调用本接口时加载算子到 Device 侧。如果不指定 ACL_RT_BINARY_LOAD_OPT_LAZY_LOAD 选项，系统默认按 此值处理。 |

| 成员名称           | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| magic          | 标识算子计算单元的魔术数字。 取值为如下宏： ● ACL_RT_BINARY_MAGIC_ELF_AICORE ● ACL_RT_BINARY_MAGIC_ELF_VECTOR_CORE ● ACL_RT_BINARY_MAGIC_ELF_CUBE_CORE 宏的定义如下： #define ACL_RT_BINARY_MAGIC_ELF_AICORE 0x43554245U #define ACL_RT_BINARY_MAGIC_ELF_VECTOR_CORE 0x41415246U #define ACL_RT_BINARY_MAGIC_ELF_CUBE_CORE 0x41494343U 关于 Core 的定义及详细说明，请参见 1.28.45 aclrtDevAttr 。                                                                               |
| cpuKernelMod e | AI CPU 算子注册模式。 取值如下： ● 0 ：调用 aclrtBinaryLoadFromFile 接口加载算子时，使用算子 信息库文件（ .json ）注册算子。该场景下， AI CPU 算子库文件 （ .so ）已经在调用 aclrtSetDevice 接口时被加载到 Device 。适 用于加载 CANN 内置算子。 ● 1 ：调用 aclrtBinaryLoadFromFile 接口加载算子时，使用算子 信息库文件（ .json ）注册算子。该场景下， aclrtBinaryLoadFromFile 接口会查找算子信息库文件同名的 AI CPU 算子库文件（ .so ）。适用于加载用户自定义算子。 ● 2 ：调用 aclrtBinaryLoadFromData 接口加载算子，并配合使 用 aclrtRegisterCpuFunc 接口注册 AI CPU 算子信息。适用于没 有算子信息库文件，也没有算子库文件的场景。 |
| rsv            | 预留值。                                                                                                                                                                                                                                                                                                                                                                                                                                 |
