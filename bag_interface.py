class BagInterface(object):
    """Interface for all bag types."""

    # Constructor
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        """
        pass

    # Accessor methods
    def is_empty(self):
        """
        Returns True if len(self) == 0,
        or False otherwise.
        """
        return True

    def clone(self):
        """
        Returns a cloned copy of self.
        True for __eq__, False for is.
        """
        return None

    def __len__(self):
        """
        Returns the number of items in self.
        """
        return 0

    def __str__(self):
        """
        Returns the string representation of self.
        """
        return ""

    def __iter__(self):
        """
        Supports iteration over a view of self.
        """
        return None

    def __add__(self, other):
        """
        Returns a new bag containing the contents of self and other.
        """
        return None

    def __eq__(self, other):
        """
        Returns true if the contents in self equals the contents in other,
        or False otherwise.
        """
        return False

    def count(self, item):
        """
        Returns the number of instances of item in self.
        """
        return 0

    # Mutator methods
    def clear(self):
        """
        Void self.
        """
        pass

    def add(self, item):
        """
        Add an item to self.
        """
        pass

    def remove(self, item):
        """
        Remove an item from self.
        Raise 'KeyError' if item is not in self.
        """
        pass