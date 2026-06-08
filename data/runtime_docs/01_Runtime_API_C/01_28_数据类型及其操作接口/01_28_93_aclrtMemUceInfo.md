# aclrtMemUceInfo

> **Section**: 1.28.93


#define MAX\_MEM\_UCE\_INFO\_ARRAY\_SIZE 128 #define UCE\_INFO\_RESERVED\_SIZE 14

typedef struct aclrtMemUceInfo {

size\_t len;

void* addr;

size\_t reserved[UCE\_INFO\_RESERVED\_SIZE];

} aclrtMemUceInfo;

| 成员名称     | 描述                                           |
|----------|----------------------------------------------|
| addr     | 内存 UCE 的错误虚拟起始地址。                            |
| len      | 内存大小，单位 Byte 。 从 addr 开始的 len 大小范围内的内存都是异常的。 |
| reserved | 预留参数。                                        |
