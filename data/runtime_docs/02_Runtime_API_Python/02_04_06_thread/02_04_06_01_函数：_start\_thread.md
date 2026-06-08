# 函数： start\_thread

> **Section**: 2.4.6.1


| C 函数原型    | 无                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------|
| Python 函数 | thr_id, ret = acl.util.start_thread(thr_func, args_list)                                                                               |
| 函数功能      | 创建线程，在线程中执行传入的 Python 函数。                                                                                                              |
| 输入说明      | thr_func ： Python 函数对象，表示用户自定义的 Python 函数。 例如： def thr_func(args_list): pass args_list ： list ，表示用户自定义的 Python 函数（ thr_func ）需要 的传入参数。 |
| 返回值说明     | thr_id ： int ，线程 ID 号。 ret ： int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。                                                                       |

| 约束说明   | 新建线程，无法自动获取 Context ，需要调用 acl.rt.set_context 接 口显式指定 Context 。   |
|--------|------------------------------------------------------------------|
