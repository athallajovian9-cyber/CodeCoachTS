"""Reporting engine for CodeCoach TS. Kid-friendly by default."""
from __future__ import annotations

from coach import TSIssue, analyze_ts


def format_report(code: str, for_parents: bool = False) -> str:
    issues = analyze_ts(code)
    if not issues:
        if for_parents:
            return "SUCCESS: Zero type safety or static linting warnings found in TypeScript file."
        return (
            "============================================================\n"
            "   🌟 ALL GOOD! YOUR TYPESCRIPT IS 100% TYPE-SAFE! 🌟       \n"
            "============================================================\n"
            "Zero 'any' leaks, strong parameters, and clean types. You're a TypeScript pro! 🚀\n"
        )

    out = []
    if for_parents:
        out.append(f"CodeCoach TS Diagnostic Report: {len(issues)} issue(s) detected.\n")
        for i in issues:
            out.append(f"Line {i.line} [{i.kind}] {i.title}: {i.message} (Solution: {i.fix_hint})")
    else:
        out.append("============================================================")
        out.append("             ⚡ CODECOACH TYPESCRIPT REVIEW                ")
        out.append("============================================================\n")
        for idx, i in enumerate(issues, start=1):
            out.append(f"👉 Tip #{idx} (Line {i.line}) - [{i.kind}]")
            out.append(f"   🛡️  {i.title}")
            out.append(f"   💡 {i.message}")
            out.append(f"   🛠️  TRY THIS: {i.fix_hint}\n")
        out.append("Every type you add makes your app bulletproof! Keep going! 💻✨")

    return "\n".join(out)
