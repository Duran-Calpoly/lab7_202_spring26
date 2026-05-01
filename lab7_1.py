from dataclasses import dataclass


@dataclass(frozen=True)
class MinHeap:
    heap: list[int]


def insert(minheap: MinHeap, value: int) -> MinHeap:
    new_heap = minheap.heap + [value]
    new_heap = heapify_up(new_heap, len(new_heap) - 1)
    return MinHeap(heap=new_heap)


def extract(minheap: MinHeap) -> tuple[int, MinHeap]:
    min_value = minheap.heap[0]
    last_value = minheap.heap[-1]
    new_heap = [last_value] + minheap.heap[1:-1]
    new_heap = heapify_down(new_heap, 0)
    return min_value, MinHeap(heap=new_heap)


def heapify_up(heap: list[int], index: int) -> list[int]:
    new_heap = heap[:]

    if index == 0:
        return new_heap

    parent = (index - 1) // 2

    if new_heap[index] < new_heap[parent]:
        temp = new_heap[index]
        new_heap[index] = new_heap[parent]
        new_heap[parent] = temp
        return heapify_up(new_heap, parent)

    return new_heap


def heapify_down(heap: list[int], index: int) -> list[int]:
    new_heap = heap[:]
    left = 2 * index + 1
    right = 2 * index + 2
    size = len(new_heap)

    if left >= size:
        return new_heap

    smallest = left

    if right < size and new_heap[right] < new_heap[left]:
        smallest = right

    if new_heap[smallest] < new_heap[index]:
        temp = new_heap[index]
        new_heap[index] = new_heap[smallest]
        new_heap[smallest] = temp
        return heapify_down(new_heap, smallest)

    return new_heap