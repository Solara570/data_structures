from abstract_bag import AbstractBag
from arrays import Array


class ArrayBag(AbstractBag):
    """
    A bag implementation based on Array.
    """

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.clear()
        self.target_index = -1
        AbstractBag.__init__(self, source_collection)

    # Accessor methods
    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __contains__(self, item):
        self.target_index = 0
        for bag_item in self:
            if bag_item == item:
                return True
            self.target_index += 1
        self.target_index = -1
        return False

    def count(self, item):
        """
        Returns the number of instances of item in self.
        """
        total = 0
        for bag_item in self:
            if bag_item == item:
                total += 1
        return total

    # Mutator methods
    def clear(self):
        """
        Void self.
        """
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0

    def add(self, item):
        """
        Add an item to self.
        """
        # Grow if the array is full
        if len(self) == len(self.items):
            self.items.grow()
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """
        Remove an item from self.
        Raise KeyError if item is not in self.
        """
        # (1) Check if the item is in self, raise KeyError if not.
        if item not in self:
            raise KeyError(f"{item} not in bag.")
        # (2) During the last checking, self.target_index is already
        #     point to the designated item, simply remove it.
        for index in range(self.target_index, len(self) - 1):
            self.items[index] = self.items[index + 1]
        # (4) Decrease logical size by 1
        self.size -= 1
        # (5) Check array memory here and decrease it if necessary
        is_under_filled = len(self) < len(self.items) // 4
        is_over_grown = len(self.items) > 2 * self.DEFAULT_CAPACITY
        if is_under_filled and is_over_grown:
            self.items.shrink()


class ArraySortedBag(ArrayBag):
    """
    A sorted bag implementation based on Array.
    Inherent most methods from ArrayBag.
    """

    def __init__(self, source_collection=None):
        ArrayBag.__init__(self, source_collection=source_collection)

    # Accessor methods
    def __contains__(self, item):
        self.target_index = -1
        left, right = 0, len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == item:
                self.target_index = mid
                return True
            elif self.items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def __eq__(self, other):
        """
        Returns true if the contents in self equals the contents in other,
        or False otherwise.
        """
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        other_iter = iter(other)
        for item in self:
            if item != next(other_iter):
                return False
        return True

    # Mutator methods
    def add(self, item):
        """
        Add an item to self.
        """
        # Grow if the array is full
        if len(self) == len(self.items):
            self.items.grow()
        # Special cases: current bag is empty or the new item is the largest
        # Add to the last
        if self.is_empty() or item > self.items[len(self) - 1]:
            ArrayBag.add(self, item)
        # Regular cases: find the index and then add the item
        else:
            left, right = 0, len(self) - 1
            target_index = left
            while left <= right:
                mid = (left + right) // 2
                if self.items[mid] == item:
                    target_index = mid
                    break
                elif self.items[mid] > item:
                    right = mid - 1
                else:
                    left = mid + 1
                    target_index = left
            for index in range(len(self) - 1, target_index - 1, -1):
                self.items[index + 1] = self.items[index]
            self.items[target_index] = item
            self.size += 1
