from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from asset_checkout.cli import main
from asset_checkout.models import Note, ProjectState, Task


class ProjectSmokeTests(unittest.TestCase):
    def test_cli_help(self) -> None:
        self.assertEqual(main([]), 0)


if __name__ == "__main__":
    unittest.main()
