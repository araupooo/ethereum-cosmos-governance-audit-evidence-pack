# Audit Report — Cosmos Hub

Governance system: Cosmos SDK x/gov on-chain governance (gaia). Chain: Cosmos Hub (cosmoshub-4).
Governance token: ATOM.

**Overall score: 61.67 / 100**

## Scores by control area

| Area | Control area | Weight | Score / 100 |
|------|--------------|--------|-------------|
| A1 | Proposal lifecycle & access | 15 | 66.67 |
| A2 | Voting & quorum rules | 20 | 58.33 |
| A3 | Timelock & execution | 20 | 50.00 |
| A4 | Treasury execution | 15 | 50.00 |
| A5 | Emergency powers & guardians | 15 | 50.00 |
| A6 | Transparency & verifiability | 15 | 100.00 |

## Verified parameters

| Parameter | Value | Verified | Sources |
|-----------|-------|----------|---------|
| bonded_atom | 341108371.99 ATOM | yes | C-HUB-POOL |
| burn_vote_veto | True boolean | yes | C-HUB-PARAMS |
| expedited_threshold | 0.667 share | yes | C-HUB-PARAMS |
| gov_module_authority | cosmos10d07y265gmmuvt4z0w9aw880jnsr700j6zn9kn address | yes | C-HUB-PROPOSALS |
| max_deposit_period_days | 14 days | yes | C-HUB-PARAMS |
| min_deposit_atom | 500 ATOM | yes | C-HUB-PARAMS |
| proposal_cancel_ratio | 0.5 ratio | yes | C-HUB-PARAMS |
| quorum_share_bonded | 0.4 share of bonded | yes | C-HUB-PARAMS |
| timelock_delay_days | (not stated / not present) days | no | C-HUB-PARAMS, C-HUB-SPEC |
| validators_bonded | 180 validators | yes | C-HUB-VALIDATORS |
| veto_threshold | 0.334 share | yes | C-HUB-PARAMS |
| voting_period_days | 7 days | yes | C-HUB-PARAMS |

### Parameter notes

- **bonded_atom**: Staking pool at snapshot 2026-11-10, block 33,818,316: 341,108,371,985,220 uatom bonded; 13,791,482,657,555 uatom not bonded.
- **burn_vote_veto**: Live params: burn_vote_veto true — deposits of vetoed proposals are burned (observed: 1042, 1045, 1046, 1056 veto-rejected).
- **expedited_threshold**: Live params: expedited threshold 0.667, expedited voting period 259200s (3 days), expedited min deposit 501 ATOM.
- **gov_module_authority**: Authority shown on proposal 1061 messages: cosmos10d07y265gmmuvt4z0w9aw880jnsr700j6zn9kn (the gov module account). Upgrades execute only via passed proposals.
- **max_deposit_period_days**: Live params: max_deposit_period 1209600s = 14 days.
- **min_deposit_atom**: Live params: min_deposit 500,000,000 uatom = 500 ATOM; min_initial_deposit_ratio 0.10 (50 ATOM to submit).
- **proposal_cancel_ratio**: Live params: proposal_cancel_ratio 0.5. Semantics (who may cancel and when) not verified from a primary source.
- **quorum_share_bonded**: Live params: quorum 0.40 — 40% of bonded voting power must vote (all options count toward quorum).
- **timelock_delay_days**: NOT PRESENT: Cosmos Hub governance has no timelock; passed proposals execute without a mandatory delay.
- **validators_bonded**: 180 bonded validators at snapshot; top-1 18.79%, top-4 37.98%, top-10 56.49%, top-33 82.08%, HHI 0.0578 (computed by scripts/measure.py).
- **veto_threshold**: Live params: veto_threshold 0.334 — a proposal is vetoed if NoWithVeto reaches 33.4% of votes.
- **voting_period_days**: Live params: voting_period 604800s = 7 days. The SDK spec's initial value was 2 weeks; the live 7-day value is the governance-set value.

## Per-check verdicts

| Check | Control | Verdict |
|-------|---------|---------|
| A1-1 | Proposal threshold exists and is public | pass |
| A1-2 | Proposer must maintain delegated power through voting | not_applicable |
| A1-3 | Permissionless / autonomous proposal path | pass |
| A1-4 | Actions per proposal bounded | fail |
| A2-1 | Voting delay (review period) >= 1 day | fail |
| A2-2 | Voting period >= 3 days | pass |
| A2-3 | Quorum defined as explicit for-votes threshold | pass |
| A2-4 | Vote-differential / anti-close-call rule | partial |
| A2-5 | Voting period consistent across primary sources | pass |
| A2-6 | Voting-power concentration measured and bounded | fail |
| A3-1 | Timelock delay >= 1 day | fail |
| A3-2 | Grace period defined | fail |
| A3-3 | Timelock admin is the governor | not_applicable |
| A3-4 | Execution is permissionless after delay | pass |
| A3-5 | Upgrade authority path documented and controlled | pass |
| A4-1 | Treasury moves only via timelocked governance | pass |
| A4-2 | No observed treasury transfer outside DAO recall | fail |
| A4-3 | Standing bounds / whitelists on treasury operations | partial |
| A5-1 | Emergency pause / cancel power exists and is documented | partial |
| A5-2 | Emergency powers are limited | partial |
| A5-3 | Guardian composition is public | not_applicable |
| A5-4 | Veto / cancel authority is time-bounded with a renewal path | not_applicable |
| A6-1 | All lifecycle parameters published in official docs | pass |
| A6-2 | Governance contracts verified with published addresses | pass |
| A6-3 | Executed proposal record publicly accessible | pass |
| A6-4 | No unresolved parameter discrepancy across primary sources | pass |
| A6-5 | Dated snapshot reproducibility | pass |

