# aclrtLaunchKernelCfg

> **Section**: 2.19.31


## 说明

定义

## 成员

任务下发的配置信息。

cfg= [{"id": attr\_id, "value": attr\_value}]

说明：

cfg 中可同时包含多个 dict ，每个 dict 中包含一对 id 和 value 。

| 成员名称       | 说明                                         |
|------------|--------------------------------------------|
| attr_id    | int ，属性 id ，取值参考 aclrtLaunchKernelAttrId 。 |
| attr_value | int ，属性值，取值参考 aclrtLaunchKernelAttrValue 。 |

说明： attr\_id 和 attr\_value 配对使用， attr\_value 随着 attr\_id 的取值来配置不同的值。
