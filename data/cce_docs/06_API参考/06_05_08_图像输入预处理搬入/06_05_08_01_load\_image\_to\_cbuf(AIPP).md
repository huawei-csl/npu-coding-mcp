# load\_image\_to\_cbuf (AIPP)

> **Section**: 6.5.8.1


## 功能说明

## 接口原型

## 参数说明

AIPP 是 AI ore 中的输入图像预处理模块。

在 AI 核心中使用 AIPP 对 SoC 有以下好处：

- 如果输入图像数据格式为 YUV420 ，与 RGB888 相比，可以减少一半的带宽消耗。
- 如果输入图像数据格式为 YUV420 ，与 RGB888 相比，可以减少一半的 L2/DDR 内存 占用。

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void load\_image\_to\_cbuf(\_\_cbuf\_\_ half *dst, uint16\_t horSize, uint16\_t verSize, uint16\_t horStartP, uint16\_t verStartP, uint16\_t sHorRes, uint8\_t topPadSize, uint8\_t botPadSize, uint16\_t lPadSize, uint16\_t rPadSize, uint8\_t sid);

void load\_image\_to\_cbuf(\_\_cbuf\_\_ int8\_t *dst, uint16\_t horSize, uint16\_t verSize, uint16\_t horStartP, uint16\_t verStartP, uint16\_t sHorRes, uint8\_t topPadSize, uint8\_t botPadSize, uint16\_t lPadSize, uint16\_t rPadSize, uint8\_t sid);

## 表 6-26 图像预处理参数说明

| 参数名       | 说明           | 取值范围        | 单位   |
|-----------|--------------|-------------|------|
| dst       | 在 L1 中的目标地址。 | /           | /    |
| horSize   | 加载图像的水平尺寸。   | [0, 2^14-1] | 像素   |
| verSize   | 加载图像的竖直尺寸。   | [0, 2^14-1] | 像素   |
| horStartP | 源图像中的水平起始位置。 | [0, 2^13-1] | 像素   |
| verStartP | 源图像中的竖直起始位置。 | [0, 2^13-1] | 像素   |

## 流水类型

| 参数名        | 说明                                                 | 取值范围        | 单位   |
|------------|----------------------------------------------------|-------------|------|
| sHorRes    | 源图像水平分辨率（对于 YUV420/ YUV422 半平面格式和 YUYV 格式， 必须是偶数）。 | [0, 2^17-1] | 像素   |
| topPadSize | 顶部 padding 尺寸。                                     | [0, 32]     | 像素   |
| botPadSize | 底部 padding 尺寸。                                     | [0, 32]     | 像素   |
| lPadSize   | 左边 padding 尺寸。                                     | [0, 32]     | 像素   |
| rPadSize   | 右边 padding 尺寸。                                     | [0, 32]     | 像素   |
| sid        | 用于 SMMU TLB 预取提示的，一般 设为 0 。                        | /           | /    |

PIPE\_MTE2
