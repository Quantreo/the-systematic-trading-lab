---
type: index
---

# Strategies : register

> **What this is** : every strategy ever opened, alive or dead, one line each. The book (what actually has a weight) is the [[Strategy Table]].
> **Open it** : when you open or close a strategy, and at the monthly review.
> **Folders** : a strategy's folder is its status. Changing status = moving the note. `Killed/` is never emptied: a dead strategy is evidence.

| Strategy | Family | Status | Version | Sharpe net (honest) | Opened | Last decision | Sheet |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FOMC Drift | Event-driven | **Killed** 2025-10-29 | v2 (6-leg basket) | 0.78 full sample, negative 2025-26 | 2024-06 | drawdown stop fired | [[FOMC Drift]] |
| Crypto XS Momentum | Trend (XS) | **Testing** (paper, half weight) | v2 (top 20 PIT) | 0.74 (t 1.7) | 2026-08 | keep on paper, judge against the book | [[Crypto XS Momentum]] |
| TSMOM 12-Month Trend | Trend | **Testing** (Pass 1 written, Pass 2 open) | v1 | | 2026-09 | Pass 2 to do | [[TSMOM 12-Month Trend]] |

## The four statuses
- **Testing** : Pass 1 written, being built and judged.
- **Live** : in the book, with a weight in the [[Strategy Table]] and a monitoring note.
- **Parked** : put on hold, not killed. The idea may still be right, but something is missing (data, a condition, a mechanism for a surprise). The sheet says what would bring it back.
- **Killed** : the kill or exit criterion fired. The sheet stays, forever: a dead strategy is evidence.

## Lifecycle
```
Testing ──keep──▶ Live ──exit criterion──▶ Killed
   │                │
   ├──park──▶ Parked ┘ (can come back to Testing)
   └──kill──▶ Killed
```
