# aclmdlRICaptureBegin

> **Section**: 1.17.1


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

## 功能说明

## 函数原型

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

开始捕获 Stream 上下发的任务。

在 aclmdlRICaptureBegin 和 aclmdlRICaptureEnd 接口之间，所有在指定 Stream 上下 发的任务不会立即执行，而是被暂存在系统内部模型运行实例中，只有在调用 aclmdlRIExecute 或 aclmdlRIExecuteAsync 接口执行模型时，这些任务才会被真正执 行，以此减少 Host 侧的任务下发开销。所有任务执行完毕后，若无需再使用内部模 型，可调用 aclmdlRIDestroy 接口及时销毁该资源。

aclmdlRICaptureBegin 和 aclmdlRICaptureEnd 接口要成对使用，且两个接口中的 Stream 应相同。在这两个接口之间，可以调用 aclmdlRICaptureGetInfo 接口获取捕 获信息，调用 aclmdlRICaptureThreadExchangeMode 接口切换当前线程的捕获模 式。此外，在调用 aclmdlRICaptureEnd 接口之后，还可以调用 aclmdlRIDebugPrint 接口打印模型信息，这在维护和测试场景下有助于问题定位。

在 aclmdlRICaptureBegin 和 aclmdlRICaptureEnd 接口之间捕获的任务，若要更新任 务（包含任务本身以及任务的参数信息），则需在 aclmdlRICaptureTaskGrpBegin 、 aclmdlRICaptureTaskGrpEnd 接口之间下发后续可能更新的任务，给任务打上任务组 的标记，然后在 aclmdlRICaptureTaskUpdateBegin 、 aclmdlRICaptureTaskUpdateEnd 接口之间更新任务的输入信息。

在 aclmdlRICaptureBegin 和 aclmdlRICaptureEnd 接口之间捕获到的任务会暂存在系 统内部模型运行实例中，随着任务数量的增加，以及通过 Event 推导、内部任务的操 作，导致更多的 Stream 进入捕获状态， Stream 资源被不断消耗，最终可能会导致并发 的调度资源不足，因此需提前规划好调度资源的使用。

aclError aclmdlRICaptureBegin(aclrtStream stream, aclmdlRICaptureMode mode)

## 参数说明

## 返回值说明

## 接口调用示例

| 参数名    | 输入 / 输出   | 说明                                                                                                                                                    |
|--------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| stream | 输入        | 指定 Stream 。类型定义请参见 aclrtStream 。                                                                                                                      |
| mode   | 输入        | 捕获模式，用于限制非安全函数（包括 aclrtMemset 、 aclrtMemcpy 、 aclrtMemcpy2d 以及使用非 Host 锁页内存 进行异步内存复制操作的接口，如 aclrtMemcpyAsync 接 口）的作用范围。 类型定义请参见 aclmdlRICaptureMode 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见单流捕获。
