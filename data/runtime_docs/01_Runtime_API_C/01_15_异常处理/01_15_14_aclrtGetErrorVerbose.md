# aclrtGetErrorVerbose

> **Section**: 1.15.14


须知：本接口为预留接口，暂不支持。

用于在发生设备故障后获取详细错误信息。此接口必须在获取故障事件之后，提交任 务中止之前调用。

aclError aclrtGetErrorVerbose(int32\_t deviceId, aclrtErrorInfo *errorInfo);

| 参数名      | 输入 / 输 出   | 说明                                               |
|----------|------------|--------------------------------------------------|
| deviceId | 输入         | Device ID 。 与 aclrtSetDevice 接口中 Device ID 保持一致。 |

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 功能说明

## 函数原型

## 参数说明

## 返回值说明

## 功能说明

## 函数原型

| 参数名       | 输入 / 输 出   | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| errorInfo | 输出         | 错误信息。 typedef enum { ACL_RT_NO_ERROR = 0, // 无错误 ACL_RT_ERROR_MEMORY = 1, // 内存错误，暂不支持 ACL_RT_ERROR_L2 = 2, // L2 Cache 二级缓存错误 ACL_RT_ERROR_AICORE = 3, // AI Core 错误 ACL_RT_ERROR_LINK = 4, // 暂不支持 ACL_RT_ERROR_OTHERS = 0xFFFF, // 其它错误 } aclrtErrorType; typedef enum aclrtAicoreErrorType { ACL_RT_AICORE_ERROR_UNKOWN, // 未知错误 ACL_RT_AICORE_ERROR_SW, // 建议排查软件错误 ACL_RT_AICORE_ERROR_HW_LOCAL, // 建议排查当前 Device 的硬件 错误 } aclrtAicoreErrorType; #define ACL_RT_MEM_UCE_INFO_MAX_NUM 20 typedef struct { size_t arraySize; // memUceInfoArray 数组大小 aclrtMemUceInfo memUceInfoArray[ACL_RT_MEM_UCE_INFO_MAX_NUM]; // 内存 UCE 的错误虚拟地址数组 } aclrtMemUceInfoArray; typedef union aclrtErrorInfoDetail { aclrtMemUceInfoArray uceInfo; // 内存 UCE （ uncorrect error ） aclrtAicoreErrorType aicoreErrType; // AI Core 错误 } aclrtErrorInfoDetail; typedef struct aclrtErrorInfo { uint8_t tryRepair; // 是否需要修复， 0 表示无需修复， 1 表示需 修复 uint8_t hasDetail; // 是否有详细报错信息， 0 表示没有， 1 表示 有 uint8_t reserved[2]; // 预留参数 aclrtErrorType errorType; // 错误类型 aclrtErrorInfoDetail detail; // 错误详细信息 } aclrtErrorInfo; |

返回 0 表示成功，返回其他值表示失败，请参见 1.28.1 aclError 。
