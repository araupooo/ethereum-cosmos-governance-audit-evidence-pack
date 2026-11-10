# Worked assessment — Cosmos Hub (cosmoshub-4)

System: Cosmos SDK x/gov on-chain governance (gaia).
Snapshot: 2026-11-10, block 33,818,316, time 2026-11-10T19:49:46Z.
Score: **61.67 / 100** (A1 66.67, A2 58.33, A3 50.00, A4 50.00, A5 50.00, A6 100.00).
Engine report: `protocols/cosmos-hub.md`. Measurements: `outputs/measurements.md`.

## Verified parameters (live on-chain)

| Parameter | Value | Source |
|-----------|-------|--------|
| Voting period | 7 days (604800s) | C-HUB-PARAMS |
| Min deposit | 500 ATOM (min initial 50 ATOM, ratio 0.10) | C-HUB-PARAMS |
| Max deposit period | 14 days (1209600s) | C-HUB-PARAMS |
| Quorum | 40% of bonded voting power | C-HUB-PARAMS |
| Threshold | >50% yes, excluding abstain | C-HUB-PARAMS |
| Veto threshold | 33.4% NoWithVeto | C-HUB-PARAMS |
| Expedited | 3 days, 66.7% threshold, 501 ATOM min deposit | C-HUB-PARAMS |
| Burn rules | burn_vote_veto true; burn_vote_quorum false; burn_proposal_deposit_prevote false | C-HUB-PARAMS |
| Proposal cancel ratio | 0.50 (semantics unverified) | C-HUB-PARAMS |
| Gov module authority | cosmos10d07y265gmmuvt4z0w9aw880jnsr700j6zn9kn | C-HUB-PROPOSALS |
| Bonded stake | 341,108,371.99 ATOM; not bonded 13,791,482.66 ATOM | C-HUB-POOL |
| Timelock | none | C-HUB-PARAMS |

## Proposal lifecycle (measured, proposals 1042–1061)

11 passed, 8 rejected, 1 in voting period (1061, Gaia v29.1.0 upgrade,
height 33935300, voting 2026-11-10 → 2026-11-17). Submission needs a
deposit (50 ATOM to submit, 500 ATOM to enter voting); voting starts
immediately when the deposit is reached — there is no voting delay.

| Proposal | Status | Turnout % bonded | Yes % decided | Veto % | Abstain % |
|----------|--------|------------------|---------------|--------|-----------|
| 1061 | VOTING_PERIOD | 0.00 | 0.00 | 0.00 | 0.00 |
| 1060 | PASSED | 53.43 | 99.98 | 0.00 | 37.60 |
| 1059 | PASSED | 49.40 | 99.42 | 0.58 | 0.01 |
| 1058 | PASSED | 59.01 | 99.72 | 0.01 | 34.20 |
| 1057 | PASSED | 55.76 | 99.94 | 0.02 | 36.19 |
| 1056 | REJECTED | 29.90 | 0.60 | 89.74 | 3.78 |
| 1055 | PASSED | 43.01 | 100.00 | 0.00 | 0.00 |
| 1054 | PASSED | 53.45 | 93.41 | 0.00 | 40.97 |
| 1053 | PASSED | 52.91 | 99.98 | 0.00 | 38.18 |
| 1052 | PASSED | 59.26 | 100.00 | 0.00 | 34.06 |
| 1051 | REJECTED | 28.25 | 99.98 | 0.00 | 28.23 |
| 1050 | REJECTED | 32.74 | 99.99 | 0.01 | 3.76 |
| 1049 | PASSED | 43.62 | 99.99 | 0.00 | 0.00 |
| 1048 | REJECTED | 17.91 | 99.99 | 0.00 | 3.99 |
| 1047 | REJECTED | 18.22 | 99.98 | 0.00 | 4.50 |
| 1046 | REJECTED | 20.76 | 0.00 | 99.99 | 0.00 |
| 1045 | REJECTED | 24.11 | 0.59 | 98.00 | 0.00 |
| 1044 | PASSED | 42.79 | 99.93 | 0.07 | 0.00 |
| 1043 | PASSED | 39.72 | 98.42 | 0.01 | 4.63 |
| 1042 | REJECTED | 31.00 | 0.02 | 99.97 | 0.00 |

Turnout vs bonded stake: min 17.91%, max 59.26%, mean 39.75% — the mean
sits just below the 40% quorum. Turnout uses the 2026-11-10 bonded figure
as the denominator for all proposals; see Limitations.

## Voting power (measured)

