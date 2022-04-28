from nodes import Node
from arrays import Array
from abstract_set import AbstractSet
from abstract_collection import AbstractCollection


class HashSet(AbstractSet, AbstractCollection):
    """
    A set implementation based on hashing
    with bucket/chaining to resolve collisions.
    Inherent set-specific methods from AbstractSet.
    """

    # Class variables
    DEFAULT_CAPACITY = 29

    # Constructor
    def __init__(self, source_collection=None, capacity=None):
        self.capacity = HashSet.DEFAULT_CAPACITY if capacity is None else capacity
        self.items = Array(self.capacity)
        self.found_node = self.prior_node = None
        self.index = -1
        AbstractCollection.__init__(self, source_collection)

    # Accessor methods
    def __contains__(self, item):
        """
        Returns True if item is in the set, or False otherwise.
        Record index, prior_node and found_node during the process
        for further use.
        """
        self.index = abs(hash(item)) % len(self.items)
        self.prior_node = None
        self.found_node = self.items[self.index]
        while self.found_node is not None:
            if self.found_node.data == item:
                return True
            else:
                self.prior_node = self.found_node
                self.found_node = self.found_node.next
        return False

    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        for index in range(len(self.items)):
            node = self.items[index]
            while node is not None:
                yield node.data
                node = node.next

    def __str__(self):
        """
        Returns the string representation of self.
        """
        return "{" + ", ".join([str(item) for item in self]) + "}"

    # Mutator methods
    def clear(self):
        """
        Makes self become empty.
        """
        self.size = 0
        self.found_node = self.prior_node = None
        self.index = -1
        self.items = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """
        Add an item to self.
        """
        if item not in self:
            new_node = Node(item, self.items[self.index])
            self.items[self.index] = new_node
            self.size += 1

    def remove(self, item):
        """
        Precondition: item is in self.
        Remove an item from self.
        Raise: KeyError if item is not in self.
        """
        if item not in self:
            raise KeyError(f"Item {item} not in the set.")
        if self.prior_node is None:
            self.items[self.index] = None
        else:
            self.prior_node.next = self.found_node.next
        self.size -= 1
