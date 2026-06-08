# acldumpRegCallback

> **Section**: 1.20.3


## 产品支持情况

## 功能说明

- -tensor ：导出通过 AscendC::DumpTensor 调测的输出数据。
- -assert ：导出通过 assert/ascendc\_assert 调测的输出数据。
- -timestamp ：导出通过 AscendC::PrintTimeStamp 调测的输出数据。
- dump\_path ：启用算子 Kernel 调测信息 Dump 功能时， dump\_path 必须配置，表 示导出 Dump 文件的存储路径，支持配置绝对路径或相对路径。

Dump 文件存储路径的优先级如下： ASCEND\_DUMP\_PATH 环境变量 &gt; ASCEND\_WORK\_PATH 环境变量 &gt; 配置文件中的 dump\_path ，环境变量的详细描 述请参见《环境变量参考》。

导出的 Dump 文件无法通过文本工具直接查看其内容，若需查看，需使用 show\_kernel\_debug\_data 工具将调测信息解析为可读格式，工具使用指导请参见 《 Ascend C 算子开发》中的'编程指南 &gt; 附录 &gt; show\_kernel\_debug\_data 工 具'。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

Dump 数据回调函数注册接口。

aclmdlInitDump 接口、 acldumpRegCallback 接口（通过该接口注册的回调函数需 由用户自行实现，回调函数实现逻辑中包括获取 Dump 数据及数据长度）、 acldumpUnregCallback 接口、 aclmdlFinalizeDump 接口配合使用，用于通过回调 函数获取 Dump 数据。场景举例如下：

- 执行一个模型，通过回调获取 Dump 数据：

支持以下两种方式：

- -在 aclInit 接口处不启用模型 Dump 配置、单算子 Dump 配置 aclInit 接口 --&gt; aclmdlInitDump 接口 --&gt; acldumpRegCallback 接口 --&gt; 模型 加载 --&gt; 模型执行 --&gt; acldumpUnregCallback 接口 --&gt; aclmdlFinalizeDump 接口 --&gt; 模型卸载 --&gt; aclFinalize 接口

## 函数原型

## 参数说明

## 返回值说明

- -在 aclInit 接口处启用模型 Dump 配置、单算子 Dump 配置，在 aclInit 接口处启 用 Dump 配置时需配置落盘路径，但如果调用了 acldumpRegCallback 接 口，则落盘不生效，以回调函数获取的 Dump 数据为准

aclInit 接口 --&gt; acldumpRegCallback 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; acldumpUnregCallback 接口 --&gt; 模型卸载 --&gt; aclFinalize 接口

- 执行两个不同的模型，通过回调获取 Dump 数据，该场景下，只要不调用 acldumpUnregCallback 接口取消注册回调函数，则可通过回调函数获取两个模 型的 Dump 数据：

aclInit 接口 --&gt; aclmdlInitDump 接口 --&gt; acldumpRegCallback 接口 --&gt; 模型 1 加 载 --&gt; 模型 1 执行 --&gt;--&gt; 模型 2 加载 --&gt; 模型 2 执行 --&gt; acldumpUnregCallback 接口 --&gt; aclmdlFinalizeDump 接口 --&gt; 模型卸载 --&gt; aclFinalize 接口

aclError acldumpRegCallback(int32\_t (* const messageCallback)(const acldumpChunk *, int32\_t len), int32\_t flag)

| 参数名              | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| messageCall back | 输入         | 回调函数指针，用于接收回调数据的回调。 ● acldumpChunk 结构体的定义如下，在实现 messageCallback 回调函数时可以获取 acldumpChunk 结构体中的 dataBuf 、 bufLen 等参数 值，用于获取 Dump 数据及其数据长度： typedef struct acldumpChunk { char fileName[ACL_DUMP_MAX_FILE_PATH_LENGTH]; // 待落盘的 Dump 数据文件名， ACL_DUMP_MAX_FILE_PATH_LENGTH 表示文件名最大长度，当前为 4096 uint32_t bufLen; // dataBuf 数据长度，单位 Byte uint32_t isLastChunk; // 标识 Dump 数据是否为最 后一个分片， 0 表示不是最后一个分片， 1 表示最后一个分片 int64_t offset; // Dump 数据文件内容的偏 移，其中 -1 表示文件追加内容 int32_t flag; // 预留 Dump 数据标识，当前数 据无标识 uint8_t dataBuf[0]; // Dump 数据的内存地址 } acldumpChunk; ● len ：表示 acldumpChunk 结构体的长度，单位 Byte 。 |
| flag             | 输入         | 在调用回调接口后是否还落盘 dump 数据： ● 0 ：不落盘，当前仅支持 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
