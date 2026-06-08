# aclrtMallocAttrType

> **Section**: 1.28.74


typedef enum {

ACL\_RT\_MEM\_ATTR\_RSV = 0,    // 预留值 ACL\_RT\_MEM\_ATTR\_MODULE\_ID,  // 表示模块 ID ACL\_RT\_MEM\_ATTR\_DEVICE\_ID,  // 表示 Device ID ACL\_RT\_MEM\_ATTR\_VA\_FLAG,    // 使用 aclrtMallocHostWithCfg 接口申请 Host 内存时，是否使用 VA

（ virtual address ）一致性功能 } aclrtMallocAttrType;
