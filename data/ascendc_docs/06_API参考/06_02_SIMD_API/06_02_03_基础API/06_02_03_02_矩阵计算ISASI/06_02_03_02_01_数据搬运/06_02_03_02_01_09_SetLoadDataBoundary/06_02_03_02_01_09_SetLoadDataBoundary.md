# SetLoadDataBoundary

> **Section**: 6.2.3.2.1.9  
> **PDF Pages**: 1027–1027  

---

<!-- page 1027 -->

```cpp
AscendC::TQue<AscendC::TPosition::A2, 1> inQueueFmA2;// weight queueAscendC::TQue<AscendC::TPosition::B1, 1> inQueueWeB1;AscendC::TQue<AscendC::TPosition::B2, 1> inQueueWeB2;pipe.InitBuffer(inQueueFmA1, 1, featureMapA1Size * sizeof(fmap_T));pipe.InitBuffer(inQueueFmA2, 1, featureMapA2Size * sizeof(fmap_T));pipe.InitBuffer(inQueueWeB1, 1, weightA1Size * sizeof(weight_T));pipe.InitBuffer(inQueueWeB2, 1, weightB2Size * sizeof(weight_T));pipe.InitBuffer(outQueueCO1, 1, dstCO1Size * sizeof(dstCO1_T));
AscendC::LocalTensor<fmap_T> featureMapA1 = inQueueFmA1.DeQue<fmap_T>();AscendC::LocalTensor<weight_T> weightB1 = inQueueWeB1.DeQue<weight_T>();AscendC::LocalTensor<fmap_T> featureMapA2 = inQueueFmA2.AllocTensor<fmap_T>();AscendC::LocalTensor<weight_T> weightB2 = inQueueWeB2.AllocTensor<weight_T>();uint16_t channelSize = 32;uint16_t H = 4, W = 4;uint8_t Kh = 2, Kw = 2;uint16_t Cout = 16;uint16_t C0, C1;uint8_t dilationH = 2, dilationW = 2;
uint8_t padList[PAD_SIZE] = {0, 0, 0, 0};AscendC::SetFmatrix(H, W, padList, FmatrixMode::FMATRIX_LEFT);/*  SetFMatrixBitModeParams param;param.SetL1H(H);param.SetL1W(W);param.SetPadList(padList);AscendC::SetFmatrix(param, FmatrixMode::FMATRIX_LEFT);*/ AscendC::SetLoadDataPaddingValue(0);AscendC::SetLoadDataRepeat({0, 1, 0});AscendC::SetLoadDataBoundary((uint32_t)0);static constexpr AscendC::IsResetLoad3dConfig LOAD3D_CONFIG = {false,false};AscendC::LoadData<fmap_T, LOAD3D_CONFIG>(featureMapA2, featureMapA1,    { padList, H, W, channelSize, k, howoRound, 0, 0, 1, 1, Kw, Kh, dilationW, dilationH, false, false, 0 });AscendC::LoadData(weightB2, weightB1, { 0, weRepeat, 1, 0, 0, false, 0 });
inQueueFmA2.EnQue<fmap_T>(featureMapA2);inQueueWeB2.EnQue<weight_T>(weightB2);inQueueFmA1.FreeTensor(featureMapA1);inQueueWeB1.FreeTensor(weightB1);
```

## 6.2.3.2.1.9 SetLoadDataBoundary

产品支持情况

产品是否支持

Atlas 350 加速卡x

Atlas A3 训练系列产品/Atlas A3 推理系列产品√

Atlas A2 训练系列产品/Atlas A2 推理系列产品√

Atlas 200I/500 A2 推理产品x

Atlas 推理系列产品AI Core√

Atlas 推理系列产品Vector Corex

Atlas 训练系列产品x
