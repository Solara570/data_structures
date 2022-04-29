from nodes import Node
from arrays import Array
from abstract_set import AbstractSet
from hash_bags import HashBag


class HashSet(AbstractSet, HashBag):
    """
    A set implementation based on hashing
    with bucket/chaining to resolve collisions.
    Inherent most methods from HashBag.
    Inherent set-specific methods from AbstractSet.
    """

    # Constructor
    def __init__(self, source_collection=None, capacity=None):
        HashBag.__init__(self, source_collection)

    # Mutator methods
    def add(self, item):
        """
        Add an item to self.
        Rehash the dict if the load factor is over 0.8.
        """
        if item not in self:
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
            raise KeyError(f"Item {item} not in the set.")
        if self.prior_node is None:
            self.items[self.index] = None
        else:
            self.prior_node.next = self.found_node.next
        self.size -= 1
