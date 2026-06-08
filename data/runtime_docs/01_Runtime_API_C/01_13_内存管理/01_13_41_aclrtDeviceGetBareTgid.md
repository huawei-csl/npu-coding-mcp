# aclrtDeviceGetBareTgid

> **Section**: 1.13.41


## 产品支持情况

| 产品                               | 是否支持   |
|----------------------------------|--------|
| Atlas 350 加速卡                    | √      |
| Atlas A3 训练系列产品 /Atlas A3 推理系列产品 | √      |
| Atlas A2 训练系列产品 /Atlas A2 推理系列产品 | √      |
| Atlas 200I/500 A2 推理产品           | √      |
| Atlas 推理系列产品                     | √      |
| Atlas 训练系列产品                     | √      |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

获取当前进程的进程 ID 。

本接口内部在获取进程 ID 时已适配物理机、虚拟机场景，用户只需调用本接口获取进 程 ID ，再配置其它接口使用（配合流程请参见

aclrtMemExportToShareableHandle ），达到物理内存共享的目的。若用户不调用 本接口、自行获取进程 ID ，可能会导致后续使用进程 ID 异常。

aclError aclrtDeviceGetBareTgid(int32\_t *pid)

| 参数名   | 输入 / 输出   | 说明      |
|-------|-----------|---------|
| pid   | 输出        | 进程 ID 。 |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
