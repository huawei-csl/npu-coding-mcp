# OpkernelLib

> **Section**: 6.4.3.7.5  
> **PDF Pages**: 3819–3819  

---

<!-- page 3819 -->

## 6.4.3.7.5 OpkernelLib

功能说明

配置算子调用的kernelLib，AICPU自定义算子调用的kernelLib固定为“CUSTAICPUKernel”。

函数原型

```cpp
OpAICPUDef &OpkernelLib(const char *value)
```

参数说明

参数输入/输出说明

value输入kernelLib值，算子调用的kernelLib固定为“CUSTAICPUKernel。

返回值说明

OpAICPUDef算子定义，OpAICPUDef请参考6.4.3.7 OpAICPUDef。

约束说明

无

## 6.4.3.7.6 KernelSo

功能说明

配置AICPU算子实现文件编译生成的动态库文件的名称。

函数原型

```cpp
OpAICPUDef &KernelSo(const char *value)
```

参数说明

参数输入/输出说明

value输入AI CPU算子实现文件编译生成的动态库文件的名称。

返回值说明

OpAICPUDef算子定义，OpAICPUDef请参考6.4.3.7 OpAICPUDef。

约束说明

无
