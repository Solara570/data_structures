from nodes import Node
from linked_bags import LinkedBag


class LinkedSet(LinkedBag):
    """
    A set implementation based on linked list.
    Inherent most methods from LinkedBag.
    """
    # Accessor methods

    def count(self, item):
        return 1 if item in self else 0
    # Mutator methods

    def add(self, item):
        """
        Add an item to self.
        """
        # Grow if the array is full
        if item not in self:
            self.items = Node(item, self.items)
            self.size += 1