180 bonded validators. Top-1 (Coinbase01) 18.79% (64,088,607 ATOM);
top-4 37.98%; top-5 42.15%; top-10 56.49%; top-33 82.08%; HHI 0.0578.
The top 4 validators together exceed the 1/3 Tendermint liveness
threshold: four validators could halt the chain by going offline, and
the top 10 hold an absolute majority of bonded stake.

Top 10 validators by bonded stake:

| Validator | ATOM | Share % |
|-----------|------|---------|
| Coinbase01 | 64,088,607.14 | 18.79 |
| Upbit Staking | 25,239,221.66 | 7.40 |
| Kiln | 23,466,915.99 | 6.88 |
| Kraken03 | 16,762,045.03 | 4.91 |
| Everstake | 14,212,694.97 | 4.17 |
| Binance Node | 10,335,706.18 | 3.03 |
| Blockdaemon | 10,089,260.49 | 2.96 |
| Ledger by Bitwise | 9,818,705.89 | 2.88 |
| Allnodes | 9,786,631.52 | 2.87 |
| Figment | 8,893,780.39 | 2.61 |

## Participation and quorum

Four proposals (1047, 1048, 1050, 1051) were **rejected despite ~99.99%
yes** because turnout (17.91–32.74%) missed the 40% quorum. Quorum, not
opposition, decided them. Four more (1042, 1045, 1046, 1056) were
veto-rejected (NoWithVeto 89.74–99.99%), and their deposits burn
(`burn_vote_veto` is true). A large abstain bloc (~34–41% of votes) recurs
on 1052, 1053, 1054, 1057, 1058, and 1060; which voters abstain was not
attributed — the pattern is reported, the cause is not claimed.

Proposal 1043 passed at 39.72% measured turnout, just under the 40%
quorum line: because the denominator is the snapshot-date bonded figure
rather than bonded stake at vote time, no quorum verdict is drawn from it.

## Timelock and execution controls

There is no timelock and no voting delay. A passed proposal's messages
execute through the chain (upgrades at a scheduled height; other messages
on passage). Proposal 1061 schedules the v29.1.0 upgrade at height
33935300. There is no mandatory review window between the vote closing
and execution, and no expiry window for passed proposals.

## Upgrade authority

Upgrades happen only through passed governance proposals
(`MsgSoftwareUpgrade`, authority = the gov module account). Proposal 1059
(Gaia v29.0.0) passed with 167.51M ATOM yes (49.40% turnout); Proposal
1061 (Gaia v29.1.0) is in voting. The upgrade path itself is controlled;
the missing control is the absence of any delay or veto window after
passage.

## Findings (10: 3 High, 5 Medium, 2 Low)

- F-01 (High, A2-6): top-4 validators hold 37.98% — over the 1/3 liveness threshold.
- F-02 (High, A3-1): no timelock; passed proposals execute without delay.
- F-03 (High, A4-2): Proposal 1058 moved 1,227,121 ATOM to a recovery multisig outside DAO recall.
- F-04 (Medium, A1-4): no maximum messages per proposal.
- F-05 (Medium, A2-1): no voting delay; voting starts as soon as the deposit is reached.
- F-06 (Medium, A2-4): no vote-differential rule.
- F-07 (Medium, A3-2): no grace period / expiry for passed proposals.
- F-08 (Medium, A5-2): limits on cancel/emergency powers unverified.
- F-17 (Low, A4-3): per-proposal bounds only; no standing treasury bounds.
- F-18 (Low, A5-1): cancel path hinted at by `proposal_cancel_ratio` (0.5) but semantics unverified.

## Remediation guidance

1. Add an execution delay (or a post-passage objection window) for
   passed proposals — today a malicious or mistaken proposal can execute
   with no review window after the vote closes.
2. Reduce liveness concentration: the top-4 validators over 1/3 is a
   structural risk no parameter change fixes quickly; delegators should be
   shown the concentration, and large custodial validators' governance
   participation should be disclosed.
3. Do not route community-pool funds through multisigs the DAO cannot
   recall; where a multisig is unavoidable (e.g. exploit recovery), time-box
   it and require a follow-up proposal returning residual funds.
4. Publish the `proposal_cancel_ratio` semantics and the emergency/cancel
   path, or remove the ambiguity by documenting that no cancel power exists.
5. Address quorum fragility: mean turnout (39.75%) sits below quorum
   (40%); four near-unanimous proposals already failed on turnout. Consider
   a lower quorum, turnout incentives, or validator voting disclosure —
   any of which must itself pass governance.
6. Cap messages per proposal and document the cap.
