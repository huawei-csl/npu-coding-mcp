# aclError

> **Section**: 2.19.1


## 说明

## 返回码定义规则：

- 规则 1 ：开发人员的环境异常或者代码逻辑错误，可以通过优化环境或代码逻辑的方式解决 问题，此时返回码定义为： 1XXXXX 。
- 规则 2 ：资源不足（ Stream 、内存等）、开发人员编程时使用的接口或参数与当前硬件不匹 配，可以通过在编程时合理使用资源的方式解决，此时返回码定义为： 2XXXXX 。
- 规则 3 ：业务功能异常，比如队列满、队列空等，此时返回码定义为 3XXXXX 。
- 规则 4 ：软硬件内部异常，包括软件内部错误、 Device 执行失败等，用户无法解决问题，需 要将问题反馈给技术支持，此时返回码定义为： 5XXXXX 。您可以获取日志后单击 Link 联系 技术支持。
- 规则 5 ：无法识别的错误，当前都映射为 500000 。您可以获取日志后单击 Link 联系技术支 持。

表 2-3 返回码列表

| 返回码                                                      | 说明          | 可能原因及解决方法                                                                                                                                                |
|----------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_SUCCESS = 0                                          | 执行成功。       | -                                                                                                                                                        |
| ACL_ERROR_NONE = 0 须知 此返回码后续版本会废弃， 请使用 ACL_SUCCESS 返回 码。 | 执行成功。 7121  | -                                                                                                                                                        |
| ACL_ERROR_INVALID_PA RAM = 100000                        | 参数校验失败。     | 请检查接口的入参值是否 正确。                                                                                                                                          |
| ACL_ERROR_UNINITIALIZ E = 100001                         | 未初始化。       | ● 请检查是否已调用 acl.init 接口进行初始 化，请确保已调用 acl.init 接口，且在其它 接口之前调用。 ● 请检查是否已调用对应 功能的初始化接口，例 如初始化 Dump 的 acl.mdl.init_dump 接 口、初始化 Profiling 的 acl.prof.init 接口。 |
| ACL_ERROR_REPEAT_INI TIALIZE = 100002                    | 重复初始化或重复加载。 | 请检查是否调用对应的接 口重复初始化或重复加 载。                                                                                                                                |
| ACL_ERROR_INVALID_FIL E = 100003                         | 无效的文件。      | 请检查文件是否存在、文 件是否能被访问等。                                                                                                                                    |

| 返回码                                          | 说明                | 可能原因及解决方法                          |
|----------------------------------------------|-------------------|------------------------------------|
| ACL_ERROR_WRITE_FILE = 100004                | 写文件失败。            | 请检查文件路径是否存 在、文件是否有写权限 等。           |
| ACL_ERROR_INVALID_FIL E_SIZE = 100005        | 无效的文件大小。          | 请检查文件大小是否符合 接口要求。                  |
| ACL_ERROR_PARSE_FILE = 100006                | 解析文件失败。           | 请检查文件内容是否合 法。                      |
| ACL_ERROR_FILE_MISSIN G_ATTR = 100007        | 文件缺失参数。           | 请检查文件内容是否完 整。                      |
| ACL_ERROR_FILE_ATTR_I NVALID = 100008        | 文件参数无效。           | 请检查文件中参数值是否 正确。                    |
| ACL_ERROR_INVALID_D UMP_CONFIG = 100009      | 无效的 Dump 配置。      | 请检查 Dump 配置是否正 确，详细配置请参见《精 度调试工具》。 |
| ACL_ERROR_INVALID_PR OFILING_CONFIG = 100010 | 无效的 Profiling 配置。 | 请检查 Profiling 配置是否 正确。             |
| ACL_ERROR_INVALID_M ODEL_ID = 100011         | 无效的模型 ID 。        | 请检查模型 ID 是否正确、 模型是否正确加载。           |
| ACL_ERROR_DESERIALIZ E_MODEL = 100012        | 反序列化模型失败。         | 模型可能与当前版本不匹 配，请重新构建模型。             |
| ACL_ERROR_PARSE_MO DEL = 100013              | 解析模型失败。           | 模型可能与当前版本不匹 配，请重新构建模型。             |
| ACL_ERROR_READ_MOD EL_FAILURE = 100014       | 读取模型失败。           | 请检查模型文件是否存 在、模型文件是否能被访 问等。         |
| ACL_ERROR_MODEL_SIZ E_INVALID = 100015       | 无效的模型大小。          | 模型文件无效，请重新构 建模型。                   |
| ACL_ERROR_MODEL_MIS SING_ATTR = 100016       | 模型缺少参数。           | 模型可能与当前版本不匹 配，请重新构建模型。             |
| ACL_ERROR_MODEL_INP UT_NOT_MATCH = 100017    | 模型的输入不匹配。         | 请检查模型的输入是否正 确。                     |
| ACL_ERROR_MODEL_OU TPUT_NOT_MATCH = 100018   | 模型的输出不匹配。         | 请检查模型的输出是否正 确。                     |
| ACL_ERROR_MODEL_NO T_DYNAMIC = 100019        | 非动态模型。            | 请检查当前模型是否支持 动态场景，如不支持，请 重新构建模型。    |

