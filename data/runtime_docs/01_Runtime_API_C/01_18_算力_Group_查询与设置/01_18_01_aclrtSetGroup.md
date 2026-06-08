# aclrtSetGroup

> **Section**: 1.18.1


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

指定当前运算使用哪个 Group 的算力，该接口必须在指定 Context 后调用。

aclError aclrtSetGroup(int32\_t groupId)

| 参数名     | 输入 / 输 出   | 说明                                                                                    |
|---------|------------|---------------------------------------------------------------------------------------|
| groupId | 输入         | 表示 Group 的 ID ，用于指定当前计算要使用的 Group 。 您需要提前调用 aclrtGetGroupInfoDetail 接口获取 Group 的 ID 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

仅支持在 Atlas 推理系列产品的 Control CPU 开放形态下调用本接口。不支持在 Atlas 推 理系列产品 Ascend EP 形态下调用本接口。

acl 接口调用顺序：调用 aclrtSetDevice 接口指定计算设备 --&gt; 调用 aclrtGetAllGroupInfo 接口获取所有 Group 信息 --&gt; 调用 aclrtGetGroupCount 接口获 取 Group 数量 --&gt; 调用 aclrtGetGroupInfoDetail 接口获取指定 Group 信息 --&gt; 调用 aclrtSetGroup 接口设置分组 --&gt; 执行其它任务 --&gt; 调用 aclrtResetDevice 接口释放计算 设备。

在调用 acl 接口设置算力 Group 前，需先调用驱动提供的 DCMI 接口 dcmi\_create\_capability\_group 创建分组。若刷新分组（例如调用 dcmi\_create\_capability\_group 接口新增分组、调用 dcmi\_delete\_capability\_group 接口

删除分组等），需重启业务进程。
