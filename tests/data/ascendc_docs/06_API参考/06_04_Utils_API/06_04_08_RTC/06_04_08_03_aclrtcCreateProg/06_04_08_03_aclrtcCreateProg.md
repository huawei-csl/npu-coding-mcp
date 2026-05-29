# aclrtcCreateProg

> **Section**: 6.4.8.3  
> **PDF Pages**: 3871–3872  

---

<!-- page 3871 -->

功能说明

编译接口，编译指定的程序。

函数原型

```cpp
aclError aclrtcCompileProg(aclrtcProg prog, int numOptions, const char **options)
```

参数说明

表6-1967接口参数说明

参数名输入/输出描述

prog输入运行时编译程序的句柄。

numOptions

输入编译选项数量。

options输入编译选项数组，保存具体的编译选项（默认添加-std=c++17）。

支持的编译选项可以参考《毕昇编译器》。

返回值说明

aclError为int类型变量，详细说明请参考6.4.8.9 RTC错误码。

约束说明

无

调用示例

```cpp
aclrtcProg prog;const char *options[] = {"--npu-arch=dav-2201"};int numOptions = sizeof(options) / sizeof(options[0]);aclError result = aclrtcCompileProg(prog, numOptions, options);
```

## 6.4.8.3 aclrtcCreateProg

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

<!-- page 3872 -->

产品是否支持

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

通过给定的参数，创建编译程序的实例。

函数原型

```cpp
aclError aclrtcCreateProg(aclrtcProg *prog, const char *src, const char *name, int numHeaders, const char **headers, const char **includeNames)
```

参数说明

表6-1968接口参数说明

参数名输入/输出描述

prog输出运行时编译程序的句柄。

src输入以字符串形式提供的Ascend C Device侧源代码内容。

name输入用户自定义的程序名称，用于标识和区分不同的编译程序，默认值为"default_program"。

numHeaders

输入指定要包含的头文件数量，必须为非负整数。

无需包含头文件或者Ascend C Device侧源代码中已包含所需头文件时，此参数需设置为0。

headers输入一个指向数组的指针，数组中的每个元素都是以'\0'结尾的字符串，表示头文件的源代码内容。当numHeaders为0时，此参数可以设置为nullptr。

includeNames

输入一个指向数组的指针，数组中的每个元素都是以'\0'结尾的字符串，表示头文件的名称。

这些名称必须与源代码中#include指令中包含的头文件名称完全一致。

返回值说明

aclError为int类型变量，详细说明请参考6.4.8.9 RTC错误码。

约束说明

无

调用示例

```cpp
aclrtcProg prog;const char *src = R""""(
```
