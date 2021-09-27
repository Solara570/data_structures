from abstract_stack import AbstractStack
from arrays import Array
from nodes import Node


class ArrayStack(AbstractStack):
    """
    A stack implementation based on Array.
    """

    # Class Variables
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        self.clear()
        AbstractStack.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        Visits items from bottom to top of the stack.
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: The stack is not empty.
        Raises KeyError if the stack is empty.
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        return self.items[len(self) - 1]

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        self.size = 0

    def push(self, item):
        """
        Inserts item at the top of the stack.
        """
        self.items.append(item)
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if the stack is empty.
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        top_item = self.items.pop(len(self) - 1)
        self.size -= 1
        return top_item


class LinkedStack(AbstractStack):
    """
    A stack implementation based on linked list.
    """

    # Constructor
    def __init__(self, source_collection=None):
        self.clear()
        AbstractStack.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        Visits items from bottom to top of the stack.
        Use a list to keep track of the items
        """
        iter_list = list()

        def visit_nodes(head):
            if head is not None:
                visit_nodes(head.next)
                iter_list.append(head.data)
        visit_nodes(self.items)
        return iter(iter_list)

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: The stack is not empty.
        Raises KeyError if the stack is empty.
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        return self.items.data

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = None
        self.size = 0

    def push(self, item):
        """
        Inserts item at the top of the stack.
        """
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if the stack is empty.
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        top_item = self.items.data
        self.items = self.items.next
        self.size -= 1
        return top_item
