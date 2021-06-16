import unitesting
import arithmetics


class TestTesting(unitesting.TestCase):

    def test_add(self):
        self.assertEqual(arithmetics.add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(arithmetics.sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(arithmetics.mul(10, 5), 50)

    def test_div(self):
        self.assertEqual(arithmetics.div(10, 5), 2)
        self.assertEqual(arithmetics.div(12, 4), 3)
        with self.assertRaises(ValueError):
            arithmetics.div(10, 0)


if __name__ == "__main__":
    unitesting.main()
