# aclprofConfigType

> **Section**: 1.28.17


```
typedef enum { ACL_PROF_SYS_HARDWARE_MEM_FREQ      = 3,
```

```
ACL_PROF_ARGS_MIN                   = 0, ACL_PROF_STORAGE_LIMIT              = 1, ACL_PROF_LLC_MODE                   = 4, ACL_PROF_SYS_IO_FREQ                = 5, ACL_PROF_SYS_INTERCONNECTION_FREQ   = 6, ACL_PROF_DVPP_FREQ                  = 7, ACL_PROF_HOST_SYS                   = 8, ACL_PROF_HOST_SYS_USAGE             = 9, ACL_PROF_HOST_SYS_USAGE_FREQ        = 10, ACL_PROF_LOW_POWER_FREQ             = 11, ACL_PROF_SYS_MEM_SERVICEFLOW        = 12, ACL_PROF_SYS_CPU_FREQ               = 13, ACL_PROF_SCALE                      = 14, ACL_PROF_ARGS_MAX                   = 15 } aclprofConfigType;
```

Atlas 350 加速卡：不支持 ACL\_PROF\_DVPP\_FREQ 、 ACL\_PROF\_HOST\_SYS 、 ACL\_PROF\_HOST\_SYS\_USAGE 、 ACL\_PROF\_HOST\_SYS\_USAGE\_FREQ 。

Atlas 推理系列产品：不支持 ACL\_PROF\_SYS\_IO\_FREQ

Atlas 200I/500 A2 推理产品：不支持

## 枚举项说明如下：

- ACL\_PROF\_STORAGE\_LIMIT ：指定落盘目录允许存放的最大文件容量，有效取 值范围为 [200, 4294967295] ，单位为 MB 。
- ACL\_PROF\_SYS\_HARDWARE\_MEM\_FREQ ：片上内存读写速率、 QoS 传输带宽、 LLC 三级缓存带宽、加速器带宽、 SoC 传输带宽、组件内存占用等的采集频率，范 围 [1,100] ，单位 Hz 。不同产品的采集内容略有差异，请以实际结果为准。已知在 安装有 glibc&lt;2.34 的环境上采集 memory 数据，可能触发 glibc 的一个已知 Bug 19329 ，通过升级环境的 glibc 版本可解决此问题。

Atlas 350 加速卡， Qos 和 SoC 支持的采集频率最大支持配置 10000 ，其他采集项 支持的最大采集频率仍为 100 ，若配置超出范围，其他采集项则按照最大采集频率 100 进行采集。

Atlas 200I/500 A2 推理产品：采集任务结束后，不建议用户增大采集频率，否则 可能导致 SoC 传输带宽数据丢失。

Atlas A2 训练系列产品 /Atlas A2 推理系列产品：采集任务结束后，不建议用户增 大采集频率，否则可能导致 SoC 传输带宽数据丢失。

。

ACL\_PROF\_SYS\_INTERCONNECTION\_FREQ 。

Atlas A3 训练系列产品 /Atlas A3 推理系列产品：采集任务结束后，不建议用户增 大采集频率，否则可能导致 SoC 传输带宽数据丢失。

- ACL\_PROF\_LLC\_MODE ： LLC Profiling 采集事件。要求同时设置 ACL\_PROF\_SYS\_HARDWARE\_MEM\_FREQ 。可以设置为：
- -read ：读事件，三级缓存读速率。
- -write ：写事件，三级缓存写速率。默认为 read 。
- ACL\_PROF\_SYS\_IO\_FREQ ： NIC 、 ROCE 、 UB 带宽数据采集频率，范围 [1,100] ， 单位 Hz 。不同产品的采集内容略有差异，请以实际结果为准。
- ACL\_PROF\_SYS\_INTERCONNECTION\_FREQ ：集合通信带宽数据（ HCCS ）、 PCIe 数据采集开关、片间传输带宽信息采集频率、 SIO 数据、 UB 带宽数据采集开 关，范围 [1,50] ，单位 Hz 。不同产品的采集内容略有差异，请以实际结果为准。
- ACL\_PROF\_DVPP\_FREQ ： DVPP 采集频率，范围 [1,100] 。
- ACL\_PROF\_HOST\_SYS ： Host 侧进程级别的性能数据采集开关，取值包括 cpu 和 mem 。
- ACL\_PROF\_HOST\_SYS\_USAGE ： Host 侧系统和所有进程的性能数据采集开关，取 值包括 cpu 和 mem 。
- ACL\_PROF\_HOST\_SYS\_USAGE\_FREQ ： CPU 利用率、内存利用率的采集频率，范 围 [1,50] 。
