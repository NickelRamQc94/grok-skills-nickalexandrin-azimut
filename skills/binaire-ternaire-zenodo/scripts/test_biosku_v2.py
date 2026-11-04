#!/usr/bin/env python3
import time, unittest
from BioSKU_Engine import BioSKUEngine, STATE_SYNTH, STATE_COLD

class TestBioSKU(unittest.TestCase):
    def setUp(self):
        self.eng = BioSKUEngine()
    def test_happy_path(self):
        self.eng.run_sequence(["K11", "S1Ø", "U99"])
        self.assertEqual(self.eng.state_name, STATE_SYNTH)
        self.assertTrue(self.eng.is_connected)
    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            self.eng.execute("AB")
    def test_invalid_op(self):
        with self.assertRaises(ValueError):
            self.eng.execute("X11")
    def test_reset(self):
        self.eng.run_sequence(["K11", "S1Ø"]); self.eng.reset()
        self.assertEqual(self.eng.state_name, STATE_COLD)
        self.assertEqual(self.eng.exec_count, 0)
    def test_determinism(self):
        a, b = BioSKUEngine(), BioSKUEngine()
        self.assertEqual(a.run_sequence(["K11", "S1Ø", "U99"]), b.run_sequence(["K11", "S1Ø", "U99"]))
    def test_run_safe(self):
        r = self.eng.run_safe(["K11", "BAD", "U99"])
        self.assertEqual(len(r["errors"]), 1)
        self.assertEqual(self.eng.exec_count, 2)
    def test_stress_1000(self):
        t0 = time.perf_counter()
        for _ in range(1000):
            self.eng.reset(); self.eng.run_sequence(["K11", "S1Ø", "U99"])
        self.assertLess(time.perf_counter()-t0, 2.0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
