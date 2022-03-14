import unittest

from sortownia.sortowanie import bubblesort
from sortownia.sortowanie import quick_sort
from sortownia.sortowanie import insertion_sort


class TestBubblesort(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        returned_list = bubblesort(empty_list)
        self.assertListEqual([], returned_list)
        self.assertListEqual([], empty_list)

    def test_one_value_list(self):
        one_value_list = [1]
        returned_list = bubblesort(one_value_list)
        self.assertListEqual([1], returned_list)
        self.assertListEqual([1], one_value_list)

    def test_sorted_list(self):
        sorted_list = [-12, 14, 16, 34, 66]
        returned_list = bubblesort(sorted_list)
        self.assertListEqual([-12, 14, 16, 34, 66], returned_list)
        self.assertListEqual([-12, 14, 16, 34, 66], sorted_list)

    def test_unsorted_list(self):
        unsorted_list = [4, 10, 1, -3, 8, -2]
        returned_list = bubblesort(unsorted_list)
        self.assertListEqual([-3, -2, 1, 4, 8, 10], returned_list)
        self.assertListEqual([4, 10, 1, -3, 8, -2], unsorted_list)

    def test_duplicat_value_in_list(self):
        list_with_duplicats = [0, 0, 5, 6, 6, 1, 1]
        returned_list = bubblesort(list_with_duplicats)
        self.assertListEqual([0, 0, 1, 1, 5, 6, 6], returned_list)
        self.assertListEqual([0, 0, 5, 6, 6, 1, 1], list_with_duplicats)

    def test_unsorted_string_list(self):
        str_list = ["c", "q", "a", "f"]
        returned_list = bubblesort(str_list)
        self.assertListEqual(["a", "c", "f", "q"], returned_list)
        self.assertListEqual(["c", "q", "a", "f"], str_list)


class TestQuicksort(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        returned_list = quick_sort(empty_list)
        self.assertListEqual([], returned_list)
        self.assertListEqual([], empty_list)

    def test_one_value_list(self):
        one_value_list = [1]
        returned_list = quick_sort(one_value_list)
        self.assertListEqual([1], returned_list)
        self.assertListEqual([1], one_value_list)

    def test_sorted_list(self):
        sorted_list = [-12, 14, 16, 34, 66]
        returned_list = quick_sort(sorted_list)
        self.assertListEqual([-12, 14, 16, 34, 66], returned_list)
        self.assertListEqual([-12, 14, 16, 34, 66], sorted_list)

    def test_unsorted_list(self):
        unsorted_list = [4, 10, 1, -3, 8, -2]
        returned_list = quick_sort(unsorted_list)
        self.assertListEqual([-3, -2, 1, 4, 8, 10], returned_list)
        self.assertListEqual([4, 10, 1, -3, 8, -2], unsorted_list)

    def test_duplicat_value_in_list(self):
        list_with_duplicats = [0, 0, 5, 6, 6, 1, 1]
        returned_list = quick_sort(list_with_duplicats)
        self.assertListEqual([0, 0, 1, 1, 5, 6, 6], returned_list)
        self.assertListEqual([0, 0, 5, 6, 6, 1, 1], list_with_duplicats)

    def test_unsorted_string_list(self):
        str_list = ["c", "q", "a", "f"]
        returned_list = quick_sort(str_list)
        self.assertListEqual(["a", "c", "f", "q"], returned_list)
        self.assertListEqual(["c", "q", "a", "f"], str_list)


class TestInsertsort(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        returned_list = insertion_sort(empty_list)
        self.assertListEqual([], returned_list)
        self.assertListEqual([], empty_list)

    def test_one_value_list(self):
        one_value_list = [1]
        returned_list = insertion_sort(one_value_list)
        self.assertListEqual([1], returned_list)
        self.assertListEqual([1], one_value_list)

    def test_sorted_list(self):
        sorted_list = [-12, 14, 16, 34, 66]
        returned_list = insertion_sort(sorted_list)
        self.assertListEqual([-12, 14, 16, 34, 66], returned_list)
        self.assertListEqual([-12, 14, 16, 34, 66], sorted_list)

    def test_unsorted_list(self):
        unsorted_list = [4, 10, 1, -3, 8, -2]
        returned_list = insertion_sort(unsorted_list)
        self.assertListEqual([-3, -2, 1, 4, 8, 10], returned_list)
        self.assertListEqual([4, 10, 1, -3, 8, -2], unsorted_list)

    def test_duplicat_value_in_list(self):
        list_with_duplicats = [0, 0, 5, 6, 6, 1, 1]
        returned_list = insertion_sort(list_with_duplicats)
        self.assertListEqual([0, 0, 1, 1, 5, 6, 6], returned_list)
        self.assertListEqual([0, 0, 5, 6, 6, 1, 1], list_with_duplicats)

    def test_unsorted_string_list(self):
        str_list = ["c", "q", "a", "f"]
        returned_list = insertion_sort(str_list)
        self.assertListEqual(["a", "c", "f", "q"], returned_list)
        self.assertListEqual(["c", "q", "a", "f"], str_list)


if __name__ == '__main__':
    unittest.main()
