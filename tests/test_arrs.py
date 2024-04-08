import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -1), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 4), [2, 3, 4])

    def test_my_slice_with_negative_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, -1), [2, 3])

    def test_my_slice_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], None, -2), [1, 2, 3])

    def test_my_slice_end_more_than_len(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], None, 4), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 4), [2, 3])

    def test_my_slice_end_none(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], None, None),[1, 2, 3])

    def test_my_slice_zero(self):
        self.assertEqual([],[])

    def test_my_slice_star_end_none(self):
        self.assertEqual(arrs.my_slice([], None, None),[])