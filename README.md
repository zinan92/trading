<div align="center">

# Trading

**A locked map of the Trading universe.**

</div>

---

Market data, research, trader methodologies, backtesting, execution infrastructure, research interfaces, full systems and knowledge collections.

This registry is generated from the canonical private registry at [zinan92/park-operating-system](https://github.com/zinan92/park-operating-system), snapshot `github-universe-2026-08-26`.

## Contract

| Field | Meaning |
|---|---|
| Primary home | This repo is the only primary home for each listed source repo |
| Source | `owned` or `starred` provenance is preserved |
| Lock | External repos point to a fixed commit SHA, not a live branch |
| Private | Private source names and links may be visible, but access may return 404 |
| History | Archived and removed entries remain auditable |

## Contents

- `snapshot.yaml` — generated scoped snapshot and export checksum
- `entries/` — owned, starred and archived projections
- `locks/` — external commit locks copied from Park OS
- `tags.yaml` — approved tag vocabulary
- `scripts/verify-scoped.sh` — generated-data verifier

Run the verifier before changing or publishing this registry:

```bash
bash scripts/verify-scoped.sh
```

The registry validates catalog integrity. It does not certify any listed product as production-ready.

