# Audit Report — ENS DAO

Governance system: OpenZeppelin Governor + TimelockController (ENSGovernor). Chain: Ethereum Mainnet.
Governance token: ENS.

**Overall score: 68.58 / 100**

## Scores by control area

| Area | Control area | Weight | Score / 100 |
|------|--------------|--------|-------------|
| A1 | Proposal lifecycle & access | 15 | 50.00 |
| A2 | Voting & quorum rules | 20 | 66.67 |
| A3 | Timelock & execution | 20 | 80.00 |
| A4 | Treasury execution | 15 | 66.67 |
| A5 | Emergency powers & guardians | 15 | 75.00 |
| A6 | Transparency & verifiability | 15 | 70.00 |

## Verified parameters

| Parameter | Value | Verified | Sources |
|-----------|-------|----------|---------|
| constitutional_approval | 66.67% share of votes | yes | C-ENS-PROCESS |
| delegated_tokens | 3980000 ENS | yes | C-ENS-TALLY |
| governor_address | 0x323A76393544d5ecca80cd6ef2A560C6a395b7E3 address | yes | C-ENS-GOVERNOR, C-ENS-FORUM-TFA |
| grace_period_days | (not stated / not present) days | no | C-ENS-PROCESS |
| max_actions_per_proposal | (not stated / not present) actions | no | C-ENS-PROCESS |
| proposal_threshold_ens | 100000 ENS delegated | yes | C-ENS-PROCESS |
| quorum_for_votes_ens | 1000000 ENS for-votes | yes | C-ENS-PROCESS |
| security_council_threshold | 5-of-8 signatures of 8 | yes | C-ENS-EP650, C-ENS-SECCOUNCIL |
| timelock_address | 0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7 address | yes | C-ENS-TIMELOCK |
| timelock_delay_days | 2 days | yes | C-ENS-PROCESS |
| token_address | 0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72 address | yes | C-ENS-SUPPORT, C-ENS-TOKEN |
| token_supply | 100000000 ENS | yes | C-ENS-TOKEN |
| vote_differential | (not stated / not present) votes | no | C-ENS-PROCESS |
| voting_delay_blocks | 1 blocks | yes | C-ENS-EP515 |
| voting_period_days | 7 days | yes | C-ENS-PROCESS |

### Parameter notes

- **constitutional_approval**: Two-thirds approval required for constitutional amendments (ENS docs).
- **delegated_tokens**: Tally ENS page, 2026-11-10: 3.98M ENS delegated of 100M total supply (3.98%). Only ~4x the 1M quorum is delegated at all.
- **governor_address**: Etherscan: 'ENS: Governance', contract ENSGovernor, verified source, 10,855 transactions; latest block seen 26,353,262. Address also given in the ENS DAO forum Treasury Flow Automation proposal.
- **grace_period_days**: NOT STATED: no grace period stated in ENS docs for the TimelockController; scored partial under A3-2.
- **max_actions_per_proposal**: NOT STATED: no explicit max actions per proposal in ENS docs.
- **proposal_threshold_ens**: Docs: at least 100k ENS (0.1% of supply) delegated to propose an executable proposal; 10,000 ENS for social proposals.
- **quorum_for_votes_ens**: 1% of total supply = 1,000,000 ENS for-votes for executable, social, and constitutional proposals (ENS docs).
- **security_council_threshold**: 5-of-8 for the successor council (EP 6.50, term to 2028-07-16). The docs security-council page still states 4-of-8 for the expired 2024 council — see A6-4.
- **timelock_address**: Etherscan: 'ENS: DAO Wallet', contract TimelockController, verified source; ETH balance 4,499.79 ETH ($9,272,266.06) at snapshot; latest transaction block 26,264,817.
- **timelock_delay_days**: 2-day timelock after a passed executable proposal (ENS docs).
- **token_address**: ENS official support page lists the $ENS token contract; Etherscan: max total supply 100,000,000 ENS, 66,118 holders, circulating 42,309,428 ENS.
- **token_supply**: Max total supply 100,000,000 ENS (Etherscan); circulating 42,309,428 ENS.
- **vote_differential**: NOT PRESENT: no vote-differential rule; simple majority plus 1% quorum.
- **voting_delay_blocks**: 1 block (EP 5.15: 'the voting delay period which is currently set to only one block'); a 24-hour delay is proposed but not in force.
- **voting_period_days**: 7 days on-chain for executable proposals; 5 days on Snapshot for social proposals.

