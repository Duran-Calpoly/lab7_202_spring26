import unittest

from lab7_1 import MinHeap
from lab7_2 import PriorityQueue, enqueue, dequeue


class TestPriorityQueue(unittest.TestCase):
    def test_enqueue(self):
        pq = PriorityQueue(heap=MinHeap(heap=[10, 20, 30]))
        result = enqueue(pq, 5)
        self.assertEqual(result.heap.heap, [5, 10, 30, 20])

    def test_enqueue_multiple(self):
        pq = PriorityQueue(heap=MinHeap(heap=[5]))
        pq = enqueue(pq, 3)
        pq = enqueue(pq, 8)
        pq = enqueue(pq, 1)
        self.assertEqual(pq.heap.heap, [1, 3, 8, 5])

    def test_dequeue(self):
        pq = PriorityQueue(heap=MinHeap(heap=[1, 3, 8, 5]))
        value, new_pq = dequeue(pq)
        self.assertEqual(value, 1)
        self.assertEqual(new_pq.heap.heap, [3, 5, 8])

    def test_dequeue_twice(self):
        pq = PriorityQueue(heap=MinHeap(heap=[1, 3, 8, 5]))
        value1, pq = dequeue(pq)
        value2, pq = dequeue(pq)

        self.assertEqual(value1, 1)
        self.assertEqual(value2, 3)
        self.assertEqual(pq.heap.heap, [5, 8])

    def test_enqueue_then_dequeue(self):
        pq = PriorityQueue(heap=MinHeap(heap=[4, 7, 9]))
        pq = enqueue(pq, 2)
        value, pq = dequeue(pq)

        self.assertEqual(value, 2)
        self.assertEqual(pq.heap.heap, [4, 7, 9])


if __name__ == "__main__":
    unittest.main()