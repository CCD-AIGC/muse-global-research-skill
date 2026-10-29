# muse-global-research-skill

> **Built for Muse** — Muse 的国内外市场调研 / 创业验证 / 内容起号调研 Skill。
> Made for Muse, compatible with Claude Code, Codex, Cursor and any agent that supports the [Agent Skills](https://agentskills.io) spec.

一个 Skill，解决三个问题：**国外市场怎么看、创业想法能不能做、内容起号抄什么格式**——而且要求每一次都拿到**国内 + 国外、最新、可核查**的数据源，而不是凭记忆拼结论。

## 为什么是这个 Skill，而不是再列一堆仓库

市面上很多高星 Skill 各管一环：深度调研管报告结构、营销库管文案 SEO、创业库管验证、社媒库管爆款。但单独用任何一个，都会出现三个老问题：

1. **数据源不稳定**：某个 RSS 今天能读、明天 403，后天路由被删，报告却还写它“可用”。
2. **国内外混写**：国外热就默认国内也能火，国内热就默认国外也有人做。
3. **结论无法复核**：数字没有来源和日期，粉丝增长没有快照基线，失败的源被悄悄跳过。

这个仓库把它们融成一条稳定链路：

```
定题 → 信号扫（RSS + 热榜 + 平台）→ 深挖（大纲确认 + 并行 + 可信度打分）
→ 创业验证（GO / PIVOT / KILL）→ 起号落点（支柱 + 钩子 + 7 天日历）→ 带“未核实清单”的交付
```

每一步失败都有降级路径，见 `docs/source-stability.md`。

## 快速开始

### 给 Muse 用（推荐）

把 `skills/muse-global-research/` 复制到你的 Muse 自定义 Skill 目录，例如：

```bash
cp -r skills/muse-global-research ~/workspace/custom-skills/
```

之后调研时直接说：“按 muse-global-research 做一次调研”，Muse 会按 `SKILL.md` 的流程走，不需要你每次贴提示词。

### 给 Claude Code / Codex 用

```bash
# Claude Code
cp -r skills/muse-global-research ~/.claude/skills/

# Codex
mkdir -p ~/.codex/skills
cp -r skills/muse-global-research ~/.codex/skills/
```

### 先测数据源稳不稳（不需要任何 API Key）

```bash
python3 scripts/check_feeds.py --config skills/muse-global-research/sources.yaml
```

脚本只用 Python 标准库。它会逐条抓 feed，判断返回的是不是 XML、有没有最新条目、日期是不是新鲜的；403、HTML 安全检测页、路由不存在都会被标为失败，不会假装成功。用法和输出格式见 `scripts/README.md`（脚本内含说明）。

## 仓库结构

```
skills/muse-global-research/
  SKILL.md            # 主流程：什么时候用、六步法、铁律、交付模板
  sources.yaml        # 分层数据源：已实测 / 文档记载待实测 / 已确认失效 / 无 RSS 走页面
  sources.opml        # 可直接导入 RSS 阅读器的订阅清单（只含已实测 + 文档记载项，失效项已剔除）
  templates/
    report.md         # 标准 / 深度报告模板
    startup-verdict.md# 创业 GO / PIVOT / KILL 模板
    creator-brief.md  # 起号选题简报模板
scripts/
  check_feeds.py      # RSS 健康检查：XML 校验、日期新鲜度、失败分级
docs/
  source-stability.md # 数据源稳定链路：主源 → 镜像 → 页面回退 → 标注未拿到
```

## 数据源分层（2026-10-29 核查，之后以实测为准）

| 层 | 含义 | 例子 |
|---|---|---|
| A 已实测 | 2026-10-29 当天脚本抓到 XML 且条目新鲜 | Hacker News、TechCrunch、The Verge、Ars、Wired、MIT Tech Review、Techmeme、GitHub Blog、虎嗅、钛媒体、IT之家 |
| B 文档记载，待实测 | 官方 / 搜索清单给出地址，但本轮未逐条实测或当轮失败 | hnrss 过滤版（10-29 返回 502）、RSSHub 各路由 |
| C 已确认失效 | 实测返回错误页 / 安全检测页，**不要再默认可用** | `rsshub.app/zhihu/hotlist`（路由不存在）、36氪直连 feed（安全检测页） |
| D 无稳定 RSS | 不编 feed 地址，走平台页 / 搜索 / 浏览器核查 | 微信公众号、小红书、抖音单账号、B站单账号（部分可用 RSSHub 路由，须实测） |

完整清单、每条的回退动作和每周复查规则在 `sources.yaml` 和 `docs/source-stability.md` 里。**不要把 B 层写成“已验证”，不要把 C 层写进常用清单。**

## 融合来源（只借方法论，不复制原文）

本 Skill 的方法论融合自以下高星仓库（星数与更新时间为 2026-10-29 GitHub 核查，主力一般 ≥1000 星）：

- 深度调研：Weizhena/Deep-Research-skills（★2438，两阶段大纲确认）、199-biotechnologies/claude-deep-research-skill（★1202，可信度打分）、hoolulu/deep-research（★605，中文券商级结构，星数不足 1000 但中文覆盖独特，列为补充）
- 创业验证：ferdinandobons/startup-skill（★1233，竞品 battle card、定位、财务预测、30 天计划）
- 营销：coreyhaines31/marketingskills（★57133，CRO、文案、SEO、增长）、irinabuht12-oss/marketing-skills（★6079）
- 社媒调研：ScrapeCreators/social-media-research-skills（★5014，爆款帖、评论挖掘、竞品与广告拆解；官方需 API Key，本 Skill 的核心路径不需要它）
- SEO：AgriciDaniel/claude-seo（★23407）、zubair-trabzada/geo-seo-claude（★11330）
- 写作质检：conorbronsdon/avoid-ai-writing（★5298，去 AI 套路；按英文校准，中文只借思路）
- 海外信号：rohunvora/x-research-skill（★1241）
- 基础设施：DIYgod/RSSHub（★46705）

需要某个方法的原文时，按上面名字去 GitHub 取最新版，不要把旧版本当现况。

## 交付标准

每次调研结束前必须自查：

- [ ] 对比表含便宜档、中档、旗舰档，不只旗舰
- [ ] 每个关键数字有来源 + 日期
- [ ] 国内 / 国外分开写结论，再写可迁移性
- [ ] 无新发现时直说，不拿老账号充数
- [ ] 粉丝增长用快照相减，基线之前写“未知”
- [ ] 结尾有“未核实 / 未拿到”清单，含失败原因

## License

MIT。见 `LICENSE`。
