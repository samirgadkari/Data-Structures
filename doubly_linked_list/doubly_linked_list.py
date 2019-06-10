import math
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def print_node(self, num_spaces):
        prev_value = "None" if self.prev is None else self.prev.value
        next_value = "None" if self.next is None else self.next.value
        value = self.value
        print(f'{" "*num_spaces}{prev_value} <- {value} -> {next_value}')

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next:
            current_next.prev = self.next

        return self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        save_prev, save_next = self.prev, self.next
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return save_prev, save_next


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def print_list(self, num_spaces):

        e = self.head
        print(f'{" "*num_spaces} list length: {self.length}')
        while e is not None:
            e.print_node(num_spaces)
            e = e.next

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is None:
            self.head = self.tail = ListNode(value, None, None)
        else:
            self.head = self.head.insert_before(value)
        self.length += 1

    def remove_from_head(self):
        saved_head = self.head
        _, next = self.head.delete()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = next
        self.length -= 1

        return saved_head.value

    def add_to_tail(self, value):
        if self.tail is None:
            e = ListNode(value, None, None)
            self.head = self.tail = e
        else:
            self.tail = self.tail.insert_after(value)
        self.length += 1

    def remove_from_tail(self):
        saved_tail = self.tail
        prev, _ = self.tail.delete()
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = prev
        self.length -= 1

        return saved_tail.value

    def move_to_front(self, node):
        update_tail = False
        if node == self.tail:
            new_tail = node.prev
            update_tail = True

        inserted_node = self.head.insert_before(node.value)
        self.head = inserted_node
        if update_tail:
            self.tail = new_tail
        node.delete()

    def move_to_end(self, node):
        update_head = False
        if node == self.head:
            new_head = node.next
            update_head = True

        inserted_node = self.tail.insert_after(node.value)  # 1 -> 40 -> None
        self.tail = inserted_node

        if update_head:
            self.head = new_head
        node.delete()

    def delete(self, node):
        if (node == self.head) and (node == self.tail):
            node.delete()
            self.head = None
            self.tail = None
        elif node == self.head:
            node_next = node.next
            node.delete()
            self.head = node_next
        elif node == self.tail:
            node_prev = node.prev
            node.delete()
            self.tail = node_prev
        else:
            node.delete()

        self.length -= 1

    def get_max(self):
        e = self.head
        if e is None:
            return None
        max_val = e.value
        while (e is not None) and (e.next is not None):
            e = e.next
            max_val = max(max_val, e.value)

        return max_val
