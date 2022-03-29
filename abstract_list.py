from abstract_collection import AbstractCollection


class AbstractList(AbstractCollection):
    """
    An abstract list implementation.
    """

    # Constructor
    def __init__(self, source_collection=None):
        """
        Maintains a count of modifications to the list.
        """
        self.mod_count = 0
        super().__init__(source_collection=source_collection)

    # Mod Count Methods
    def get_mod_count(self):
        """
        Returns the count of modifications to the list.
        """
        return self.mod_count

    def inc_mod_count(self):
        """
        Increments the count of modifications to the list.
        """
        self.mod_count += 1

    # Accessors
    def index(self, item):
        """
        Precondition: item is in the list.
        Returns the position of the item.
        Raises: ValueError is item is not in the list.
        """
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + "is not in the list.")

    # Mutators
    def add(self, item):
        """
        Add an item to self.
        """
        self.insert(len(self), item)

    def remove(self, item):
        """
        Precondition: item is in the list.
        Remove an item.
        Raises: ValueError is item is not in the list.
        """
        position = self.index(item)
        self.pop(position)
