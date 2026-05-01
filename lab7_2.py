from dataclasses import dataclass

from lab7_1 import MinHeap, insert, extract


@dataclass(frozen=True)
class PriorityQueue:
    heap: MinHeap


def enqueue(pq: PriorityQueue, value: int) -> PriorityQueue:
    new_heap = insert(pq.heap, value)
    return PriorityQueue(heap=new_heap)


def dequeue(pq: PriorityQueue) -> tuple[int, PriorityQueue]:
    value, new_heap = extract(pq.heap)
    return value, PriorityQueue(heap=new_heap)