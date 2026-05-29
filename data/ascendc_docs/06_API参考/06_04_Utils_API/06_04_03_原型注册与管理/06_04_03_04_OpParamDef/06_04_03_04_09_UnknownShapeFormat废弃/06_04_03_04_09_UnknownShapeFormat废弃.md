# UnknownShapeFormat（废弃）

> **Section**: 6.4.3.4.9  
> **PDF Pages**: 3796–3796  

---

<!-- page 3796 -->

## 6.4.3.4.9 UnknownShapeFormat（废弃）

功能说明

须知

●该接口废弃，并将在后续版本移除，请不要使用该接口。无需针对动态/静态shape单独设置format，统一使用Format接口来设置即可。

●如果开发者使用了该接口，并开启-Werror -Wall编译选项开启所有警告当做错误处理，会有编译报错。此时可以通过添加-Wno-deprecated编译选项来消除，但是存在后续接口在版本中移除后编译报错的风险，建议不要使用该接口，统一使用Format接口来设置。

编译选项加在自定义算子工程目录下op_host/CMakeLists.txt中的cust_optiling、cust_opproto编译target上，样例如下：

```cpp
target_compile_options(cust_optiling PRIVATE        -Wno-deprecated)
```

未知Shape情况下的Format的默认值。

函数原型

```cpp
OpParamDef &UnknownShapeFormat(std::vector<ge::Format> formats)
```

参数说明

参数输入/输出说明

formats输入算子参数数据格式。

返回值说明

OpDef算子定义，OpDef请参考6.4.3.3 OpDef。

约束说明

无

## 6.4.3.4.10 ValueDepend

功能说明

标识该输入是否为“数据依赖输入”，数据依赖输入是指在Tiling/InferShape等函数实现时依赖该输入的具体数据。该输入数据为host侧数据，开发者在Tiling函数/InferShape函数中可以通过TilingContext类的GetInputTensor/InferShapeContext类的GetInputTensor获取这个输入数据。
