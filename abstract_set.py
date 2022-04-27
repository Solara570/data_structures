class AbstractSet(object):
    """
    Generic set method implementations.
    It only contains "and", "or", "subtract" and "is_subset" methods.
    """

    # Set methods
    def __and__(self, other):
        """
        Returns the intersection of self and other.
        """
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __or__(self, other):
        """
        Returns the union of self and other.
        """
        return self + other

    def __sub__(self, other):
        """
        Returns the difference of self and other.
        """
        intersection = type(self)()
        for item in self:
            if item not in other:
                intersection.add(item)
        return intersection

    def __eq__(self, other):
        """
        Returns True if self is equal to other.
        """
        if self is other:
            return True
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def is_subset(self, other):
        """
        Returns True if self is the subset of other, or False otherwise.
        """
        for item in self:
            if item not in other:
                return False
        return True
