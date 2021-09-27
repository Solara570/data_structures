from abstract_collection import AbstractCollection


class AbstractStack(AbstractCollection):
    """
    An abstract stack implementation.
    """
    # Constructor

    def __init__(self, source_collection=None):
        super().__init__(source_collection=source_collection)

    # Mutator Methods
    def add(self, item):
        """
        Add an item to self.
        """
        self.push(item)
