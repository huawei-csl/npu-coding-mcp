# GetTransDataMaxMinTmpSize

> **Section**: 6.2.4.10.4  
> **PDF Pages**: 2877–2878  

---

<!-- page 2877 -->

```cpp
204 220 236 252]     [ 13  29  45  61  77  93 109 125 141 157 173 189      205 221 237 253]     [ 14  30  46  62  78  94 110 126 142 158 174 190      206 222 238 254]     [ 15  31  47  63  79  95 111 127 143 159 175 191      207 223 239 255]]]
[[[256 272 288 304 320 336 352 368 384 400 416 432      448 464 480 496]     [257 273 289 305 321 337 353 369 385 401 417 433      449 465 481 497]     [258 274 290 306 322 338 354 370 386 402 418 434      450 466 482 498]     [259 275 291 307 323 339 355 371 387 403 419 435      451 467 483 499]]
[[260 276 292 308 324 340 356 372 388 404 420 436      452 468 484 500]     [261 277 293 309 325 341 357 373 389 405 421 437      453 469 485 501]     [262 278 294 310 326 342 358 374 390 406 422 438      454 470 486 502]     [263 279 295 311 327 343 359 375 391 407 423 439      455 471 487 503]]
[[264 280 296 312 328 344 360 376 392 408 424 440      456 472 488 504]     [265 281 297 313 329 345 361 377 393 409 425 441      457 473 489 505]     [266 282 298 314 330 346 362 378 394 410 426 442      458 474 490 506]     [267 283 299 315 331 347 363 379 395 411 427 443      459 475 491 507]]
[[268 284 300 316 332 348 364 380 396 412 428 444      460 476 492 508]     [269 285 301 317 333 349 365 381 397 413 429 445      461 477 493 509]     [270 286 302 318 334 350 366 382 398 414 430 446      462 478 494 510]     [271 287 303 319 335 351 367 383 399 415 431 447      463 479 495 511]]]]]]
```

## 6.2.4.10.4 GetTransDataMaxMinTmpSize

功能说明

kernel侧TransData接口的计算需要开发者预留/申请临时空间，本接口用于在host侧获取预留/申请的最大最小临时空间大小，开发者基于此范围选择合适的空间大小作为Tiling参数传递到kernel侧使用。

●为保证功能正确，预留/申请的临时空间大小不能小于最小临时空间大小。

●在最小临时空间-最大临时空间范围内，随着临时空间增大，kernel侧接口计算性能会有一定程度的优化提升。为了达到更好的性能，开发者可以根据实际的内存使用情况进行空间预留/申请。该接口最大临时空间当前等于最小临时空间。

函数原型

```cpp
bool GetTransDataMaxMinTmpSize(const platform_ascendc::PlatformAscendC& platform, const ge::Shape& srcShape, const ge::Shape& dstShape,const ge::DataType dataType, const TransDataConfig &config, uint32_t& maxValue, uint32_t& minValue)
```

<!-- page 2878 -->

参数说明

表6-1320接口参数列表

接口输入/输出

功能

platform输入传入硬件平台的信息，PlatformAscendC定义请参见6.4.2.1.2 构造及析构函数。

srcShape输入输入源操作数的shape大小，参数取值与TransData接口的params.srcLayout参数中的shape信息保持一致。

dstShape输入输出目的操作数的shape大小，参数取值与TransData接口的params.dstLayout参数中的shape信息保持一致。

dataType输入输入的数据类型，ge::DataType类型，当前只支持half/float/uint16_t/int16_t数据类型的输入。

config输入数据格式转换的场景，参数取值与TransData接口的config参数保持一致。当前支持的转换场景有：NCDHW ->NDC1HWC0、NDC1HWC0 -> NCDHW、NCDHW ->FRACTAL_Z_3D、FRACTAL_Z_3D -> NCDHW。TransDataConfig类型，具体定义如下。struct TransDataConfig {    DataFormat srcFormat;    DataFormat dstFormat;};

```cpp
enum class DataFormat : uint8_t {    ND = 0,    NZ,    NCHW,    NC1HWC0,    NHWC,    NCDHW,    NDC1HWC0,    FRACTAL_Z_3D,};
```

maxValue输出TransData接口能完成计算所需的最大临时空间大小，超出该值的空间不会被该接口使用。

说明

maxValue仅作为参考值，有可能大于Unified Buffer剩余空间的大小，该场景下，开发者需要根据Unified Buffer剩余空间的大小来选取合适的临时空间大小。

minValue输出TransData接口能完成计算所需最小临时空间大小。为保证功能正确，接口计算时预留/申请的临时空间不能小于该数值。

返回值说明

GetTransDataMaxMinTmpSize返回值为true/false，true表示成功获取TransData接口内部计算需要的最大和最小临时空间大小；false表示获取失败。
