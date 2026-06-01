# Host 和 Device 异构并行

> **Section**: 3.3.1


CCE Host 和 Device 异构并行系统，主要包含两个特征：

- Host 函数和 Kernel 函数是异步执行模式，可以通过 aclrtSynchronizeStream API 进 行同步。
- Kernel 函数也可以通过多 Stream 进行并发执行。详细请参见' Runtime 运行时 API &gt; Stream 管理'。
