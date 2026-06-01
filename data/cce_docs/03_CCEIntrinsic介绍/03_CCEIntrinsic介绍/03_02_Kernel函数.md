# Kernel 函数

> **Section**: 3.2


```
如异构编程 QuickStartDemoACL.cce 所示， Kernel 函数是由 __global__ 关键字标注的特 殊函数，是设备函数的入口，由 Host 侧通过特定的异构调用语法 <<<>>> 执行。一个 cce 文件可包含若干个 Kernel 函数， Host 代码既可以和 Device 代码共存于同一文件中， 也可以分开存放，基本符合常规 C++ 函数调用习惯。 // moduleA.cce // Kernel 函数 __global__ [aicore] void foo(/* Args */...) {} __global__ [aicore] void bar(/* Args */...) {} RetCode_t FooAPI(/* Args */ ...) { foo<<<blockDim, nullptr, stream>>>(...); } // moduleB.cce extern __global__ [aicore] void bar(/*Args*/ ...); extern RetCode_t FooAPI(...); int main() { bar<<<...>>>(...); FooAPI(...); }
```

## Kernel 函数（含设备侧函数）有以下使用约束：

- 不支持 Kernel 函数调用 Kernel 函数。
- 不支持递归调用。
- 不支持动态内存分配。
- 不支持 C++ 标准库。
- 不支持某些基础数据类型，如 double 。
- 部分支持 C++11 、 C++14 、 C++17 特性。
- AICore 运行环境不包含操作系统，简而言之，除了上述明确不支持的特性外，设 备侧编程也不支持依赖 OS 、 IO 、中断等相关的特性。
