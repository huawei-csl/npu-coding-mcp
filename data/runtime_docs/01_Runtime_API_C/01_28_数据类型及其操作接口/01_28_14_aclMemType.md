# aclMemType

> **Section**: 1.28.14


```
ACL_MEMTYPE_DEVICE = 0,  //Device 内存 ACL_MEMTYPE_HOST = 1,    //Host 内存 ACL_MEMTYPE_HOST_COMPILE_INDEPENDENT = 2   //Host 内存
```

```
typedef enum { } aclMemType;
```

ACL\_MEMTYPE\_HOST 和 ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT 都标识 Host 内存，但在使用上有区别：

- ACL\_MEMTYPE\_HOST ：若通过 aclSetCompileopt 接口将 ACL\_OP\_JIT\_COMPILE 设置为 disable ，设置该选项时，算子输入或输出的值的变化，不会触发算子重新 编译；若通过 aclSetCompileopt 接口将 ACL\_OP\_JIT\_COMPILE 设置为 enable ，算 子输入或输出的值的变化，会触发算子重新编译。
- ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT ：设置该选项时，算子输入或 输出的值的变化，都不会触发算子重新编译。若算子编译时依赖其输入或输出的 值，此时如果设置为 ACL\_MEMTYPE\_HOST\_COMPILE\_INDEPENDENT ，则可能 会导致编译失败。
