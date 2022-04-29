from nodes import Node
from arrays import Array
from abstract_bag import AbstractBag
from abstract_collection import AbstractCollection


class HashBag(AbstractBag):
    """
    A bag implementation based on hashing
    with bucket/chaining to resolve collisions.
    """

    # Class variables
    DEFAULT_CAPACITY = 29

    # Constructor
    def __init__(self, source_collection=None, capacity=None):
        self.capacity = HashBag.DEFAULT_CAPACITY if capacity is None else capacity
        self.items = Array(self.capacity)
        self.found_node = self.prior_node = None
        self.index = -1
        AbstractCollection.__init__(self, source_collection)

    # Accessor methods
    def __contains__(self, item):
        """
        Returns True if item is in the bag, or False otherwise.
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

    def load_factor(self):
        """
        Returns the load factor of self.
        """
        return self.size / self.capacity

    # Mutator methods
    def clear(self):
        """
        Makes self become empty.
        """
        self.size = 0
        self.found_node = self.prior_node = None
        self.index = -1
        self.items = Array(self.capacity)

    def add(self, item):
        """
        Add an item to self.
        Rehash the dict if the load factor is over 0.8.
        """
        self.index = abs(hash(item)) % len(self.items)
        new_node = Node(item, self.items[self.index])
        self.items[self.index] = new_node
        self.size += 1
        while self.load_factor() > 0.8:
            self.rehash()

    def remove(self, item):
        """
        Precondition: item is in self.
        Remove an item from self.
        Raise: KeyError if item is not in self.
        """
        if item not in self:
            raise KeyError(f"Item {item} not in the bag.")
        if self.prior_node is None:
            self.items[self.index] = None
        else:
            self.prior_node.next = self.found_node.next
        self.size -= 1

    def rehash(self):
        """
        Increases the capacity by 2 and reload all items.
        """
        # Extract all items
        items = []
        for index in range(len(self.items)):
            node = self.items[index]
            while node is not None:
                items.append(node.data)
                node = node.next
        # Increase capacity and clear self.
        self.capacity *= 2
        self.clear()
        # Add items back to self.
        for item in items:
            self.add(item)
