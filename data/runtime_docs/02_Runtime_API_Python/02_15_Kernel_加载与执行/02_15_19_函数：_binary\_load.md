# 函数： binary\_load

> **Section**: 2.15.19


## 产品支持情况

## 功能说明

注意，此处仅销毁 acl.rt.binary 的数据，调用 acl.rt.create\_binary 接口时传入的 data 内 存需由用户自行、及时释放，否则可能会导致内存异常。

- C 函数原型

aclError aclrtDestroyBinary(aclrtBinary binary)

- python 函数
- ret = acl.rt.destroy\_binary(binary)

| 参数名    | 说明                               |
|--------|----------------------------------|
| binary | int ，待销毁的 acl.rt.binary 类型的指针地址。 |

| 产品                                | 是否支持   |
|-----------------------------------|--------|
| Atlas 350 加速卡                     | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系 列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系 列产品 | √      |
| Atlas 训练系列产品                      | √      |
| Atlas 推理系列产品                      | √      |
| Atlas 200I/500 A2 推理产品            | √      |

解析、加载算子二进制文件，输出指向算子二进制的 binHandle ，同时将算子二进制文 件数据拷贝至当前 Context 对应的 Device 上。仅支持 Ascend C 自定义算子。

## 函数原型

## 参数说明

## 返回值说明

| 返回值        | 说明                            |
|------------|-------------------------------|
| bin_handle | int ，指向二进制的 handle 的指针地址。     |
| ret        | int ，错误码，返回 0 表示成功，返回其它值表示失败。 |
