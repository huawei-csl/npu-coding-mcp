# img2colv2\_cbuf\_to\_cb

> **Section**: 6.5.7.3


## 功能说明

## 接口原型

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ half *dst, \_\_cbuf\_\_ half *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ uint32\_t *dst, \_\_cbuf\_\_ uint32\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ int32\_t *dst, \_\_cbuf\_\_ int32\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ float *dst, \_\_cbuf\_\_ float *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ uint8\_t *dst, \_\_cbuf\_\_ uint8\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ int8\_t *dst, \_\_cbuf\_\_ int8\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_ca(\_\_ca\_\_ bfloat16\_t *dst, \_\_cbuf\_\_ bfloat16\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

## // dst 和 src 在此处为 b4 类型的数据

void img2colv2\_cbuf\_to\_ca\_s4(\_\_ca\_\_ void *dst, \_\_cbuf\_\_ void *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

该接口将卷积核从 L1 搬运到 L0B 上。在搬运过程中将 Co*Wk*Hk*Ci 大小的卷积核按照 Co 维度展开，展开后的每一列大小为 Ci*Wk*Hk ，共有 Co 列的二维矩阵。

- Co 表示卷积核个数，也就是输出通道数；
- Wk 表示卷积核的水平尺寸；
- Hk 表示卷积核的竖直尺寸；
- Ci 表示输入通道数；

## // 相同接口的不同原型区别在于源地址和目的地址的数据类型不同

void img2colv2\_cbuf\_to\_cb(\_\_cb\_\_ float *dst, \_\_cbuf\_\_ float *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_cb(\_\_cb\_\_ uint32\_t *dst, \_\_cbuf\_\_ uint32\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

## 流水类型

void img2colv2\_cbuf\_to\_cb(\_\_cb\_\_ int32\_t *dst, \_\_cbuf\_\_ int32\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_cb(\_\_cb\_\_ half *dst, \_\_cbuf\_\_ half *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

void img2colv2\_cbuf\_to\_cb(\_\_cb\_\_ bfloat16\_t *dst, \_\_cbuf\_\_ bfloat16\_t *src, uint16\_t stepK, uint16\_t stepM, uint16\_t posK, uint16\_t posM, uint8\_t strideW, uint8\_t strideH, uint8\_t Wk, uint8\_t Hk, uint8\_t dilationW, uint8\_t dilationH, bool filterW, bool filterH, bool transpose, bool fmatrixCtrl, uint16\_t sizeChannel);

PIPE\_MTE1
