# Claims — claims-and-evidence index

Every claim maps to an evidence file, a script, and an output. Evidence
references are files, or `file:line` where a line matters. Run outputs live
in `outputs/run1/` (and the byte-identical clean reproduction in
`outputs/run2-clean/`).

### C-01 — ENS DAO scores 68.58 / 100 under framework v1.1.0
Statement: ENS DAO scores 68.58 / 100 (A1 50.00, A2 66.67, A3 80.00, A4 66.67, A5 75.00, A6 70.00) across 27 checks.
Evidence: outputs/run1/ens.score.json, protocols/ens.md, outputs/run1/run-manifest.json
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1

### C-02 — Cosmos Hub scores 61.67 / 100 under framework v1.1.0
Statement: Cosmos Hub scores 61.67 / 100 (A1 66.67, A2 58.33, A3 50.00, A4 50.00, A5 50.00, A6 100.00) across 27 checks.
Evidence: outputs/run1/cosmos-hub.score.json, protocols/cosmos-hub.md, outputs/run1/run-manifest.json
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1

### C-03 — 24 findings: 3 High, 13 Medium, 8 Low
Statement: The engine emits 24 findings — 3 High (all Cosmos Hub), 13 Medium, 8 Low.
Evidence: outputs/run1/findings.json, findings.md
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1

### C-04 — ENS governor and timelock are verified contracts
Statement: ENS Governor is 0x323A76393544d5ecca80cd6ef2A560C6a395b7E3 (ENSGovernor, verified) and the DAO Wallet timelock is 0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7 (TimelockController, verified), holding 4,499.79 ETH.
Evidence: protocols/ens.json, snapshots/ens-recorded-votes-2026-11-11.json
Script: none (Etherscan pages fetched 2026-11-10 21:05–21:07 UTC; see citations C-ENS-GOVERNOR, C-ENS-TIMELOCK)

### C-05 — ENS parameters: 100k threshold, 1% quorum, 7-day vote, 2-day timelock, 1-block delay
Statement: ENS executable proposals need 100,000 ENS delegated, a 1% (1,000,000 ENS) quorum, a 7-day voting period, and a 2-day timelock; the voting delay is 1 block.
Evidence: protocols/ens.json, snapshots/ens-docs-governance-process-2026-11-11.html, snapshots/ens-docs-ep-5-15-2026-11-11.html
Script: none (ENS docs fetched 2026-11-10 21:11 UTC; see citations C-ENS-PROCESS, C-ENS-EP515)

### C-06 — Only 3.98% of ENS is delegated
Statement: 3,980,000 ENS of 100,000,000 (3.98%) is delegated; quorum (1,000,000 ENS) is 25.13% of delegated supply.
Evidence: outputs/measurements.json, outputs/measurements.md, snapshots/ens-recorded-votes-2026-11-11.json
Script: python3 scripts/measure.py

### C-07 — ENS docs disagree with EP 6.50 on the Security Council
Statement: The ENS docs security-council page states a 4-of-8 council, while EP 6.50 seated a 5-of-8 council for a term to 2028-07-16; finding F-16 (Medium).
Evidence: findings.md, snapshots/ens-docs-security-council-2026-11-11.html, snapshots/ens-docs-ep-6-50-2026-11-11.html
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1

### C-08 — EP 6.45 defeated, EP 6.50 passed
Statement: EP 6.45 (council renewal) was defeated 3,859,981 against vs 1,137,702 for; EP 6.50 (successor grant) passed 4,228,716 for vs 94,526 against (4.32% of supply, 4.32x quorum).
Evidence: outputs/measurements.json, outputs/measurements.md, snapshots/ens-recorded-votes-2026-11-11.json
Script: python3 scripts/measure.py

### C-09 — Cosmos Hub params: 40% quorum, 7-day vote, 500 ATOM deposit
Statement: Live Cosmos Hub gov params (2026-11-10): voting period 7 days, min deposit 500 ATOM, max deposit period 14 days, quorum 40%, threshold 50%, veto threshold 33.4%, expedited 3 days / 66.7% / 501 ATOM.
Evidence: snapshots/cosmoshub-gov-params-2026-11-11.json, outputs/measurements.json
Script: python3 scripts/measure.py