## Per-check verdicts

| Check | Control | Verdict |
|-------|---------|---------|
| A1-1 | Proposal threshold exists and is public | pass |
| A1-2 | Proposer must maintain delegated power through voting | fail |
| A1-3 | Permissionless / autonomous proposal path | partial |
| A1-4 | Actions per proposal bounded | partial |
| A2-1 | Voting delay (review period) >= 1 day | fail |
| A2-2 | Voting period >= 3 days | pass |
| A2-3 | Quorum defined as explicit for-votes threshold | pass |
| A2-4 | Vote-differential / anti-close-call rule | partial |
| A2-5 | Voting period consistent across primary sources | pass |
| A2-6 | Voting-power concentration measured and bounded | partial |
| A3-1 | Timelock delay >= 1 day | pass |
| A3-2 | Grace period defined | partial |
| A3-3 | Timelock admin is the governor | pass |
| A3-4 | Execution is permissionless after delay | pass |
| A3-5 | Upgrade authority path documented and controlled | partial |
| A4-1 | Treasury moves only via timelocked governance | partial |
| A4-2 | No observed treasury transfer outside DAO recall | pass |
| A4-3 | Standing bounds / whitelists on treasury operations | partial |
| A5-1 | Emergency pause / cancel power exists and is documented | pass |
| A5-2 | Emergency powers are limited | pass |
| A5-3 | Guardian composition is public | partial |
| A5-4 | Veto / cancel authority is time-bounded with a renewal path | partial |
| A6-1 | All lifecycle parameters published in official docs | partial |
| A6-2 | Governance contracts verified with published addresses | pass |
| A6-3 | Executed proposal record publicly accessible | pass |
| A6-4 | No unresolved parameter discrepancy across primary sources | fail |
| A6-5 | Dated snapshot reproducibility | pass |

## Findings (this protocol)

### F-09 — Medium — A1-2 Proposer must maintain delegated power through voting

Observed: No proposer-maintenance rule in the OpenZeppelin Governor used by ENS: nothing cancels a proposal if the proposer falls below 100,000 ENS delegated during voting (EP 5.15 discusses only the voting delay, not proposer maintenance).

Expected: Contract cancels the proposal if the proposer falls below threshold

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-10 — Medium — A2-1 Voting delay (review period) >= 1 day

Observed: Voting delay is 1 block (EP 5.15: 'the voting delay period which is currently set to only one block'). EP 5.15 proposes a 24-hour delay; not yet in force at snapshot date.

Expected: Delay >= 1 day, stated in docs

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-11 — Medium — A2-4 Vote-differential / anti-close-call rule

Observed: No vote-differential rule: executable proposals pass on a simple majority plus the 1% quorum. The two-thirds rule for constitutional amendments is an approval threshold, not a differential.

Expected: Winning option must exceed the runner-up by a stated margin

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-12 — Medium — A2-6 Voting-power concentration measured and bounded

Observed: Delegated share measured: 3,980,000 ENS of 100,000,000 (3.98%) delegated (Tally, 2026-11-10). Per-delegate / top-holder concentration (HHI) not measured: Tally delegate voting powers were not captured in the snapshot — disclosed as a limitation.

Expected: Top-10 voter/validator share and HHI (or delegated share) measured from a dated snapshot; top-4 validators/delegates hold under 1/3 of voting power

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-13 — Medium — A3-5 Upgrade authority path documented and controlled

Observed: Upgrade path is via passed executable proposals through the governor/timelock (docs: executable proposals can upgrade an ENS core contract), but the controlling authority for the ENS root and the pending Governor Nexus changes were not verified as a single documented path.

Expected: Who can upgrade the governance contracts / chain (and at what height or delay) is stated in a primary source and the path requires a passed governance proposal

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-14 — Medium — A4-1 Treasury moves only via timelocked governance

