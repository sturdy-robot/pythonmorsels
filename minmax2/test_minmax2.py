import unittest

from minmax2 import minmax2


class MinMaxTests(unittest.TestCase):

    """Tests for minmax."""

    def test_ordered_numbers(self):
        self.assertEqual(minmax2([0, 1, 2, 3, 4]), (0, 4))

    def test_with_out_of_order_numbers(self):
        self.assertEqual(minmax2([10, 8, 7, 5.0, 3, 6, 2]), (2, 10))

    def test_single_item(self):
        self.assertEqual(minmax2([10]), (10, 10))

    def test_same_item_multiple_times(self):
        self.assertEqual(minmax2([8, 8, 8]), (8, 8))
        self.assertEqual(minmax2([7, 5, 6, 5, 7]), (5, 7))

    def test_negative_numbers(self):
        self.assertEqual(minmax2([-10, -8, -7, -5, -3]), (-10, -3))

    def test_strings(self):
        words = ["alfalfa", "animal", "apple", "acoustic", "axiom"]
        self.assertEqual(minmax2(words), ("acoustic", "axiom"))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            minmax2(['a', 2])

    def test_very_large_numbers(self):
        self.assertEqual(minmax2([2 ** 1000, -2 ** 1000]), (-2 ** 1000, 2 ** 1000))

    def test_error_on_empty_iterable(self):
        with self.assertRaises(ValueError):
            minmax2([])

    def test_default_value(self):
        self.assertEqual(minmax2([], default=0), (0, 0))
        self.assertEqual(minmax2([], default=None), (None, None))
        self.assertEqual(minmax2([], default='a'), ('a', 'a'))
        self.assertEqual(minmax2([-10], default='a'), (-10, -10))
        self.assertEqual(minmax2([10], default='a'), (10, 10))
        with self.assertRaises(TypeError):
            minmax2([1], 0)

    def test_key_functions(self):
        words = ["alfalfa", "animal", "apple", "acoustic"]
        self.assertEqual(minmax2(words, key=len), ("apple", "acoustic"))
        def a_count(word): return word.count('a')
        self.assertEqual(minmax2(words, key=a_count), ("apple", "alfalfa"))
        with self.assertRaises(TypeError):
            minmax2([1], lambda x: x)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_with_non_lists(self):
        self.assertEqual(minmax2((89, 17, 70, 9)), (9, 89))
        self.assertEqual(minmax2({8, 7, 5, 3, 9, 6, 2}), (2, 9))
        self.assertEqual(minmax2(n ** 2 for n in range(1, 4)), (1, 9))
        with self.assertRaises(ValueError):
            minmax2(iter([]))

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_response_min_and_max_attributes(self):
        words = ["alfalfa", "animal", "apple", "acoustic", "axiom"]
        output = minmax2(words)
        self.assertEqual(output.min, "acoustic")
        self.assertEqual(output.max, "axiom")

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_any_number_of_arguments(self):
        self.assertEqual(minmax2(1, 8, 3, 9, 2), (1, 9))
        self.assertEqual(minmax2('hi', 'hey'), ('hey', 'hi'))
        self.assertEqual(minmax2('a'), ('a', 'a'))
        self.assertEqual(minmax2('abcd'), ('a', 'd'))
        with self.assertRaises(TypeError):
            minmax2()


if __name__ == "__main__":
    unittest.main(verbosity=2)