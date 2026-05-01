# Lab 7: Heaps and Priority Queues

## CSC 202

In this lab, you will practice working with two closely related data structures:

- Min-heaps
- Priority queues

A min-heap allows us to efficiently keep track of the smallest element. A priority queue can be built on top of a min-heap so that elements are removed in priority order.

---

## Learning Goals

By the end of this lab, you should be able to:

- understand the behavior of a min-heap
- trace how insert and extract affect heap structure
- write unit tests to confirm expected behavior
- implement a priority queue using heap operations
- use previously written functions as building blocks for a new abstraction

---

## Files

You will work with these files:

- `lab7_1.py`
- `test_1.py`
- `lab7_2.py`
- `test_2.py`

---

## Day 1: MinHeap Testing

For Day 1, your goal is to **confirm the behavior of the `MinHeap`**.

The heap operations have already been implemented for you. Your job is to study the provided code and write unit tests for the missing test cases.

### Your tasks

In `test_1.py`:

- read the existing `MinHeap` code in `lab7_1.py`
- understand how `insert`, `extract`, `heapify_up`, and `heapify_down` behave
- write **one test case for each missing unit test**
- run your tests and confirm they pass

### Focus

Your goal is not to rewrite the heap implementation. Your goal is to verify that the implementation behaves correctly.

---

## Day 2: Priority Queue Implementation

For Day 2, you will build a priority queue on top of your heap functions.

You will use the imported heap functions from Day 1 to complete the priority queue operations.

### Your tasks

In `lab7_2.py`:

- implement `enqueue`
- implement `dequeue`

These functions should use the imported heap functions rather than reimplementing heap logic from scratch.

Then, in `test_2.py`:

- run the provided unit tests
- confirm that your priority queue implementation works correctly

---

## Submission Checklist

Before asking for sign-off, make sure you have completed all of the following:

- completed the missing unit tests in `test_1.py`
- implemented `enqueue` in `lab7_2.py`
- implemented `dequeue` in `lab7_2.py`
- run all tests successfully
- checked that your code follows the required function-based style

---

## Sign-Off

Once both days are complete, **get signed off by the TA or instructor**.

Be prepared to explain:

- how a min-heap maintains order
- what `heapify_up` does
- what `heapify_down` does
- how a priority queue uses heap operations
- how your tests confirm correctness

---
