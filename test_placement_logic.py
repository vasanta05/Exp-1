
import unittest
from placement_logic import predict_placement


class TestPlacementLogic(unittest.TestCase):

    def test_placed_student(self):
        self.assertEqual(
            predict_placement(8.0, 75, 80),
            "PLACED"
        )

    def test_low_cgpa(self):
        self.assertEqual(
            predict_placement(6.0, 75, 80),
            "NOT PLACED"
        )

    def test_low_aptitude_score(self):
        self.assertEqual(
            predict_placement(8.0, 40, 80),
            "NOT PLACED"
        )

    def test_low_communication_score(self):
        self.assertEqual(
            predict_placement(8.0, 75, 40),
            "NOT PLACED"
        )


if __name__ == "__main__":
    unittest.main()
