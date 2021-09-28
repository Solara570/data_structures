from arrays import Array
from nodes import Node
from abstract_collection import AbstractCollection


class LinkedQueue(AbstractCollection):
    """
    A queue implementation based on linked list.
    """

    # Constructor
    def __init__(self, source_collection=None):
        self.clear()
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        Visits items from front to rear of the queue.
        """
        probe = self.front
        while probe is not None:
            yield probe.data
            probe = probe.next

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: The stack is not empty.
        Raises KeyError if the stack is empty.
        """
        if self.is_empty():
            raise KeyError("The queue is empty.")
        return self.front.data

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.front = None
        self.rear = None
        self.size = 0

    def add(self, item):
        """
        Inserts item at the rear of the queue.
        """
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises KeyError if the queue is empty.
        """
        if self.is_empty():
            raise KeyError("The queue is empty.")
        front_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return front_item

    def remove(self, item):
        """
        Removes a given item from the queue.
        Precondition: the item is in the queue.
        Raises KeyError if item is not in the queue.
        """
        if self.is_empty():
            raise KeyError(f"'{item}' not in queue.")
        prev = self.front
        probe = self.front.next
        if prev.data == item:
            self.front = self.front.next
        else:
            while probe is not None:
                if probe.data == item:
                    prev.next = probe.next
                    break
                prev = prev.next
                probe = probe.next
            if probe is None:
                raise KeyError(f"'{item}' not in queue.")
        self.size -= 1


class ArrayQueue(AbstractCollection):
    """
    A queue implementation based on Array.
    """

    # Class Variables
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        self.clear()
        AbstractCollection.__init__(self, source_collection)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        Visits items from front to rear of the queue.
        """
        count = 0
        cursor = self.front
        while cursor is not None and count < len(self):
            yield self.items[cursor]
            cursor = (cursor + 1) % len(self.items)
            count += 1

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: The queue is not empty.
        Raises KeyError if the queue is empty.
        """
        if self.is_empty():
            raise KeyError("The queue is empty.")
        return self.items[self.front]

    # Mutators
    def clear(self):
        """
        Makes self become empty.
        """
        self.items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self.front = None
        self.rear = None
        self.size = 0

    def add(self, item):
        """
        Inserts item at the rear of the queue.
        """
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.items[0] = item
        else:
            if len(self) == len(self.items):
                temp = Array(len(self.items) * 2)
                cursor = 0
                for curr_item in self:
                    temp[cursor] = curr_item
                    cursor += 1
                self.items = temp
                self.front = 0
                self.rear = len(self) - 1
            self.rear = (self.rear + 1) % len(self.items)
            self.items[self.rear] = item
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises KeyError if the queue is empty.
        """
        if self.is_empty():
            raise KeyError("The queue is empty.")
        front_item = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        if self.is_empty():
            self.clear()
        elif len(self.items) >= 2 * ArrayQueue.DEFAULT_CAPACITY and len(self) <= len(self.items) // 2:
            temp = Array(len(self.items) // 2)
            cursor = 0
            for curr_item in self:
                temp[cursor] = curr_item
                cursor += 1
            self.items = temp
            self.front = 0
            self.rear = len(self) - 1
        return front_item

    def remove(self, item):
        """
        Removes a given item from the queue.
        Precondition: the item is in the queue.
        Raises KeyError if item is not in the queue.
        """
        if self.is_empty():
            raise KeyError(f"'{item}' not in queue.")
        cursor = self.front
        for array_item in self:
            if array_item == item:
                break
            cursor = (cursor + 1) % len(self.items)
        if cursor == (self.rear + 1) % len(self.items):
            raise KeyError(f"'{item}' not in queue.")
        elif self.is_empty():
            self.clear()
        elif cursor >= self.front:
            for ind in range(cursor, self.front - 1, -1):
                self.items[ind] = self.items[ind - 1]
            self.front = (self.front + 1) % len(self.items)
        else:
            for ind in range(cursor, self.rear):
                self.items[ind] = self.items[ind + 1]
            self.rear = (self.rear + len(self.items) - 1) % len(self.items)
        self.size -= 1


class LinkedPriorityQueue(LinkedQueue):
    """
    A priority queue implementation based on linked list.
    Inherent most methods from LinkedQueue.
    """

    def __init__(self, source_collection=None):
        LinkedQueue.__init__(self, source_collection)

    def add(self, new_item):
        """
        Inserts a new item based on its priority.
        Note: A has a greater priority than B if A < B.
        """
        if self.is_empty() or new_item > self.rear.data:
            # Least priority - add to the back
            LinkedQueue.add(self, new_item)
        else:
            # Search for a position for the new item
            probe = self.front
            while probe is not None and new_item >= probe.data:
                trailer = probe
                probe = probe.next
            # The new item should be added before probe
            new_node = Node(new_item, probe)
            if probe == self.front:
                self.front = new_node
            else:
                trailer.next = new_node
            self.size += 1
