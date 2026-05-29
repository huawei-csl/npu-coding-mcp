# CreateCubeResGroup

> **Section**: 6.2.3.12.1.3  
> **PDF Pages**: 1938–1938  

---

<!-- page 1938 -->

## 6.2.3.12.1.3 CreateCubeResGroup

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品x

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Corex

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x

功能说明

快速创建CubeResGroupHandle对象，内部完成消息队列空间和同步事件分配。推荐使用该接口，避免使用CubeResGroupHandle的构造函数创建对象，出现不同对象的消息队列空间冲突、同步事件错误等情况。

函数原型

```cpp
template <int groupID, class MatmulApiType, template <class, class> class CallBack, typename CubeMsgType>__aicore__ inline CubeResGroupHandle<CubeMsgType> CreateCubeResGroup(KfcWorkspace& desc, uint8_t blockStart, uint8_t blockSize, uint8_t msgQueueSize, GM_ADDR tiling)
```

参数说明

表6-787模板参数说明

参数说明

groupID用于表示Group的编号，int32取值范围。

MatmulApiType

定义的AIC计算对象类型。

CallBack回调函数类，需要实现Init和Call两个接口。

CubeMsgType

用户自定义的消息结构体。
