# TQueBind构造函数

> **Section**: 2  
> **PDF Pages**: 1791–1791  

---

<!-- page 1791 -->

表6-697模板参数说明

参数名描述

src源逻辑位置，支持的TPosition可以为VECIN、VECOUT、A1、A2、B1、B2、CO1、CO2。关于TPosition的具体介绍请参考6.2.6.7 TPosition。支持的src和dst组合请参考表6-696。

dst目的逻辑位置，TPosition可以为VECIN、VECOUT、A1、A2、B1、B2、CO1、CO2。

depthTQue的深度，一般不超过4。

mask如果用户在某一个Que上，数据搬运的时候需要做转换，可以设置为0或1。一般不需要用户配置，默认为0。

设置为0，代表数据格式从ND转换为NZ，目前仅支持TPosition为A1或B1。

## ?.2. TQueBind 构造函数

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

创建TQueBind对象。

函数原型

```cpp
__aicore__ inline TQueBind()
```

参数说明

无

约束说明

无