| 返回码                                                  | 说明                           | 可能原因及解决方法                                           |
|------------------------------------------------------|------------------------------|-----------------------------------------------------|
| ACL_ERROR_OP_TYPE_N OT_MATCH = 100020                | 单算子类型不匹配。                    | 请检查算子类型是否正 确。                                       |
| ACL_ERROR_OP_INPUT_ NOT_MATCH = 100021               | 单算子的输入不匹配。                   | 请检查算子的输入是否正 确。                                      |
| ACL_ERROR_OP_OUTPU T_NOT_MATCH = 100022              | 单算子的输出不匹配。                   | 请检查算子的输出是否正 确。                                      |
| ACL_ERROR_OP_ATTR_N OT_MATCH = 100023                | 单算子的属性不匹配。                   | 请检查算子的属性是否正 确。                                      |
| ACL_ERROR_OP_NOT_FO UND = 100024                     | 单算子未找到。                      | 请检查算子类型是否支 持。                                       |
| ACL_ERROR_OP_LOAD_F AILED = 100025                   | 单算子加载失败。                     | 模型可能与当前版本不匹 配，请重新构建单算子模 型。                          |
| ACL_ERROR_UNSUPPOR TED_DATA_TYPE = 100026            | 不支持的数据类型。                    | 请检查数据类型是否存在 或当前是否支持。                                |
| ACL_ERROR_FORMAT_N OT_MATCH = 100027                 | Format 不匹配。                  | 请检查 Format 是否正确。                                    |
| ACL_ERROR_BIN_SELECT OR_NOT_REGISTERED = 100028      | 使用二进制选择方式编译 算子接口时，算子未注册 选择器。 | 请检查是否调用 acl.op.register_compile_f unc 接口注册算子选择 器。   |
| ACL_ERROR_KERNEL_NO T_FOUND = 100029                 | 编译算子时，算子 Kernel 未注册。         | 请检查是否调用 acl.op.create_kernel 接口 注册算子 Kernel 。       |
| ACL_ERROR_BIN_SELECT OR_ALREADY_REGISTERE D = 100030 | 使用二进制选择方式编译 算子接口时，算子重复注 册。   | 请检查是否重复调用 acl.op.register_compile_f unc 接口注册算子选择 器。 |
| ACL_ERROR_KERNEL_AL READY_REGISTERED = 100031        | 编译算子时，算子 Kernel 重复注册。        | 请检查是否重复调用 acl.op.create_kernel 接口 注册算子 Kernel 。     |
| ACL_ERROR_INVALID_Q UEUE_ID = 100032                 | 无效的队列 ID 。                   | 请检查队列 ID 是否正确。                                      |
| ACL_ERROR_REPEAT_SU BSCRIBE = 100033                 | 重复订阅。                        | 请检查针对同一个 Stream ，是否重复调用 acl.rt.subscribe_report 接口。 |

| 返回码                                                                                              | 说明                                 | 可能原因及解决方法                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_STREAM_N OT_SUBSCRIBE = 100034 须知 此返回码后续版本会废弃， 请使用 ACL_ERROR_RT_STREAM_ NO_CB_REG 返回码。 | Stream 未订阅。                        | 请检查是否已调用 acl.rt.subscribe_report 接口。                                                                                                                                  |
| ACL_ERROR_THREAD_N OT_SUBSCRIBE = 100035 须知 此返回码后续版本会废弃， 请使用 ACL_ERROR_RT_THREAD_ SUBSCRIBE 返回码。 | 线程未订阅。                             | 请检查是否已调用 acl.rt.subscribe_report 接口。                                                                                                                                  |
| ACL_ERROR_WAIT_CALL BACK_TIMEOUT = 100036 须知 此返回码后续版本会废弃， 请使用 ACL_ERROR_RT_REPORT_ TIMEOUT 返回码。  | 等待 callback 超时。                    | 请检查是否已调用 acl.rt.launch_callback 接 口下发 callback 任务。 请检查 acl.rt.process_report 接口 中超时时间是否合理。 请检查 callback 任务是否 已经处理完成，如果已处 理完成，但还调用 acl.rt.process_report 接 口，则需优化代码逻辑。 |
| ACL_ERROR_REPEAT_FIN ALIZE = 100037                                                              | 重复去初始化。                            | 请检查是否重复调用 acl.finalize 接口进行去初 始化。                                                                                                                                     |
| ACL_ERROR_NOT_STATIC _AIPP = 100038 须知 此返回码后续版本会废弃， 请使用 ACL_ERROR_GE_AIPP_NO T_EXIST 返回码。        | 静态 AIPP 配置信息不存 在。                  | 调用 acl.mdl.get_first_aipp_inf o 接口时，请传入正确的 index 值。                                                                                                                   |
| ACL_ERROR_COMPILING _STUB_MODE = 100039                                                          | 运行应用前配置的动态库 路径是编译桩的路径，不 是正确的动态库路径。 | 请检查动态库路径的配 置，确保使用运行模式的 动态库。                                                                                                                                           |

| 返回码                                       | 说明                                      | 可能原因及解决方法                                                                                                                                                                                                          |
|-------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_PROF_ALRE ADY_RUN = 100042      | 已存在采集 Profiling 数据 的任务。                 | ● 请检查代码逻辑，'通 过调用 pyacl API 方式采 集 Profiling 数据'的配 置不能与其它方式的 Profiling 配置并存，只 能保留一种，各种方式 的 Profiling 采集配置请 参见《性能调优工 具》。 ● 请检查是否对同一个 Device 重复下发了多次 Profiling 配置，请参考 2.16.1 Profiling 数据 采集接口中的接口调用 要求、接口调用顺序调 整代码逻辑。 |
| ACL_ERROR_PROF_NOT_ RUN = 100043          | 未使用 acl.prof.init 接口先 进行 Profiling 初始化。 | 请检查采集 Profiling 数据 的接口调用顺序，参考 2.16.1 Profiling 数据采集 接口中的说明。                                                                                                                                                        |
| ACL_ERROR_DUMP_ALR EADY_RUN = 100044      | 已存在获取 Dump 数据的 任务。                      | 请检查在调用 acl.mdl.init_dump 接 口、 acl.mdl.set_dump 接 口、 acl.mdl.finalize_dump 接 口配置 Dump 信息前，是 否已调用 acl.init 接口配置 Dump 信息，如是，请调 整代码逻辑，保留一种方 式配置 Dump 信息即可。                                                             |
| ACL_ERROR_DUMP_NOT _RUN = 100045          | 未使用 acl.mdl.init_dump 接口 先进行 Dump 初始化。  | 请检查获取 Dump 数据的 接口调用顺序，参考 acl.mdl.init_dump 接口 处的说明。                                                                                                                                                                |
| ACL_ERROR_PROF_REPE AT_SUBSCRIBE = 148046 | 重复订阅同一个模型。                              | 请检查接口调用顺序，参 考 2.16.1 Profiling 数据采 集接口中的说明。                                                                                                                                                                        |

