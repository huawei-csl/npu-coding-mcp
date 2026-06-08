# 函数： get\_version

> **Section**: 2.18.5


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

查询接口版本号， pyacl 接口版本号命名可以采用： A.B.C 模式，其中， A 表示有不兼容 修改， B 表示新增接口， C 表示 bug 修复。

- C 函数原型 aclError aclrtGetVersion(int32\_t *majorVersion, int32\_t *minorVersion, int32\_t *patchVersion)
- python 函数

无

| 返回值            | 说明                                                                                                                                               |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| major_vers ion | int ，主版本号，从 1 开始，如果出现接口的不兼容变更时，加 1 。                                                                                                             |
| minor_vers ion | int ，次版本号，从 0 开始，按照迭代周期，有新增接口时加 1 。                                                                                                              |
| patch_versi on | int ，补丁版本号，从 0 开始，表示本版本仅仅解决了问题，在 ' majorVersion '、' minorVersion '不变的情况下加 1 。但 ' majorVersion '、' minorVersion '增加的时候， ' patchVersion '一般为' 0 '。 |
| ret            | int ，错误码，返回 0 表示成功，返回其它值表示失败。                                                                                                                    |

major\_version, minor\_version, patch\_version, ret = acl.get\_version()
