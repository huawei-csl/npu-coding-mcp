# aclrtLaunchKernelAttrId

> **Section**: 1.28.70


typedef enum aclrtLaunchKernelAttrId {

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_DYN\_UBUF\_SIZE = 2, // 用于指定 SIMT 算子执行时需要的 VECTOR CORE 内 部 UB buffer 的大小

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_SCHEM\_MODE = 1,        // 调度模式

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_ENGINE\_TYPE = 3,       // 算子执行引擎

偏移量

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_BLOCKDIM\_OFFSET,       // numBlocks

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_BLOCK\_TASK\_PREFETCH,   // 任务下发时，是否阻止硬件预取本任务的信

息

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_TIMEOUT,               //

} aclrtLaunchKernelAttrId;

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_DATA\_DUMP,             //

是否开启 Dump

任务调度器等待任务执行的超时时间，单位秒

任务调度器等待任务执行的超时时间，单位微秒

ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_TIMEOUT\_US = 8,        //