| 返回码                                                 | 说明                                        | 可能原因及解决方法                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_PROF_API_C ONFLICT = 148047               | 采集性能数据的接口调用 冲突。                           | 两种方式的 Profiling 性能 数据采集接口不能交叉调 用， acl.prof.init 接口和 acl.prof.finalize 接口之间 不能调用 acl.prof.model_subscrib e 接口、 acl.prof.get_op_* 接口、 acl.prof.model_unsubscr ibe 接口， acl.prof.model_subscrib e 接口和 acl.prof.model_unsubscr ibe 接口之间不能调用 acl.prof.init 接口、 acl.prof.start 接口、 acl.prof.stop 接口、 acl.prof.finalize 接口。 |
| ACL_ERROR_INVALID_M AX_OPQUEUE_NUM_CO NFIG = 148048 | 无效的算子缓存信息老化 配置。                           | 请检查算子缓存信息老化 配置，参考 acl.init 处的配 置说明及示例。                                                                                                                                                                                                                                                                              |
| ACL_ERROR_INVALID_OP P_PATH = 148049                | 没有设置 ASCEND_OPP_PATH 环境 变量，或该环境变量的值 设置错误。 | 请检查是否设置 ASCEND_OPP_PATH 环境 变量，且该环境变量的值 是否为 opp 软件包的安装 路径。                                                                                                                                                                                                                                                           |
| ACL_ERROR_OP_UNSUPP ORTED_DYNAMIC = 148050          | 算子不支持动态 Shape 。                           | ● 请检查单算子模型文件 中该算子的 Shape 是否 为动态，如果是动态 的，需要修改为固定 Shape 。 ● 请检查编译算子时， aclTensorDesc 的 Shape 是否为动态，如果是动 态的，需要按照固定 Shape 重新创建 aclTensorDesc 。                                                                                                                                                                           |
| ACL_ERROR_RELATIVE_R ESOURCE_NOT_CLEARE D = 148051  | 相关的资源尚未释放。                                | 在销毁通道描述信息时， 如果相关的通道尚未销毁 则返回此错误码。请检查 与此通道描述信息相关联 的通道是否被销毁。                                                                                                                                                                                                                                                           |

| 返回码                                                                                        | 说明                                     | 可能原因及解决方法                                                                                                                                                           |
|--------------------------------------------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_UNSUPPOR TED_JPEG = 148052                                                       | JPEGD 功能不支持的输入 图片编码格式（例如算术 编码、渐进式编码等）。 | 实现 JPEGD 图片解码功能 时，仅支持 Huffman 编 码，压缩前的原图像色彩 空间为 YUV ，像素的各分 量比例为 4 : 4 : 4 或 4 : 2 : 2 或 4 : 2 : 0 或 4 : 0 : 0 或 4 : 4 : 0 ，不支持算术编码、 不支持渐进 JPEG 格式、不 支持 JPEG2000 格式。 |
| ACL_ERROR_BAD_ALLOC = 200000                                                               | 申请内存失败。                                | 请检查硬件环境上的内存 剩余情况。                                                                                                                                                   |
| ACL_ERROR_API_NOT_S UPPORT = 200001                                                        | 接口不支持。                                 | 请检查调用的接口当前是 否支持。                                                                                                                                                    |
| ACL_ERROR_INVALID_DE VICE = 200002 须知 此返回码后续版本会废弃， 请使用 ACL_ERROR_RT_INVALID_ DEVICEID 返回码。 | 无效的 Device 。                           | 请检查 Device 是否存在。                                                                                                                                                    |
| ACL_ERROR_MEMORY_A DDRESS_UNALIGNED = 200003                                               | 内存地址未对齐。                               | 请检查内存地址是否符合 接口要求。                                                                                                                                                   |
| ACL_ERROR_RESOURCE_ NOT_MATCH = 200004                                                     | 资源不匹配。                                 | 请检查调用接口时，是否 传入正确的 Stream 、 Context 等资源。                                                                                                                             |
| ACL_ERROR_INVALID_RE SOURCE_HANDLE = 200005                                                | 无效的资源句柄。                               | 请检查调用接口时，传入 的 Stream 、 Context 等资 源是否已被销毁或占用。                                                                                                                       |
| ACL_ERROR_FEATURE_U NSUPPORTED = 200006                                                    | 特性不支持。                                 | 您可以获取日志后单击 Link 联系技术支持。                                                                                                                                             |
| ACL_ERROR_PROF_MOD ULES_UNSUPPORTED = 200007                                               | 下发了不支持的 Profiling 配置。                  | 请参见 acl.prof.create_config 中 的说明检查 Profiling 的配 置是否正确。                                                                                                              |
| ACL_ERROR_STORAGE_O VER_LIMIT = 300000                                                     | 超出存储上限。                                | 请检查硬件环境上的存储 剩余情况。                                                                                                                                                   |
| ACL_ERROR_INTERNAL_E RROR = 500000                                                         | 未知内部错误。                                | 您可以获取日志后单击 Link 联系技术支持。                                                                                                                                             |
| ACL_ERROR_FAILURE = 500001                                                                 | 系统内部 ACL 的错误。                          | 您可以获取日志后单击 Link 联系技术支持。                                                                                                                                             |

