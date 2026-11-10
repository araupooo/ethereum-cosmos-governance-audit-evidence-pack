# Findings — Ethereum and Cosmos Governance Audit Evidence Pack

Total: 24 findings — 3 High, 13 Medium, 8 Low.
Every finding is emitted by the audit engine from a rubric check outcome.
Trigger for every finding: `bash scripts/run_all.sh`

## Severity-ranked findings

### F-01 — High — Cosmos Hub — A2-6 Voting-power concentration measured and bounded

- Outcome: fail
- Observed: Top-4 bonded validators hold 37.98% of bonded stake — over the 1/3 Tendermint liveness threshold. Top-1 18.79% (Coinbase01), top-10 56.49%, HHI 0.0578, from the 2026-11-10 bonded-validators snapshot (180 validators).
- Expected: Top-10 voter/validator share and HHI (or delegated share) measured from a dated snapshot; top-4 validators/delegates hold under 1/3 of voting power
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-02 — High — Cosmos Hub — A3-1 Timelock delay >= 1 day

- Outcome: fail
- Observed: No timelock: a passed proposal executes through the chain (upgrade at a scheduled height, or the message executes on passage). There is no mandatory execution delay after the vote closes.
- Expected: Delay >= 1 day, stated in docs
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-03 — High — Cosmos Hub — A4-2 No observed treasury transfer outside DAO recall

- Outcome: fail
- Observed: Proposal 1058 passed and moved 1,227,121 ATOM recovered after the Neutron exploit to the Neutron recovery multisig — funds the DAO cannot recall at its own discretion. Proposal 1060 similarly routes community-pool USDC through a community multisig.
- Expected: No executed proposal moved funds to an address the DAO cannot recall
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-04 — Medium — Cosmos Hub — A1-4 Actions per proposal bounded

- Outcome: fail
- Observed: No maximum number of messages per proposal is stated in the live gov params or the Cosmos SDK gov spec; proposals in the window carry one message type each, but multi-message proposals are not bounded by a documented cap.
- Expected: Explicit max actions per proposal (e.g. 10)
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-05 — Medium — Cosmos Hub — A2-1 Voting delay (review period) >= 1 day

- Outcome: fail
- Observed: No voting delay: once a proposal reaches the 500 ATOM minimum deposit it enters the voting period immediately. The deposit period (up to 14 days) is the only review window, and it can be as short as the time to fund the deposit.
- Expected: Delay >= 1 day, stated in docs
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-06 — Medium — Cosmos Hub — A2-4 Vote-differential / anti-close-call rule

- Outcome: partial
- Observed: No vote-differential rule: a proposal passes on >50% yes (excluding abstain) plus 40% quorum. The 33.4% veto threshold is a rejection rule, not a winning-margin rule.
- Expected: Winning option must exceed the runner-up by a stated margin
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-07 — Medium — Cosmos Hub — A3-2 Grace period defined

- Outcome: fail
- Observed: No grace period: Cosmos Hub governance has no expiry window for passed proposals; the concept does not exist in the gov module.
- Expected: Expiry window stated in docs
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-08 — Medium — Cosmos Hub — A5-2 Emergency powers are limited

- Outcome: partial
- Observed: Limits on emergency/cancel powers were not verified from a primary source; the cancel parameter exists but its bounds are undocumented in the fetched sources.
- Expected: Documented limits: cannot seize funds, cannot unpause, cannot upgrade
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-09 — Medium — ENS DAO — A1-2 Proposer must maintain delegated power through voting

- Outcome: fail
- Observed: No proposer-maintenance rule in the OpenZeppelin Governor used by ENS: nothing cancels a proposal if the proposer falls below 100,000 ENS delegated during voting (EP 5.15 discusses only the voting delay, not proposer maintenance).
- Expected: Contract cancels the proposal if the proposer falls below threshold
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-10 — Medium — ENS DAO — A2-1 Voting delay (review period) >= 1 day

- Outcome: fail
- Observed: Voting delay is 1 block (EP 5.15: 'the voting delay period which is currently set to only one block'). EP 5.15 proposes a 24-hour delay; not yet in force at snapshot date.
- Expected: Delay >= 1 day, stated in docs
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-11 — Medium — ENS DAO — A2-4 Vote-differential / anti-close-call rule

- Outcome: partial
- Observed: No vote-differential rule: executable proposals pass on a simple majority plus the 1% quorum. The two-thirds rule for constitutional amendments is an approval threshold, not a differential.
- Expected: Winning option must exceed the runner-up by a stated margin
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-12 — Medium — ENS DAO — A2-6 Voting-power concentration measured and bounded

- Outcome: partial
- Observed: Delegated share measured: 3,980,000 ENS of 100,000,000 (3.98%) delegated (Tally, 2026-11-10). Per-delegate / top-holder concentration (HHI) not measured: Tally delegate voting powers were not captured in the snapshot — disclosed as a limitation.
- Expected: Top-10 voter/validator share and HHI (or delegated share) measured from a dated snapshot; top-4 validators/delegates hold under 1/3 of voting power
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-13 — Medium — ENS DAO — A3-5 Upgrade authority path documented and controlled

