# Citations — Primary Sources

Every parameter value in `protocols/*.json` cites one of the sources below.
"Primary" means the protocol's own documentation, governance forum, official
contract reference, verified block-explorer record, or live on-chain data.
"Secondary" means an independent write-up that quotes or reads the primary
source; secondary sources are flagged as such and never used alone for a
scored parameter, except where noted.

## ENS DAO

### C-ENS-PROCESS — ENS Governance Process (official docs)
URL: https://docs.ens.domains/dao/governance/process/
Establishes: three proposal types; executable quorum 1% and minimum approval
50%; social quorum 1% and 50%; constitutional amendment quorum 1% and
two-thirds approval; 100,000 ENS delegated to submit an executable proposal;
7-day on-chain voting period; 2-day timelock; 5-day Snapshot voting period;
0.1% (100k ENS) threshold. Snapshot saved as
`snapshots/ens-docs-governance-process-2026-11-11.html`. Fetched directly
2026-11-10 21:11 UTC.

### C-ENS-SECCOUNCIL — ENS DAO Security Council (official docs)
URL: https://docs.ens.domains/dao/security-council/
Establishes: the council as a 4-of-8 multi-sig with a cancel-only mandate
(cannot propose, amend, or initiate governance actions); time-limited
authority (two years after deployment, unix timestamp 1784919179, after
which any address may call `renounceTimelockRoleByExpiration()`); veto
introduced in EP 5.7, members confirmed in EP 5.10, implemented in EP 5.13;
`SecurityCouncil.sol` deployed to 0xb8fa0ce3f91f41c5292d07475b445c35ddf63ee0.
NOTE: this page still describes the expired 2024 council; it conflicts with
EP 6.50 (see C-ENS-EP650). Snapshot saved as
`snapshots/ens-docs-security-council-2026-11-11.html`. Fetched directly
2026-11-10 21:11 UTC.

### C-ENS-EP515 — EP 5.15 (official docs)
URL: https://docs.ens.domains/dao/proposals/5.15/
Establishes: status Passed; ProposalBond design (1,000 ENS initial value,
vote For / Against / Against with penalty / Abstain); voting delay currently
set to only one block, with a 24-hour delay agreed as the sensible default;
two audits planned for the governor change. Snapshot saved as
`snapshots/ens-docs-ep-5-15-2026-11-11.html`. Fetched directly 2026-11-10
21:11 UTC.

### C-ENS-EP650 — EP 6.50 (official docs)
URL: https://docs.ens.domains/dao/proposals/6.50/
Establishes: successor Security Council election; 5/8 threshold for action;
binding Appointment Agreement with the ENS Foundation; removal mechanism;
scope unchanged ("cancellation of timelocked proposals, nothing more");
quorum 1% (1,000,000 ENS); 5-day vote. Snapshot saved as
`snapshots/ens-docs-ep-6-50-2026-11-11.html`. Fetched directly 2026-11-10
21:11 UTC.

### C-ENS-GOVERNOR — ENS Governor on Etherscan (verified contract)
URL: https://etherscan.io/address/0x323A76393544d5ecca80cd6ef2A560C6a395b7E3
Establishes: contract ENSGovernor, verified source (MIT, v0.8.7), labelled
"ENS: Governance", 10,855 transactions; latest block seen 26,353,262;
`castVote` / `castVoteBySig` activity. Fetched 2026-11-10 21:07 UTC.

### C-ENS-TIMELOCK — ENS DAO Wallet (Timelock) on Etherscan (verified contract)
URL: https://etherscan.io/address/0xFe89cc7aBB2C4183683ab71653C4cdc9B02D44b7
Establishes: contract TimelockController, verified source (MIT, v0.8.7),
labelled "ENS: DAO Wallet"; ETH balance 4,499.789408485555923108 ETH
($9,272,266.06 at $2,060.60/ETH); latest transaction block 26,264,817.
Fetched 2026-11-10 21:05 UTC.

### C-ENS-TOKEN — ENS token on Etherscan (verified contract)
URL: https://etherscan.io/token/0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72
Establishes: contract ENSToken, verified source (MIT, v0.8.7); max total
supply 100,000,000 ENS; 66,118 holders; circulating supply 42,309,428 ENS;
price $4.42. Fetched 2026-11-10 21:07 UTC.

### C-ENS-SUPPORT — Official ENS websites, apps, and tools (ENS support)
URL: https://support.ens.domains/en/articles/8874786-official-ens-websites-apps-and-tools
Establishes: the $ENS token contract 0xC18360217D8F7Ab5e7c516566761Ea12Ce7F9D72;
governance runs on the $ENS token. Snapshot saved as
`snapshots/ens-support-official-sites-2026-11-11.html`. Updated 2026-11-05.

### C-ENS-TALLY — ENS governance on Tally
URL: https://www.tally.xyz/gov/ens
Establishes (as displayed 2026-11-10 21:06 UTC): 77 proposals, no active
proposals; 117.01K delegates, 66.12K token holders; delegated tokens
3.98M; quorum 1M; proposal threshold 100K; treasury $50.58M (1 source);
[7.2] Meta-Governance Term 7 funding request (Oct 30, 2026): 1.47M for /
0 against / 15K abstain, 1.48M total, 59 addresses, pending queue;
[7.3] Governor Nexus Update (Oct 29, 2026): 516.48K displayed, 49
addresses, closed; [7.2] Oct 21, 2026: 1.1M displayed, 53 addresses,
closed. Snapshot saved as `snapshots/tally-ens-gov-2026-11-11.html`.