### C-10 — Top-4 Cosmos Hub validators hold 37.98% of bonded stake
Statement: Top-1 validator holds 18.79%, top-4 hold 37.98% (over the 1/3 liveness threshold), top-10 hold 56.49%, HHI 0.0578, across 180 bonded validators; finding F-01 (High).
Evidence: outputs/measurements.json, outputs/measurements.md, snapshots/cosmoshub-validators-bonded-2026-11-11.json
Script: python3 scripts/measure.py

### C-11 — Cosmos Hub turnout 17.91–59.26%, mean 39.75%
Statement: Across decided proposals 1042–1060, turnout vs bonded stake ranged 17.91–59.26% (mean 39.75%); four proposals were rejected despite ~99.99% yes because turnout missed the 40% quorum.
Evidence: outputs/measurements.json, outputs/measurements.md, snapshots/cosmoshub-proposals-latest20-2026-11-11.json
Script: python3 scripts/measure.py

### C-12 — Four Cosmos Hub proposals veto-rejected
Statement: Proposals 1042, 1045, 1046, and 1056 were rejected with NoWithVeto shares of 99.97%, 98.0%, 99.99%, and 89.74%; burn_vote_veto is true, so their deposits burn.
Evidence: outputs/measurements.json, outputs/measurements.md, snapshots/cosmoshub-proposals-latest20-2026-11-11.json
Script: python3 scripts/measure.py

### C-13 — Proposal 1058 moved 1,227,121 ATOM outside DAO recall
Statement: Proposal 1058 passed and moved 1,227,121 ATOM recovered after the Neutron exploit to the Neutron recovery multisig; finding F-03 (High).
Evidence: outputs/measurements.json, snapshots/cosmoshub-proposals-latest20-2026-11-11.json
Script: python3 scripts/measure.py

### C-14 — Cosmos Hub has no timelock
Statement: Cosmos Hub governance has no timelock and no voting delay: a passed proposal executes without a mandatory delay; finding F-02 (High).
Evidence: protocols/cosmos-hub.json, snapshots/cosmoshub-gov-params-2026-11-11.json
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1

### C-15 — Proposal 1061 is in its voting period
Statement: Proposal 1061 (Gaia v29.1.0 upgrade, height 33935300) was in its voting period at snapshot time (2026-11-10 11:57 UTC to 2026-11-17 11:57 UTC), with zero votes tallied yet.
Evidence: snapshots/cosmoshub-proposals-latest20-2026-11-11.json, outputs/measurements.json
Script: python3 scripts/measure.py

### C-16 — Snapshots are dated with block heights and reproduce the tables
Statement: ENS snapshot 2026-11-10, Ethereum block 26,353,262; Cosmos Hub snapshot 2026-11-10, block 33,818,316; `scripts/clean_reproduce.sh` re-runs from a fresh copy and requires byte-identical outputs.
Evidence: snapshots/manifest.md, outputs/run1/run-manifest.json
Script: bash scripts/clean_reproduce.sh (see outputs/run2-clean/ after it runs)

### C-17 — Compound Governor Bravo address remains unverified
Statement: No primary source for the Compound Governor Bravo mainnet address was found in this round; no Compound address is published in this pack.
Evidence: citations.md, docs/methodology.md
Script: none (search performed 2026-11-10; see citations C-COMP-ADDR)

### C-18 — Framework v1.1.0 adds 4 checks to v1.0.0
Statement: Framework v1.1.0 extends v1.0.0 (23 checks) with A2-6 concentration, A3-5 upgrade authority, A5-4 time-bounded veto, and A6-5 snapshot reproducibility — 27 checks total.
Evidence: framework/rubric.json, framework/scoring-rubric.md, docs/gap-list.md
Script: python3 audit-engine/audit.py --profiles protocols --out outputs/run1
