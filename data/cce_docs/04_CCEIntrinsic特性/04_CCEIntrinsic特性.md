# CCE Intrinsic 特性

> **Section**: 4


\_\_global\_\_ 执行空间限定符声明一个 kernel 函数。该 kernel 函数有如下属性：

- 在设备上执行
- 只能被主机侧函数调用
- \_\_global\_\_ 只是表示这是设备侧函数的入口，并不表示具体的设备类型，具体的设 备类型由 [aicore] 标记。

## 注意

- \_\_global\_\_ 函数必须返回 void 类型，并且不能是 class 的成员函数。
- 主机侧可以使用 &lt;&lt;&lt;&gt;&gt;&gt; 直接进行 \_\_global\_\_ 函数异构调用。
- \_\_global\_\_ 的调用是异步的，函数返回并不表示 kernel 函数在设备侧已经执行完 成。如果需要同步，须使用 Runtime 提供的同步接口显式同步，如 aclrtSynchronizeStream(...) 。

AICore 执行空间限定符声明一个设备侧函数，它具有如下属性：

## host 限定符

- 在 AICore 设备上执行。
- 只能被 \_\_global\_\_ 函数，或者其他 aicore 函数调用。

## 代码示例：

```
// Only callable from device functions with same kind of execution space [aicore] void bar() {} // Define a kernel function execute on AICore device __global__ [aicore] void foo() { bar(); }
```

host 执行空间限定符声明一个主机侧函数，具有以下属性：

- 只能在主机侧执行
- 只能被主机侧函数调用
- \_\_global\_\_ 和 [host] 不能一起使用

## 注意事项：

- [host] 限定符是可选项，无函数执行空间限定符定义的函数，默认是 host 函数。
- 非 \_\_global\_\_ 函数可以同时被声明为 host 和 aicore 函数，编译器会为主机侧和设备 侧都生成代码。

## 代码示例：

```
[aicore] void f() {} // defines a host side function void foo() {} // defines a host side function [host] void bar() { f();     // Error. foo();   // OK. } // define a function executing on both host and aicore // it should be able to compile on both host and aicore // otherwise it will report compiler error [host, aicore] void tee() { f(); // Error. Function execution space does not match } // Error. __global__ [host] void kfunc() {} // Error. __global__ [host,aicore] void kfunc() {}
```
