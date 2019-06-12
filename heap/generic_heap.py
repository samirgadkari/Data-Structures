class Heap:
    LEFT_NODE = 0
    RIGHT_NODE = 1
    UPDATE_UPWARDS = 0
    UPDATE_DOWNWARDS = 1

    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator

    def swap_these(self, p_idx, p_value, l_idx, l_value, r_idx, r_value):
        if l_value is None and r_value is not None:
            if self.comparator(p_value, r_value):
                return p_idx, p_idx
            else:
                return p_idx, r_idx

        if r_value is None and l_value is not None:
            if self.comparator(p_value, l_value):
                return p_idx, p_idx
            else:
                return p_idx, l_idx

        if self.comparator(p_value, l_value) and self.comparator(
                p_value, r_value):
            return p_idx, p_idx

        if self.comparator(l_value, r_value):
            return p_idx, l_idx
        else:
            return p_idx, r_idx

    def node_left_or_right(self, original_idx):
        if (original_idx - 1) % 2 == 0:  # Left node
            return Heap.LEFT_NODE
        if (original_idx - 2) % 2 == 0:  # Right node
            return Heap.RIGHT_NODE
        raise ValueError(
            f"Node index {original_idx} is neither left or right node")

    def parent_idx(self, original_idx):
        pos = self.node_left_or_right(original_idx)
        if pos == Heap.LEFT_NODE:
            return (original_idx - 1) // 2
        else:
            return (original_idx - 2) // 2

    def child_indexes(self, original_idx):
        i = original_idx * 2
        return i + 1, i + 2

    def update_structure(self, idx, direction):
        if ((idx == 0) and (direction == Heap.UPDATE_UPWARDS)) or (
            (idx >= len(self.storage)) and
            (direction == Heap.UPDATE_DOWNWARDS)):
            return

        if direction == Heap.UPDATE_UPWARDS:
            p_idx = self.parent_idx(idx)
            l_idx, r_idx = self.child_indexes(p_idx)
        else:
            p_idx = idx
            l_idx, r_idx = self.child_indexes(p_idx)

        p_value = self.storage[p_idx]

        l_value = r_value = None
        if l_idx < len(self.storage):
            l_value = self.storage[l_idx]

        if r_idx < len(self.storage):
            r_value = self.storage[r_idx]

        if (l_value is None) and (r_value is None):
            return
        idx1, idx2 = self.swap_these(p_idx, p_value, l_idx, l_value, r_idx,
                                     r_value)

        if idx1 != idx2:
            self.storage[idx1], self.storage[idx2] = self.storage[
                idx2], self.storage[idx1]
            if direction == Heap.UPDATE_UPWARDS:
                self.update_structure(p_idx, direction)
            else:
                if self.storage[idx1] == self.storage[idx2]:
                    return
                if idx1 > idx2:
                    self.update_structure(idx1, direction)
                else:
                    self.update_structure(idx2, direction)

    def print_heap(self, s):
        print(s)
        for i in range(len(self.storage)):
            print(self.storage[i], end=' ')
        print()

    def insert(self, value):
        '''Inserts element at the correct location in the heap'''

        insert_idx = len(self.storage)
        self.storage.append(value)
        self._bubble_up(insert_idx)

    def delete(self):
        '''Deletes the top of the heap (the root)'''

        res = self.storage[0]

        # Swap root element with the last element
        last_idx = len(self.storage) - 1
        self.storage[last_idx], self.storage[0] = self.storage[
            0], self.storage[last_idx]

        # Delete the last element (which was the root element)
        self.storage = self.storage[:-1]

        # Heapify the whole heap
        self._sift_down(0)
        return res

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        self.update_structure(index, Heap.UPDATE_UPWARDS)

    def _sift_down(self, index):
        self.update_structure(index, Heap.UPDATE_DOWNWARDS)
