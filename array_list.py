from arrays import Array
from abstract_list import AbstractList
from array_list_iterator import ArrayListIterator


class ArrayList(AbstractList):
    """
    A list implementation based on Array.
    """
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.items = Array(ArrayList.DEFAULT_CAPACITY)
        super().__init__(source_collection)

    # Accessors
    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __getitem__(self, i):
        """
        Preconditions: 0 <= i <= len(self)-1
        Returns the item at position i.
        Raises: IndexError if i is out of bound.
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range.")
        return self.items[i]

    # Mutators
    def __setitem__(self, i, item):
        """
        Preconditions: 0 <= i <= len(self)-1
        Replaces the item at position i.
        Raises: IndexError if i is out of bound.
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range.")
        self.items[i] = item

    def insert(self, i, item):
        """
        Inserts the item at position i.
        """
        self.items.insert(i, item)
        self.size += 1
        self.inc_mod_count()

    def pop(self, i=None):
        """
        Pop the item at position i.
        """
        if i is None:
            i = len(self) - 1
        item = self.items.pop(i)
        self.size -= 1
        self.inc_mod_count()
        return item

    def list_iterator(self):
        """
        Returns a list iterator.
        """
        return ArrayListIterator(self)
