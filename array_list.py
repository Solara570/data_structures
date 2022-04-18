from arrays import Array
from abstract_list import AbstractList
from array_list_iterator import ArraySortedListIterator, ArrayListIterator


class ArraySortedList(AbstractList):
    """
    A sorted list implementation based on Array.
    """
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.items = Array(ArraySortedList.DEFAULT_CAPACITY)
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

    def __contains__(self, item):
        """
        Returns True if the item is in the list or False otherwise.
        """
        try:
            return self.index(item) < len(self)
        except ValueError:
            return False

    def index(self, item):
        """
        Precondition: item is in the list.
        Returns the position of the item.
        Raises: ValueError is item is not in the list.
        """
        left, right = 0, len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == item:
                return mid
            elif self.items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        raise ValueError(str(item) + " not in the list.")

    # Helper method - find the place to add for the new item
    def get_insert_index(self, item):
        # Empty or greater than the last element - Add to the end
        if self.is_empty() or item > self.items[len(self) - 1]:
            return len(self)
        # Smaller than the first element - Add to the beginning
        elif item < self.items[0]:
            return 0
        # Else - Use binary search to find the place
        else:
            left, right = 0, len(self) - 1
            while left < right:
                mid = (left + right) // 2
                if self.items[mid] == item:
                    return mid
                elif self.items[mid] > item:
                    right = mid
                else:
                    left = mid + 1
            return left

    # Mutators
    def clear(self):
        """
        Removes all items in the list.
        """
        self.size = 0
        self.mod_count = 0
        self.items = Array(ArraySortedList.DEFAULT_CAPACITY)

    def add(self, item):
        """
        Add an item to self in the correct position.
        """
        ind = self.get_insert_index(item)
        self.items.insert(ind, item)
        self.size += 1
        self.mod_count += 1

    def pop(self, i=None):
        """"
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
        return ArraySortedListIterator(self)


class ArrayList(ArraySortedList):
    """
    A list implementation based on Array.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        ArraySortedList.__init__(self, source_collection)

    # Accessors
    def index(self, item):
        """
        Precondition: item is in the list.
        Returns the position of the item.
        Raises: ValueError is item is not in the list.
        """
        return AbstractList.index(self, item)

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

    def add(self, item):
        """
        Add an item to self.
        """
        return AbstractList.add(self, item)

    def list_iterator(self):
        """
        Returns a list iterator.
        """
        return ArrayListIterator(self)
