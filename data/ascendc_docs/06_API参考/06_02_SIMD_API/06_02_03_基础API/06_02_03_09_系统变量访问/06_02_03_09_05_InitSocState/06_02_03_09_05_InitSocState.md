# InitSocState

> **Section**: 6.2.3.9.5  
> **PDF Pages**: 1868–1868  

---

<!-- page 1868 -->

函数原型

```cpp
__aicore__ inline void GetArchVersion(uint32_t& coreVersion)
```

参数说明

参数名输入/输出描述

coreVersion输出AI处理器架构版本

数据类型：uint32_t

返回值说明

无

约束说明

在调用GetArchVersion接口前，需先定义coreVersion ，调用GetArchVersion接口后coreVersion会变成相对应架构版本号的值。

由于硬件约束，在查看转换后的AI处理器架构版本号时需要将其打印成十六进制的数或者自行转换成十六进制的数。

调用示例

如下样例通过调用GetArchVersion接口获取AI处理器架构版本号。    uint32_t coreVersion = 0;//定义AI处理器版本    AscendC::GetArchVersion(coreVersion);    AscendC::PRINTF("core version is %x", coreVersion);//需用%x将其打印成十六进制的数

不同型号服务器有不同的架构版本号取值，如下表所示：

架构版本号型号

200Atlas 推理系列产品AI Core

220Atlas A2 训练系列产品/Atlas A2 推理系列产品

Atlas A3 训练系列产品/Atlas A3 推理系列产品

Atlas 350 加速卡

暂未正式确定，请以最终商发版本说明为准。

## 6.2.3.9.5 InitSocState

产品支持情况

产品是否支持

Atlas 350 加速卡√