| 返回码                                   | 说明                       | 可能原因及解决方法               |
|---------------------------------------|--------------------------|-------------------------|
| ACL_ERROR_GE_FAILURE = 500002         | 系统内部 GE 的错误。             |                         |
| ACL_ERROR_RT_FAILURE = 500003         | 系统内部 RUNTIME 的错 误。       |                         |
| ACL_ERROR_DRV_FAILUR E = 500004       | 系统内部 DRV （ Driver ） 的错误。 |                         |
| ACL_ERROR_PROFILING_ FAILURE = 500005 | Profiling 相关错误。          | 您可以获取日志后单击 Link 联系技术支持。 |

表 2-4 内部 RUNTIME 的返回码列表

| 返回码                                             | 含义                     | 可能原因及解决方法                                        |
|-------------------------------------------------|------------------------|--------------------------------------------------|
| ACL_RT_SUCCESS = 0                              | 执行成功。                  | -                                                |
| ACL_ERROR_RT_PARAM_ INVALID = 107000            | 参数校验失败。                | 请检查接口入参是否正 确。                                    |
| ACL_ERROR_RT_INVALID _DEVICEID = 107001         | 无效的 Device ID 。        | 请检查 Device ID 是否合 法。                             |
| ACL_ERROR_RT_CONTEX T_NULL = 107002             | context 为空。            | 请检查是否调用 acl.rt.set_context 或 acl.rt.set_device 。 |
| ACL_ERROR_RT_STREAM _CONTEXT = 107003           | stream 不在当前 Context 内。 | 请检查 Stream 所在的 Context 与当前 Context 是 否一致。        |
| ACL_ERROR_RT_MODEL_ CONTEXT = 107004            | model 不在当前 Context 内。  | 请检查加载的模型与当前 Context 是否一致。                        |
| ACL_ERROR_RT_STREAM _MODEL = 107005             | stream 不在当前 model 内。   | 请检查 Stream 是否绑定过 该模型。                            |
| ACL_ERROR_RT_EVENT_T IMESTAMP_INVALID = 107006  | event 时间戳无效。           | 请检查 Event 是否创建。                                  |
| ACL_ERROR_RT_EVENT_T IMESTAMP_REVERSAL = 107007 | event 时间戳反转。           | 请检查 Event 是否创建。                                  |
| ACL_ERROR_RT_ADDR_U NALIGNED = 107008           | 内存地址未对齐。               | 请检查所申请的内存地址 是否对齐，详细内存申请 接口的约束请参见 2.12 内 存管理。     |
| ACL_ERROR_RT_FILE_OP EN = 107009                | 打开文件失败。                | 请检查文件是否存在。                                       |

| 返回码                                        | 含义                            | 可能原因及解决方法                                                                                                              |
|--------------------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_RT_FILE_WR ITE = 107010          | 写文件失败。                        | 请检查文件是否存在或者 是否具备写权限。                                                                                                   |
| ACL_ERROR_RT_STREAM _SUBSCRIBE = 107011    | stream 未订阅或重复订 阅。             | 请检查当前 stream 是否订 阅或重复订阅。                                                                                               |
| ACL_ERROR_RT_THREAD _SUBSCRIBE = 107012    | 线程未订阅或重复订阅。                   | 请检查当前线程是否订阅 或重复订阅。                                                                                                     |
| ACL_ERROR_RT_GROUP_ NOT_SET = 107013       | 未设置 Group 。                   | -                                                                                                                      |
| ACL_ERROR_RT_GROUP_ NOT_CREATE = 107014    | 未创建对应的 Group 。                | 请检查调用接口时设置的 Group ID 是否在支持的范 围内， Group ID 的取值范 围： [0, (Group 数量 -1)] 。                                                 |
| ACL_ERROR_RT_STREAM _NO_CB_REG = 107015    | 该 callback 对应的 Stream 未注册到线程。 | 请检查 stream 是否已经注 册到线程，检查是否调用 acl.rt.subscribe_report 接口。                                                               |
| ACL_ERROR_RT_INVALID _MEMORY_TYPE = 107016 | 无效的内存类型。                      | 请检查内存类型是否合 法。                                                                                                          |
| ACL_ERROR_RT_INVALID _HANDLE = 107017      | 无效的资源句柄。                      | 检查对应输入和使用的参 数是否正确 .                                                                                                    |
| ACL_ERROR_RT_INVALID _MALLOC_TYPE = 107018 | 申请使用的内存类型不正 确。                | 检查对应输入和使用的内 存类型是否正确。                                                                                                   |
| ACL_ERROR_RT_WAIT_TI MEOUT = 107019        | 执行任务超时。                       | 请尝试重新执行下发任务 的接口。                                                                                                       |
| ACL_ERROR_RT_TASK_TI MEOUT = 107020        | 执行任务超时。                       | 请排查业务编排是否合理 或者设置合理的超时时 间。                                                                                              |
| ACL_ERROR_RT_SYSPARA MOPT_NOT_SET = 107021 | 获取当前 Context 中的系统 参数值失败。      | 未设置当前 Context 中的系 统参数值。                                                                                                |
| ACL_ERROR_RT_DEVICE_ TASK_ABORT = 107022   | Device 上的任务丢弃操作 与其它操作冲突。      | 该错误码是由于调用 acl.rt.device_task_abort 接口停止 Device 上的任务 与其它接口操作冲突，用 户需排查代码逻辑，等待 acl.rt.device_task_abort 接口执行完成后，才执行 其它操作。 |

