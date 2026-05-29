# GetDataBlockSizeInBytes

> **Section**: 6.2.3.9.3  
> **PDF Pages**: 1866–1866  

---

<!-- page 1866 -->

参数说明

无

返回值说明

GetBlockIdx返回当前核的索引，index的范围为[0, 用户配置的NumBlocks数量)。

同时启动AIC和AIV的场景：

当AIC和AIV比例为1:2时，AIC上取值范围为[0, 用户配置的NumBlocks数量), AIV上取值范围为[0, 2 * 用户配置的NumBlocks数量)；

当AIC和AIV比例为1:1时，AIC上取值范围为[0, 用户配置的NumBlocks数量)，AIV上取值范围为[0, 用户配置的NumBlocks数量)。

约束说明

GetBlockIdx为一个系统内置函数，返回当前核的index。

调用示例

// srcGm、dstGm为外部输入的gm空间AscendC::GlobalTensor<float> srcGlobal;AscendC::GlobalTensor<float> dstGlobal;blockNum = AscendC::GetBlockNum(); // 获取核总数perBlockSize = srcDataSize / blockNum; // 每个核平分处理相同个数blockIdx = AscendC::GetBlockIdx(); // 获取当前工作的核IDsrcGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ float*>(srcGm + blockIdx * perBlockSize * sizeof(float)), perBlockSize);    // 分配每个核上的srcGlobal的内存地址dstGlobal.SetGlobalBuffer(reinterpret_cast<__gm__ float*>(dstGm + blockIdx * perBlockSize * sizeof(float)), perBlockSize);    // 分配每个核上的dstGlobal的内存地址

## 6.2.3.9.3 GetDataBlockSizeInBytes

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品√

功能说明

获取当前芯片版本一个datablock的大小，单位为byte。开发者根据datablock的大小来计算API指令中待传入的repeatTime 、DataBlock Stride、Repeat Stride等参数值。
