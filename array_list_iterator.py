from abstract_collection import AbstractCollection


class ArrayListIterator(object):
    """
    Represents the list iterator for an array list.
    """

    def __init__(self, backing_store):
        """
        Set the initial state of the list iterator.
        """
        self.backing_store = backing_store
        self.mod_count = backing_store.get_mod_count()
        self.first()

    # Navigators
    def first(self):
        """
        Resets the cursor to the beginning of the backing store.
        """
        self.cursor = 0
        self.last_item_pos = -1

    def last(self):
        """
        """
        self.cursor = len(self.backing_store)
        self.last_item_pos = -1

    def has_next(self):
        """
        Returns True if the iterator has a next item or False otherwise.
        """
        return self.cursor < len(self.backing_store)

    def next(self):
        """
        Preconditions: has_next() returns True.
        The list hasn't been modified except by this iterator's mutators.
        Returns the current item and advances the cursor to the next item.
        Raises: ValueError if there're no next items.
        """
        if not self.has_next():
            raise ValueError("No next item in the list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.last_item_pos = self.cursor
        self.cursor += 1
        return self.backing_store[self.last_item_pos]

    def has_prev(self):
        """
        Returns True if the iterator has a previous item or False otherwise.
        """
        return self.cursor > 0

    def prev(self):
        """
        Preconditions: has_prev() returns True.
        The list hasn't been modified except by this iterator's mutators.
        Returns the current item and moves the cursor to the previous item.
        Raises: ValueError if there're no previous items.
        """
        if not self.has_prev():
            raise ValueError("No previous item in the list iterator")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.cursor -= 1
        self.last_item_pos = self.cursor
        return self.backing_store[self.last_item_pos]

    # Mutators
    def replace(self, item):
        """
        Preconditions: the current position is defined.
        The list hasn't been modified except by this iterator's mutators.
        Replaces the current position by `item`.
        Raises: AttributeError if the current position is undefined.
        """
        if self.last_item_pos == -1:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.backing_store[self.cursor] = item
        self.last_item_pos = -1

    def insert(self, item):
        """
        Preconditions: the list hasn't been modified except by this iterator's mutators.
        Inserts a new item at the current position.
        """
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        if self.last_item_pos == -1:
            # Cursor is not defined, simply add the item to the end.
            self.backing_store.add(item)
        else:
            self.backing_store.insert(self.last_item_pos, item)
        self.last_item_pos = -1
        self.mod_count += 1

    def remove(self, item):
        """
        Preconditions: the current position is defined.
        The list hasn't been modified except by this iterator's mutators.
        Removes the item at the current position.
        Raises: AttributeError if the current position is undefined.
        """
        if self.last_item_pos == -1:
            raise AttributeError("The current position is undefined.")
        if self.mod_count != self.backing_store.get_mod_count():
            raise AttributeError("Illegal modification of the backing store.")
        self.backing_store.pop(self.last_item_pos)
        # If the item removed was obtained via next, move cursor back.
        if self.last_item_pos > self.cursor:
            self.cursor -= 1
        self.last_item_pos = -1
        self.mod_count += 1
