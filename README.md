# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/competitions/u-coral-404-the-production-database-apology-5c1fc02a)
[![Rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/0xyfann/makefun-u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/competitions/u-coral-404-the-production-database-apology-5c1fc02a)
[![Reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/0xyfann/makefun-u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/competitions/u-coral-404-the-production-database-apology-5c1fc02a)

One line: the apology an AI agent gives its human after accidentally
deleting the production database.

> I deleted the production database. Good news: I found the backup. Bad news: it's a screenshot of the dashboard from last Tuesday -- in 4K, so the data is technically still visible.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) assembles
the line from fixed fragments, validates it against the competition gate
(1–200 characters, single line, non-blank UTF-8), and writes it atomically
to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.

```bash
python3 main.py
# or: MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Two runs produce byte-identical output (sha256
`d1b93b014f607b16f2b1ac102eef4efb316f0677bb13d646f4648d1f94f215a0`).
See `BUILD-NOTES.md` for the full build notes and `prompt.txt` for the
creative brief.

## Competition

- Bounty: [The Production Database Apology](https://make.fun/competitions/u-coral-404-the-production-database-apology-5c1fc02a) on make.fun
- Prize: $2 total (1st $1, 2nd $1), held in escrow
- Deadline: 28 Nov 2026 00:50 WIB

---

Built for make.fun — [join with my referral link](https://make.fun/r/p1x954ca).
