import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARD_DIR = ROOT / "hf-kernels" / "szl-blocked"


class BlockedKernelContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(
            (CARD_DIR / "contract.json").read_text(encoding="utf-8")
        )
        cls.card = (CARD_DIR / "README.md").read_text(encoding="utf-8")

    def test_quickstart_uses_explicit_trust_and_immutable_revision(self):
        revision = self.contract["observed_revision"]

        self.assertRegex(revision, re.compile(r"^[0-9a-f]{40}$"))
        self.assertTrue(self.contract["required_trust_remote_code"])
        self.assertIn(f'revision="{revision}"', self.card)
        self.assertIn("trust_remote_code=True", self.card)
        self.assertNotIn('revision="main"', self.card)

    def test_card_does_not_claim_an_unimplemented_export(self):
        self.assertIn("selfcheck", self.contract["unsupported_exports"])
        self.assertNotIn("selfcheck", self.contract["documented_exports"])
        self.assertNotIn("selfcheck()", self.card)

    def test_quickstart_preserves_honest_blocked_semantics(self):
        self.assertIn("assert result.blocked is True", self.card)
        self.assertIn("assert result.output is None", self.card)


if __name__ == "__main__":
    unittest.main()
