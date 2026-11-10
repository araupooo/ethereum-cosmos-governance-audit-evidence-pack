#!/usr/bin/env python3
"""Build docs/index.html from engine outputs + claims.md (deterministic).

Usage: python3 scripts/build_docs.py --run outputs/run1 --claims claims.md --out docs/index.html
The page is generated from pack data, so it is excluded from SHA256SUMS.
"""
import argparse
import html
import json
import pathlib
import re


def parse_claims(path):
    claims = []
    current = None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^### (C-\d+) — (.*)$", line.strip())
        if m:
            current = {"id": m.group(1), "title": m.group(2).strip(), "statement": ""}
            claims.append(current)
            continue
        if current is not None and line.startswith("Statement:"):
            current["statement"] = line[len("Statement:"):].strip()
    return claims


def main():
    ap = argparse.ArgumentParser(description="Build docs/index.html")
    ap.add_argument("--run", required=True)
    ap.add_argument("--claims", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    rundir = pathlib.Path(args.run)
    scores = []
    for sp in sorted(rundir.glob("*.score.json")):
        scores.append(json.load(open(sp, encoding="utf-8")))
    scores.sort(key=lambda s: s["protocol"])
    findings = json.load(open(rundir / "findings.json", encoding="utf-8"))["findings"]
    meas = json.load(open(pathlib.Path("outputs") / "measurements.json", encoding="utf-8"))
    claims = parse_claims(args.claims)
    n_high = sum(1 for f in findings if f["severity"] == "High")
    n_med = sum(1 for f in findings if f["severity"] == "Medium")
    n_low = sum(1 for f in findings if f["severity"] == "Low")

    esc = html.escape
    out = []
    out.append("<!DOCTYPE html>")
    out.append("<html lang=\"en\"><head><meta charset=\"utf-8\">")
    out.append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
    out.append("<title>Ethereum and Cosmos Governance Audit Evidence Pack — Findings</title>")
    out.append("<style>body{font-family:system-ui,sans-serif;max-width:960px;margin:2em auto;padding:0 1em;line-height:1.5}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:6px 8px;text-align:left}th{background:#eee}.high{color:#b00000;font-weight:bold}.medium{color:#8a6d00;font-weight:bold}.low{color:#444}code{background:#f4f4f4;padding:1px 4px}</style>")
    out.append("</head><body>")
    out.append("<h1>Ethereum and Cosmos Governance Audit Evidence Pack</h1>")
    out.append("<p>Framework version 1.1.0 (extends v1.0.0). Six control areas (A1–A6), 27 checks, weights sum to 100. "
               "Area score is the mean of its checks (pass 1.0, partial 0.5, fail 0.0); "
               "protocol score is the weighted sum. Every parameter is verified against a "
               "primary source; unverified values are scored partial or fail, never invented.</p>")
    out.append("<h2>Per-protocol scores</h2>")
    out.append("<table><tr><th>Protocol</th><th>System</th><th>Score / 100</th>"
               "<th>A1</th><th>A2</th><th>A3</th><th>A4</th><th>A5</th><th>A6</th></tr>")
    for s in scores:
        a = {x["id"]: x["score"] for x in s["areas"]}
        out.append(f"<tr><td>{esc(s['protocol'])}</td><td>{esc(s['system'])}</td>"
                   f"<td><strong>{s['score']:.2f}</strong></td>"
                   f"<td>{a['A1']:.2f}</td><td>{a['A2']:.2f}</td><td>{a['A3']:.2f}</td>"
                   f"<td>{a['A4']:.2f}</td><td>{a['A5']:.2f}</td><td>{a['A6']:.2f}</td></tr>")
    out.append("</table>")
    out.append(f"<h2>Findings ({len(findings)} — {n_high} High, {n_med} Medium, {n_low} Low)</h2>")
    out.append("<table><tr><th>ID</th><th>Severity</th><th>Protocol</th><th>Check</th>"
               "<th>Observed</th><th>Expected</th></tr>")
    for f in findings:
        cls = f["severity"].lower()
        out.append(f"<tr><td>{esc(f['id'])}</td><td class=\"{cls}\">{esc(f['severity'])}</td>"
                   f"<td>{esc(f['protocol'])}</td><td>{esc(f['check'])} {esc(f['control'])}</td>"
                   f"<td>{esc(f['observed'])}</td><td>{esc(f['expected'])}</td></tr>")
    out.append("</table>")
    ch = meas["cosmos_hub"]
    out.append(f"<h2>Measured tables — Cosmos Hub (snapshot 2026-11-10, block {ch['snapshot']['block_height']})</h2>")
    out.append(f"<p>Bonded: {ch['bonded_atom']:,.2f} ATOM; validators bonded: {ch['validators_bonded']}. "
               f"Validator concentration: top-1 {ch['validator_concentration']['top1']}%, "
               f"top-4 {ch['validator_concentration']['top4']}%, top-10 {ch['validator_concentration']['top10']}%, "
               f"top-33 {ch['validator_concentration']['top33']}%, HHI {ch['validator_concentration']['hhi']}. "
               f"Turnout (vs bonded): min {ch['summary']['turnout_min_pct']}%, max {ch['summary']['turnout_max_pct']}%, "
               f"mean {ch['summary']['turnout_mean_pct']}%.</p>")
    out.append("<table><tr><th>Proposal</th><th>Status</th><th>Turnout % bonded</th><th>Yes % decided</th><th>Veto %</th><th>Abstain %</th></tr>")
    for r in ch["proposals"]:
        out.append(f"<tr><td>{esc(r['id'])}</td><td>{esc(r['status'].replace('PROPOSAL_STATUS_', ''))}</td>"
                   f"<td>{r['turnout_pct_bonded']}</td><td>{r['yes_pct_decided']}</td>"
                   f"<td>{r['veto_pct_total']}</td><td>{r['abstain_pct_total']}</td></tr>")
    out.append("</table>")
    en = meas["ens_dao"]
    out.append(f"<h2>Measured tables — ENS DAO (snapshot 2026-11-10, Ethereum block {en['snapshot']['eth_block_height']})</h2>")
    out.append(f"<p>Total supply: {en['token']['total_supply']:,} ENS; delegated: {en['tally']['delegated_tokens']:,} ENS "
               f"({en['delegated_share_pct_supply']}% of supply); quorum 1,000,000 ENS; threshold 100,000 ENS. "
               f"Treasury (Tally): ${en['tally']['treasury_usd']:,}.</p>")
    out.append("<table><tr><th>Vote</th><th>For</th><th>Against</th><th>Abstain</th><th>Total</th><th>% of supply</th><th>Quorum multiple</th></tr>")
    for v in en["votes"]:
        if "total" in v:
            ab = "—" if v["abstain"] is None else f"{v['abstain']:,}"
            out.append(f"<tr><td>{esc(v['id'])}</td><td>{v['for']:,}</td><td>{v['against']:,}</td><td>{ab}</td>"
                       f"<td>{v['total']:,}</td><td>{v['total_pct_supply']}</td><td>{v['quorum_multiple']}x</td></tr>")
        else:
            out.append(f"<tr><td>{esc(v['id'])}</td><td>—</td><td>—</td><td>—</td>"
                       f"<td>{v['total_displayed']:,} (displayed)</td><td>—</td><td>—</td></tr>")
    out.append("</table>")
    out.append("<h2>Claims</h2><ol>")
    for c in claims:
        out.append(f"<li><strong>{esc(c['id'])}</strong> — {esc(c['title'])}: {esc(c['statement'])}</li>")
    out.append("</ol>")
    out.append("<h2>Reproduce</h2>")
    out.append("<p><code>bash scripts/run_all.sh</code> — runs the engine on both profiles, "
               "verifies digests, and checks the generated reports, findings page, and this page "
               "against the committed files. <code>bash scripts/clean_reproduce.sh</code> re-runs "
               "from a fresh copy and requires byte-identical outputs.</p>")
    out.append("<p>Source files: <code>framework/spec.md</code>, <code>framework/scoring-rubric.md</code>, "
               "<code>framework/rubric.json</code>, <code>audit-engine/audit.py</code>, "
               "<code>protocols/*.json</code>, <code>claims.md</code>, <code>findings.md</code>, "
               "<code>citations.md</code>, <code>evidence.json</code>.</p>")
    out.append("</body></html>")
    pathlib.Path(args.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"build_docs.py: wrote {args.out} ({len(scores)} protocols, {len(findings)} findings, {len(claims)} claims)")


if __name__ == "__main__":
    main()
