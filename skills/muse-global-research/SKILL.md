---
name: muse-global-research
description: >
  Use for any China + overseas market research, startup validation, or content
  creator launch research. Fuses deep-research structure, startup validation,
  marketing/SEO, and social outlier research into one stable pipeline with
  tiered RSS sources, fallback chains, and a verified / unverified evidence
  split. Use when the user asks whether a market, idea, topic, or format is
  worth doing, what competitors do, or what to publish to launch an account.
---

# Muse Global Research

> Built for Muse. Language: answer in the user's language (Chinese by default for this user). Reports are concise and scannable, no clickbait.
> Core promise: every round must end with fresh, checkable domestic + overseas evidence — or an explicit "not obtained" list. Never fill a gap with an invented number, a reconstructed curve, or an old summary presented as new.

## When to use

- A market / product / model / format: is it hot, is it worth doing, who already does it?
- A startup idea: market size, competitors, pricing, positioning, GO / PIVOT / KILL.
- A content launch: topics, benchmark accounts, hooks, formats, a 7-day calendar.
- A China vs overseas comparison: same topic, different heat, players, and wording on each side.

Do NOT use this full pipeline for a single live fact (one price, one stock level, one flight). Use the relevant specialist route or the provider page directly, and verify it there.

## Iron rules (they outrank any attractive-looking source)

