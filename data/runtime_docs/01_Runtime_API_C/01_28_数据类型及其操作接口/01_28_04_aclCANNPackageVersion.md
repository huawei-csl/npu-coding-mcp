# aclCANNPackageVersion

> **Section**: 1.28.4


#define ACL\_PKG\_VERSION\_MAX\_SIZE       128

```
#define ACL_PKG_VERSION_PARTS_MAX_SIZE 64
```

typedef struct aclCANNPackageVersion {

char majorVersion[ACL\_PKG\_VERSION\_PARTS\_MAX\_SIZE];    // 主版本号

char version[ACL\_PKG\_VERSION\_MAX\_SIZE];               // 完整版本号

char minorVersion[ACL\_PKG\_VERSION\_PARTS\_MAX\_SIZE];    // 次版本号

char patchVersion[ACL\_PKG\_VERSION\_PARTS\_MAX\_SIZE];    // 补丁版本号，如果查询不到，就补 0 char reserved[ACL\_PKG\_VERSION\_MAX\_SIZE];

char releaseVersion[ACL\_PKG\_VERSION\_PARTS\_MAX\_SIZE];  // 发布号，如果查询不到，就补 0

} aclCANNPackageVersion;
