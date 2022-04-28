from abstract_set import AbstractSet
from array_bags import ArrayBag, ArraySortedBag


class ArraySet(AbstractSet, ArrayBag):
    """
    A set implementation based on Array.
    Inherent most methods from ArrayBag.
    Inherent set-specific methods from AbstractSet.
    """

    # Constructor
    def __init__(self, source_collection=None):
        ArrayBag.__init__(self, source_collection)

    # Accessor methods
    def count(self, item):
        return 1 if item in self else 0

    # Mutator methods
    def add(self, item):
        """
        Add an item to self.
        """
        if item not in self:
            ArrayBag.add(self, item)


class ArraySortedSet(AbstractSet, ArraySortedBag):
    """
    A sorted set implementation based on Array.
    Inherent most methods from ArraySet.
    """

    # Constructor
    def __init__(self, source_collection=None):
        ArraySortedBag.__init__(self, source_collection)

    # Accessor methods
    def count(self, item):
        return 1 if item in self else 0

    # Mutator methods
    def add(self, item):
        """
        Add an item to self.
        """
        if item not in self:
            ArraySortedBag.add(self, item)
