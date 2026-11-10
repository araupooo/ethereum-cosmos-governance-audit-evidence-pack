# Methodology — framework v1.1.0 (extended)

Base: Multi-Protocol Governance Audit Framework v1.0.0
(https://github.com/araupooo/multi-protocol-governance-audit-framework).
This pack extends it to one Ethereum system (ENS DAO) and Cosmos Hub.

## Control catalogue

Six control areas, weights summing to 100, with **27 checks** in total
(A1: 4, A2: 6, A3: 5, A4: 3, A5: 4, A6: 5). Checks are scored pass (1.0),
partial (0.5), fail (0.0), or `not_applicable` (excluded from the area mean
and emitting no finding). Area score is the mean of its applicable checks,
scaled to 0–100. The protocol score is the weighted sum of area scores.
See `framework/scoring-rubric.md` and the machine-readable
`framework/rubric.json` (the engine's single source of truth).

New in v1.1.0 (see `docs/gap-list.md`): A2-6 voting-power concentration,
A3-5 upgrade authority, A5-4 time-bounded veto/cancel, A6-5 dated
snapshot reproducibility.

## Scoring rules

- A check is **pass** only when the primary source establishes the control
  fully and the observed record (executed proposals, measured tallies) does
  not contradict it.
- A check is **partial** when the control exists but is incomplete, bounded
  only in part, or verified from a secondary source / by inference.
- A check is **fail** when the control is absent, contradicted by an observed
  event, or the parameter is unverifiable from any primary source.
- A check is **not_applicable** only when the control's premise cannot exist
  in that system (e.g. no timelock means no timelock admin; no guardian
  means no guardian composition). An absent control whose premise does
  exist still fails.
- Scores are computed by `audit-engine/audit.py` from
  `framework/rubric.json` and the protocol profiles. Scores are never
  hand-written.

## Severity rules

Severity is a property of the control, not of the protocol:

- **High** — the gap can move protocol or treasury funds, remove the
  timelock / quorum protection entirely, or let a small validator set halt
  the chain.
- **Medium** — the gap weakens a protection, creates ambiguity in a core
  parameter, or hides who holds an emergency power.
- **Low** — a documentation, verifiability, or bounded-delegation gap with
  no direct path to fund movement.

## Threat model (extends v1.0.0)

1. **Treasury raid by narrow majority** (v1.0.0): a bloc just over quorum
   moves treasury funds outside DAO recall. Observed here: Cosmos Hub
   Proposal 1058 moved 1,227,121 ATOM to a recovery multisig.
2. **Parameter ambiguity**: two primary sources state different values for
   the same parameter. Observed here: ENS docs state a 4-of-8 Security
   Council while EP 6.50 seated a 5-of-8 council.
3. **Guardian capture / unaccountable emergency power** (v1.0.0): an
   emergency actor can cancel without a published identity, limit, or
   expiry. Observed here: ENS's old council authority expired 2026-07-24
   while the docs still describe it.
4. **Timelock bypass / absence**: execution without delay, or no timelock
   at all. Observed here: Cosmos Hub has no timelock; ENS's voting delay
   is 1 block.
5. **Silent parameter change** (v1.0.0): a core parameter is not published,
   so a change cannot be detected. Observed here: ENS's 1-block voting
   delay lives only in EP 5.15, not the main process doc.
6. **Quorum failure despite near-unanimous support**: turnout below quorum
   rejects proposals that almost every voter supports. Observed here: four
   Cosmos Hub proposals (1047, 1048, 1050, 1051) rejected with ~99.99% yes
   because turnout was 17.91–32.74% against a 40% quorum.
7. **Validator concentration / liveness**: a small validator set holds over
   1/3 of bonded stake and can halt the chain. Observed here: the top 4
   Cosmos Hub validators hold 37.98%.
8. **Low delegation / quorum capture**: so little supply is delegated that
   quorum is a small fraction of delegated power. Observed here: 3.98% of
   ENS is delegated; quorum (1M ENS) is 25.13% of delegated supply.

## Measurement method

`scripts/measure.py` (Python 3, stdlib only, no network) computes every
measured number from the dated snapshots in `snapshots/`:

- Cosmos Hub: per-proposal turnout = total votes (yes + abstain + no +
  NoWithVeto, in ATOM) / bonded ATOM at the snapshot date; yes share =
  yes / (yes + no + NoWithVeto); veto share and abstain share are shares
  of total votes; quorum met = turnout >= 40%. Validator concentration:
  top-n shares and Herfindahl-Hirschman Index from the bonded-validators
  snapshot.
- ENS DAO: per-vote totals, share of 100,000,000 ENS total supply, and
  quorum multiple = total votes / 1,000,000 ENS, from values transcribed
  from fetched Tally / docs / news pages (recorded in
  `snapshots/ens-recorded-votes-2026-11-11.json` with a source per vote).

Caveat (disclosed in Limitations): historical Cosmos Hub turnout uses the
2026-11-10 bonded figure (341,108,371.99 ATOM) as the denominator for all
proposals in the window; the chain's own quorum check uses bonded stake at
vote time. The four quorum-fail verdicts (turnout 17.91–32.74%) are far
enough below 40% to be robust to that drift; Proposal 1043 (39.72%) sits
inside the drift band and no quorum verdict is drawn from it.

## Evidence standard

- Every parameter value in a profile cites a primary source by ID; the
  citation table is `citations.md`.
- Every finding is emitted by the engine from a check outcome; the trigger
  command and the observed vs expected values are recorded in `findings.md`.
- Every claim in `claims.md` maps to an evidence file, a script, and an
  output line.
- `scripts/run_all.sh` regenerates all outputs; `scripts/clean_reproduce.sh`
  re-runs from a fresh copy and requires byte-identical outputs.
- `docs/index.html` is generated from the engine output by
  `scripts/build_docs.py` and is therefore excluded from `SHA256SUMS`.

## Limitations (honest)

- Compound's Governor Bravo mainnet address remains unverified from a
  primary source (carried forward from v1.0.0; re-attempted this round, no
  primary source found). No Compound address is published here.
- ENS per-delegate and top-holder concentration (HHI) were not measured:
  Tally's delegate voting powers were not captured in the snapshot. Only
  the delegated share (3.98% of supply) is measured.
- The ENS Governor Nexus social vote ([7.3], 516,480 displayed, 49
  addresses) is reported as a displayed total only; its for/against split
  could not be resolved from the Tally page, so no quorum verdict is drawn
  from it.
- EP 6.45 / EP 6.50 vote totals come from a secondary analysis
  (caper.network) that cites on-chain reads; the EP 6.50 execution is
  corroborated by the same source's role read at block 25,710,457.
- Cosmos Hub historical turnout uses the snapshot-date bonded denominator
  (see Measurement method); Proposal 1043 (39.72%) is borderline.
- The Cosmos Hub `proposal_cancel_ratio` (0.5) parameter's semantics were
  not verified from a primary source; it is scored partial, not pass.
- The engine scores documented parameters and observed proposals; it does
  not re-execute proposals on-chain and does not audit contract source code
  beyond the published parameters.
