import unittest

from lab7_1 import MinHeap, insert, extract, heapify_up, heapify_down


class TestMinHeap(unittest.TestCase):
    def test_insert(self):
        h = MinHeap(heap=[10, 20, 30])
        result = insert(h, 5)
        self.assertEqual(result.heap, [5, 10, 30, 20])

    def test_insert_multiple(self):
        pass

    def test_extract(self):
        h = MinHeap(heap=[1, 3, 8, 5])
        value, new_h = extract(h)
        self.assertEqual(value, 1)
        self.assertEqual(new_h.heap, [3, 5, 8])

    def test_extract_twice(self):
        pass

    def test_heapify_up(self):
        heap = [5, 10, 8, 20, 15, 9, 1]
        result = heapify_up(heap, 6)
        self.assertEqual(result, [1, 10, 5, 20, 15, 9, 8])

    def test_heapify_down(self):
        heap = [9, 3, 5]
        result = heapify_down(heap, 0)
        self.assertEqual(result, [3, 9, 5])


if __name__ == "__main__":
    unittest.main()
