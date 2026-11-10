# Measurements — from dated snapshots

Computed by `scripts/measure.py` from files in `snapshots/` only. No network access.

## Cosmos Hub (snapshot 2026-11-10, block 33818316)

- Bonded: 341,108,371.99 ATOM; validators bonded: 180
- Validator concentration: top-1 18.79%, top-4 37.98%, top-5 42.15%, top-10 56.49%, top-33 82.08%, HHI 0.0578
- Top-4 exceed 1/3 of bonded stake: True
- Proposals 1042–1061: 11 passed, 8 rejected, 1 voting
- Turnout (vs bonded): min 17.91%, max 59.26%, mean 39.75%
- Quorum 40%; rejected despite a yes-majority because turnout missed quorum: 1051, 1050, 1048, 1047
- Veto-rejected (NoWithVeto over 33.4%): 1056, 1046, 1045, 1042

| Proposal | Status | Turnout % bonded | Yes % decided | Veto % | Abstain % |
|----------|--------|------------------|---------------|--------|-----------|
| 1061 | VOTING_PERIOD | 0.0 | 0.0 | 0.0 | 0.0 |
| 1060 | PASSED | 53.43 | 99.98 | 0.0 | 37.6 |
| 1059 | PASSED | 49.4 | 99.42 | 0.58 | 0.01 |
| 1058 | PASSED | 59.01 | 99.72 | 0.01 | 34.2 |
| 1057 | PASSED | 55.76 | 99.94 | 0.02 | 36.19 |
| 1056 | REJECTED | 29.9 | 0.6 | 89.74 | 3.78 |
| 1055 | PASSED | 43.01 | 100.0 | 0.0 | 0.0 |
| 1054 | PASSED | 53.45 | 93.41 | 0.0 | 40.97 |
| 1053 | PASSED | 52.91 | 99.98 | 0.0 | 38.18 |
| 1052 | PASSED | 59.26 | 100.0 | 0.0 | 34.06 |
| 1051 | REJECTED | 28.25 | 99.98 | 0.0 | 28.23 |
| 1050 | REJECTED | 32.74 | 99.99 | 0.01 | 3.76 |
| 1049 | PASSED | 43.62 | 99.99 | 0.0 | 0.0 |
| 1048 | REJECTED | 17.91 | 99.99 | 0.0 | 3.99 |
| 1047 | REJECTED | 18.22 | 99.98 | 0.0 | 4.5 |
| 1046 | REJECTED | 20.76 | 0.0 | 99.99 | 0.0 |
| 1045 | REJECTED | 24.11 | 0.59 | 98.0 | 0.0 |
| 1044 | PASSED | 42.79 | 99.93 | 0.07 | 0.0 |
| 1043 | PASSED | 39.72 | 98.42 | 0.01 | 4.63 |
| 1042 | REJECTED | 31.0 | 0.02 | 99.97 | 0.0 |

## ENS DAO (snapshot 2026-11-10, Ethereum block 26353262)

- Total supply: 100,000,000 ENS; delegated: 3,980,000 ENS (3.98% of supply); quorum 1,000,000 ENS; threshold 100,000 ENS
- Treasury (Tally): $50,580,000; DAO Wallet (timelock) ETH balance: 4,499.79 ETH ($9,272,266.06)

| Vote | For | Against | Abstain | Total | % of supply | Quorum multiple |
|------|-----|---------|---------|-------|-------------|-----------------|
| EP-6.50-grant | 4,228,716 | 94,526 | — | 4,323,242 | 4.32 | 4.32x |
| EP-6.45-renewal | 1,137,702 | 3,859,981 | 1,761 | 4,999,444 | 5.0 | 5.0x |
| TALLY-7.2-METAGOV-TERM7 | 1,470,000 | 0 | 15,000 | 1,485,000 | 1.49 | 1.49x |
| TALLY-7.2-METAGOV-TERM7-OCT21 | — | — | — | 1,100,000 (displayed) | — | — |
| TALLY-7.3-GOVERNOR-NEXUS | — | — | — | 516,480 (displayed) | — | — |
