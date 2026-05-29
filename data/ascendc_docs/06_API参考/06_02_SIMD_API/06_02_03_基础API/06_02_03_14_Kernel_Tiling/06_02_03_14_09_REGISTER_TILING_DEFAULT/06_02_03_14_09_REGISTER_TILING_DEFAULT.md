# REGISTER_TILING_DEFAULT

> **Section**: 6.2.3.14.9  
> **PDF Pages**: 1988–1988  

---

<!-- page 1988 -->

if (workspace == nullptr) {        return;    }    KernelAdd op;    KERNEL_TASK_TYPE_DEFAULT(KERNEL_TYPE_MIX_AIC_1_1);    op.Init(x, y, z, tilingData.numBlocks, tilingData.totalLength, tilingData.tileNum);    // 当TilingKey为1或2时，执行Process1；为3或4时，执行Process2    if (TILING_KEY_LIST(1,2)) {        op.Process1();    } else if (TILING_KEY_LIST(3,4)) {        KERNEL_TASK_TYPE(4, KERNEL_TYPE_MIX_AIC_1_2);        op.Process2();    }     // 其他代码逻辑    ...    // 此处示例当TilingKey为3或4时，会执行ProcessOther    if (TILING_KEY_LIST(3,4)) {        op.ProcessOther();    }}

配套的Host侧Tiling函数示例（伪代码）：

ge::graphStatus TilingFunc(gert::TilingContext* context){    // 其他代码逻辑    ...    if (context->GetInputShape(0) > 10) {        context->SetTilingKey(1);    } else if (some condition) {        context->SetTilingKey(2);    } else if (some condition) {        context->SetTilingKey(3);    } else if (some condition) {        context->SetTilingKey(4);    }}

## 6.2.3.14.9 REGISTER_TILING_DEFAULT

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Core√

Atlas 训练系列产品x

功能说明

用于在kernel侧注册用户使用标准C++语法自定义的默认TilingData结构体。
