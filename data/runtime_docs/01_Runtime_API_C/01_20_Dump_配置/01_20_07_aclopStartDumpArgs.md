# aclopStartDumpArgs

> **Section**: 1.20.7


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | ☓      |
| Atlas 训练系列产品                     | √      |

调用本接口开启算子信息统计功能，并需与 aclopStopDumpArgs 接口配合使用，将 算子信息文件输出到 path 参数指定的目录，一个 shape 对应一个算子信息文件，文件中 包含算子类型、算子属性、算子输入 &amp; 输出的 format/ 数据类型 /shape 等信息。

使用场景：例如要统计某个模型执行涉及哪些算子，可在模型执行之前调用 aclopStartDumpArgs 接口，在模型执行之后调用 aclopStopDumpArgs 接口，接口调用 成功后，在 path 参数指定的目录下生成每个算子 shape 的算子信息文件。

aclError aclopStartDumpArgs(uint32\_t dumpType, const char *path)

| 参数名      | 输入 / 输 出   | 说明                                                                                                           |
|----------|------------|--------------------------------------------------------------------------------------------------------------|
| dumpType | 输入         | 指定 dump 信息的类型。 当前仅支持 ACL_OP_DUMP_OP_AICORE_ARGS ，表示 统计所有算子信息。 #define ACL_OP_DUMP_OP_AICORE_ARGS 0x00000001U |

## 返回值说明

## 约束说明

仅支持在单算子 API 执行（例如，接口名前缀为 aclnn 的接口）场景下使用本接口，否 则无法生成 dump 文件。
