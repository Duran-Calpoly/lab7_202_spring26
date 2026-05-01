from dataclasses import dataclass

from lab7_1 import MinHeap, insert, extract


@dataclass(frozen=True)
class PriorityQueue:
    heap: MinHeap


def enqueue(pq: PriorityQueue, value: int) -> PriorityQueue:
    pass


def dequeue(pq: PriorityQueue) -> tuple[int, PriorityQueue]:
    pass
