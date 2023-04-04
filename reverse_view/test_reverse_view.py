from collections.abc import Generator, Iterable
import sys
import unittest


from reverse_view import ReverseView


class ReverseViewTests(unittest.TestCase):

    """Tests for ReverseView."""

    def test_can_iterate_at_least_once(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])

    def test_can_iterate_more_than_once(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])
        self.assertEqual(list(view), list(view))

    def test_updating_sequence_updates_view(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])
        numbers.append(29)
        self.assertEqual(list(view), [29, 18, 11, 7, 4, 3, 1, 2])
        numbers.pop(0)
        self.assertEqual(list(view), [29, 18, 11, 7, 4, 3, 1])

    def test_no_memory_used(self):
        numbers = list(range(10000))
        view = ReverseView(numbers)
        self.assertLess(
            get_size(view, seen={id(numbers)}),
            get_size(numbers)//2,
            'Too much memory used',
        )
        self.assertNotEqual(type(view), list)
        self.assertNotEqual(type(view), tuple)

    def test_does_not_slice_sequence(self):
        class UnsliceableList(list):
            def __getitem__(self, index):
                if not isinstance(index, int):
                    return NotImplemented("Only indexes accepted")
                return super().__getitem__(index)
        numbers = UnsliceableList([2, 1, 3, 4, 7, 11, 18])
        view = ReverseView(numbers)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])

    # To test bonus 1, comment out the next line.
    #@unittest.expectedFailure
    def test_has_length_and_repr_and_is_indexable(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)

        # Has length
        self.assertEqual(len(view), 7)
        self.assertEqual(len(view), 7)
        numbers.append(29)
        self.assertEqual(len(view), 8)
        numbers.pop()
        self.assertEqual(len(view), 7)

        # Is indexable
        self.assertEqual(view[0], 18)
        self.assertEqual(view[-1], 2)
        self.assertEqual(view[2], 7)
        self.assertEqual(view[-2], 1)
        numbers.append(29)
        self.assertEqual(view[0], 29)
        self.assertEqual(view[-1], 2)
        numbers.pop(0)
        self.assertEqual(view[0], 29)
        self.assertEqual(view[-1], 1)

        # Has a nice string representation
        self.assertEqual(list(view), [29, 18, 11, 7, 4, 3, 1])
        self.assertEqual(str(view), "[29, 18, 11, 7, 4, 3, 1]")

    # To test bonus 2, comment out the next line.
    @unittest.expectedFailure
    def test_slicing_count_method_and_index_method(self):
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)

        # Slicing
        self.assertEqual(list(view[:3]), [18, 11, 7])
        self.assertEqual(list(view[2:]), [7, 4, 3, 1, 2])
        self.assertEqual(list(view[:-1]), [18, 11, 7, 4, 3, 1])
        self.assertEqual(list(view[::-1]), numbers)

        # count and index methods
        self.assertEqual(view.count(4), 1)
        self.assertEqual(view.index(4), 3)
        self.assertEqual(view.count(5), 0)
        with self.assertRaises(ValueError):
            view.index(5)
        self.assertEqual(view.index(3), 4)
        numbers.insert(0, 3)
        self.assertEqual(view.index(3), 4)
        self.assertEqual(view.count(3), 2)
        numbers.append(3)
        self.assertEqual(view.index(3), 0)
        self.assertEqual(view.count(3), 3)

    # To test bonus 3, comment out the next line.
    @unittest.expectedFailure
    def test_mutability(self):
        # Supports mutation for mutable sequences
        numbers = [2, 1, 3, 4, 7, 11, 18]
        view = ReverseView(numbers)
        view.pop()
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1])
        self.assertEqual(list(numbers), [1, 3, 4, 7, 11, 18])
        view.pop(-1)
        self.assertEqual(list(view), [18, 11, 7, 4, 3])
        self.assertEqual(list(numbers), [3, 4, 7, 11, 18])
        view.extend([1, 2])
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2])
        self.assertEqual(list(numbers), [2, 1, 3, 4, 7, 11, 18])
        view.append(0)
        self.assertEqual(list(view), [18, 11, 7, 4, 3, 1, 2, 0])
        self.assertEqual(list(numbers), [0, 2, 1, 3, 4, 7, 11, 18])
        view.pop(1)
        self.assertEqual(list(view), [18, 7, 4, 3, 1, 2, 0])
        view.insert(1, 14)
        self.assertEqual(list(view), [18, 14, 7, 4, 3, 1, 2, 0])
        view.insert(0, 29)
        self.assertEqual(list(view), [29, 18, 14, 7, 4, 3, 1, 2, 0])
        self.assertEqual(list(numbers), [0, 2, 1, 3, 4, 7, 14, 18, 29])
        view[0] = -1
        self.assertEqual(list(view), [-1, 18, 14, 7, 4, 3, 1, 2, 0])

        # Doesn't support mutation for immutable sequences
        numbers = (2, 1, 3, 4, 7, 11, 18)
        view = ReverseView(numbers)
        with self.assertRaises(Exception):
            view.append(29)
        with self.assertRaises(Exception):
            view.insert(0, 29)
        with self.assertRaises(Exception):
            view.pop()


def get_size(obj, seen=None):
    """Return size of any Python object."""
    if seen is None:
        seen = set()
    size = sys.getsizeof(obj)
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    if isinstance(obj, Generator):
        next(obj)
        size += sum(
            get_size(value, seen)
            for value in obj.gi_frame.f_locals.values()
        )
    elif hasattr(obj, '__slots__'):
        size += sum(
            get_size(getattr(obj, attr), seen)
            for attr in obj.__slots__
            if hasattr(obj, attr)
        )
    elif hasattr(obj, '__dict__'):
        dict_size = get_size(obj.__dict__, seen)
        size += dict_size
        if isinstance(obj, Iterable):
            next(iter(obj))
            seen.remove(id(obj.__dict__))
            size += max(
                get_size(obj.__dict__, seen) - sys.getsizeof(obj.__dict__),
                0)
    if isinstance(obj, dict):
        size += sum(
            get_size(k, seen) + get_size(v, seen)
            for k, v in obj.items()
        )
    elif isinstance(obj, (list, tuple, set, frozenset)):
        size += sum(get_size(item, seen) for item in obj)
    return size


class AllowUnexpectedSuccessRunner(unittest.TextTestRunner):
    """Custom test runner to avoid FAILED message on unexpected successes."""
    class resultclass(unittest.TextTestResult):
        def wasSuccessful(self):
            return not (self.failures or self.errors)


if __name__ == "__main__":
    from platform import python_version
    if sys.version_info < (3, 6):
        sys.exit("Running {}.  Python 3.6 required.".format(python_version()))
    unittest.main(verbosity=2, testRunner=AllowUnexpectedSuccessRunner)
