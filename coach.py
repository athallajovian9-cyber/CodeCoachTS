"""CodeCoach TypeScript (TS) - Kid-Friendly Type Safety & Linter Engine.
Detects beginner TypeScript pitfalls, 'any' abuse, missing type annotations,
unnecessary assertions, and teaches strict type safety with approachable language.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List


@dataclass
class TSIssue:
    kind: str
    line: int
    title: str
    message: str
    fix_hint: str


def analyze_ts(code: str) -> List[TSIssue]:
    issues: List[TSIssue] = []
    lines = code.splitlines()

    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()

        # Skip comment lines
        if line.startswith("//") or line.startswith("/*"):
            continue

        # 1. 'any' type trap: const x: any = ...
        if re.search(r':\s*any\b', line):
            issues.append(TSIssue(
                kind="TRICKY PITFALL",
                line=idx,
                title="THE 'any' ESCAPE HATCH TURNS OFF SAFETY!",
                message="Using ': any' turns off TypeScript's superpower! It makes TypeScript act like regular JavaScript.",
                fix_hint="Give it a real type like ': string', ': number', or ': boolean'!"
            ))

        # 2. Non-null assertion operator abuse: x!.something
        if re.search(r'[a-zA-Z0-9_]!\.[a-zA-Z0-9_]', line):
            issues.append(TSIssue(
                kind="QUIET BUG",
                line=idx,
                title="DANGEROUS FORCE-NOT-NULL (!.) OPERATOR!",
                message="Using '!' forces TypeScript to trust you, but if the value is actually empty, your app will crash!",
                fix_hint="Check if the value exists first using an 'if' check or optional chaining '?.'"
            ))

        # 3. Parameter without type annotation: function add(a, b)
        if re.search(r'\bfunction\s+[a-zA-Z_$][a-zA-Z0-9_$]*\s*\([a-zA-Z0-9_$,\s]+\)', line):
            if ":" not in line:
                issues.append(TSIssue(
                    kind="MISSING TYPE",
                    line=idx,
                    title="FUNCTION PARAMETERS HAVE NO TYPES!",
                    message="TypeScript does not know what kind of ingredients this function accepts.",
                    fix_hint="Add types to parameters, e.g. function greet(name: string, score: number)"
                ))

        # 4. Old JavaScript var in TS
        if re.search(r'\bvar\s+[a-zA-Z_$][a-zA-Z0-9_$]*', line):
            issues.append(TSIssue(
                kind="OUTDATED HABIT",
                line=idx,
                title="OLD 'var' IN MODERN TYPESCRIPT!",
                message="'var' is legacy code. TypeScript best practices always use 'let' or 'const'.",
                fix_hint="Replace 'var' with 'const' (unchanging) or 'let' (changing)."
            ))

        # 5. Loose == check
        if re.search(r'[^=!<>]={2}[^=]', line) and "===" not in line:
            issues.append(TSIssue(
                kind="TRICKY PITFALL",
                line=idx,
                title="USE STRICT TRIPLE EQUALS '==='!",
                message="Double '==' allows unexpected type coercion.",
                fix_hint="Use '===' so both values and types must match strictly."
            ))

        # 6. Type assertion instead of proper typing: as unknown as any
        if "as any" in line or "as unknown as" in line:
            issues.append(TSIssue(
                kind="TYPE BYPASS",
                line=idx,
                title="FORCEFUL TYPE CAST DETECTED!",
                message="Casting with 'as any' bypasses type safety checks.",
                fix_hint="Refactor types or write a type guard instead of casting."
            ))

    return issues
