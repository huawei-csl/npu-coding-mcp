# aclprofEventAttributes

> **Section**: 1.28.18


```
typedef struct { uint16_t version; uint16_t size; uint32_t messageType;   // MESSAGE_TYPE_TENSOR_INFO union Message { aclprofTensorInfo *tensorInfo; } message; } aclprofEventAttributes; typedef struct { uint64_t opNameId;      // 通过 uint64_t aclprofStr2Id(const char *message) 转换 uint64_t opTypeId; uint32_t resv; uint32_t tensorNum; uint32_t kernelType; uint32_t blockNums; void *stream;           // stream 信息 aclprofTensor *tensors; } aclprofTensorInfo; typedef struct { uint32_t type;          // tensor 类型， 0: input, 1: output uint32_t format;        // format 类型 : aclFormat uint32_t dataType;      // dataType 类型 aclDataType uint32_t shapeDim;      // shape dim <= 8 uint32_t shape[8];      // tensor 内存大小 }aclprofTensor; typedef enum{ MESSAGE_TYPE_TENSOR_INFO = 0 }ProfMessageType;
```
