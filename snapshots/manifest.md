# Snapshot manifest

All snapshots were fetched 2026-11-10 (UTC) / 2026-11-11 (WIB) and are saved
unedited. Measurements in `outputs/measurements.json` come only from these
files (`scripts/measure.py`, no network).

## Cosmos Hub (cosmoshub-4) — fetched 2026-11-10 19:49 UTC via https://cosmos-rest.publicnode.com

| File | Contents | Block / height |
|------|----------|----------------|
| `cosmoshub-latest-block-2026-11-11.json` | Latest block header | 33,818,316 at 2026-11-10T19:49:46Z |
| `cosmoshub-gov-params-2026-11-11.json` | Live gov params (voting/deposit/tally) | same fetch |
| `cosmoshub-proposals-latest20-2026-11-11.json` | Proposals 1042–1061 with final tallies | same fetch |
| `cosmoshub-staking-pool-2026-11-11.json` | Bonded 341,108,371,985,220 uatom; not bonded 13,791,482,657,555 uatom | same fetch |
| `cosmoshub-validators-bonded-2026-11-11.json` | 180 bonded validators with tokens | same fetch |

Note: the `cosmos/bank/v1beta1/supply/uatom` endpoint returned
`{"code":-32701,"message":"not implemented"}` on this LCD and was not
saved; total ATOM supply is therefore not claimed anywhere in this pack.

## ENS DAO (Ethereum Mainnet) — fetched 2026-11-10 21:05–21:11 UTC

| File | Contents |
|------|----------|
| `ens-docs-governance-process-2026-11-11.html` | ENS docs governance process page (raw HTML) |
| `ens-docs-security-council-2026-11-11.html` | ENS docs security-council page (raw HTML) |
| `ens-docs-ep-5-15-2026-11-11.html` | ENS docs EP 5.15 page (raw HTML) |
| `ens-docs-ep-6-50-2026-11-11.html` | ENS docs EP 6.50 page (raw HTML) |
| `ens-support-official-sites-2026-11-11.html` | ENS official sites support page (raw HTML) |
| `tally-ens-gov-2026-11-11.html` | Tally ENS governance page (raw HTML) |
| `ens-recorded-votes-2026-11-11.json` | Values transcribed from fetched Etherscan / Tally / docs / news pages, one source per value; Ethereum block anchor 26,353,262 (governor latest block seen) |

Etherscan pages (governor, timelock, token) were read via the page fetcher
and are recorded in `ens-recorded-votes-2026-11-11.json` with their URLs;
their raw HTML was not saved because the fetcher returns rendered text.
