# 过时 API 对照表

审查代码时，如发现以下已废弃的 API，请标记为"不通过"并给出替换建议。

## pandas

| 已废弃 | 替换为 | 废弃版本 | 说明 |
|--------|--------|---------|------|
| `DataFrame.append()` | `pd.concat([df1, df2])` | 1.4.0 | append 在 2.0 中已移除 |
| `DataFrame.swaplevel()` 无参数 | 显式传入 `i, j` 参数 | 1.5.0 | 未来版本不再支持隐式参数 |

## numpy

| 已废弃 | 替换为 | 废弃版本 | 说明 |
|--------|--------|---------|------|
| `np.bool` | `np.bool_` 或 `bool` | 1.20.0 | 内置类型别名已移除 |
| `np.int` | `np.int_` 或 `int` | 1.20.0 | 同上 |
| `np.float` | `np.float64` 或 `float` | 1.20.0 | 同上 |
| `np.object` | `np.object_` 或 `object` | 1.20.0 | 同上 |

> 此表需要持续维护——每当库发布新版本时，检查 Release Notes 中的 Deprecation 部分并更新。
