# aclrtcGetBinDataSize

> **Section**: 6.4.8.6  
> **PDF Pages**: 3875–3875  

---

<!-- page 3875 -->

参数说明

表6-1970接口参数说明

参数名输入/输出描述

prog输入运行时编译程序的句柄。

binData输出编译得到的Device侧二进制数据。

返回值说明

aclError为int类型变量，详细说明请参考6.4.8.9 RTC错误码。

约束说明

无

调用示例

```cpp
aclrtcProg prog;char binData[32] = "some bin data ...";aclError result = aclrtcGetBinData(prog, binData);
```

## 6.4.8.6 aclrtcGetBinDataSize

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

获取编译的二进制数据大小。用于在aclrtcGetBinData获取二进制数据时分配对应大小的内存空间。

函数原型

```cpp
aclError aclrtcGetBinDataSize(aclrtcProg prog, size_t *binDataSizeRet)
```
