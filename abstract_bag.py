from abstract_collection import AbstractCollection


class AbstractBag(AbstractCollection):
    """
    An abstract bag implementation.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        AbstractCollection.__init__(self, source_collection)
        # super().__init__(source_collection)

    # Accessor methods
    def __str__(self):
        """
        Returns the string representation of self.
        """
        return "{" + ", ".join(map(str, self)) + "}"

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
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
