# Evidence index — claims → source / script / output

See `claims.md` for the full claim-to-evidence index (C-01–C-18). This
page is the short map from each scored area to where its evidence lives.

## ENS DAO

| Area | Evidence |
|------|----------|
| A1 lifecycle | ENS docs process page (`snapshots/ens-docs-governance-process-2026-11-11.html`); EP 5.15 (`snapshots/ens-docs-ep-5-15-2026-11-11.html`) |
| A2 voting/quorum | ENS docs process page; Tally page (`snapshots/tally-ens-gov-2026-11-11.html`); measurements (`outputs/measurements.md`, script `scripts/measure.py`) |
| A3 timelock/execution | Etherscan governor + timelock pages (recorded in `snapshots/ens-recorded-votes-2026-11-11.json`); ENS docs process page |
| A4 treasury | Tally treasury figure; ENS forum Treasury Flow Automation post (C-ENS-FORUM-TFA); Etherscan DAO Wallet balance |
| A5 emergency powers | ENS docs security-council page; EP 6.50 page (`snapshots/ens-docs-ep-6-50-2026-11-11.html`) |
| A6 transparency | All of the above; finding F-16 records the 4-of-8 vs 5-of-8 discrepancy |

## Cosmos Hub

| Area | Evidence |
|------|----------|
| A1 lifecycle | Live gov params (`snapshots/cosmoshub-gov-params-2026-11-11.json`); proposals file (`snapshots/cosmoshub-proposals-latest20-2026-11-11.json`) |
| A2 voting/quorum | Live gov params; proposals file; validators file (`snapshots/cosmoshub-validators-bonded-2026-11-11.json`); measurements (`outputs/measurements.md`, script `scripts/measure.py`) |
| A3 timelock/execution | Live gov params (no timelock parameter exists); proposals file (upgrade heights, e.g. 1061 at height 33935300) |
| A4 treasury | Proposals file (1058: 1,227,121 ATOM to Neutron recovery multisig; 1060: community-pool USDC via multisig) |
| A5 emergency powers | Live gov params (`proposal_cancel_ratio` 0.5; semantics unverified) |
| A6 transparency | Live LCD endpoints (no API key); snapshot manifest (`snapshots/manifest.md`) |

## Reproduction

- `bash scripts/run_all.sh` — measure + engine + checks + digests
- `bash scripts/clean_reproduce.sh` — fresh-copy re-run; must report MATCH
- `bash scripts/verify_digests.sh` — `sha256sum -c SHA256SUMS`
