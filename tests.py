import unittest

from run import Run


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.run = Run()

    def test_empty_string(self):
        input_str = ""
        self.assertEqual(self.run.process_input(input_str), 0)

    def test_single_A(self):
        input_str = "A"
        self.assertEqual(self.run.process_input(input_str), 50)

    def test_three_As(self):
        input_str = "AAA"
        self.assertEqual(self.run.process_input(input_str), 130)

    def test_three_A_With_B(self):
        input_str = "AAAB"
        self.assertEqual(self.run.process_input(input_str), 160)

    def test_two_A_two_B(self):
        input_str = "AABB"
        self.assertEqual(self.run.process_input(input_str), 145)

    def test_six_As(self):
        input_str = "AAAAAA"
        self.assertEqual(self.run.process_input(input_str), 260)

    def test_threeAs_threeBs(self):
        input_str = "ABABAB"
        self.assertEqual(self.run.process_input(input_str), 205)


if __name__ == '__main__':
    unittest.main()
