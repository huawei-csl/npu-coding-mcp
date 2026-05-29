# 纯搬运类算子VECIN和VECOUT建议复用

> **Section**: 3.8.5.9  
> **PDF Pages**: 598–599  

---

<!-- page 598 -->

pipe.InitBuffer(tmpSoftmaxBuf, softmaxBufSize * sizeof(uint8_t));  // 单独分配Softmax的临时Buf 32KBTBuf<TPosition::VECCALC> tmpSumBuf;pipe.InitBuffer(tmpSumBuf, sumBufSize * sizeof(T)); // 单独分配Add的临时Buf，且softmaxBufSize * sizeof(uint8_t) + sumBufSize * sizeof(T) <= 64KB...for (int i = 0; i < 16; i++) {    ...    LocalTensor<uint8_t> tmpSoftmaxTensor = tmpSoftmaxBuf.Get<uint8_t>(softmaxBufSize);    SoftMax<T, true, true>(dstTensor, expSumTensor, dstMaxTensor, srcTensor, tmpSoftmaxTensor, tiling);    ...    DataCopy(src0Tensor, src0Gm[i * blockLen / sizeof(T)], Params);    ...    LocalTensor<T> tmpSumTensor = tmpSumBuf.Get<T>(sumBufSize);    Add<T>(tmpSumTensor, src0Tensor, src1Tensor, count);    ...}...

【正例】

SoftMax高阶API计算需要临时Buffer空间，算子在进行其他计算时可以共享此临时Buffer，按照上述假设只需要搬运512 / 64 = 8次。

...constexpr int32_t blockLen = 64 * 1024;TBuf<TPosition::VECCALC> tmpSharedBuf;pipe.InitBuffer(tmpSharedBuf, bufferSize); // 共享分配bufferSize = MAX(softmaxBufSize * sizeof(uint8_t), sumBufSize * sizeof(T)) <= 64KB...for (int i = 0; i < 8; i++) {    ...    LocalTensor<uint8_t> tmpSharedTensor = tmpSharedBuf.Get<uint8_t>(softmaxBufSize);    SoftMax<T, true, true>(dstTensor, expSumTensor, dstMaxTensor, srcTensor, tmpSharedTensor, tiling);    ...    DataCopy(src0Tensor, src0Gm[i * blockLen / sizeof(T)], Params);    ...    LocalTensor<T> tmpSumTensor = tmpSharedBuf.Get<T>(sumBufSize);    Add<T>(tmpSumTensor, src0Tensor, src1Tensor, count);    ...}...

## 3.8.5.9 纯搬运类算子VECIN 和VECOUT 建议复用

【优先级】高

【描述】纯搬运类算子在执行时并不涉及实际vector计算，若存在冗余的vector指令，会导致算子整体执行时间变长。这种场景可以使用Ascend C针对纯搬运类算子提供的TQueBind接口，该接口可以将VECIN与VECOUT绑定，省略将数据从VECIN拷贝到VECOUT的步骤，从而避免vector的无谓消耗。

【反例】

此段代码为了保证数据搬入和数据搬出之间的流水同步，存在LocalTensor ->LocalTensor的DataCopy指令。template <typename ComputeT> class KernelExample { public:     ...     __aicore__ inline void Process(...)     {         for (int i = 0; i < iLen; ++i) {             ...              auto iLocal = QueI.AllocTensor<ComputeT>();             DataCopy(iLocal, inGm[i * 32], size);             QueI.EnQue(iLocal);             iLocal = QueI.DeQue<ComputeT>();             for (int j = 0; j < jLen; ++j) {

<!-- page 599 -->

...                 auto oLocal = QueO.AllocTensor<ComputeT>();                 DataCopy(oLocal, iLocal, size); // LocalTensor -> LocalTensor的DataCopy指令,以实现数据从VECIN到VECOUT的搬运                 QueO.EnQue(oLocal);

```cpp
auto oLocal = QueO.DeQue<ComputeT>();
                 DataCopyPad(outGm[j], oLocal, ...);
                 QueO.FreeTensor(oLocal);             }             QueI.FreeTensor(iLocal);         }     }
private:     ...      TQue<TPosition::VECIN, BUFFER_NUM> QueI;
     TQue<TPosition::VECOUT, BUFFER_NUM> QueO;     ... };
extern "C" __global__ __aicore__ void example_kernel(...) {     ...     op.Process(...); }
```

【正例】

将LocalTensor -> LocalTensor的DataCopy指令替换为TQueBind接口，减少将VECIN拷贝到VECOUT的步骤，从而避免了冗余拷贝。

```cpp
template <typename ComputeT> class KernelExample { public:     ...     __aicore__ inline void Process(...)     {         for (int i = 0;
 i < iLen; ++i) {             ...              auto bindLocal = queBind.AllocTensor<ComputeT>();
             DataCopy(bindLocal, inGm[i * 32], size);
             queBind.EnQue(bindLocal);
             bindLocal = queBind.DeQue<ComputeT>();
             for (int j = 0;
 j < jlen; ++j) {                 ...                 DataCopyPad(outGm[j], bindLocal, ...);             }             queBind.FreeTensor(bindLocal);         }     }
```

private:     ...      TQueBind<TPosition::VECIN, TPosition::VECOUT, BUFFER_NUM> queBind; // 使用TQueBind替换原来的QueI，QueO     ... };

```cpp
extern "C" __global__ __aicore__ void example_kernel(...) {     ...     op.Process(...); }
```

【性能对比】
