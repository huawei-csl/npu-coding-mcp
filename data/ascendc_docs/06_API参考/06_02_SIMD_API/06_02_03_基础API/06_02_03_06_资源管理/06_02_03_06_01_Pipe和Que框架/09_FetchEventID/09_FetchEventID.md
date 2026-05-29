# FetchEventID

> **Section**: 9  
> **PDF Pages**: 1743–1743  

---

<!-- page 1743 -->

返回值说明

无

调用示例

AscendC::TEventID eventID = GetTPipePtr()->AllocEventID<AscendC::HardEvent::V_S>(); //需要插入scalar等vector的同步，申请对应的HardEvent的IDAscendC::SetFlag<AscendC::HardEvent::V_S>(eventID);..................AscendC::WaitFlag<AscendC::HardEvent::V_S>(eventID);GetTPipePtr()->ReleaseEventID<AscendC::HardEvent::V_S>(eventID); //释放scalar等vector的同步HardEvent的ID......

## ?.9. FetchEventID

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

根据HardEvent（硬件类型的同步事件）获取相应可用的TEventID，此接口不会申请TEventID，仅提供可用的TEventID。

函数原型

```cpp
template <HardEvent evt>__aicore__ inline TEventID FetchEventID()__aicore__ inline TEventID FetchEventID(HardEvent evt)
```

参数说明

参数名输入/输出

含义

evt输入HardEvent类型，硬件同步类型。

该类型的具体说明请参考 SetFlag/WaitFlag(ISASI)中同步类型的说明。
