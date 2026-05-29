# show_kernel_debug_data工具

> **Section**: 2.10.5  
> **PDF Pages**: 356–357  

---

<!-- page 356 -->

```cpp
DynamicInputOutputInfo input(kInput, dynamic_input_name_dense_defaults.c_str(),      dynamic_input_name_dense_defaults.size(), dynamic_input_attr_name_dense_defaults.c_str(),      dynamic_input_attr_name_dense_defaults.size());
  value.push_back(input);
  const std::string dynamic_output_name_sparse_indices = "sparse_indices";
  const std::string dynamic_output_attr_name_sparse_indices = "num_sparse";
  DynamicInputOutputInfo output(kOutput,       dynamic_output_name_sparse_indices.c_str(),      dynamic_output_name_sparse_indices.size(), dynamic_output_attr_name_sparse_indices.c_str(),      dynamic_output_attr_name_sparse_indices.size());
  value.push_back(output);
  const std::string dynamic_output_name_sparse_values = "sparse_values";
  const std::string dynamic_output_attr_name_sparse_values = "sparse_types";
  DynamicInputOutputInfo output1(kOutput,       dynamic_output_name_sparse_values.c_str(),      dynamic_output_name_sparse_values.size(), dynamic_output_attr_name_sparse_values.c_str(),      dynamic_output_attr_name_sparse_values.size());
  value.push_back(output1);
  const std::string dynamic_output_name_sparse_shapes = "sparse_shapes";
  const std::string dynamic_output_attr_name_sparse_shapes = "sparse_types";
  DynamicInputOutputInfo output2(kOutput,       dynamic_output_name_sparse_shapes.c_str(),      dynamic_output_name_sparse_shapes.size(), dynamic_output_attr_name_sparse_shapes.c_str(),      dynamic_output_attr_name_sparse_shapes.size());
  value.push_back(output2);
  const std::string dynamic_output_name_dense_values = "dense_values";
  const std::string dynamic_output_attr_name_dense_values = "Tdense";
  DynamicInputOutputInfo output3(kOutput,       dynamic_output_name_dense_values.c_str(),      dynamic_output_name_dense_values.size(), dynamic_output_attr_name_dense_values.c_str(),      dynamic_output_attr_name_dense_values.size());
  value.push_back(output3);
  AutoMappingByOpFnDynamic(op_src, op, value);
  return SUCCESS;}
// register ParseSingleExample op to GEREGISTER_CUSTOM_OP("ParseSingleExample")    .FrameworkType(TENSORFLOW)    .OriginOpType("ParseSingleExample")    .ParseParamsByOperatorFn(ParseSingleExampleMapping)    }
```

说明

暂不支持同时有可选输入和动态输入的算子映射。

## 2.10.5 show_kernel_debug_data 工具

在Ascend C算子程序代码中，用户可以使用AscendC::DumpTensor、AscendC::printf、AscendC::PrintTimeStamp、ascendc_assert接口打印相关调试信息，并通过“Runtime运行时 API > 初始化和去初始化 > aclInit”或直接配置acl.json文件，启用Dump配置，导出Ascend C算子Kernel的调测信息。本工具提供了对调测信息的离线解析能力，帮助用户获取并解析调试信息，即将导出的bin文件解析成可读格式。本工具的使用示例可参考show_kernel_debug_data样例。

说明

show_kernel_debug_data支持多用户并发调用，但用户需要指定不同的落盘路径，否则可能出现落盘内容被覆盖等问题。

<!-- page 357 -->

产品支持情况

产品是否支持

Atlas 350 加速卡√

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品√

Atlas 推理系列产品√

Atlas 训练系列产品x

工具安装

步骤1安装工具。

工具跟随CANN软件包发布（参考环境准备完成CANN安装），其路径默认为“${INSTALL_DIR}/tools/show_kernel_debug_data”，其中${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

步骤2设置环境变量。

●root用户安装Ascend-cann-toolkit包时source /usr/local/Ascend/cann/set_env.sh

●非root用户安装Ascend-cann-toolkit包时source ${HOME}/Ascend/cann/set_env.sh

步骤3检查工具是否安装成功。

执行如下命令，若能正常显示--help或-h信息，则表示工具环境正常，功能可正常使用。show_kernel_debug_data -h

**----结束**

使用方法

●命令行方式show_kernel_debug_data <bin_file_path> [<output_path>]

参数可选/必选说明

<bin_file_path>

必选kernel侧调试信息落盘的bin文件或包含bin文件的目录路径，例如“/input/dump_workspace.bin”。

<output_path>

可选解析结果的保存路径，例如“/output_dir”。默认是当前命令行执行目录下。