| 返回码                                        | 含义                 | 可能原因及解决方法                                            |
|--------------------------------------------|--------------------|------------------------------------------------------|
| ACL_ERROR_RT_STREAM _ABORT = 107023        | 正在清除 Stream 上的任 务。 | 正在清除指定 Stream 上的 任务，不支持同步等待该 Stream 上的任务执行。          |
| ACL_ERROR_RT_FEATUR E_NOT_SUPPORT = 207000 | 特性不支持。             | 您可以获取日志后单击 Link 联系技术支持。                              |
| ACL_ERROR_RT_MEMOR Y_ALLOCATION = 207001   | 内存申请失败。            | 请检查硬件环境上的存储 剩余情况。                                    |
| ACL_ERROR_RT_MEMOR Y_FREE = 207002         | 内存释放失败。            | 您可以获取日志后单击 Link 联系技术支持。                              |
| ACL_ERROR_RT_AICORE_ OVER_FLOW = 207003    | aicore 算子运算溢出 .    | 请检查对应的 aicore 算子 运算是否有溢出。                            |
| ACL_ERROR_RT_NO_DEV ICE = 207004           | Device 不可用。        | 请检查 Device 是否正常运 行。                                  |
| ACL_ERROR_RT_RESOUR CE_ALLOC_FAIL = 207005 | 内存申请失败。            | 请检查硬件环境上的存储 剩余情况。                                    |
| ACL_ERROR_RT_NO_PER MISSION = 207006       | 没有操作权限。            | 请检查运行应用的用户权 限是否正确。                                   |
| ACL_ERROR_RT_NO_EVE NT_RESOURCE = 207007   | Event 资源不足。        | 请参考 acl.rt.create_event 接口 处的说明检查 Event 数量是 否符合要求。   |
| ACL_ERROR_RT_NO_STR EAM_RESOURCE = 207008  | Stream 资源不足。       | 请参考 acl.rt.create_stream 接口 处的说明检查 Stream 数量 是否符合要求。 |
| ACL_ERROR_RT_NO_NO TIFY_RESOURCE = 207009  | 系统内部 Notify 资源不 足。 | 数据预处理的并发任务太 多或模型推理时消耗资源 太多，建议尝试减少并发 任务或卸载部分模型。       |
| ACL_ERROR_RT_NO_MO DEL_RESOURCE = 207010   | 模型资源不足。            | 建议卸载部分模型。                                            |
| ACL_ERROR_RT_NO_CD Q_RESOURCE = 207011     | Runtime 内部资源不足。    | 您可以获取日志后单击 Link 联系技术支持。                              |
| ACL_ERROR_RT_OVER_LI MIT = 207012          | 队列数目超出上限。          | 请销毁不需要的队列之后 再创建新的队列。                                 |

| 返回码                                                                        | 含义                               | 可能原因及解决方法                                                                                |
|----------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------|
| ACL_ERROR_RT_QUEUE_ EMPTY = 207013                                         | 队列为空。                            | 不能从空队列中获取数 据，请先向队列中添加数 据，再获取。                                                            |
| ACL_ERROR_RT_QUEUE_ FULL = 207014                                          | 队列已满。                            | 不能向已满的队列中添加 数据，请先从队列中获取 数据，再添加。                                                          |
| ACL_ERROR_RT_REPEATE D_INIT = 207015                                       | 队列重复初始化。                         | 建议初始化一次队列即 可，不要重复初始化。                                                                    |
| ACL_ERROR_RT_DEVIDE_ OOM = 207018                                          | Device 侧内存耗尽。                    | 排查 Device 上的内存使用 情况，并根据 Device 上的 内存规格合理规划内存的 使用。                                        |
| static const int32_t ACL_ERROR_RT_FEATUR E_NOT_SUPPORT_UPDA TE_OP = 207019 | 当前驱动版本不支持更新 该算子。                 | 请检查驱动版本。 您可以单击 Link ，在'固 件与驱动'页面下载 Ascend HDK 25.0.RC1 或 更高版本的驱动安装包， 并参考相应版本的文档进 行安装、升级。 |
| ACL_ERROR_RT_INTERNE L_ERROR = 507000                                      | Host 上的 runtime 模块内 部错误。         | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_TS_ERR OR = 507001                                            | Device 上的 task scheduler 模块内部错误。 | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_STREAM _TASK_FULL = 507002                                    | stream 上的 task 数量满。              | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_STREAM _TASK_EMPTY = 507003                                   | stream 上的 task 数量为 空。            | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_STREAM _NOT_COMPLETE = 507004                                 | stream 上的 task 未全部执 行完成。         | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_END_OF _SEQUENCE = 507005                                     | AI CPU 上的 task 执行完 成。            | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_EVENT_ NOT_COMPLETE = 507006                                  | event 未完成。                       | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_CONTEX T_RELEASE_ERROR = 507007                               | context 释放失败。                    | 您可以获取日志后单击 Link 联系技术支持。                                                                  |
| ACL_ERROR_RT_SOC_VE RSION = 507008                                         | 获取 soc version 失败。               | 您可以获取日志后单击 Link 联系技术支持。                                                                  |

