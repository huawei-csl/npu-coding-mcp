# aclrtGetGroupInfoDetail

> **Section**: 1.18.4


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | ☓      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | ☓      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | ☓      |
| Atlas 200I/500 A2 推理产品           | ☓      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | ☓      |

查询当前 Context 下指定 Group 的算力信息。

aclError  aclrtGetGroupInfoDetail(const aclrtGroupInfo *groupInfo, int32\_t groupIndex, aclrtGroupAttr attr, void *attrValue, size\_t valueLen, size\_t *paramRetSize)

| 参数名       | 输入 / 输 出   | 说明                                                              |
|-----------|------------|-----------------------------------------------------------------|
| groupInfo | 输入         | 指定算力详细信息的首地址的指针。 需提前调用 aclrtGetAllGroupInfo 接口获取所有 Group 的算力信息。 |

## 返回值说明

## 约束说明

| 参数名           | 输入 / 输 出   | 说明                                                                                                        |
|---------------|------------|-----------------------------------------------------------------------------------------------------------|
| groupIndex    | 输入         | 访问 groupInfo 连续内存块的 Group 索引。 Group 索引的取值范围： [0, (Group 数量 -1)] ，用户可调 用 aclrtGetGroupCount 接口获取 Group 数量。 |
| attr          | 输入         | 指定要获取其算力值的算力属性。类型定义请参见 aclrtGroupAttr 。                                                                   |
| attrValue     | 输出         | 获取指定算力属性所对应的算力值的指针。 用户需根据每个属性的属性值数据类型申请对应大小的 内存，用于存放属性值。                                                  |
| valueLen      | 输入         | 表示 attrValue 的最大长度，单位为 Byte 。                                                                             |
| paramRetSiz e | 输出         | 实际返回的 attrValue 大小的指针，单位为 Byte 。                                                                          |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。

仅支持在 Atlas 推理系列产品的 Control CPU 开放形态下调用本接口。不支持在 Atlas 推 理系列产品 Ascend EP 形态下调用本接口。

acl 接口调用顺序：调用 aclrtSetDevice 接口指定计算设备 --&gt; 调用 aclrtGetAllGroupInfo 接口获取所有 Group 信息 --&gt; 调用 aclrtGetGroupCount 接口获 取 Group 数量 --&gt; 调用 aclrtGetGroupInfoDetail 接口获取指定 Group 信息 --&gt; 调用 aclrtSetGroup 接口设置分组 --&gt; 执行其它任务 --&gt; 调用 aclrtResetDevice 接口释放计算 设备。

在调用 acl 接口设置算力 Group 前，需先调用驱动提供的 DCMI 接口 dcmi\_create\_capability\_group 创建分组。若刷新分组（例如调用 dcmi\_create\_capability\_group 接口新增分组、调用 dcmi\_delete\_capability\_group 接口 删除分组等），需重启业务进程。
