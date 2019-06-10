class Node:
    def __init__(self, item=None):
        self.next = None
        self.prev = None
        self.item = item


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.head = None
        self.tail = None

    def enqueue(self, item):
        e = Node(item)

        temp = self.head
        if temp is not None:
            temp.prev = e
        e.next = temp
        e.prev = None

        self.head = e
        if temp is None:
            self.tail = self.head
        self.size += 1

    def dequeue(self):
        if self.tail is None:
            return None

        e = self.tail
        if e.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = e.prev

        self.size -= 1
        return e.item

    def len(self):
        return self.size