| 返回码                                           | 含义                                          | 可能原因及解决方法                                                                     |
|-----------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------|
| ACL_ERROR_RT_TASK_TY PE_NOT_SUPPORT = 507009  | 不支持的 task 类型。                               |                                                                               |
| ACL_ERROR_RT_LOST_H EARTBEAT = 507010         | task scheduler 丢失心跳。                        |                                                                               |
| ACL_ERROR_RT_MODEL_ EXECUTE = 507011          | 模型执行失败。                                     |                                                                               |
| ACL_ERROR_RT_REPORT _TIMEOUT = 507012         | 获取 task scheduler 的消息 失败。                   | 排查接口的超时时间设置 是否过短，适当增长超时 时间。如果增长超时时间 后，依然有超时报错，再 排查日志。 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_SYS_DM A = 507013                | system dma （ Direct Memory Access ）硬件执 行错误。 | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICORE_ TIMEOUT = 507014         | aicore 执行超时。                                | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICORE_ EXCEPTION = 507015       | aicore 执行异常。                                | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICORE_ TRAP_EXCEPTION = 507016  | aicore trap 执行异常。                           | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICPU_T IMEOUT = 507017          | aicpu 执行超时。                                 | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICPU_E XCEPTION = 507018        | aicpu 执行异常。                                 | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICPU_D ATADUMP_RSP_ERR = 507019 | aicpu 执行数据 dump 后未 给 task scheduler 返回响 应。  | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_AICPU_ MODEL_RSP_ERR = 507020    | aicpu 执行模型后未给 task scheduler 返回响应。          | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_PROFILI NG_ERROR = 507021        | profiling 功能执行异常。                           | 您可以获取日志后单击 Link 联系技术支持。                                                       |
| ACL_ERROR_RT_IPC_ERR OR = 507022              | 进程间通信异常。                                    | 您可以获取日志后单击 Link 联系技术支持。                                                       |

| 返回码                                                | 含义                         | 可能原因及解决方法               |
|----------------------------------------------------|----------------------------|-------------------------|
| ACL_ERROR_RT_MODEL_ ABORT_NORMAL = 507023          | 模型退出。                      |                         |
| ACL_ERROR_RT_KERNEL_ UNREGISTERING = 507024        | 算子正在去注册。                   |                         |
| ACL_ERROR_RT_RINGBU FFER_NOT_INIT = 507025         | ringbuffer （环形缓冲区） 功能未初始化。 |                         |
| ACL_ERROR_RT_RINGBU FFER_NO_DATA = 507026          | ringbuffer （环形缓冲区） 没有数据。   |                         |
| ACL_ERROR_RT_KERNEL_ LOOKUP = 507027               | RUNTIME 内部的 kernel 未 注册。   |                         |
| ACL_ERROR_RT_KERNEL_ DUPLICATE = 507028            | 重复注册 RUNTIME 内部的 kernel 。  |                         |
| ACL_ERROR_RT_DEBUG_ REGISTER_FAIL = 507029         | debug 功能注册失败。              |                         |
| ACL_ERROR_RT_DEBUG_ UNREGISTER_FAIL = 507030       | debug 功能去注册失败。             |                         |
| ACL_ERROR_RT_LABEL_C ONTEXT = 507031               | 标签不在当前 Context 内。          | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_PROGRA M_USE_OUT = 507032             | 注册的 program 数量超过 限制。       | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_DEV_SET UP_ERROR = 507033             | Device 启动失败。               | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_VECTOR _CORE_TIMEOUT = 507034         | vector core 执行超时。          | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_VECTOR _CORE_EXCEPTION = 507035       | vector core 执行异常。          | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_VECTOR _CORE_TRAP_EXCEPTIO N = 507036 | vector core trap 执行异 常。    | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_CDQ_BA TCH_ABNORMAL = 507037          | Runtime 内部资源申请异 常。         | 您可以获取日志后单击 Link 联系技术支持。 |

| 返回码                                                     | 含义                                        | 可能原因及解决方法               |
|---------------------------------------------------------|-------------------------------------------|-------------------------|
| ACL_ERROR_RT_DIE_MO DE_CHANGE_ERROR = 507038            | die 模式修改异常，不能修 改 die 模式。                  | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_DIE_SET _ERROR = 507039                    | 单 die 模式不能指定 die 。                        | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_INVALID _DIEID = 507040                    | 指定 die id 错误。                             |                         |
| ACL_ERROR_RT_DIE_MO DE_NOT_SET = 507041                 | die 模式没有设置。                               |                         |
| ACL_ERROR_RT_AICORE_ TRAP_READ_OVERFLOW = 507042        | aicore trap 读越界异常。                        |                         |
| ACL_ERROR_RT_AICORE_ TRAP_WRITE_OVERFLO W= 507043       | aicore trap 写越界异常。                        |                         |
| ACL_ERROR_RT_VECTOR _CORE_TRAP_READ_OVE RFLOW = 507044  | vector core trap 读越界异 常。                  |                         |
| ACL_ERROR_RT_VECTOR _CORE_TRAP_WRITE_OV ERFLOW = 507045 | vector core trap 写越界异 常。                  |                         |
| ACL_ERROR_RT_STREAM _SYNC_TIMEOUT = 507046              | 在指定的超时等待事件 中，指定的 stream 中所有 任务还没有执行完成。    |                         |
| ACL_ERROR_RT_EVENT_S YNC_TIMEOUT = 507047               | 在指定的 Event 同步等待 中，超过指定时间，该 Event 还有没有执行完。 |                         |
| ACL_ERROR_RT_FFTS_PL US_TIMEOUT = 507048                | 内部任务执行超时。                                 |                         |
| ACL_ERROR_RT_FFTS_PL US_EXCEPTION = 507049              | 内部任务执行异常。                                 | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_FFTS_PL US_TRAP_EXCEPTION = 507050         | 内部任务 trap 异常。                             | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_SEND_M SG = 507051                         | 数据入队过程中消息发送 失败。                           | 您可以获取日志后单击 Link 联系技术支持。 |
| ACL_ERROR_RT_COPY_D ATA = 507052                        | 数据入队过程中内存拷贝 失败。                           | 您可以获取日志后单击 Link 联系技术支持。 |

