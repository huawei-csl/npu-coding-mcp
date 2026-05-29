# aclrtcGetCompileLog

> **Section**: 6.4.8.8  
> **PDF Pages**: 3877–3877  

---

<!-- page 3877 -->

参数说明

表6-1972接口参数说明

参数名输入/输出描述

prog输入运行时编译程序的句柄。

logSizeRet输出编译日志的长度。

返回值说明

aclError为int类型变量，详细说明请参考6.4.8.9 RTC错误码。

约束说明

无

调用示例

```cpp
aclrtcProg prog;size_t logSize;aclError result = aclrtcGetCompileLogSize(prog, &logSize);
```

## 6.4.8.8 aclrtcGetCompileLog

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

获取编译日志的内容，以字符串形式保存。

函数原型

```cpp
aclError aclrtcGetCompileLog(aclrtcProg prog, char *log)
```
