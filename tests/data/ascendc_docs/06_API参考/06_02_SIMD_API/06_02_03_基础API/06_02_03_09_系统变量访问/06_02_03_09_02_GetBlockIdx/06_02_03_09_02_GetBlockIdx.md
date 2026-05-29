# GetBlockIdx

> **Section**: 6.2.3.9.2  
> **PDF Pages**: 1865–1865  

---

<!-- page 1865 -->

函数原型

```cpp
__aicore__ inline int64_t GetBlockNum()
```

参数说明

无

返回值说明

当前任务配置的核数。

约束说明

无。

调用示例

// srcGm、dstGm为外部输入的gm空间AscendC::GlobalTensor<float> srcGlobal;AscendC::GlobalTensor<float> dstGlobal;blockNum = AscendC::GetBlockNum(); // 获取核总数perBlockSize = srcDataSize / blockNum; // 每个核平分处理相同个数blockIdx = AscendC::GetBlockIdx(); // 获取当前工作的核IDsrcGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ float*>(srcGm + blockIdx * perBlockSize * sizeof(float)), perBlockSize);    // 分配每个核上的srcGlobal的内存地址dstGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ float*>(dstGm + blockIdx * perBlockSize * sizeof(float)), perBlockSize);    // 分配每个核上的dstGlobal的内存地址

## 6.2.3.9.2 GetBlockIdx

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

获取当前核的index，用于代码内部的多核逻辑控制及多核偏移量计算等。

函数原型

```cpp
__aicore__ inline int64_t GetBlockIdx()
```