## Findings (this protocol)

### F-01 — High — A2-6 Voting-power concentration measured and bounded

Observed: Top-4 bonded validators hold 37.98% of bonded stake — over the 1/3 Tendermint liveness threshold. Top-1 18.79% (Coinbase01), top-10 56.49%, HHI 0.0578, from the 2026-11-10 bonded-validators snapshot (180 validators).

Expected: Top-10 voter/validator share and HHI (or delegated share) measured from a dated snapshot; top-4 validators/delegates hold under 1/3 of voting power

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-02 — High — A3-1 Timelock delay >= 1 day

Observed: No timelock: a passed proposal executes through the chain (upgrade at a scheduled height, or the message executes on passage). There is no mandatory execution delay after the vote closes.

Expected: Delay >= 1 day, stated in docs

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-03 — High — A4-2 No observed treasury transfer outside DAO recall

Observed: Proposal 1058 passed and moved 1,227,121 ATOM recovered after the Neutron exploit to the Neutron recovery multisig — funds the DAO cannot recall at its own discretion. Proposal 1060 similarly routes community-pool USDC through a community multisig.

Expected: No executed proposal moved funds to an address the DAO cannot recall

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-04 — Medium — A1-4 Actions per proposal bounded

Observed: No maximum number of messages per proposal is stated in the live gov params or the Cosmos SDK gov spec; proposals in the window carry one message type each, but multi-message proposals are not bounded by a documented cap.

Expected: Explicit max actions per proposal (e.g. 10)

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-05 — Medium — A2-1 Voting delay (review period) >= 1 day

Observed: No voting delay: once a proposal reaches the 500 ATOM minimum deposit it enters the voting period immediately. The deposit period (up to 14 days) is the only review window, and it can be as short as the time to fund the deposit.

Expected: Delay >= 1 day, stated in docs

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-06 — Medium — A2-4 Vote-differential / anti-close-call rule

Observed: No vote-differential rule: a proposal passes on >50% yes (excluding abstain) plus 40% quorum. The 33.4% veto threshold is a rejection rule, not a winning-margin rule.

Expected: Winning option must exceed the runner-up by a stated margin

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-07 — Medium — A3-2 Grace period defined

Observed: No grace period: Cosmos Hub governance has no expiry window for passed proposals; the concept does not exist in the gov module.

Expected: Expiry window stated in docs

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-08 — Medium — A5-2 Emergency powers are limited

Observed: Limits on emergency/cancel powers were not verified from a primary source; the cancel parameter exists but its bounds are undocumented in the fetched sources.

Expected: Documented limits: cannot seize funds, cannot unpause, cannot upgrade

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-17 — Low — A4-3 Standing bounds / whitelists on treasury operations

Observed: Each treasury/community-pool transfer needs its own vote; no standing per-operation bounds or whitelists were found in the live params or the sampled proposals.

Expected: Explicit per-operation bounds or whitelists

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

### F-18 — Low — A5-1 Emergency pause / cancel power exists and is documented

Observed: Only the proposal_cancel_ratio parameter (0.5) hints at a cancel path; its semantics were not verified from a primary source. No documented emergency pause power for governance exists.

Expected: Pause and/or cancel power documented

Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS

## Executed proposal (evidence)

- ID: 1059
- Title: Gaia v29.0.0 upgrade
- Date: 2026-10-27
- Outcome: Passed; upgrade scheduled by governance proposal
- Votes for: 167514965005755
- Votes against: 2335547396
- Note: Gaia v29.0.0 upgrade passed 2026-10-27 to 2026-11-03: 167,514,965,005,755 uatom yes (167.51M ATOM), 14,360,797,150 uatom abstain, 2,335,547,396 no, 982,855,548,871 uatom NoWithVeto (0.98M ATOM, 0.58%). Turnout 49.40% of bonded stake at the snapshot denominator (see limitations: historical turnout uses the 2026-11-10 bonded figure).
- Sources: C-HUB-PROPOSALS, C-HUB-PARAMS

## Method

Scored by audit-engine/audit.py from framework/rubric.json and this protocol's profile. Every parameter value cites a primary source; unverified values are recorded as such and scored partial or fail, never invented. See citations.md for the source table.