- Outcome: partial
- Observed: Upgrade path is via passed executable proposals through the governor/timelock (docs: executable proposals can upgrade an ENS core contract), but the controlling authority for the ENS root and the pending Governor Nexus changes were not verified as a single documented path.
- Expected: Who can upgrade the governance contracts / chain (and at what height or delay) is stated in a primary source and the path requires a passed governance proposal
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-14 — Medium — ENS DAO — A4-1 Treasury moves only via timelocked governance

- Outcome: partial
- Observed: Treasury moves mostly via timelocked governance, but the Treasury Flow Automation proposal grants Karpatkey a scoped permission to send ETH/USDC to wallet.ensdao.eth without a proposal; the timelock keeps a 6-month USDC runway (~$8M).
- Expected: Treasury controlled only through the timelock
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-15 — Medium — ENS DAO — A6-1 All lifecycle parameters published in official docs

- Outcome: partial
- Observed: Voting delay (1 block) is stated only in EP 5.15, not in the main governance-process doc; the timelock grace period is not stated anywhere in ENS docs.
- Expected: Every parameter (threshold, quorum, delay, period, timelock, grace) stated
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-16 — Medium — ENS DAO — A6-4 No unresolved parameter discrepancy across primary sources

- Outcome: fail
- Observed: Direct discrepancy: docs.ens.domains/dao/security-council states a 4-of-8 council, while EP 6.50 (July 2026) seated a 5-of-8 council for a term to 2028-07-16.
- Expected: All primary sources agree on all parameters
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-17 — Low — Cosmos Hub — A4-3 Standing bounds / whitelists on treasury operations

- Outcome: partial
- Observed: Each treasury/community-pool transfer needs its own vote; no standing per-operation bounds or whitelists were found in the live params or the sampled proposals.
- Expected: Explicit per-operation bounds or whitelists
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-18 — Low — Cosmos Hub — A5-1 Emergency pause / cancel power exists and is documented

- Outcome: partial
- Observed: Only the proposal_cancel_ratio parameter (0.5) hints at a cancel path; its semantics were not verified from a primary source. No documented emergency pause power for governance exists.
- Expected: Pause and/or cancel power documented
- Evidence: C-HUB-PARAMS, C-HUB-POOL, C-HUB-PROPOSALS, C-HUB-SPEC, C-HUB-VALIDATORS
- Trigger: `bash scripts/run_all.sh`

### F-19 — Low — ENS DAO — A1-3 Permissionless / autonomous proposal path

- Outcome: partial
- Observed: No live autonomous/bond proposal path. EP 5.15 (social, passed) approves a 1,000 ENS ProposalBond design in principle; it is not implemented, so the 100,000 ENS threshold remains the only gate.
- Expected: Any address can lock a small amount to create an autonomous proposal, or equivalent
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-20 — Low — ENS DAO — A1-4 Actions per proposal bounded

- Outcome: partial
- Observed: No explicit max actions per proposal stated in ENS docs. Payloads are bounded in practice only by block gas limits; no stated max verified.
- Expected: Explicit max actions per proposal (e.g. 10)
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-21 — Low — ENS DAO — A3-2 Grace period defined

- Outcome: partial
- Observed: No grace period stated in ENS docs for the OpenZeppelin TimelockController; whether queued operations expire was not verified from a primary source at audit time.
- Expected: Expiry window stated in docs
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-22 — Low — ENS DAO — A4-3 Standing bounds / whitelists on treasury operations

- Outcome: partial
- Observed: Standing bound exists in part: the Treasury Flow Automation policy keeps a 6-month runway (~$8M USDC) in the timelock. No per-operation whitelist or cap schedule was verified.
- Expected: Explicit per-operation bounds or whitelists
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-23 — Low — ENS DAO — A5-3 Guardian composition is public

- Outcome: partial
- Observed: New council members are named individuals (EP 6.50) and the 5-of-8 threshold is published, but the official docs page still describes the expired 4-of-8 council, so the published composition is inconsistent across primary sources.
- Expected: Multisig threshold and signers published
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

### F-24 — Low — ENS DAO — A5-4 Veto / cancel authority is time-bounded with a renewal path

- Outcome: partial
- Observed: New council term runs to 2028-07-16 with an expiry mechanism carried from the 2024 design, but the docs page still describes the old council whose authority expired 2026-07-24; the renewal path was demonstrated (EP 6.45 defeated, EP 6.50 re-founded) rather than documented as a rule.
- Expected: Cancel/veto authority carries an expiry and a documented renewal path (re-vote / re-election)
- Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN
- Trigger: `bash scripts/run_all.sh`

## Findings by protocol

- Cosmos Hub: F-01, F-02, F-03, F-04, F-05, F-06, F-07, F-08, F-17, F-18
- ENS DAO: F-09, F-10, F-11, F-12, F-13, F-14, F-15, F-16, F-19, F-20, F-21, F-22, F-23, F-24
