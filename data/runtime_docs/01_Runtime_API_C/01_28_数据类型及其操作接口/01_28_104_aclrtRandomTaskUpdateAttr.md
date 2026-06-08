# aclrtRandomTaskUpdateAttr

> **Section**: 1.28.104


typedef struct { void *srcAddr;

size\_t size; uint32\_t rsv[4]; } aclrtRandomTaskUpdateAttr;

| 成员名称    | 说明                                                                                                                                                        |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| srcAddr | 存放待刷新数据的 Device 内存地址，需按照 aclrtRandomNumTaskInfo 结构体组织数据，且仅支持 更新该结构体内的 randomParaAddr 、 randomResultAddr 、 randomCounterAddr 、 randomSeed 、 randomNum 参数值。 |
| size    | 内存大小，单位 Byte 。                                                                                                                                            |
| rsv     | 预留参数。当前固定配置为 0 。                                                                                                                                          |
