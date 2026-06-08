# 函数： dump\_reg\_callback

> **Section**: 2.17.3


## 产品支持情况

## 功能说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

Dump 数据回调函数注册接口。

2.17.1 函数： init\_dump 接口、 2.17.3 函数： dump\_reg\_callback 接口（通过该接口 注册的回调函数需由用户自行实现，回调函数实现逻辑中包括获取 Dump 数据及数据长 度）、 2.17.4 函数： dump\_unreg\_callback 接口、 2.17.5 函数：fi nalize\_dump 接口 配合使用，用于通过回调函数获取 Dump 数据。场景举例如下：

- 执行一个模型，通过回调获取 Dump 数据：

支持以下两种方式：

- -在 aclInit 接口处不启用模型 Dump 配置、单算子 Dump 配置 2.5.1 函数： init 接口 --&gt; 2.17.1 函数： init\_dump 接口 --&gt; 2.17.3 函数： dump\_reg\_callback 接口 --&gt; 模型加载 --&gt; 模型执行 --&gt; 2.17.4 函数： dump\_unreg\_callback 接口 --&gt; 2.17.5 函数：fi nalize\_dump 接口 --&gt; 模型卸 载 --&gt; 2.5.2 函数：fi nalize 接口
- -在 aclInit 接口处启用模型 Dump 配置、单算子 Dump 配置，在 aclInit 接口处启 用 Dump 配置时需配置落盘路径，但如果调用了 2.17.3 函数： dump\_reg\_callback 接口，则落盘不生效，以回调函数获取的 Dump 数据为

准

2.5.1 函数： init 接口 --&gt; 2.17.3 函数： dump\_reg\_callback 接口 --&gt; 模型加 载 --&gt; 模型执行 --&gt; 2.17.4 函数： dump\_unreg\_callback 接口 --&gt; 模型卸载 --&gt; 2.5.2 函数：fi nalize 接口

- 执行两个不同的模型，通过回调获取 Dump 数据，该场景下，只要不调用 2.17.4 函数： dump\_unreg\_callback 接口取消注册回调函数，则可通过回调函数获取两 个模型的 dump 数据：

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

2.5.1 函数： init 接口 --&gt; 2.17.1 函数： init\_dump 接口 --&gt; 2.17.3 函数： dump\_reg\_callback 接口 --&gt; 模型 1 加载 --&gt; 模型 1 执行 --&gt;--&gt; 模型 2 加载 --&gt; 模型 2 执 行 --&gt; 2.17.4 函数： dump\_unreg\_callback 接口 --&gt; 2.17.5 函数：fi nalize\_dump 接口 --&gt; 模型卸载 --&gt; 2.5.2 函数：fi nalize 接口

- C 函数原型

aclError acldumpRegCallback(int32\_t (* const messageCallback)(const acldumpChunk *, int32\_t len), int32\_t flag)

- python 函数

ret = acl.mdl.dump\_reg\_callback(mdl\_dump\_callback, flag)

| 参数名                | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mdl_dump_ca llback | 用于接收回调数据的回调函数，有如下两个参数： ● dump_chunk ： dict ，在实现 mdl_dump_callback 函数时可以获 取 dump_chunk 中的 data_fuf 、 buf_len 等参数值，用于获取 Dump 数据及其数据长度： { "file_name": file_name, // 待落盘的 Dump 数据文件名 "data_buf": data_buf, // Dump 数据的内存地址 "buf_len": buf_len, // data_buf 数据长度，单位 Byte "is_last_chunk": is_last_chunk, // 标识 Dump 数据是否为最后一个分片， 0 表示不 是最后一个分片， 1 表示最后一个分片 "offset": offset, // Dump 数据文件内容的偏移，其中 -1 表示文件追加内容 "flag": flag // 预留 Dump 数据标识，当前数据无标识 } |
| flag               | int ，在调用回调接口后是否还落盘 dump 数据。 ● 0 ：不落盘，当前仅支持 0                                                                                                                                                                                                                                                                                                                                                                                                     |

| 返回值   | 说明                            |
|-------|-------------------------------|
| ret   | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |

无
