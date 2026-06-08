# aclmdlRICaptureThreadExchangeMode

> **Section**: 1.17.3


须知：本接口为试验特性，后续版本可能会存在变更，不支持应用于商用产品中。

## 产品支持情况

## 功能说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

切换当前线程的捕获模式。

调用本接口会将调用线程的捕获模式设置为 *mode 中包含的值，并通过 *mode 返回该 线程之前设置的模式。

建议在 aclmdlRICaptureBegin 和 aclmdlRICaptureEnd 接口之间调用本接口切换当前 线程的模式。各捕获模式的配置说明如下，说明中的其它线程指'没有调用 aclmdlRICaptureBegin 接口、不在捕获状态'的线程。

- 若 aclmdlRICaptureBegin 接口将捕获模式设置为 ACL\_MODEL\_RI\_CAPTURE\_MODE\_RELAXED （下文简称 RELAXED 模式），表示 所有线程都可以调用非安全函数，这时即使在其它线程（指不在捕获状态的线

## 函数原型

## 参数说明

## 返回值说明

## 接口调用示例

- 程）中调用本接口将捕获模式设置为其它值也不会生效，其它线程还是按照 RELAXED 模式。
- 若 aclmdlRICaptureBegin 接口将捕获模式设置为
- ACL\_MODEL\_RI\_CAPTURE\_MODE\_THREAD\_LOCAL （下文简称 THREAD\_LOCAL 模式），表示当前线程禁止调用非安全函数，但其它线程可以调用非安全函数。 如果本线程要调用非安全函数，需调用本接口将当前线程模式切换为 RELAXED 模 式。
- 若 aclmdlRICaptureBegin 接口将捕获模式设置为 ACL\_MODEL\_RI\_CAPTURE\_MODE\_GLOBAL （下文简称 GLOBAL 模式），表示所 有线程都不可以调用非安全函数。本线程若要调用非安全函数，需调用本接口切 换为 RELAXED 模式，其它线程若要调用非安全函数，需调用本接口切换为 RELAXED 模式或 THREAD\_LOCAL 模式。

aclError aclmdlRICaptureThreadExchangeMode(aclmdlRICaptureMode *mode)

| 参数名   | 输入 / 输出   | 说明                                                                                                                                                    |
|-------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| mode  | 输入 & 输 出  | 捕获模式，用于限制非安全函数（包括 aclrtMemset 、 aclrtMemcpy 、 aclrtMemcpy2d 以及使用非 Host 锁页内存 进行异步内存复制操作的接口，如 aclrtMemcpyAsync 接 口）的作用范围。 类型定义请参见 aclmdlRICaptureMode 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

接口调用示例，参见单流捕获。
