# aclrtMemcpyBatchAttr

> **Section**: 1.28.82


typedef struct {

aclrtMemLocation srcLoc;

aclrtMemLocation dstLoc;

uint8\_t rsv[16];

} aclrtMemcpyBatchAttr;

| 成员名称   | 说明                                  |
|--------|-------------------------------------|
| dstLoc | 目的内存所在位置。类型定义请参见 aclrtMemLocation 。 |
| srcLoc | 源内存所在位置。类型定义请参见 aclrtMemLocation 。  |
| rsv    | 预留参数，当前固定配置为 0 。                    |
