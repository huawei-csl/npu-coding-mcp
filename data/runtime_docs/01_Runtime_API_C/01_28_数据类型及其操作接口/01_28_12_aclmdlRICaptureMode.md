# aclmdlRICaptureMode

> **Section**: 1.28.12


typedef enum {

ACL\_MODEL\_RI\_CAPTURE\_MODE\_THREAD\_LOCAL, // 当前线程禁止调用非安全函数

ACL\_MODEL\_RI\_CAPTURE\_MODE\_GLOBAL = 0,   // 全局禁止，所有线程都不可以调用非安全函数

ACL\_MODEL\_RI\_CAPTURE\_MODE\_RELAXED,      // 全局不禁止，所有线程都可以调用非安全函数 } aclmdlRICaptureMode;
