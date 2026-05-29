# PlatformInfo

> **Section**: 6.4.5.2.14  
> **PDF Pages**: 3853–3854  

---

<!-- page 3853 -->

## 6.4.5.2.14 PlatformInfo

功能说明

将指向fe::PlatFormInfos的指针传入TilingContext。

函数原型

```cpp
ContextBuilder &PlatformInfo(void *platformInfo)
```

参数说明

参数输入/输出说明

platformInfo

输入指向fe::PlatFormInfos类型数据的void指针

返回值说明

当前ContextBuilder的对象。

约束说明

由于TilingContext与KernelContext、TilingParseContext内部数据排序不同，Platform()只支持以调用BuildTilingContext()为前提来使用；其他场景建议用Outputs接口，否则发生未定义行为。

调用示例

void AddPlatformInfo(fe::PlatFormInfos *platformInfo){    ......    auto kernelContextHolder = context_ascendc::ContextBuilder()                                     ...... // 增加算子输入输出接口的调用                                     .PlatformInfo(reinterpret_cast<void*>(platformInfo));                                     .BuildTilingContext();

```cpp
......}
```

## 6.4.5.2.15 AddPlatformInfo

功能说明

设置硬件平台信息便于用户在算子Tiling函数调测中使用。支持以下两种设置方式：

●自动获取当前硬件平台信息：传入空指针，自动获取当前硬件信息并添加到ContextBuilder类中。

●指定硬件平台信息：传入具体的AI处理器型号，添加对应硬件信息至ContextBuilder类中。

若设置失败，会打印报错信息。关于日志配置和查看，请参考《环境变量参考》中“辅助功能 > 日志”章节。

<!-- page 3854 -->

函数原型

```cpp
ContextBuilder &AddPlatformInfo(const char* customSocVersion)
```

参数说明

参数名输入/输出描述

customSocVersion

输入AI处理器型号。配置方式如下：

●针对如下产品：在安装AI处理器的服务器执行npu-smi info命令进行查询，获取Name信息。实际配置值为AscendName，例如Name取值为xxxyy，实际配置值为Ascendxxxyy。Atlas A2 训练系列产品/Atlas A2 推理系列产品

Atlas 200I/500 A2 推理产品

Atlas 推理系列产品

Atlas 训练系列产品

●针对Atlas A3 训练系列产品/Atlas A3 推理系列产品，在安装AI处理器的服务器执行npu-smi info -tboard -i id -c chip_id命令进行查询，获取ChipName和NPU Name信息，实际配置值为ChipName_NPU Name。例如Chip Name取值为Ascendxxx，NPU Name取值为1234，实际配置值为Ascendxxx_1234。其中：

–id：设备id，通过npu-smi info -l命令查出的NPU ID即为设备id。

–chip_id：芯片id，通过npu-smi info -m命令查出的Chip ID即为芯片id。

●针对Atlas 350 加速卡，在安装AI处理器的服务器执行npu-smi info -t board -i id命令进行查询，获取Chip Name和NPU Name信息，实际配置值为ChipName_NPU Name。例如Chip Name取值为Ascendxxx，NPU Name取值为1234，实际配置值为Ascendxxx_1234。其中，id为设备id，通过npu-smi info -l命令查出的NPU ID即为设备id。

返回值说明

当前ContextBuilder对象。

约束说明

AddPlatformInfo调用后需要通过BuildTilingContext来构建Tiling的上下文，并传递给Tiling函数来使用。

调用示例

```cpp
void AddPlatformInfoDemo(......){
```
