class AbstractCollection(object):
    """
    An abstract collection implementation.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        self.size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    # Accessors
    def is_empty(self):
        """
        Returns True if len(self) == 0,
        or False otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        Returns the number of items in self.
        """
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """
        Returns a new bag containing the contents of self and other.
        """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

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

    def clone(self):
        """
        Returns a cloned copy of self.
        """
        return type(self)(self)

    def count(self, item):
        """
        Returns the number of instances of item in self.
        """
        total = 0
        for collection_item in self:
            if item == collection_item:
                total += 1
        return total
