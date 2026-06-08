# acldumpType

> **Section**: 1.28.8


```
enum acldumpType { AIC_ERR_BRIEF_DUMP = 1,         // 轻量化 exception dump AIC_ERR_NORM_DUMP = 2,          // 普通 exception dump ，在轻量化 exception dump 基础上，还会导出 Shape 、 Data Type 、 Format 以及属性信息 AIC_ERR_DETAIL_DUMP = 3,        // 在轻量化 exception dump 基础上，还会导出 AI Core 的内部存储、寄存器 以及调用栈信息 DATA_DUMP = 4,                  // 模型 Dump 配置、单算子 Dump 配置 OVERFLOW_DUMP = 5               // 溢出算子 Dump };
```
