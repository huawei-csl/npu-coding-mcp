# REGIST_MATMUL_OBJ

> **Section**: 6.2.4.2.1.13  
> **PDF Pages**: 2339–2339  

---

<!-- page 2339 -->

## 6.2.4.2.1.13 REGIST_MATMUL_OBJ

功能说明

初始化Matmul对象。

函数原型

```cpp
REGIST_MATMUL_OBJ(tpipe, workspace, ...)
```

参数说明

表6-1036参数说明

参数名输入/输出

描述

tpipe输入Tpipe对象。

workspace

输入系统workspace指针。

...输入可变参数，传入Matmul对象和与之对应的Tiling结构，要求Tiling结构的数据类型为TCubeTiling结构。

Tiling参数可以通过Host侧 GetTiling接口获取，并传递到kernel侧使用。

返回值说明

无

约束说明

●在分离模式中，本接口必须在InitBuffer接口前调用。

●在程序中，最多支持定义4个Matmul对象。

●当代码中只有一个Matmul对象时，本接口可以不传入tiling参数，通过Init接口单独传入tiling参数。

●当代码中有多个Matmul对象时，必须满足Matmul对象与其tiling参数一一对应，依次传入，具体方式请参考调用示例。

●在分离模式中，调用本接口后，AIC核仅会执行下述AIV核发起的接口，其他接口不会在AIC核执行：

–Matmul Kernel侧接口。

–基础数据搬运和随路转换ND2NZ搬运接口，仅支持数据通路为GM -> A1、B1的数据搬运。

调用示例

Tpipe pipe;// 推荐：初始化单个matmul对象，传入tiling参数REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);// 推荐：初始化多个matmul对象，传入对应的tiling参数