1. **No invented data.** A failed, blocked, or rate-limited source is "not obtained this round", with its reason. Never pad, never reconstruct, never present an old summary as a current figure.
2. **Three evidence classes, labelled every time:** verified (seen this round, with date), reported (someone else's reporting, with its source), unverified (rumour, inference, uncheckable). Conclusions rest only on verified + clearly labelled reported evidence.
3. **Full price tiers.** Comparison tables always cover cheap / mid / flagship tiers. Flagship-only is an incomplete answer, not a style choice.
4. **China and overseas separately first.** Heat on one side does not imply heat on the other. List evidence per side, then write transferability: what transfers, what does not, and why.
5. **No padded discoveries.** Every round runs a separate new-account / new-format hunt. If nothing qualifies, say "no new discovery this round" plainly.
6. **No follower history without a snapshot.** Public pages show only the current follower count. Growth = current snapshot minus your own baseline snapshot. Before the baseline, growth is "unknown".
7. **Stop on rate limits.** On 429 / 403 / bot-check / route-not-found, stop at that source, switch to its fallback in `sources.yaml`, or mark it not obtained. Do not retry in a loop, do not route around a block with another tool.

## The six-step pipeline

### 1. Frame it in one sentence, then confirm the outline

Before searching, pin down (ask one question if a key item is missing):

- Object: exact product / market / topic / account type
- Decision: build or not, which topic, which format to copy
- Geography: China / overseas / both compared
- Window: last 24h for breakouts + last 7 days by default (30 days for deep reports)
- Output tier: flash table / standard report / deep report (see Delivery)
- Budget: free / low-cost launch vs paid / buildable (this sets the price tiers)

Then draft an outline and, for standard/deep work, confirm it with the user before deep research. This is the two-phase method borrowed from Weizhena/Deep-Research-skills: outline first, investigation second. A vague outline must not be papered over with search results.

### 2. Signal sweep (fast, 15–30 minutes, no deep dives yet)

In order, and stop at "what is hot and what just broke out":

1. **RSS, from `sources.yaml`.** Read Tier A first, then Tier B. Take 3–5 latest titles + dates per side, filter by keyword. Run `scripts/check_feeds.py` when a feed's health is in doubt; its output, not memory, decides whether a feed counts.
2. **Rankings and platform lists.** Bilibili popular, Douyin hot list, GitHub Trending, Hacker News, Product Hunt. Where there is no reliable RSS, use search / browser — never invent a feed URL. When a hot list is used, always compare it with the previous day: new entries, rank rises ≥10, items dropping out of the top 50, and yesterday's rank on every item — never present a bare list with no comparison.
3. **Social signals.** X/Twitter threads (rohunvora/x-research-skill method: follow threads, source the briefing), Bilibili keyword search, Zhihu hot list, Weibo hot search — via current RSSHub routes only after a live test, otherwise via the platform page.
4. **Deduplicate and grade.** Multi-source appearance = "multi-source corroborated". A single-source breakout = "lead to verify", which must go through Step 3 before it becomes a conclusion.

### 3. Deep research (parallel + credibility-scored)

- **Parallelise only splittable work.** If the task splits into independent sub-topics, use one coordinator with one shared output schema, and report coverage (success / total) plus unresolved gaps at the end. Single-topic work does not need this.
- **Credibility tiers.** Tier 1: official / primary (official site, filing, paper, official account). Tier 2: trusted media. Tier 3: creator / media retelling. Tier 4: anonymous rumour. Key numbers (market size, funding, users, price) need Tier 1 or 2, otherwise they go in the unverified list.
- **Broker-grade structure (hoolulu/deep-research method).** Conclusions first, traceable sources, counter-arguments, and scenario forecasts (bull / base / bear) — not a list of advantages.
- **Re-date everything.** Every "latest" figure carries "verified on <date> from <source>". A search snippet's date is not the event's date.

### 4. Startup validation (idea → verdict)

Borrowed and compressed from ferdinandobons/startup-skill (its 8 phases and 30-day plan, not its text):

1. Market: TAM / SAM / SOM, each with its definition and source. If SOM cannot be written, say so; do not substitute TAM.
2. Competitors: 3–7 direct + 1–2 substitutes. For each: positioning, price tiers, channels, content formats, monetisation, top complaints.
3. Buyer and payment: who pays, why now, what drives repeat / renewal, acquisition-cost range (or "range unverified").
4. Moat and risk: copyability, platform-policy risk, copyright risk, supply-chain / compliance risk, one line each.
5. Verdict — exactly one: **GO** (with first step), **PIVOT** (with the new angle), or **KILL** (with the single fatal reason). "Worth watching" is not a verdict.

Use `templates/startup-verdict.md` for the output shape.

### 5. Content launch (research → publishable actions)

Research that does not become publishable actions is unfinished work:

1. **Pillars.** Distil 3–4 content pillars from the research (e.g. tool tests, industry teardowns, new-account watch, failure post-mortems), one representative topic per pillar.
2. **Outlier method (ScrapeCreators method, no API key required for the core path).** For a benchmark account, compare a post's views against that account's own median, not against a celebrity account. A post far above its own median is an outlier; record its hook, format, topic, and date, then look for a repeatable pattern across 2+ outliers.
3. **Comment mining.** From comments on outlier posts, extract questions, objections, pain points, and the audience's own wording. Those become topic angles and titles — quoted, not paraphrased into generic claims.
4. **Hooks and formats (blacktwist method, as a supplement).** Hook (first 3 seconds / first line), single post, thread, carousel, video script, cross-platform rewrite. Every core asset gets at least 2 platform adaptations (Bilibili + Douyin / Xiaohongshu / X, as fits the user).
5. **Creator snapshots (Muse's Bilibili method, generalised).** First sighting creates a baseline: time, account, link, follower count, trigger video, its views. Recheck on cadence; report interval growth and growth since first seen. Thresholds to start from: interval growth ≥1000 followers, or ≥30%, or trending within 24h of first sighting — adjust only when the user changes them. Approximate counts (e.g. shown only in ten-thousands) are labelled "approx." until a precise recheck.
6. **7-day calendar + review metrics.** Topics, formats, platforms, and exactly what to measure (views / engagement / follower growth / conversion). Review uses only the user's own account metrics; a competitor's public numbers never substitute for the user's own performance.
7. **Writing QA (avoid-ai-writing method).** Strip AI-pattern phrasing and template filler from titles and scripts. Note: its detector is calibrated for English; for Chinese copy, borrow the "remove the pattern" checklist, do not quote an English detector score.

Use `templates/creator-brief.md` for the output shape. Promise no follower outcome; state what will be tested and what the next round will look at.

### 6. Delivery (three tiers)

- **Flash:** one table (event / source / date / heat signal / corroborated?) + one judgement line. For daily / per-round screening.
- **Standard:** conclusions first + full-tier comparison + competitor table + risks + next step + unverified list. For build-or-not decisions.
- **Deep:** standard + confirmed outline + full source appendix + counter-arguments + scenario forecasts + 7-day calendar. For a formal report / proposal.

Every tier ends with an "Unverified / not obtained" section. If there is none, write "no unverified key items this round".

Use `templates/report.md` and do not invent a new structure per report.

## Source stability (the part that makes this skill repeatable)

Full rules are in `docs/source-stability.md` and the machine-readable list is `sources.yaml`. The short version:

- **Tier A (verified live, 2026-10-29, via `scripts/check_feeds.py`):** Hacker News (30 items, newest 2026-10-29), TechCrunch (20 items, newest 2026-10-28), The Verge, Ars Technica, Wired, MIT Technology Review, Techmeme, GitHub Blog (all XML with 2026-10-28 items), plus domestic HuXiu (43 items, newest 2026-10-29 10:09 +0800), TMTPost (20 items, 2026-10-29 10:03 +0800), IT Home (60 items, 2026-10-29). Tier A means "passed the last health check", not "will never fail" — re-check weekly.
- **Tier B (documented, test before use):** hnrss filtered Hacker News (2026-10-29 check returned 502 — keep as Tier B, not promoted on a single failure), and RSSHub routes for Bilibili / Weibo / Juejin. Test one item before citing; a documented URL is not a verified feed.
- **Tier C (confirmed dead — do not use as a default):** `rsshub.app/zhihu/hotlist` — 2026-10-29 browser check: the RSSHub site loads, but this route returns "route does not exist or has been deleted", with no feed items. 36Kr direct feed (`https://36kr.com/feed`) — 2026-10-29 direct fetch returned a security-check page, not XML. For both, use the fallback in `sources.yaml` or mark not obtained.
- **Tier D (no stable RSS — use the page, not an invented feed):** WeChat accounts, Xiaohongshu, Douyin single accounts, and most Bilibili single accounts unless a current RSSHub route is live-tested that round.
- **Fallback chain per source:** direct official feed → RSSHub route (live-tested) → alternate RSSHub instance / self-hosted instance → platform page via browser / search → mark not obtained. Never skip straight from a failed feed to a guessed figure.
- **Weekly health check:** run `scripts/check_feeds.py` against `sources.yaml`. Demote a Tier A/B source after two consecutive failed weeks to "under repair"; do not silently keep it in the常用 list.

## Pre-delivery checklist

- [ ] Comparison table has cheap tier, not flagship-only?
- [ ] Every key number has source + date?
- [ ] China / overseas written separately, then transferability?
- [ ] New-discovery section is genuinely new, or plainly says none?
- [ ] Follower growth computed from snapshots, nothing invented before baseline?
- [ ] Unverified / not-obtained list written, with failure reasons?
- [ ] Report concise, scannable, no clickbait conclusion?

## What this skill does not do

- It does not hold API keys for ScrapeCreators, Ryze, or any paid tool. Those are optional accelerators; the core path (RSS + public pages + search + browser) needs no key, and this skill never claims a keyed connection it does not have.
- It does not copy other repositories' SKILL.md files. It borrows their methods and links to them; fetch the latest version from the source repo when a method's detail matters.
- It does not replace Muse's own account analytics: for the user's own accounts, use the connected analytics; for competitors, use public evidence only.
