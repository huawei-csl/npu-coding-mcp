# 函数： ptr\_to\_numpy

> **Section**: 2.4.3


## 须知

该接口即将废弃，建议使用 acl.util.ptr\_to\_bytes 接口。

| C 函数原型    | 无                                                |
|-----------|--------------------------------------------------|
| Python 函数 | output = acl.util.ptr_to_numpy(ptr, shape, type) |
| 函数功能      | 将指针地址数据转换为 numpy 数组，可以使 Python 代码直接访 问。          |

| 输入说明   | ptr ： int ， C 语言中的指针地址，是能够访问的数据的首地址。 shape ： tuple ，需要构造的 numpy 的 Shape 。 type ： int ，表示 ptr 中数据的数据类型。 下面举例一些常用的类型（未列出类型详见 Numpy 手册， NumPy C-API 中的数据类型 API ，以下列出类型以手册中数据为准）： ● 0 ： NPY_BOOL ● 1 ： NPY_BYTE ， NPY_INT8 ● 2 ： NPY_UINT8 ● 3 ： NPY_SHORT ， NPY_INT16 ● 4 ： NPY_USHORT ， NPY_UINT16 ● 5 ： NPY_INT ， NPY_INT32 ● 6 ： NPY_UINT ， NPY_UINT32 ● 7 ： NPY_INT64 ● 8 ： NPY_UINT64 ● 9 ： NPY_LONGLONG ● 10 ： NPY_ULONGLONG ● 11 ： NPY_FLOAT32 ● 12 ： NPY_DOUBLE   |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 返回值说明  | output ： numpy 类型。                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 约束说明   | 无                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 注意事项   | ● 修改示例如下： np_arr_out = acl.util.ptr_to_numpy(host_ptr, np_arr_in.shape, NPY_INT32) 修改后使用： bytes_out = acl.util.ptr_to_bytes(ptr, size) np_arr_out = np.frombuffer(bytes_out, dtype=np.int32).reshape(np_arr_in.shape) ● 若要继续使用该接口，需要运行环境为 python ≥ 3.8 且 numpy ≥ 1.22.0 。                                                                                                                                                                                              |
