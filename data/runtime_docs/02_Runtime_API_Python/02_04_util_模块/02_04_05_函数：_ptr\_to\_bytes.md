# 函数： ptr\_to\_bytes

> **Section**: 2.4.5


| C 函数原型    | 无                                                                                                                                        |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| Python 函数 | bytes_out = acl.util.ptr_to_bytes(ptr, size)                                                                                             |
| 函数功能      | 将 void* 数据转换为 bytes 对象，可以使 Python 代码直接访问。                                                                                                |
| 输入说明      | ptr ： int ， C 语言中的指针地址，能够访问的数据的首地址。 size ： int ，数据的大小，单位 Byte 。                                                                          |
| 返回值说明     | bytes_out ： bytes 对象。                                                                                                                    |
| 约束说明      | 无                                                                                                                                        |
| 注意事项      | 修改示例如下： bytes_out = acl.util.ptr_to_bytes(bytes_ptr, size) 由于 acl.util.ptr_to_bytes 会导致数据性能下降，更建议使用函 数： acl.util.bytes_to_ptr 的数据进行后续运算。 |
