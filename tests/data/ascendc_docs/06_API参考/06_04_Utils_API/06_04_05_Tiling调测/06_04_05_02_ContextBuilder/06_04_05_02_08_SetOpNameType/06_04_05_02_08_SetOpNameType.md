# SetOpNameType

> **Section**: 6.4.5.2.8  
> **PDF Pages**: 3848–3848  

---

<!-- page 3848 -->

## 6.4.5.2.8 SetOpNameType

功能说明

设置算子的名字与类型

函数原型

```cpp
ContextBuilder &SetOpNameType(const std::string& opName, const std::string& opType)
```

参数说明

参数输入/输出说明

opName输入算子名字

opType输入算子类型

返回值说明

当前ContextBuilder的对象。

约束说明

无

调用示例

```cpp
std::string opName = "tmpNode";std::string opType = "FlashAttentionScore";context_ascendc::ContextBuilder builder;(void)builder.SetOpNameType(opName, opType);
```

## 6.4.5.2.9 IrInstanceNum

功能说明

基于算子的IR定义，声明实例化时每种输入的实际个数。

函数原型

```cpp
ContextBuilder &IrInstanceNum(std::vector<uint32_t> instanceNum)
```

参数说明

参数输入/输出说明

instanceNum

输入基于算子IR原型定义，按照输入的index顺序声明实例化个数。
