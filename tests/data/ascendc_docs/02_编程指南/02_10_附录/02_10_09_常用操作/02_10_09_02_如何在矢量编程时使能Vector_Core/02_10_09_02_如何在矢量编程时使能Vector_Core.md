# 如何在矢量编程时使能Vector Core

> **Section**: 2.10.9.2  
> **PDF Pages**: 392–392  

---

<!-- page 392 -->

// 获取算子使用的workspace空间大小aclnnStatus aclnnAddNCustomGetWorkspaceSize(const aclTensorList *srcList, const aclTensor *out, uint64_t *workspaceSize, aclOpExecutor **executor);–算子原型定义中，输入数据的参数类型设置为动态，示例如下。this->Input("srcList")    .ParamType(DYNAMIC)    .DataType({ge::DT_FLOAT16})    .Format({ge::FORMAT_ND});–host侧算子实现，获取动态输入信息的接口，需使用对应的动态接口。

例如，Tiling函数和InferShape函数中，GetDynamicInputShape接口用于获取动态输入的shape信息，InferDataType函数中，GetDynamicInputDataType接口用于获取动态输入的数据类型，示例如下。

```cpp
namespace ge {static graphStatus InferShape(gert::InferShapeContext *context){    const gert::Shape *x1_shape = context->GetDynamicInputShape(0, 0);
    gert::Shape *y_shape = context->GetOutputShape(0);    *y_shape = *x1_shape;
    return GRAPH_SUCCESS;}
```

static graphStatus InferDataType(gert::InferDataTypeContext *context){    const auto inputDataType = context->GetDynamicInputDataType(0, 0);    context->SetOutputDataType(0, inputDataType);    return ge::GRAPH_SUCCESS;}} // namespace ge–kernel侧算子实现，入参需传入动态结构的数据，并使用AscendC::ListTensorDesc结构做解析。

核函数入参需传入动态结构的数据，例如GM_ADDR srcList，示例如下。

extern "C" __global__ __aicore__ void addn_custom(GM_ADDR srcList, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)对传入的参数srcList，需使用AscendC::ListTensorDesc结构做解析，得到每个tensor的具体信息，示例如下。

```cpp
AscendC::ListTensorDesc keyListTensorDescInit((__gm__ void*)srcList);GM_ADDR x = (__gm__ uint8_t*)keyListTensorDescInit.GetDataPtr<__gm__ uint8_t>(0);GM_ADDR y = (__gm__ uint8_t*)keyListTensorDescInit.GetDataPtr<__gm__ uint8_t>(1);
```

## 2.10.9.2 如何在矢量编程时使能Vector Core

针对Atlas 推理系列产品，其硬件架构除了AI Core外，还额外设置了单独的VectorCore，作为AI Core中Vector计算单元的补充，从而缓解Vector计算瓶颈。Vector Core只包括了两种基础计算资源：向量计算单元（Vector Unit）和标量计算单元（ScalarUnit），分别用于完成向量与标量的数据计算。矢量算子开发时，使能Vector Core，算子执行时会同时启动AI Core和Vector Core，这些核并行执行相同的核函数代码。

本节将重点介绍如何使能Atlas 推理系列产品中的Vector Core。学习本节内容之前，建议您先熟悉算子实现、2.10.7 基于样例工程完成Kernel直调、2.10.2 工程化算子开发的相关内容，掌握基于AI Core的算子端到端开发流程。在此基础上本章将重点阐述使能Vector Core时的差异点。具体如下：

1.完成算子kernel侧开发时，需要通过宏KERNEL_TASK_TYPE_DEFAULT使能Vector Core，算子执行时会同时启动AI Core和Vector Core，此时AI Core会当成Vector Core使用。如下的代码样例展示了使能Vector Core的方法：extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *workspace, __gm__ uint8_t *tiling){    GET_TILING_DATA(tilingData, tiling);