Observed: Treasury moves mostly via timelocked governance, but the Treasury Flow Automation proposal grants Karpatkey a scoped permission to send ETH/USDC to wallet.ensdao.eth without a proposal; the timelock keeps a 6-month USDC runway (~$8M).

Expected: Treasury controlled only through the timelock

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-15 — Medium — A6-1 All lifecycle parameters published in official docs

Observed: Voting delay (1 block) is stated only in EP 5.15, not in the main governance-process doc; the timelock grace period is not stated anywhere in ENS docs.

Expected: Every parameter (threshold, quorum, delay, period, timelock, grace) stated

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-16 — Medium — A6-4 No unresolved parameter discrepancy across primary sources

Observed: Direct discrepancy: docs.ens.domains/dao/security-council states a 4-of-8 council, while EP 6.50 (July 2026) seated a 5-of-8 council for a term to 2028-07-16.

Expected: All primary sources agree on all parameters

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-19 — Low — A1-3 Permissionless / autonomous proposal path

Observed: No live autonomous/bond proposal path. EP 5.15 (social, passed) approves a 1,000 ENS ProposalBond design in principle; it is not implemented, so the 100,000 ENS threshold remains the only gate.

Expected: Any address can lock a small amount to create an autonomous proposal, or equivalent

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-20 — Low — A1-4 Actions per proposal bounded

Observed: No explicit max actions per proposal stated in ENS docs. Payloads are bounded in practice only by block gas limits; no stated max verified.

Expected: Explicit max actions per proposal (e.g. 10)

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-21 — Low — A3-2 Grace period defined

Observed: No grace period stated in ENS docs for the OpenZeppelin TimelockController; whether queued operations expire was not verified from a primary source at audit time.

Expected: Expiry window stated in docs

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-22 — Low — A4-3 Standing bounds / whitelists on treasury operations

Observed: Standing bound exists in part: the Treasury Flow Automation policy keeps a 6-month runway (~$8M USDC) in the timelock. No per-operation whitelist or cap schedule was verified.

Expected: Explicit per-operation bounds or whitelists

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-23 — Low — A5-3 Guardian composition is public

Observed: New council members are named individuals (EP 6.50) and the 5-of-8 threshold is published, but the official docs page still describes the expired 4-of-8 council, so the published composition is inconsistent across primary sources.

Expected: Multisig threshold and signers published

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

### F-24 — Low — A5-4 Veto / cancel authority is time-bounded with a renewal path

Observed: New council term runs to 2028-07-16 with an expiry mechanism carried from the 2024 design, but the docs page still describes the old council whose authority expired 2026-07-24; the renewal path was demonstrated (EP 6.45 defeated, EP 6.50 re-founded) rather than documented as a rule.

Expected: Cancel/veto authority carries an expiry and a documented renewal path (re-vote / re-election)

Evidence: C-ENS-CAPER, C-ENS-EP515, C-ENS-EP650, C-ENS-FORUM-TFA, C-ENS-GOVERNOR, C-ENS-PROCESS, C-ENS-SECCOUNCIL, C-ENS-SUPPORT, C-ENS-TALLY, C-ENS-TIMELOCK, C-ENS-TOKEN

## Executed proposal (evidence)

- ID: 6.50
- Title: Security Council successor election and grant (EP 6.50)
- Date: 2026-07-20
- Outcome: Passed 4,228,716 for vs 94,526 against; council seated for a term to 2028-07-16
- Votes for: 4228716
- Votes against: 94526
- Note: EP 6.50 elected the successor Security Council and granted it PROPOSER_ROLE on the timelock. Execution is confirmed by on-chain reads (new council contract holds PROPOSER_ROLE at block 25,710,457). The preceding renewal EP 6.45 was defeated 3,859,981 against vs 1,137,702 for.
- Sources: C-ENS-EP650, C-ENS-CAPER

## Method

Scored by audit-engine/audit.py from framework/rubric.json and this protocol's profile. Every parameter value cites a primary source; unverified values are recorded as such and scored partial or fail, never invented. See citations.md for the source table.
