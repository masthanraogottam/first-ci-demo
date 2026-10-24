"""Unit tests for result_logic.py."""

import unittest

from result_logic import predict_result


class TestPredictResult(unittest.TestCase):
    def test_pass_when_marks_and_attendance_meet_requirements(self):
        self.assertEqual(predict_result(70, 85), "PASS")

    def test_fail_when_marks_are_below_requirement(self):
        self.assertEqual(predict_result(30, 85), "FAIL")

    def test_fail_when_attendance_is_below_requirement(self):
        self.assertEqual(predict_result(70, 60), "FAIL")


if __name__ == "__main__":
    unittest.main()
