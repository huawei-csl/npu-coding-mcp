# GetCurNpuArch

> **Section**: 6.4.2.1.5  
> **PDF Pages**: 3762–3762  

---

<!-- page 3762 -->

返回值

当前硬件平台版本型号的枚举类。该枚举类和AI处理器型号的对应关系请通过CANN软件安装后文件存储路径下include/tiling/platform/platform_ascendc.h头文件获取。

AI处理器的型号请通过如下方式获取：

●针对如下产品：在安装AI处理器的服务器执行npu-smi info命令进行查询，获取Name信息。实际配置值为AscendName，例如Name取值为xxxyy，实际配置值为Ascendxxxyy。

Atlas A2 训练系列产品/Atlas A2 推理系列产品

Atlas 200I/500 A2 推理产品

Atlas 推理系列产品

Atlas 训练系列产品

●针对Atlas A3 训练系列产品/Atlas A3 推理系列产品，在安装AI处理器的服务器执行npu-smi info -t board -i id -c chip_id命令进行查询，获取Chip Name和NPUName信息，实际配置值为Chip Name_NPU Name。例如Chip Name取值为Ascendxxx，NPU Name取值为1234，实际配置值为Ascendxxx_1234。其中：

–id：设备id，通过npu-smi info -l命令查出的NPU ID即为设备id。

–chip_id：芯片id，通过npu-smi info -m命令查出的Chip ID即为芯片id。

●针对Atlas 350 加速卡，在安装AI处理器的服务器执行npu-smi info -t board -iid命令进行查询，获取Chip Name和NPU Name信息，实际配置值为ChipName_NPU Name。例如Chip Name取值为Ascendxxx，NPU Name取值为1234，实际配置值为Ascendxxx_1234。

其中，id为设备id，通过npu-smi info -l命令查出的NPU ID即为设备id。

约束说明

无

调用示例

ge::graphStatus TilingXXX(gert::TilingContext* context) {    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());    auto socVersion = ascendcPlatform.GetSocVersion();    // 根据所获得的版本型号自行设计Tiling策略    // ASCENDXXX请替换为实际的版本型号    if (socVersion == platform_ascendc::SocVersion::ASCENDXXX) {        // ...    }    return ret;}

## 6.4.2.1.5 GetCurNpuArch

功能说明

获取当前硬件平台芯片架构版本号。

函数原型

```cpp
NpuArch GetCurNpuArch(void) const
```
