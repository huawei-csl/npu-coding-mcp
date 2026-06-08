# aclrtMallocConfig

> **Section**: 1.28.76


typedef struct {

aclrtMallocAttribute* attrs; size\_t numAttrs; } aclrtMallocConfig;

| 成员名称     | 说明                                                |
|----------|---------------------------------------------------|
| attrs    | 属性，本参数是数组，可存放多个属性。类型定义请参 见 aclrtMallocAttribute 。 |
| numAttrs | 属性个数。                                             |
