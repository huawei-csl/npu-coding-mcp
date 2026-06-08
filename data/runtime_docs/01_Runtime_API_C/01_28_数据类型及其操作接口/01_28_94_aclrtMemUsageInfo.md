# aclrtMemUsageInfo

> **Section**: 1.28.94


typedef struct aclrtMemUsageInfo {

char name[32];          // 组件名称 uint64\_t curMemSize;    // 当前占用的内存大小，单位 Byte uint64\_t memPeakSize;   // 该组件的峰值内存，单位 Byte size\_t reserved[8];     // 预留参数 } aclrtMemUsageInfo;
