#!/usr/bin/env python3
# heap.py
# max/min-heap data structure

import math

class Heap:
  def __init__(self):
    self.array = []

  def _parent(self, i):
    return math.floor((i-1)/2)

  def _left(self, i):
    return 2*i + 1

  def _right(self, i):
    return 2*i + 2

  def _swap(self, i, j):
    n = len(self.array)
    if 0 <= i and i < n and 0 <= j and j < n:
      tmp = self.array[i]
      self.array[i] = self.array[j]
      self.array[j] = tmp

  def _heapify(self, i):
    n = len(self.array)
    cur = i
    while True:
      l, r = self._left(i), self._right(i)
      smallest = cur

      if l < n and self.array[l][1] < self.array[i][1]:
        smallest = l

      if r < n and self.array[r][1] < self.array[smallest][1]:
        smallest = r

      if cur != smallest:
        self._swap(cur, smallest)
        cur = smallest

      else:
        break

  def size(self):
    return len(self.array)

  def insert(self, elem, priority=None):
    self.array.append((elem, priority if priority is not None else elem))

    i = len(self.array) - 1
    parent = self._parent(i)
    while i > 0 and self.array[parent][1] > self.array[i][1]:
      self._swap(parent, i)
      i = parent
      parent = self._parent(i)
  
  def peekMin(self):
    return None if len(self.array) == 0 else self.array[0]

  def extractMin(self):
    if len(self.array) == 1:
      return self.array.pop()

    elif len(self.array) > 1:
      minVal, cost = self.array[0]
      last = self.array.pop()
      self.array[0] = last
      self._heapify(0)
      return (minVal, cost)

    else:
      return None


def testHeap():
  h = Heap()
  h.insert(5)
  h.insert(6)
  h.insert(1)
  h.insert(3)
  h.insert(7)

  print("{} should equal 1", h.extractMin())
  print("{} should equal 3", h.extractMin())
  print("{} should equal 5", h.extractMin())
  print("{} should equal 6", h.extractMin())
  print("{} should equal 7", h.extractMin())

if __name__ == "__main__":
  testHeap()
