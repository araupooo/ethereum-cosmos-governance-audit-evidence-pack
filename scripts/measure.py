#!/usr/bin/env python3
"""Measure governance concentration and participation from dated snapshots.

Stdlib only. Reads snapshots/cosmoshub-*.json and
snapshots/ens-recorded-votes-2026-11-11.json, writes deterministic
outputs/measurements.json and outputs/measurements.md.

Usage: python3 scripts/measure.py [--snapshots snapshots] [--out outputs]
No network access: every number comes from the saved snapshot files.
"""
import argparse
import json
import pathlib


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def pct(part, whole):
    return round(100.0 * part / whole, 2) if whole else 0.0


def main():
    ap = argparse.ArgumentParser(description="Measure governance snapshots")
    ap.add_argument("--snapshots", default="snapshots")
    ap.add_argument("--out", default="outputs")
    args = ap.parse_args()
    snap = pathlib.Path(args.snapshots)
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    # ---- Cosmos Hub ----
    params = load(snap / "cosmoshub-gov-params-2026-11-11.json")["params"]
    block = load(snap / "cosmoshub-latest-block-2026-11-11.json")["block"]["header"]
    pool = load(snap / "cosmoshub-staking-pool-2026-11-11.json")["pool"]
    proposals = load(snap / "cosmoshub-proposals-latest20-2026-11-11.json")["proposals"]
    validators = load(snap / "cosmoshub-validators-bonded-2026-11-11.json")["validators"]
    bonded_atom = int(pool["bonded_tokens"]) / 1e6
    quorum = float(params["quorum"])
    veto_threshold = float(params["veto_threshold"])
    threshold = float(params["threshold"])

    vals = sorted(validators, key=lambda v: -int(v["tokens"]))
    total_tokens = sum(int(v["tokens"]) for v in vals)
    shares = [int(v["tokens"]) / total_tokens for v in vals]
    hhi = round(sum(s * s for s in shares), 4)
    top = {}
    for n in (1, 4, 5, 10, 33):
        top[f"top{n}"] = pct(sum(int(v["tokens"]) for v in vals[:n]), total_tokens)
    top_validators = [
        {"moniker": v["description"]["moniker"],
         "tokens_atom": round(int(v["tokens"]) / 1e6, 2),
         "share_pct": pct(int(v["tokens"]), total_tokens)}
        for v in vals[:10]
    ]

    rows = []
    for p in proposals:
        t = p["final_tally_result"]
        yes = int(t["yes_count"]) / 1e6
        ab = int(t["abstain_count"]) / 1e6
        no = int(t["no_count"]) / 1e6
        veto = int(t["no_with_veto_count"]) / 1e6
        total = yes + ab + no + veto
        decided = yes + no + veto
        rows.append({
            "id": p["id"], "title": p.get("title", ""),
            "status": p["status"],
            "voting_start": p.get("voting_start_time", ""),
            "voting_end": p.get("voting_end_time", ""),
            "yes_atom": round(yes, 2), "abstain_atom": round(ab, 2),
            "no_atom": round(no, 2), "veto_atom": round(veto, 2),
            "total_atom": round(total, 2),
            "turnout_pct_bonded": pct(total, bonded_atom),
            "yes_pct_decided": pct(yes, decided) if decided else 0.0,
            "veto_pct_total": pct(veto, total) if total else 0.0,
            "abstain_pct_total": pct(ab, total) if total else 0.0,
            "quorum_met": total >= quorum * bonded_atom if total else False,
            "vetoed": veto >= veto_threshold * total if total else False,
        })
    decided_rows = [r for r in rows if r["total_atom"] > 0]
    turnouts = [r["turnout_pct_bonded"] for r in decided_rows]
    quorum_fails = [r for r in decided_rows
                    if r["status"] == "PROPOSAL_STATUS_REJECTED"
                    and not r["quorum_met"] and r["yes_pct_decided"] > 50]
    veto_fails = [r for r in decided_rows if r["vetoed"]]
    cosmos = {
        "snapshot": {"date": "2026-11-10", "block_height": int(block["height"]),
                     "block_time": block["time"], "chain_id": block["chain_id"]},
        "params": {"voting_period_s": int(params["voting_period"].rstrip("s")),
                   "min_deposit_atom": int(params["min_deposit"][0]["amount"]) / 1e6,
                   "max_deposit_period_s": int(params["max_deposit_period"].rstrip("s")),
                   "quorum": quorum, "threshold": threshold,
                   "veto_threshold": veto_threshold,
                   "expedited_voting_period_s": int(params["expedited_voting_period"].rstrip("s")),
                   "expedited_threshold": float(params["expedited_threshold"]),
                   "expedited_min_deposit_atom": int(params["expedited_min_deposit"][0]["amount"]) / 1e6,
                   "burn_vote_veto": params["burn_vote_veto"],
                   "burn_vote_quorum": params["burn_vote_quorum"],
                   "burn_proposal_deposit_prevote": params["burn_proposal_deposit_prevote"],
                   "min_initial_deposit_ratio": float(params["min_initial_deposit_ratio"]),
                   "proposal_cancel_ratio": float(params["proposal_cancel_ratio"])},
        "bonded_atom": round(bonded_atom, 2),
        "not_bonded_atom": round(int(pool["not_bonded_tokens"]) / 1e6, 2),
        "validators_bonded": len(vals),
        "validator_concentration": {"hhi": hhi, **top, "top10": top_validators},
        "top4_exceeds_one_third": top["top4"] > 100 / 3,
        "proposals": rows,
        "summary": {
            "n": len(rows),
            "decided": len(decided_rows),
            "passed": sum(1 for r in rows if r["status"] == "PROPOSAL_STATUS_PASSED"),
            "rejected": sum(1 for r in rows if r["status"] == "PROPOSAL_STATUS_REJECTED"),
            "voting": sum(1 for r in rows if r["status"] == "PROPOSAL_STATUS_VOTING_PERIOD"),
            "turnout_min_pct": min(turnouts), "turnout_max_pct": max(turnouts),
            "turnout_mean_pct": round(sum(turnouts) / len(turnouts), 2),
            "quorum_fail_despite_yes_majority": [r["id"] for r in quorum_fails],
            "veto_rejected": [r["id"] for r in veto_fails],
        },
    }

    # ---- ENS DAO ----
    ens = load(snap / "ens-recorded-votes-2026-11-11.json")
    supply = ens["token"]["total_supply"]
    ens_votes = []
    for v in ens["votes"]:
        if v.get("for") is None:
            ens_votes.append({"id": v["id"], "title": v["title"],
                              "total_displayed": v.get("total_displayed"),
                              "voters": v.get("voters"), "status": v["status"],
                              "note": "displayed total only; for/against split not resolved from the page"})
            continue
        total = v["for"] + v["against"] + (v["abstain"] or 0)
        decided = v["for"] + v["against"]
        ens_votes.append({
            "id": v["id"], "title": v["title"], "status": v["status"],
            "for": v["for"], "against": v["against"], "abstain": v["abstain"],
            "total": total, "voters": v.get("voters"),
            "total_pct_supply": pct(total, supply),
            "for_pct_decided": pct(v["for"], decided) if decided else 0.0,
            "quorum_multiple": round(total / 1000000, 2),
            "quorum_met": total >= 1000000,
        })
    ens_out = {
        "snapshot": {"date": "2026-11-10", "eth_block_height": ens["governor"]["latest_block_seen"],
                     "fetched": ens["recorded"]},
        "token": ens["token"],
        "governor": ens["governor"],
        "timelock": ens["timelock"],
        "tally": ens["tally"],
        "delegated_share_pct_supply": pct(ens["tally"]["delegated_tokens"], supply),
        "security_council": ens["security_council"],
        "votes": ens_votes,
    }

    doc = {"cosmos_hub": cosmos, "ens_dao": ens_out}
    (out / "measurements.json").write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = []
    lines.append("# Measurements — from dated snapshots")
    lines.append("")
    lines.append("Computed by `scripts/measure.py` from files in `snapshots/` only. No network access.")
    lines.append("")
    lines.append(f"## Cosmos Hub (snapshot 2026-11-10, block {cosmos['snapshot']['block_height']})")
    lines.append("")
    lines.append(f"- Bonded: {cosmos['bonded_atom']:,.2f} ATOM; validators bonded: {cosmos['validators_bonded']}")
    lines.append(f"- Validator concentration: top-1 {top['top1']}%, top-4 {top['top4']}%, top-5 {top['top5']}%, top-10 {top['top10']}%, top-33 {top['top33']}%, HHI {hhi}")
    lines.append(f"- Top-4 exceed 1/3 of bonded stake: {cosmos['top4_exceeds_one_third']}")
    lines.append(f"- Proposals 1042–1061: {cosmos['summary']['passed']} passed, {cosmos['summary']['rejected']} rejected, {cosmos['summary']['voting']} voting")
    lines.append(f"- Turnout (vs bonded): min {cosmos['summary']['turnout_min_pct']}%, max {cosmos['summary']['turnout_max_pct']}%, mean {cosmos['summary']['turnout_mean_pct']}%")
    lines.append(f"- Quorum 40%; rejected despite a yes-majority because turnout missed quorum: {', '.join(cosmos['summary']['quorum_fail_despite_yes_majority'])}")
    lines.append(f"- Veto-rejected (NoWithVeto over 33.4%): {', '.join(cosmos['summary']['veto_rejected'])}")
    lines.append("")
    lines.append("| Proposal | Status | Turnout % bonded | Yes % decided | Veto % | Abstain % |")
    lines.append("|----------|--------|------------------|---------------|--------|-----------|")
    for r in rows:
        lines.append(f"| {r['id']} | {r['status'].replace('PROPOSAL_STATUS_', '')} | {r['turnout_pct_bonded']} | {r['yes_pct_decided']} | {r['veto_pct_total']} | {r['abstain_pct_total']} |")
    lines.append("")
    lines.append(f"## ENS DAO (snapshot 2026-11-10, Ethereum block {ens_out['snapshot']['eth_block_height']})")
    lines.append("")
    lines.append(f"- Total supply: {supply:,} ENS; delegated: {ens['tally']['delegated_tokens']:,} ENS ({ens_out['delegated_share_pct_supply']}% of supply); quorum 1,000,000 ENS; threshold 100,000 ENS")
    lines.append(f"- Treasury (Tally): ${ens['tally']['treasury_usd']:,}; DAO Wallet (timelock) ETH balance: {ens['timelock']['eth_balance']:,.2f} ETH (${ens['timelock']['eth_value_usd']:,.2f})")
    lines.append("")
    lines.append("| Vote | For | Against | Abstain | Total | % of supply | Quorum multiple |")
    lines.append("|------|-----|---------|---------|-------|-------------|-----------------|")
    for v in ens_votes:
        if "total" in v:
            ab = "—" if v['abstain'] is None else f"{v['abstain']:,}"
            lines.append(f"| {v['id']} | {v['for']:,} | {v['against']:,} | {ab} | {v['total']:,} | {v['total_pct_supply']} | {v['quorum_multiple']}x |")
        else:
            lines.append(f"| {v['id']} | — | — | — | {v['total_displayed']:,} (displayed) | — | — |")
    lines.append("")
    (out / "measurements.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"measure.py: cosmos {cosmos['summary']['passed']} passed / {cosmos['summary']['rejected']} rejected / "
          f"{cosmos['summary']['voting']} voting; turnout {cosmos['summary']['turnout_min_pct']}–{cosmos['summary']['turnout_max_pct']}%; "
          f"top-10 validators {top['top10']}%, HHI {hhi}")
    print(f"measure.py: ENS delegated {ens_out['delegated_share_pct_supply']}% of supply; "
          f"{len(ens_votes)} votes recorded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
