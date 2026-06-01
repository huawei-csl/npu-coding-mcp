# wait\_flag\_dev

> **Section**: 6.6.6.4


## 功能说明

和ff ts\_cross\_core\_sync 配套使用（通过fl agID 关联），用于等待所有同步对象到达 flagID 对应的同步点。

void wait\_flag\_dev(int64\_t flagID);

## 表 6-38 参数说明

| 参数名    | 说明   | 取值范围    | 单位   |
|--------|------|---------|------|
| flagID | 事件标号 | [0, 15] | /    |

PIPE\_S
