# CheckLocalMemoryIA(ISASI)

> **Section**: 6.2.3.11.2.4  
> **PDF Pages**: 1918–1919  

---

<!-- page 1918 -->

返回值说明

无

约束说明

无。

调用示例

AscendC::LocalTensor<half> src0Local;AscendC::LocalTensor<half> src1Local;AscendC::LocalTensor<half> dstLocal;constexpr int32_t count = 512;    // 参与计算的元素个数if (src1Local[0] == 0) {    // 如果除数为0，则报异常    AscendC::Trap();} else {    AscendC::Divs(dstLocal, src0Local, src1Local[0], 512);}

## 6.2.3.11.2.4 CheckLocalMemoryIA(ISASI)

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

check设定范围内的UB读写行为，如果有设定范围的读写行为则会出现EXCEPTION报错，无设定范围的读写行为则不会报错。

函数原型

```cpp
__aicore__ inline void CheckLocalMemoryIA(const CheckLocalMemoryIAParam& checkParams)
```

<!-- page 1919 -->

参数说明

表6-779参数说明

参数名称输入/输出含义

checkParams输入用于配置对UB访问的检查行为，类型为CheckLocalMemoryIAParam。

具体定义请参考${INSTALL_DIR}/include/ascendc/basic_api/interface/kernel_struct_mm.h，${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。

参数说明请参考表6-780。

表6-780 CheckLocalMemoryIAParam 结构体内参数说明

参数名称含义

enableBit配置的异常寄存器，取值范围：enableBit∈[0,3]，默认为0。

●0：异常寄存器0。

●1：异常寄存器1。

●2：异常寄存器2。

●3：异常寄存器3。

startAddrCheck的起始地址，32B对齐，取值范围：startAddr∈[0, 65535]，默认值为0。比如，可通过LocalTensor.GetPhyAddr()/32来获取startAddr。

endAddrCheck的结束地址，32B对齐，取值范围：endAddr∈[0, 65535] 。默认值为0。

isScalarRead

Check标量读访问。

●false：不开启，默认为false。

●true：开启。

isScalarWrite

Check标量写访问。

●false：不开启，默认为false。

●true：开启。

isVectorRead

Check矢量读访问。

●false：不开启，默认为false。

●true：开启。

isVectorWrite

Check矢量写访问。

●false：不开启，默认为false。

●true：开启。
