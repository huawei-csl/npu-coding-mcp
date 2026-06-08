# 函数： stop\_thread

> **Section**: 2.4.6.2


| C 函数原型    | 无                                                               |
|-----------|-----------------------------------------------------------------|
| Python 函数 | ret = acl.util.stop_thread(thr_id)                              |
| 函数功能      | 等待由 acl.util.start_thread 接口创建的线程退出。                            |
| 输入说明      | thr_id ： int ，线程 ID 号。需指定由 acl.util.start_thread 接口获得 的线程 ID 号。 |
| 返回值说明     | ret ： int ，错误码。 ● 返回 0 表示成功。 ● 返回其它值表示失败。                       |
| 约束说明      | 无                                                               |
