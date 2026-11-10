# Worked assessment — ENS DAO (Ethereum Mainnet)

System: OpenZeppelin Governor + TimelockController (`ENSGovernor`).
Snapshot: 2026-11-10, Ethereum block 26,353,262 (governor latest block seen).
Score: **68.58 / 100** (A1 50.00, A2 66.67, A3 80.00, A4 66.67, A5 75.00, A6 70.00).
Engine report: `protocols/ens.md`. Measurements: `outputs/measurements.md`.

## Verified parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Governor | 0x323A76393544d5ecca80cd6ef2A560C6a395b7E3 (`ENSGovernor`, verified) | C-ENS-GOVERNOR |
| Timelock / DAO Wallet | 0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7 (`TimelockController`, verified) | C-ENS-TIMELOCK |
| Token | 0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72, 100,000,000 ENS max supply | C-ENS-TOKEN, C-ENS-SUPPORT |
| Proposal threshold (executable) | 100,000 ENS delegated (0.1% of supply); social 10,000 ENS | C-ENS-PROCESS |
| Quorum | 1% = 1,000,000 ENS for-votes (all proposal types) | C-ENS-PROCESS |
| Voting period | 7 days on-chain; 5 days on Snapshot | C-ENS-PROCESS |
| Voting delay | 1 block | C-ENS-EP515 |
| Timelock delay | 2 days | C-ENS-PROCESS |
| Approval | Simple majority; constitutional amendments two-thirds | C-ENS-PROCESS |
| Security Council | 5-of-8 (EP 6.50, term to 2028-07-16); docs page still says 4-of-8 | C-ENS-EP650, C-ENS-SECCOUNCIL |

## Proposal lifecycle

Draft (forum) → draft PR (governance-docs repo) → Snapshot (social) or
governor `propose()` (executable) → 7-day on-chain vote → 2-day timelock
→ execution. The timelock held 4,499.79 ETH ($9,272,266.06) at snapshot;
Tally reports a $50.58M treasury. 77 proposals exist on Tally; none was
active at snapshot time.

## Voting power and participation (measured)

Only **3,980,000 ENS (3.98% of supply)** is delegated at all. Quorum
(1,000,000 ENS) is 25.13% of delegated supply — a single holder of 1%
of supply can meet quorum alone if they vote.

| Vote | For | Against | Abstain | Total | % of supply | Quorum multiple |
|------|-----|---------|---------|-------|-------------|-----------------|
| EP 6.50 grant | 4,228,716 | 94,526 | — | 4,323,242 | 4.32 | 4.32x |
| EP 6.45 renewal | 1,137,702 | 3,859,981 | 1,761 | 4,999,444 | 5.00 | 5.00x |
| [7.2] Meta-Gov Term 7 (Oct 30) | 1,470,000 | 0 | 15,000 | 1,485,000 | 1.49 | 1.49x |
| [7.2] Meta-Gov Term 7 (Oct 21) | — | — | — | 1,100,000 displayed | — | — |
| [7.3] Governor Nexus Update | — | — | — | 516,480 displayed | — | — |

The two on-chain votes both cleared quorum by 4–5x, but total turnout was
only 4–5% of supply. The renewal EP 6.45 was defeated (77.2% against) and
the successor council was then re-founded by EP 6.50 (97.8% for) — the
governance process worked as designed, but it took two full votes to
replace an expiring veto authority.

## Quorum and thresholds

Quorum is met comfortably on the sampled on-chain votes (4.32x, 5.00x),
but the margin is thin in absolute terms: the Oct 30 social vote totalled
1.48M (1.49x quorum) with only 59 addresses voting. With 3.98% of supply
delegated, quorum is structurally easy to meet — and structurally easy for
a small number of large delegates to meet alone. Per-delegate concentration
(HHI) was not measured (limitation).

## Timelock and execution controls

Passed executable proposals queue in the TimelockController for 2 days
and can then be executed by any address. The Security Council holds
PROPOSER_ROLE on the timelock and can cancel queued operations only;
it cannot move funds, propose, or amend. The old council's authority
expired 2026-07-24 (unix 1784919179); the new 5-of-8 council's term runs
to 2028-07-16.

## Upgrade authority

Executable proposals can upgrade ENS core contracts through the
governor/timelock. A pending Governor Nexus update (social vote [7.3],
Oct 29, 2026) would add three proposal types (Standard, Optimistic, Bond),
a 2-day delay for migration proposals, and a conditional 48-hour voting
extension; it is not yet in force and is not scored as live.

## Findings (14: 0 High, 8 Medium, 6 Low)

- F-09 (Medium, A1-2): no proposer-maintenance rule in the OZ Governor.
- F-10 (Medium, A2-1): voting delay is 1 block; a 24-hour delay is proposed (EP 5.15) but not in force.
- F-11 (Medium, A2-4): no vote-differential rule.
- F-12 (Medium, A2-6): only 3.98% of supply delegated; per-delegate concentration unmeasured.
- F-13 (Medium, A3-5): upgrade path via governor is documented, but the root authority and pending Nexus changes are not verified as one path.
- F-14 (Medium, A4-1): Karpatkey holds a scoped permission to move ETH/USDC without a proposal.
- F-15 (Medium, A6-1): voting delay stated only in EP 5.15; grace period not stated anywhere.
- F-16 (Medium, A6-4): docs say 4-of-8 council; EP 6.50 seated a 5-of-8 council.
- F-19 (Low, A1-3): no live autonomous/bond proposal path; EP 5.15 approves the design only.
- F-20 (Low, A1-4): no stated max actions per proposal.
- F-21 (Low, A3-2): no grace period verified for the timelock.
- F-22 (Low, A4-3): standing bounds exist only in part (6-month runway policy).
- F-23 (Low, A5-3): council composition is inconsistent across primary sources.
- F-24 (Low, A5-4): renewal path demonstrated in practice, not documented as a rule.

## Remediation guidance

1. Enact the EP 5.15 voting delay (24 hours) before the Governor Nexus
   upgrade lands — a 1-block delay leaves no review window between
   proposal creation and the voting snapshot.
2. Fix the docs security-council page to state the 5-of-8 council, its
   members, and the 2028-07-16 term; a stale emergency-power page is
   itself a finding (F-16).
3. Implement the ProposalBond (EP 5.15) so the 100,000 ENS threshold is
   not the only gate to proposing.
4. Publish the timelock grace period (or state that queued operations do
   not expire) and a max-actions bound.
5. Narrow or time-box the Karpatkey no-vote transfer permission, and
   publish per-operation caps.
6. Publish per-delegate voting power so concentration can be measured;
   3.98% delegation means quorum is decided by very few addresses.
