# aclrtCacheLastTaskOpInfo

> **Section**: 1.27.10


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 接口调用流程

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

基于捕获方式构建模型运行实例场景下，把指定内存中的算子信息按照 infoSize 大小缓 存到当前线程中最后下发的任务上。

aclError aclrtCacheLastTaskOpInfo(const void * const infoPtr, const size\_t infoSize)

| 参数名      | 输入 / 输 出   | 说明                                 |
|----------|------------|------------------------------------|
| infoPtr  | 输入         | 缓存信息内存地址指针，此处是 Host 内存             |
| infoSize | 输入         | 缓存信息内存大小，取值范围： (0, 64K] ，单位 Byte 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

本接口需与以下其它关键接口配合使用，以便控制后续采集性能数据时附带算子信 息：

1. 调用 aclmdlRICaptureBegin 接口开始捕获任务。
2. 调用 aclrtSetStreamAttribute 接口开启算子信息缓存开关。
3. 下发算子执行任务，例如调用 aclrtLaunchKernelWithConfig 接口。
4. 调用 aclrtGetStreamAttribute 接口获取算子信息缓存开关是否开启。

## 功能说明

## 函数原型

## 参数说明

只有在捕获状态下，且通过 aclrtSetStreamAttribute 接口开启了算子信息缓存开 关，此处的 aclrtGetStreamAttribute 接口才能获取到算子信息缓存开关已开启的 状态，后续才可以缓存算子信息。

5. 调用 aclrtCacheLastTaskOpInfo 接口缓存算子信息。
6. 再次调用 aclrtSetStreamAttribute 接口关闭算子信息缓存开关。
7. 调用 aclmdlRICaptureEnd 接口结束任务捕获。
8. 开启采集性能数据（参见 1.21.1 Profiling 数据采集接口章节下的接口）后，调用 aclmdlRIExecuteAsync 接口执行推理。 在此过程中，采集的性能数据会附带算子信息。
9. 最后，调用 aclmdlRIDestroy 接口销毁模型运行实例时，算子缓存信息也会被一 并释放。
