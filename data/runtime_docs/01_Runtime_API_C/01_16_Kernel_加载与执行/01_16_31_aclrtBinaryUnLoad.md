# aclrtBinaryUnLoad

> **Section**: 1.16.31


## 产品支持情况

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 约束说明

调用本接口删除算子二进制数据时，需跟 aclrtBinaryLoadFromFile 、

aclrtBinaryLoadFromData 或者 aclrtBinaryLoad 接口在同一个 Context 下，这样才能 一并删除加载算子二进制文件时拷贝到 Device 上的算子二进制数据，否则可能会导致 Device 上的算子二进制数据删除异常。
