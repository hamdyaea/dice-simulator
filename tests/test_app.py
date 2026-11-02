# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
FILE = Path(__file__).resolve().parents[1] / "DiceSimulator.py"
spec = importlib.util.spec_from_file_location("app_under_test", FILE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class ApplicationTests(unittest.TestCase):

    def test_roll(self):
        self.assertEqual(len(app.roll(6, 4)), 4)
        self.assertTrue(all(1 <= n <= 6 for n in app.roll(6, 20)))

    def test_validation(self):
        with self.assertRaises(ValueError): app.roll(1, 1)
        with self.assertRaises(ValueError): app.roll(6, 0)

    def test_gui(self):
        window = app.DiceApp()
        try:
            window.throw()
            self.assertTrue(window.result.get().isdigit())
        finally: window.destroy()

if __name__ == "__main__":
    unittest.main()
