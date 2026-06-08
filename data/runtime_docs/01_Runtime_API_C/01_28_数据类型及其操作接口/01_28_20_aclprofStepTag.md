# aclprofStepTag

> **Section**: 1.28.20


typedef enum{

```
ACL_STEP_START = 0, // step  start ACL_STEP_END = 1    // step  end } aclprofStepTag;
```

![Figure](../../images/figure_6435.png)

**[Image: figure_6435.png (157x46, 4.7KB)]**

同一个 aclprofStepInfo 对象、同一个 tag 只能设置一次，否则 Profiling 解析会出错。
