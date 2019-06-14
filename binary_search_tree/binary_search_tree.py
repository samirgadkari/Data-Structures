import math


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        e = BinarySearchTree(value)
        if e.value <= self.value:
            if self.left is None:
                self.left = e
                return
            self.left.insert(value)
        else:
            if self.right is None:
                self.right = e
                return
            self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

        return False

    def get_max(self):
        max_val = self.value
        if self.left:
            max_val = max(self.left.get_max(), max_val)
        if self.right:
            max_val = max(self.right.get_max(), max_val)
        return max_val

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
