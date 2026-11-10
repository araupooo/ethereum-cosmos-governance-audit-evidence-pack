# Gap list — extending framework v1.0.0 to ENS DAO and Cosmos Hub

Base: Multi-Protocol Governance Audit Framework v1.0.0
(https://github.com/araupooo/multi-protocol-governance-audit-framework):
6 control areas A1–A6, 23 checks, weights sum 100; scored Aave 92.50 /
Compound 86.13 / Uniswap 75.88; 17 findings F-01–F-17.

## System choice

**Ethereum system: ENS DAO** (not Aave, Compound, or Uniswap, which the
framework already covers). Chosen because its governance data is the most
publicly accessible of the candidates considered (Lido DAO, MakerDAO/Sky,
Arbitrum DAO): the governance process, proposal texts, and contract
addresses are published in ENS docs; the Governor, Timelock, and token are
verified contracts on Etherscan; and Tally publishes live delegation,
treasury, and vote totals. Lido was rejected for this round because its
dual-governance design needs a separate control model; MakerDAO/Sky and
Arbitrum DAO because their emergency/upgrade paths (Spell pause, Security
Council + constitutional thresholds) could not be verified to the same
depth in the time available.

**Cosmos Hub** (cosmoshub-4): on-chain governance via the Cosmos SDK x/gov
module, with all parameters, proposals, tallies, and validator stakes
readable from public LCD endpoints with no API key.

## What v1.0.0 does not cover (gaps this pack closes)

| # | Gap | How v1.1.0 closes it |
|---|-----|----------------------|
| G-1 | No voting-power concentration measurement (top-holder / top-voter share, HHI). v1.0.0 scores quorum and thresholds but never measures who holds the votes. | New check **A2-6** (fail High): top-10 share + HHI from a dated snapshot; fail if top-4 exceed 1/3 of voting power. Measured for both systems (`scripts/measure.py`). |
| G-2 | No upgrade-authority check. v1.0.0 never asks who can upgrade the governance contracts or the chain. | New check **A3-5** (fail High): upgrade path must be stated in a primary source and require a passed governance proposal. |
| G-3 | No time-bound on veto/cancel authority. v1.0.0 checks that a guardian exists and is limited, but not that its power expires. | New check **A5-4** (fail Medium): cancel/veto authority must carry an expiry and a documented renewal path. |
| G-4 | No snapshot-reproducibility requirement. v1.0.0 measurements are not tied to dated snapshots with block heights. | New check **A6-5** (fail Medium): every measured dataset saved as a dated snapshot with block height; scripts re-run against it. |
| G-5 | Rubric assumes EVM Governor Bravo / Timelock shapes (voting delay, grace period, timelock admin). Cosmos Hub has no timelock, no voting delay, and deposit-gated proposals. | `not_applicable` outcomes (excluded from area means, no finding) where a control cannot apply: A1-2, A3-3, A5-3, A5-4 for Cosmos Hub. Absent-but-applicable controls still fail (A3-1, A3-2 for Cosmos Hub). |
| G-6 | v1.0.0 has no measured participation tables (turnout per proposal vs quorum). | `scripts/measure.py` computes turnout, yes/veto/abstain shares, and quorum multiples from snapshots; `outputs/measurements.md` is the measured record. |
| G-7 | Compound Governor Bravo mainnet address unverified in v1.0.0 (placeholder limitation carried forward). | Attempted again in this round: a primary source for the Compound Governor Bravo address was NOT found (search returned only Uniswap's reference and secondary write-ups). The limitation is carried forward, unresolved, in the Limitations section. No address is published here. |
| G-8 | v1.0.0 has no social/off-chain proposal tier in scope. ENS runs social proposals (Snapshot, 5 days, 10,000 ENS) alongside executable ones. | Profiles record both tiers; on-chain checks score the executable tier, and social-tier numbers are reported as measured participation, not scored. |

## What is reused unchanged

- The 23 v1.0.0 checks, area weights (A1 15, A2 20, A3 20, A4 15, A5 15, A6 15), and pass/partial/fail scoring.
- `audit-engine/audit.py` (one patch: `not_applicable` checks now emit no finding; v1.0.0 never used that outcome).
- The evidence standard: every parameter cites a primary source; every finding is emitted by the engine; `run_all.sh` / `clean_reproduce.sh` / `verify_digests.sh` reproduce the outputs byte-identically.

## What is NOT carried over

- No v1.0.0 numbers are reused: all measurements here are new, from fresh
  dated snapshots (ENS 2026-11-10, Ethereum block 26,353,262; Cosmos Hub
  2026-11-10, block 33,818,316).
- Aave / Compound / Uniswap are not re-scored here.
