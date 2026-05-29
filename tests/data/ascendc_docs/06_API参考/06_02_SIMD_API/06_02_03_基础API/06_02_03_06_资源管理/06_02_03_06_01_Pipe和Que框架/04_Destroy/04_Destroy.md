# Destroy

> **Section**: 4  
> **PDF Pages**: 1736–1736  

---

<!-- page 1736 -->

// 第一次执行流程：使用pipeIn管道AscendC::TPipe pipeIn;pipeIn.Init();  // 初始化pipeIn管道资源op.Init(x, z, srcSize, &pipeIn);op.Process();pipeIn.Destroy();  // 销毁pipeIn管道资源

// 第二次执行流程：复用算子对象，但更换为pipeCast管道AscendC::TPipe pipeCast;pipeCast.Init();  // 初始化pipeCast管道资源op.Init(x, z, srcSize, &pipeCast);op.Process();pipeCast.Destroy();  // 销毁pipeCast管道资源

## ?.4. Destroy

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

释放资源。

函数原型

```cpp
__aicore__ inline void Destroy()
```

约束说明

用于重复申请释放tpipe，创建tpipe对象后，可调用Destroy手动释放资源。

返回值说明

无

调用示例

AscendC::TPipe pipe; // Pipe内存管理对象AscendC::TQue<AscendC::TPosition::VECOUT, 2> que; //输出数据Queue队列管理对象，TPosition为VECOUTuint8_t num = 2;uint32_t len = 128;pipe.InitBuffer(que, num, len);pipe.Destroy();
