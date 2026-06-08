# aclprofInit

> **Section**: 1.21.1.2


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

初始化 Profiling ，目前用于设置保存性能数据的文件的路径。

aclError aclprofInit(const char *profilerResultPath, size\_t length)

1 )--&gt; aclprofStart 接口 ( 指定 Device 1 和 Device 2)--&gt; 模型 1 加载 --&gt; 模型 1 执 行 --&gt; 模型 2 加载 --&gt; 模型 2 执行 --&gt; aclprofStop 接口 --&gt; aclprofStop 接口 --&gt; aclprofFinalize --&gt; 执行其它任务 --&gt; 模型卸载 --&gt; aclFinalize 接口

## 参数说明

## 返回值说明

## 约束说明

与 aclprofFinalize 接口配对使用，先调用 aclprofInit 接口再调用 aclprofFinalize 接口。
