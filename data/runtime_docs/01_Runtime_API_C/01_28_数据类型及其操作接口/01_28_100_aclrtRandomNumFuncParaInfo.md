# aclrtRandomNumFuncParaInfo

> **Section**: 1.28.100


```
typedef struct { aclrtRandomNumFuncType funcType; union { aclrtDropoutBitmaskInfo dropoutBitmaskInfo; aclrtUniformDisInfo uniformDisInfo; aclrtNormalDisInfo normalDisInfo; } paramInfo; } aclrtRandomNumFuncParaInfo;
```

| 成员名称               | 说明                                                   |
|--------------------|------------------------------------------------------|
| funcType           | 函数类别。类型定义请参见 aclrtRandomNumFuncType 。                |
| dropoutBitmaskInfo | Dropout bitmask 信息。类型定义请参见 aclrtDropoutBitmaskInfo 。 |
| uniformDisInfo     | 均匀分布信息。类型定义请参见 aclrtUniformDisInfo 。                 |
| normalDisInfo      | 正态分布信息或截断正态分布信息。类型定义请参见 aclrtNormalDisInfo 。         |