### C-ENS-FORUM-TFA — [Executable] Treasury Flow Automation (ENS DAO forum)
URL: https://discuss.ens.domains/t/executable-treasury-flow-automation/21923
Establishes: Governor 0x323A76393544d5ecca80cd6ef2A560C6a395b7E3
(governor.ensdao.eth); Registrar Manager + Karpatkey scoped permission to
send ETH/USDC to wallet.ensdao.eth without a proposal; timelock keeps a
6-month USDC runway (~$8M); ~$1M yield missed since January 2024 from idle
capital. Retrieved via search-result excerpts of the forum post.

### C-ENS-CAPER — Security councils and emergency powers (caper.network)
URL: https://caper.network/wiki/dao-governance/concepts/fundamentals/security-councils
Establishes (secondary, cites on-chain reads): EP 6.45 renewal defeated
3,859,981 ENS against, 1,137,702 for, 1,761 abstaining; EP 6.50 executable
grant passed 4,228,716 ENS for to 94,526 against; on-chain reads at block
25,710,457 (2026-08-08) show the new council contract holds PROPOSER_ROLE
on the ENS timelock with a 5-of-8 Safe threshold, and neither the expired
2024 contract nor the defeated-renewal contract holds the role; term runs
to 16 July 2028. Retrieved via search-result excerpts.

## Cosmos Hub

### C-HUB-PARAMS — Cosmos Hub live gov params (public LCD)
URL: https://cosmos-rest.publicnode.com/cosmos/gov/v1/params/voting
Establishes (live on-chain, fetched 2026-11-10 19:49 UTC): voting period
604800s (7 days); min deposit 500,000,000 uatom (500 ATOM);
max deposit period 1209600s (14 days); quorum 0.40; threshold 0.50;
veto threshold 0.334; min initial deposit ratio 0.10; proposal cancel
ratio 0.50; expedited voting period 259200s (3 days); expedited threshold
0.667; expedited min deposit 501,000,000 uatom (501 ATOM); burn vote veto
true; burn vote quorum false; burn proposal deposit prevote false.
Snapshot saved as `snapshots/cosmoshub-gov-params-2026-11-11.json`.

### C-HUB-PROPOSALS — Cosmos Hub proposals 1042–1061 (public LCD)
URL: https://cosmos-rest.publicnode.com/cosmos/gov/v1/proposals?pagination.limit=20&pagination.reverse=true
Establishes (live on-chain, fetched 2026-11-10 19:49 UTC): proposal IDs,
titles, statuses, voting windows, and final tally results for proposals
1042–1061, including 1061 (Gaia v29.1.0 upgrade, voting period,
height 33935300), 1060 (community-pool USDC migration, passed), 1059
(Gaia v29.0.0 upgrade, passed), 1058 (1,227,121 ATOM Neutron recovery,
passed), 1056/1046/1045/1042 (veto-rejected). Snapshot saved as
`snapshots/cosmoshub-proposals-latest20-2026-11-11.json`.

### C-HUB-VALIDATORS — Cosmos Hub bonded validators (public LCD)
URL: https://cosmos-rest.publicnode.com/cosmos/staking/v1beta1/validators?status=BOND_STATUS_BONDED&pagination.limit=200
Establishes (live on-chain, fetched 2026-11-10 19:49 UTC): 180 bonded
validators and their bonded tokens; top validator Coinbase01 64,088,607
ATOM (18.79%). Snapshot saved as
`snapshots/cosmoshub-validators-bonded-2026-11-11.json`.

### C-HUB-POOL — Cosmos Hub staking pool (public LCD)
URL: https://cosmos-rest.publicnode.com/cosmos/staking/v1beta1/pool
Establishes (live on-chain, fetched 2026-11-10 19:49 UTC): bonded tokens
341,108,371,985,220 uatom; not bonded 13,791,482,657,555 uatom. Snapshot
saved as `snapshots/cosmoshub-staking-pool-2026-11-11.json`.

### C-HUB-BLOCK — Cosmos Hub latest block (public LCD)
URL: https://cosmos-rest.publicnode.com/cosmos/base/tendermint/v1beta1/blocks/latest
Establishes (live on-chain, fetched 2026-11-10 19:49 UTC): chain
cosmoshub-4, height 33,818,316, time 2026-11-10T19:49:46Z. Snapshot saved
as `snapshots/cosmoshub-latest-block-2026-11-11.json`.

### C-HUB-SPEC — x/gov module specification (Cosmos docs)
URL: https://docs.cosmos.network/sdk/latest/modules/gov/README
Establishes: 1-token-1-vote for bonded holders; deposit then voting
period; quorum as minimum voting power cast; threshold >50% yes excluding
abstain; veto if NoWithVeto exceeds 1/3; expedited threshold 66.7%;
burn rules for veto/quorum/pre-vote deposits. Retrieved via search-result
excerpts of the official spec.

## Framework

### C-FRAME-V1 — Multi-Protocol Governance Audit Framework v1.0.0
URL: https://github.com/araupooo/multi-protocol-governance-audit-framework
Establishes: the base framework (6 areas, 23 checks, weights sum 100;
Aave 92.50 / Compound 86.13 / Uniswap 75.88; 17 findings). Reviewed from
the public repository above (framework v1.0.0).

### C-COMP-ADDR — Compound Governor Bravo address (UNRESOLVED)
No primary source found in this round. The Compound Governor Bravo
mainnet address remains unverified; no address is published in this pack.
Carried forward from framework v1.0.0.
