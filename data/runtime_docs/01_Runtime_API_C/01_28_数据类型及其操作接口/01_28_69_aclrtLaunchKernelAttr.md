# aclrtLaunchKernelAttr

> **Section**: 1.28.69


typedef struct aclrtLaunchKernelAttr { aclrtLaunchKernelAttrId id; aclrtLaunchKernelAttrValue value; } aclrtLaunchKernelAttr;

Launch Kernel 时，每个属性是由属性标识 aclrtLaunchKernelAttr.id 及其对应的属性值 aclrtLaunchKernelAttr.value 组成，例如， aclrtLaunchKernelAttr.id 为 ACL\_RT\_LAUNCH\_KERNEL\_ATTR\_SCHEM\_MODE 时， aclrtLaunchKernelAttr.value 需 根据 schemMode 的取值来配置。

aclrtLaunchKernelAttr.id 的定义请参见 aclrtLaunchKernelAttrId 。

aclrtLaunchKernelAttr.value 的定义请参见 aclrtLaunchKernelAttrValue 。
