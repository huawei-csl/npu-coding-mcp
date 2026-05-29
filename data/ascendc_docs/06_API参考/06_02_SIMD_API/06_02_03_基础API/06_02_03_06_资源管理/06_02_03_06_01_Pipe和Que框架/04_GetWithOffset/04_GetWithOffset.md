# GetWithOffset

> **Section**: 4  
> **PDF Pages**: 1809–1809  

---

<!-- page 1809 -->

约束说明

len的数值是Tensor中元素的个数，len*sizeof(T)不能超过TBuf初始化时的长度。

返回值说明

获取到的LocalTensor。

调用示例

// 为TBuf初始化分配内存，分配内存长度为1024字节AscendC::TPipe pipe;AscendC::TBuf<AscendC::TPosition::VECCALC> calcBuf; // 模板参数为TPosition中的VECCALC类型uint32_t byteLen = 1024;pipe.InitBuffer(calcBuf, byteLen);// 从calcBuf获取Tensor,Tensor为pipe分配的所有内存大小，为1024字节AscendC::LocalTensor<int32_t> tempTensor1 = calcBuf.Get<int32_t>();// 从calcBuf获取Tensor,Tensor为128个int32_t类型元素的内存大小，为512字节AscendC::LocalTensor<int32_t> tempTensor2 = calcBuf.Get<int32_t>(128);

对同一个TBuf对象连续调用Get接口，获取到的Tensor首地址是相同的，不会依次向后偏移。如果需要获取偏移之后的Tensor，可以使用如下方法：

AscendC::TPipe pipe;// 模板参数为TPosition中的VECCALC类型AscendC::TBuf<AscendC::TPosition::VECCALC> calcBuf; // 分配一个2048字节的连续空间uint32_t byteLen = 2048;pipe.InitBuffer(calcBuf, byteLen);// 从calcBuf获取tensor1，tensor1为pipe分配的所有内存大小，为2048字节AscendC::LocalTensor<int32_t> tensor1 = calcBuf.Get<int32_t>();// 用户指定tensor1的第256个int32_t的偏移位置为tensor2的首地址，实际上tensor2可以使用的内存大小为1024字节，两个tensor首地址相差256 * sizeof(int32_t)字节auto tensor2 = tensor1[256];

## ?.4. GetWithOffset

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

以TBuf为基地址，向后偏移指定长度，将偏移后的地址作为起始地址，提取长度为指定值的Tensor。