| 返回码                                               | 含义                                                        | 可能原因及解决方法                                                  |
|---------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------|
| ACL_ERROR_RT_DEVICE_ MEM_ERROR = 507053           | 出现内存 UCE （ uncorrect error ，指系统硬件不能直 接处理恢复内存错误）的 错误虚拟地址。  | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_HBM_M ULTI_BIT_ECC_ERROR = 507054    | HBM 比特 ECC 故障。                                            | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_SUSPECT _DEVICE_MEM_ERROR = 507055   | 多进程、多 Device 场景 下，可能出现内存 UCE 错 误。                         | 由于当前 Device 访问的对 端 Device 内存发生故障， 用户需排查对端 Device 进 程的错误信息。 |
| ACL_ERROR_RT_LINK_ER ROR = 507056                 | 多 Device 场景下，两个 Device 之间的通信断链。                           | 建议重试，若依然报错， 则需检查两个 Device 之间 的通信链路。                        |
| ACL_ERROR_RT_SUSPECT _REMOTE_ERROR = 507057       | 多进程、多 Device 场景 下，对端 Device 内存可能 出现故障，或者当前 Device 内存访问越界。 | 用户需排查对端 Device 进 程的错误信息或当前 Device 的内存访问情况。                 |
| ACL_ERROR_RT_DRV_INT ERNAL_ERROR = 507899         | Driver 模块内部错误。                                            | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_AICPU_I NTERNAL_ERROR = 507900       | AI CPU 模块内部错误。                                            | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_SOCKET _CLOSE = 507901               | 内部 HDC （ Host Device Communication ）会话链 接断开。              | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_AICPU_I NFO_LOAD_RSP_ERR = 507902    | AI CPU 调度处理失败。                                            | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_STREAM _CAPTURE_INVALIDATED = 507903 | 模型捕获异常。                                                   | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_RT_COMM_ OP_RETRY_FAIL = 507904         | 通信算子重执行失败                                                 | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_SNAPSHOT_ LOCK_TIMEOUT = 507905         | 调用 aclrtSnapShotProcessLoc k 接口超时。                        | 您可以获取日志后单击 Link 联系技术支持。                                    |
| ACL_ERROR_SNAPSHOT_ LOCK_FAILED = 507906          | 锁定当前进程失败。                                                 | 您可以获取日志后单击 Link 联系技术支持。                                    |

| 返回码                                                    | 含义                   | 可能原因及解决方法   |
|--------------------------------------------------------|----------------------|-------------|
| ACL_ERROR_SNAPSHOT_ UNLOCK_FAILED = 507907             | 解锁当前进程失败。            |             |
| ACL_ERROR_SNAPSHOT_ BACKUP_FAILED = 507908             | 备份快照进程失败。            |             |
| ACL_ERROR_SNAPSHOT_ RESTORE_FAILED = 507909            | 恢复快照进程失败。            |             |
| ACL_ERROR_HOST_MEM ORY_ALREADY_REGISTER ED = 507910    | Host 内存已经被注册。        |             |
| ACL_ERROR_HOST_MEM ORY_NOT_REGISTERED = 507911         | 待取消注册的 Host 内存未 曾注册。 |             |
| ACL_ERROR_SNAPSHOT_ CALLBACK_FAILED = 507912           | 快照某个阶段，执行回调 函数失败。    |             |
| ACL_ERROR_SNAPSHOT_ REGISTER_CALLBACK_FAI LED = 507913 | 注册回调函数失败。            |             |

表 2-5 内部 GE 的返回码列表

| 返回码                                            | 含义       | 可能原因及解决方法                                                                                                                                                |
|------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL_ERROR_GE_PARAM_ INVALID = 145000           | 参数校验失败。  | 请检查接口的入参值是否 正确。                                                                                                                                          |
| ACL_ERROR_GE_EXEC_N OT_INIT = 14500            | 未初始化。    | ● 请检查是否已调用 acl.init 接口进行初始 化，请确保已调用 acl.init 接口，且在其 它接口之前调用。 ● 请检查是否已调用对应 功能的初始化接口，例 如初始化 Dump 的 acl.mdl.init_dump 接 口、初始化 Profiling 的 acl.prof.init 接口。 |
| ACL_ERROR_GE_EXEC_M ODEL_PATH_INVALID = 145002 | 无效的模型路径。 | 请检查模型路径是否正 确。                                                                                                                                            |

