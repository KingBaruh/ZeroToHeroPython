import numpy as np

class Queue_list:
    def __init__(self, size=10):
        self.queue = np.empty(size)
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        nextTail = self.tail
        if nextTail == len(self.queue) - 1:
            nextTail = 0
        else:
            nextTail += 1

        if nextTail == self.head:
            print("Queue is full")
            return

        self.queue[nextTail] = value
        self.tail = nextTail

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        x = self.queue[self.head]
        if self.head == len(self.queue) - 1:
            self.head = 0
        else:
            self.head += 1

        return x

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[self.head]

    def isEmpty(self):
        return self.head == self.tail

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next





