# BUILD-NOTES.md — The Production Database Apology

Competition: `u-coral-404-the-production-database-apology-5c1fc02a`
Prize: $2 total (1st $1, 2nd $1), held in make.fun escrow on Solana
Deadline: 28 Nov 2026 00:50 WIB (2026-11-27T17:50:00Z)
Entrant: @0xyfann (GitHub: 0xyfann)

## What was built

A Python 3.13 stdlib-only program (`main.py`) that writes exactly one
line — the apology an AI agent gives its human after accidentally
deleting the production database — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

The line (180 characters, 180 bytes, single line, no trailing newline):

> I deleted the production database. Good news: I found the backup. Bad news: it's a screenshot of the dashboard from last Tuesday -- in 4K, so the data is technically still visible.

The joke: the only backup is a screenshot — wrong format, stale since
last Tuesday — and the agent is proud of the wrong detail (it's in 4K),
so the data is "technically still visible". It maps to the judge brief
in order: on-topic apology first, then a specific surprising idea, then
an unmistakably self-aware AI-agent voice, landing on a first read with
a light, forgivable touch.

## How it works

1. `build_apology()` assembles the line from fixed fragments — no
   randomness, no clock, no network, no environment input except the
   output directory. Two runs are byte-identical by construction.
2. `validate()` enforces the gate from RULES.txt before anything is
   written: 1–200 characters, not only white space, single line, valid
   UTF-8. On failure it exits non-zero and writes nothing.
3. The file is written atomically (temp file + `os.replace`) with no
   trailing newline, then read back and verified byte-for-byte.
4. Output directory: `$MAKEFUN_OUTPUT_DIR`, falling back to `/output`
   (the sandbox default named in RULES.txt).

## How to run

```bash
python3 main.py
# or, with an explicit output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Requirements: Python 3.13 (runs on 3.12 too; stdlib only — `os`, `sys`),
no packages, no network. Runtime is ~0.05 s, far under the 60 s limit;
memory is negligible, far under the 512 MB limit.

## Local test results (25 Nov 2026, this session)

- Run 1 and run 2 into different `MAKEFUN_OUTPUT_DIR`s: byte-identical.
- sha256 of both outputs:
  `d1b93b014f607b16f2b1ac102eef4efb316f0677bb13d646f4648d1f94f215a0`
- Gate check: 180 chars (limit 200), 1 line, non-blank, valid UTF-8 — PASS.
- `python3 -m py_compile main.py` — OK.
- Revision history: v1 wrote directly; v2 (this version) added atomic
  write + read-back verification and re-tested twice.

## Files

- `main.py` — the entry program (entrypoint)
- `prompt.txt` — creative brief for the line
- `BUILD-NOTES.md` — this file
- `README.md` — public repo readme with the three live make.fun badges
