"""Unit test suite for CodeCoach TS."""
import unittest
from coach import analyze_ts

class TestCodeCoachTS(unittest.TestCase):
    def test_clean_ts(self):
        code = "const score: number = 100;\nfunction greet(name: string): void { console.log(name); }"
        issues = analyze_ts(code)
        self.assertEqual(len(issues), 0)

    def test_any_pitfall(self):
        code = "let data: any = 'untyped';"
        issues = analyze_ts(code)
        self.assertTrue(any(i.kind == "TRICKY PITFALL" for i in issues))

    def test_non_null_assertion(self):
        code = "const x = player!.health;"
        issues = analyze_ts(code)
        self.assertTrue(any(i.kind == "QUIET BUG" for i in issues))

    def test_untyped_parameters(self):
        code = "function calculate(x, y) { return x + y; }"
        issues = analyze_ts(code)
        self.assertTrue(any(i.kind == "MISSING TYPE" for i in issues))

    def test_forceful_cast(self):
        code = "const val = input as any;"
        issues = analyze_ts(code)
        self.assertTrue(any(i.kind == "TYPE BYPASS" for i in issues))

if __name__ == "__main__":
    unittest.main()
