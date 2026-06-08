# aclsysGetCANNVersion （废弃）

> **Section**: 1.27.6


须知：此接口后续版本会废弃，请使用 aclsysGetVersionStr 、 aclsysGetVersionNum 接口。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

查询 CANN 软件包版本号。

aclError aclsysGetCANNVersion(aclCANNPackageName name, aclCANNPackageVersion *version)

## 参数说明

## 返回值说明

| 参数名     | 输入 / 输 出   | 说明                                                              |
|---------|------------|-----------------------------------------------------------------|
| name    | 输入         | 指定要查询的软件包。类型定义请参见 aclCANNPackageName 。 若指定要查询的软件包没有安装，则本接口返回报错。 |
| version | 输出         | CANN 软件包版本号。类型定义请参见 aclCANNPackageVersion 。                     |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
