# GetBaseAddr

> **Section**: 10  
> **PDF Pages**: 1744–1744  

---

<!-- page 1744 -->

约束说明

相比于 AllocEventID，FetchEventID适用于临时使用ID的场景，获取ID后，不会对ID进行占用。在一些复杂的使用场景下，需要开发者自行保证使用正确。比如相同流水连续调用SetFlag/WaitFlag，如果两次传入的ID都是使用FetchEventID获取的，因为两者ID相同会出现程序卡死等未定义行为，这时推荐用户使用AllocEventID。

返回值说明

TEventID

调用示例

AscendC::TEventID eventIdVToS = GetTPipePtr()->FetchEventID(AscendC::HardEvent::V_S); //需要插scalar等vector的同步，申请对应的HardEvent的IDAscendC::SetFlag<AscendC::HardEvent::V_S>(eventIdVToS);AscendC::WaitFlag<AscendC::HardEvent::V_S>(eventIdVToS);

## ?.10. GetBaseAddr

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

根据传入的logicPos（逻辑抽象位置），获取该位置的基础地址，只在CPU调试场景下此接口生效。通常用于计算Tensor在logicPos的偏移地址即Tensor地址减去GetBaseAddr返回值。

函数原型

```cpp
inline uint8_t* GetBaseAddr(int8_t logicPos)
```
