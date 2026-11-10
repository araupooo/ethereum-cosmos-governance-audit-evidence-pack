# Ethereum and Cosmos Governance Audit Evidence Pack — Specification

Version 1.1.0 — extends the Multi-Protocol Governance Audit Framework
v1.0.0 (https://github.com/araupooo/multi-protocol-governance-audit-framework)
to one live Ethereum governance system (ENS DAO) and Cosmos Hub.

## 1. Purpose

This pack scores the governance systems of two live systems against a fixed
control catalogue, using only parameters verified against primary sources
(official documentation, governance contracts, executed proposals, and
dated on-chain snapshots). Every scored value carries a citation to the
primary source that establishes it. Where a parameter could not be verified
from a primary source, the profile records it as unverified and the engine
scores it as a partial or failed check rather than inventing a value.

## 2. Scope

| System | Governance system | Chain |
|--------|-------------------|-------|
| ENS DAO | OpenZeppelin Governor + TimelockController (ENSGovernor) | Ethereum Mainnet |
| Cosmos Hub | Cosmos SDK x/gov on-chain governance (gaia) | cosmoshub-4 |

Each profile (`protocols/<name>.json`) records: proposal threshold,
quorum, voting delay, voting period, timelock delay, grace period, execution
path, emergency powers / guardian, and at least one real executed proposal,
each with a citation. Measured concentration and participation come from
`scripts/measure.py` over the dated snapshots in `snapshots/`.

Snapshots: ENS 2026-11-10, Ethereum block 26,353,262 (governor latest
block seen); Cosmos Hub 2026-11-10, block 33,818,316.

## 3. Control catalogue

Six control areas, weights summing to 100, with **27 checks** in total
(A1: 4, A2: 6, A3: 5, A4: 3, A5: 4, A6: 5). New in v1.1.0: A2-6
(voting-power concentration), A3-5 (upgrade authority), A5-4 (time-bounded
veto/cancel), A6-5 (dated snapshot reproducibility). See
`framework/scoring-rubric.md`, `docs/gap-list.md`, and the machine-readable
`framework/rubric.json` (the engine's single source of truth).

Checks are scored pass (1.0), partial (0.5), fail (0.0), or
`not_applicable` (excluded from the area mean, no finding). Area score is
the mean of its applicable checks, scaled to 0–100. The protocol score is
the weighted sum of area scores.

| Area | Control area | Weight | What it tests |
|------|--------------|--------|---------------|
| A1 | Proposal lifecycle & access | 15 | Who can propose, proposer-power maintenance, autonomous path, action bounds |
| A2 | Voting & quorum rules | 20 | Delay, period, quorum definition, differential, cross-source consistency, concentration |
| A3 | Timelock & execution | 20 | Delay, grace period, timelock admin, permissionless execution, upgrade authority |
| A4 | Treasury execution | 15 | Treasury only via timelock, observed outcomes, standing bounds |
| A5 | Emergency powers & guardians | 15 | Pause/cancel exists, powers limited, guardian composition public, time-bounded veto |
| A6 | Transparency & verifiability | 15 | Parameters published, contracts verified, proposal record public, no discrepancies, dated snapshots |

## 4. Scoring rules

- A check is **pass** only when the primary source establishes the control
  fully and the observed record (executed proposals, measured tallies) does
  not contradict it.
- A check is **partial** when the control exists but is incomplete, bounded
  only in part, or verified from a secondary source / by inference.
- A check is **fail** when the control is absent, contradicted by an observed
  event, or the parameter is unverifiable from any primary source.
- A check is **not_applicable** only when the control's premise cannot exist
  in that system. An absent control whose premise does exist still fails.
- Scores are computed by `audit-engine/audit.py` from `framework/rubric.json`
  and the protocol profiles. Scores are never hand-written.

## 5. Severity rules

Each check declares a severity for its fail and partial outcomes in
`rubric.json`. Severity is a property of the control, not of the protocol:

- **High** — the gap can move protocol or treasury funds, remove the
  timelock / quorum protection entirely, or let a small validator set halt
  the chain.
- **Medium** — the gap weakens a protection, creates ambiguity in a core
  parameter, or hides who holds an emergency power.
- **Low** — a documentation, verifiability, or bounded-delegation gap with
  no direct path to fund movement.

## 6. Threat model

See `docs/methodology.md` (8 scenarios, each with an observed instance in
this pack's window).

## 7. Evidence standard

- Every parameter value in a profile cites a primary source by ID; the
  citation table is `citations.md`.
- Every finding is emitted by the engine from a check outcome; the trigger
  command and the observed vs expected values are recorded in `findings.md`.
- Every claim in `claims.md` maps to an evidence file, a script, and an
  output line.
- `scripts/measure.py` computes all measured numbers from snapshots only
  (no network); `scripts/run_all.sh` regenerates all outputs;
  `scripts/clean_reproduce.sh` re-runs from a fresh copy and requires
  byte-identical outputs.
- `docs/index.html` is generated from the engine output by
  `scripts/build_docs.py` and is therefore excluded from `SHA256SUMS`
  (stated here and in the README).

## 8. Limitations (honest)

- Compound's Governor Bravo mainnet address remains unverified from a
  primary source (carried forward from v1.0.0; re-attempted this round).
- ENS per-delegate / top-holder concentration (HHI) was not measured;
  only the delegated share (3.98% of supply) is measured.
- The ENS Governor Nexus social vote total is reported as a displayed
  total only; no quorum verdict is drawn from it.
- EP 6.45 / EP 6.50 vote totals come from a secondary analysis that cites
  on-chain reads.
- Cosmos Hub historical turnout uses the snapshot-date bonded denominator;
  Proposal 1043 (39.72%) is borderline and no quorum verdict is drawn
  from it.
- The Cosmos Hub `proposal_cancel_ratio` semantics were not verified from
  a primary source.
- The engine scores documented parameters and observed proposals; it does
  not re-execute proposals on-chain and does not audit contract source code
  beyond the published parameters.