| 返回码                                                  | 含义                                         | 可能原因及解决方法                                                  |
|------------------------------------------------------|--------------------------------------------|------------------------------------------------------------|
| ACL_ERROR_GE_EXEC_M ODEL_ID_INVALID = 145003         | 无效的模型 ID 。                                 | 请检查模型 ID 是否正确、 模型是否正确加载。                                   |
| ACL_ERROR_GE_EXEC_M ODEL_DATA_SIZE_INVALI D = 145006 | 无效的模型大小。                                   | 无效的模型大小。                                                   |
| ACL_ERROR_GE_EXEC_M ODEL_ADDR_INVALID = 145007       | 无效的模型内存地址。                                 | 请检查模型地址是否有 效。                                              |
| ACL_ERROR_GE_EXEC_M ODEL_QUEUE_ID_INVALI D = 145008  | 无效的队列 ID 。                                 | 无效的队列 ID 。                                                 |
| ACL_ERROR_GE_EXEC_LO AD_MODEL_REPEATED = 145009      | 重复初始化或重复加载。                                | 请检查是否调用对应的接 口重复初始化或重复加 载。                                  |
| ACL_ERROR_GE_DYNAMI C_INPUT_ADDR_INVALID = 145011    | 无效的动态分档输入地 址。                              | 请检查动态分档输入地 址。                                              |
| ACL_ERROR_GE_DYNAMI C_INPUT_LENGTH_INVAL ID = 145012 | 无效的动态分档输入长 度。                              | 请检查动态分档输入长 度。                                              |
| ACL_ERROR_GE_DYNAMI C_BATCH_SIZE_INVALID = 145013    | 无效的动态分档 Batch 大 小。                         | 请检查动态分档 Batch 大 小。                                         |
| ACL_ERROR_GE_AIPP_BA TCH_EMPTY = 145014              | 无效的 AIPP Batch 数。                          | 请检查 AIPP Batch 数是否 正确。                                     |
| ACL_ERROR_GE_AIPP_N OT_EXIST = 145015                | AIPP 配置不存在。                                | 请检查 AIPP 是否配置。                                             |
| ACL_ERROR_GE_AIPP_M ODE_INVALID = 145016             | 无效的 AIPP 模式。                               | 请检查模型转换时配置的 AIPP 模式是否正确。                                   |
| ACL_ERROR_GE_OP_TAS K_TYPE_INVALID = 145017          | 无效的任务类型。                                   | 请检查算子类型是否正 确。                                              |
| ACL_ERROR_GE_OP_KER NEL_TYPE_INVALID = 145018        | 无效的算子类型。                                   | 请检查算子类型是否正 确。                                              |
| ACL_ERROR_GE_PLGMG R_PATH_INVALID = 145019           | 无效的 so 文件，包括 so 文 件的路径层级太深、 so 文 件被误删除等情况。 | 请检查运行应用前配置的 环境变量 LD_LIBRARY_PATH 是否正 确，详细描述请参见编译 运行处的操作指导。 |

| 返回码                                                       | 含义               | 可能原因及解决方法                                                       |
|-----------------------------------------------------------|------------------|-----------------------------------------------------------------|
| ACL_ERROR_GE_FORMA T_INVALID = 145020                     | 无效的 format 。     | 请检查 Tensor 数据的 format 是否有效。                                     |
| ACL_ERROR_GE_SHAPE_I NVALID = 145021                      | 无效的 shape 。      | 请检查 Tensor 数据的 shape 是否有效。                                      |
| ACL_ERROR_GE_DATATY PE_INVALID = 145022                   | 无效的数据类型。         | 请检查 Tensor 数据的数据 类型是否有效。                                        |
| ACL_ERROR_GE_MEMOR Y_ALLOCATION = 245000                  | 申请内存失败。          | 请检查硬件环境上的内存 剩余情况。                                               |
| ACL_ERROR_GE_MEMOR Y_OPERATE_FAILED = 245001;             | 内存初始化、内存复制操 作失败。 | 请检查内存地址是否正 确、硬件环境上的内存是 否足够等。                                    |
| ACL_ERROR_GE_DEVICE_ MEMORY_ALLOCATION_ FAILED = 245002;  | 申请 Device 内存失败。  | Device 内存已用完，无法 继续申请，请释放部分 Device 内存，再重新尝 试。                    |
| ACL_ERROR_GE_USER_R AISE_EXCEPTION = 345103               | 用户自定义函数主动抛异 常。   | 用户可根据 DataFlowInfo 中设置的 UserData 识别出 来哪个输入的数据执行报 错了，再根据报错排查问 题。 |
| ACL_ERROR_GE_DATA_N OT_ALIGNED = 345104                   | 数据未对齐。           | 若用户自定义函数存在多 个输出时，需排查用户代 码中是否少设置输出，缺 少输出可能会导致数据对 齐异常。            |
| ACL_ERROR_GE_INTERN AL_ERROR = 545000                     | 未知内部错误。          | 您可以获取日志后单击 Link 联系技术支持。                                         |
| ACL_ERROR_GE_LOAD_ MODEL = 545001                         | 系统内部加载模型失败。      | 您可以获取日志后单击 Link 联系技术支持。                                         |
| ACL_ERROR_GE_EXEC_LO AD_MODEL_PARTITION_ FAILED = 545002  | 系统内部加载模型失败。      | 您可以获取日志后单击 Link 联系技术支持。                                         |
| ACL_ERROR_GE_EXEC_LO AD_WEIGHT_PARTITION _FAILED = 545003 | 系统内部加载模型权值失 败。   | 您可以获取日志后单击 Link 联系技术支持。                                         |
| ACL_ERROR_GE_EXEC_LO AD_TASK_PARTITION_FAI LED = 545004   | 系统内部加载模型任务失 败。   | 您可以获取日志后单击 Link 联系技术支持。                                         |

| 返回码                                                       | 含义             | 可能原因及解决方法   |
|-----------------------------------------------------------|----------------|-------------|
| ACL_ERROR_GE_EXEC_LO AD_KERNEL_PARTITION_ FAILED = 545005 | 系统内部加载模型算子失 败。 |             |
| ACL_ERROR_GE_EXEC_RE LEASE_MODEL_DATA = 545006            | 系统内释放模型空间失 败。  |             |
| ACL_ERROR_GE_COMMA ND_HANDLE = 545007                     | 系统内命令操作失败。     |             |
| ACL_ERROR_GE_GET_TE NSOR_INFO = 545008                    | 系统内获取张量数据失 败。  |             |
| ACL_ERROR_GE_UNLOA D_MODEL = 545009                       | 系统内卸载模型空间失 败。  |             |
| ACL_ERROR_GE_MODEL_ EXECUTE_TIMEOUT = 545601              | 模型执行超时。        |             |
