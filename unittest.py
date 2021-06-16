import unittest
import Arithmetics


class TestTesting(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Arithmetics.add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(Arithmetics.sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(Arithmetics.mul(10, 5), 50)

    def test_div(self):
        self.assertEqual(Arithmetics.div(10, 5), 2)
        self.assertEqual(Arithmetics.div(12, 4), 3)
        with self.assertRaises(ValueError):
            Arithmetics.div(10, 0)


if __name__ == "__main__":
    unittest.main()
