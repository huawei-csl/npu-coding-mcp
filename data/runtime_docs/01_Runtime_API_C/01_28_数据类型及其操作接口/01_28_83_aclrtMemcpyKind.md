# aclrtMemcpyKind

> **Section**: 1.28.83


```
typedef enum aclrtMemcpyKind { ACL_MEMCPY_HOST_TO_HOST,     // Host 内的内存复制 ACL_MEMCPY_HOST_TO_DEVICE,   // Host 到 Device 的内存复制 ACL_MEMCPY_DEVICE_TO_HOST,   // Device 到 Host 的内存复制 ACL_MEMCPY_DEVICE_TO_DEVICE, // Device 内或两个 Device 间的内存复制 ACL_MEMCPY_DEFAULT,          // 由系统根据源、目的内存地址自行判断拷贝方向 ACL_MEMCPY_HOST_TO_BUF_TO_DEVICE,   // Host 到 Device 的内存复制，但 Host 内存会暂存在 Runtime 管 理的缓存中，内存复制接口调用成功后，就可以释放 Host 内存 ACL_MEMCPY_INNER_DEVICE_TO_DEVICE,  // Device 内的内存复制 ACL_MEMCPY_INTER_DEVICE_TO_DEVICE,  // 两个 Device 之间的内存复制 } aclrtMemcpyKind;
```
