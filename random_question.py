"""Random quiz and reward system for CodeCoach TS."""
from __future__ import annotations

import random

QUESTIONS = [
    {
        "q": "What happens when you use the 'any' type in TypeScript?",
        "options": [
            "A) It makes the code run 2x faster",
            "B) It turns off TypeScript's type checking",
            "C) It locks the variable forever",
            "D) It converts the code into HTML"
        ],
        "answer": "B",
        "hint": "'any' tells TypeScript to stop checking that variable!"
    },
    {
        "q": "What is the correct way to type an array of numbers in TypeScript?",
        "options": ["A) number[]", "B) Array<number>", "C) Both A and B", "D) numbers()"],
        "answer": "C",
        "hint": "TypeScript supports both bracket syntax and generic syntax!"
    },
    {
        "q": "Which file extension is used for standard TypeScript files?",
        "options": ["A) .js", "B) .ts", "C) .py", "D) .type"],
        "answer": "B",
        "hint": "TS stands for TypeScript!"
    },
    {
        "q": "What keyword defines a blueprint for an object structure in TypeScript?",
        "options": ["A) blueprint", "B) interface", "C) layout", "D) schema"],
        "answer": "B",
        "hint": "It starts with 'inter-'"
    }
]

REWARDS = [
    "🛡️ Type Guardian Shield!",
    "💎 Diamond TypeScript Architect Badge!",
    "⚡ Static Analysis Wizard Trophy!",
    "🚀 Zero-Bug Compiler Token!"
]

def run_quiz():
    q = random.choice(QUESTIONS)
    print("\n" + "=" * 55)
    print("      🎯 CODECOACH TS: CHALLENGE QUESTION!       ")
    print("=" * 55)
    print(f"\n{q['q']}\n")
    for opt in q["options"]:
        print(f"  {opt}")
    print()

    ans = input("Your Answer (A, B, C, or D): ").strip().upper()
    if ans == q["answer"]:
        reward = random.choice(REWARDS)
        print("\n🎉 CORRECT! PHENOMENAL WORK!")
        print(f"🎁 REWARD UNLOCKED: {reward}\n")
    else:
        print(f"\n❌ Not quite! The correct answer was {q['answer']}.")
        print(f"💡 Hint: {q['hint']}\n")

if __name__ == "__main__":
    run_quiz()
