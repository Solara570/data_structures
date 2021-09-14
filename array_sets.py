from array_bags import ArrayBag


class ArraySet(ArrayBag):
    """
    A set implementation based on Array.
    Inherent most methods from ArrayBag.
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
            if len(self) == len(self.items):
                self.items.grow()
            self.items[len(self)] = item
            self.size += 1


class ArraySortedSet(ArraySet):
    """
    A sorted set implementation based on Array.
    Inherent most methods from ArraySet.
    """

    # Accessor methods
    def __contains__(self, item):
        left, right = 0, len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == item:
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
            self.items[len(self)] = item
            self.size += 1
        # Regular cases: find the index and then add the item
        elif item not in self:
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
