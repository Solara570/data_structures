from abstract_set import AbstractSet
from nodes import Node
from linked_bags import LinkedBag, TreeSortedBag


class LinkedSet(AbstractSet, LinkedBag):
    """
    A set implementation based on linked list.
    Inherent most methods from LinkedBag.
    Inherent set-specific methods from AbstractSet.
    """

    # Constructor
    def __init__(self, source_collection=None):
        LinkedBag.__init__(self, source_collection)

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
            LinkedBag.add(self, item)


class TreeSortedSet(AbstractSet, TreeSortedBag):
    """
    A set implementation based on linked BST.
    Inherent most methods from TreeSortedBag.
    Inherent set-specific methods from AbstractSet.
    """

    # Constructor
    def __init__(self, source_collection=None):
        TreeSortedBag.__init__(self, source_collection)

    # Accessor methods
    def count(self, item):
        return 1 if item in self else 0

    def __eq__(self, other):
        """
        Returns true if the contents in self equals the contents in other,
        or False otherwise.
        """
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for item in other:
            if item not in self:
                return False
        return True

    # Mutator methods
    def add(self, item):
        """
        Add an item to self.
        """
        # Grow if the array is full
        if item not in self:
            TreeSortedBag.add(self, item)
